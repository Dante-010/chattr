# Generated by Django 3.1.3 on 2020-12-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='id',
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='room_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
