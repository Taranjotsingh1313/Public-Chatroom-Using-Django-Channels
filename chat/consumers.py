from chat.models import userh
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
class PublicChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        pass

    async def receive_json(self, content):
        print(content)
        if content['command'] == 'connected':
            await self.channel_layer.group_add(
                'publicchat',
                self.channel_name
            )
            await add(self.scope['user'])
            await self.channel_layer.group_send(
                'publicchat',
                {
                    'type':'m.m',
                    'command':'user',
                    'no':await cu()
                }
            )
        else:
            await self.channel_layer.group_send(
                'publicchat',
                {
                    'type':'chat.message',
                    'message':content['message'],
                    'user':content['user'],
                    'command':'received'
                }
            )
        pass

    async def disconnect(self, code):
        await dele(self.scope['user'])
        pass

    async def chat_message(self,event):
        await self.send_json({
            'message':event['message'],
            'user':event['user'],
            'command':event['command']
        })
    async def m_m(self,event):
        await self.send_json({
            'command':event['command'],
            'no':event['no'],
        })
@database_sync_to_async
def add(user):
    return userh.objects.create(user=user)
@database_sync_to_async
def dele(user):
    return userh.objects.filter(user=user).first().delete()
@database_sync_to_async
def cu():
    return userh.objects.count()