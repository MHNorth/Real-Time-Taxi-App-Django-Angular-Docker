from channels.generic.websocket import AsyncJsonWebsocketConsumer


class UberConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            await self.accept()