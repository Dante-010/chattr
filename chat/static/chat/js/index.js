document.querySelector('#rooms').classList.add('active')

function enterRoom(roomName) {
    window.location.pathname = '/chat/' + roomName + '/';
}