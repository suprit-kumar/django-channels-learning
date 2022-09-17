from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from random import randint
from time import sleep
from channels.exceptions import StopConsumer


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room = 'test_consumer'
        self.room_group = 'test_consumner_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from django channels'}))
        # raise StopConsumer()

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        try:
            for _ in range(1000):
                self.send(json.dumps({'message': randint(1, 100)}))
                sleep(1)
        except:
            raise StopConsumer
            # pass
            # raise StopConsumer()

    def disconnect(self, *args, **kwargs):
        print("Disconnect")
        # self.send({
        #     "type": "websocket.close"
        # })

        raise StopConsumer

    def send_notification(self, event):
        print('send_notification')
        print(event)
        self.send(json.dumps({'response': event.get('value')}))
