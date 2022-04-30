from typing import Any
from thefirstock import thefirstock
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.websocket.enums import MessageTopic


client = thefirstock.webSocketLogin()
ws = client.ws


@ws.on_connect
def connected(client, message):
    if message.get('s') == 'OK':
        client.subscribe_touchline('NSE', '22')


@ws.on_message(MessageTopic.TOUCHLINE_FEED)
def msg_handler(client: WsClient, message: Any):
    print(message)


ws.connect(uid='PP1583', actid='PP1583')
ws.run_forever()
