from channels.testing import ChannelsLiveServerTestCase

from django.test import AsyncClient
from django.test import TestCase
from django.utils import timezone

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from .models import ChatRoom

# NOTE: Requires "geckodriver" binary to be installed in $PATH
# If you'd like to use chromedriver, you can change this line to
# test_driver = webdriver.Chrome()
test_driver = webdriver.Firefox()

# === Normal Tests ===
class MyTests(TestCase):
    async_client = AsyncClient()
    async def test_user_accessing_non_existing_room(self):
        # Since no chat rooms have been added to our test db, you can enter any name here
        response = await self.async_client.get('idonotexist')
        self.assertEqual(response.status_code, 404)
    
# === Live Server Tests ===
class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True  # emulate StaticLiveServerTestCase

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            cls.driver = test_driver
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_when_chat_message_posted_then_seen_by_everyone_in_same_room(self):
        try:
            ChatRoom.objects.create(room_name='room', creation_date=timezone.now())
            self._enter_chat_room('room')

            self._open_new_window()
            self._enter_chat_room('room')

            self._switch_to_window(0)
            self._post_message('hello')
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 1 from window 1')
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 2 from window 1')
        finally:
            self._close_all_new_windows()

    def test_when_chat_message_posted_then_not_seen_by_anyone_in_different_room(self):
        try:
            ChatRoom.objects.create(room_name='room', creation_date=timezone.now())
            ChatRoom.objects.create(room_name='room2', creation_date=timezone.now())

            self._enter_chat_room('room')
            self._open_new_window()
            self._enter_chat_room('room2')

            self._switch_to_window(0)
            self._post_message('hello')
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 1 from window 1')

            self._switch_to_window(1)
            self._post_message('world')
            WebDriverWait(self.driver, 2).until(lambda _:
                'world' in self._chat_log_value,
                'Message was not received by window 2 from window 2')
            self.assertTrue('hello' not in self._chat_log_value,
                'Message was improperly received by window 2 from window 1')
        finally:
            self._close_all_new_windows()

    def test_open_rooms_displayed_on_index_page(self):
        try:
            ChatRoom.objects.create(room_name='room', creation_date=timezone.now())
            ChatRoom.objects.create(room_name='room2', creation_date=timezone.now())
            self._enter_index()
            # Select list containing all open rooms
            rooms = self._room_list.find_elements_by_tag_name('input')
            self.assertEqual(rooms[0].get_property('value'), 'room', "Room 'room' does not exist")
            self.assertEqual(rooms[1].get_property('value'), 'room2', "Room 'room2' does not exist")
        finally:
            self._close_all_new_windows()



    # === Utility ===

    def _enter_chat_room(self, room_name):
        self.driver.get(self.live_server_url + '/chat/' + room_name)

    def _enter_index(self):
        self.driver.get(self.live_server_url + '/')

    def _open_new_window(self):
        self.driver.execute_script('window.open("about:blank", "_blank");')
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def _close_all_new_windows(self):
        while len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.execute_script('window.close();')
        if len(self.driver.window_handles) == 1:
            self.driver.switch_to.window(self.driver.window_handles[0])

    def _switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def _post_message(self, message):
        ActionChains(self.driver).send_keys(message + '\n').perform()

    # === Properties === 

    @property
    def _chat_log_value(self):
        return self.driver.find_element_by_id('chat-log').get_property('value')
    
    @property
    def _room_list(self):
        return self.driver.find_element_by_id('room-list')
