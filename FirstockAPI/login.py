from thefirstock import thefirstock

from typing import Any
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.common import RequestSourceType
from thefirstock.pyClient.models import LoginRequestModel

from thefirstock.pyClient.websocket.enums import MessageTopic

login = thefirstock.firstock_login(
                uid='',
                pwd='',
                factor2='',
                vc='',
                appkey='',
)

client = thefirstock.webSocketLogin(login)

ws = client.ws

@ws.on_connect
def connected(client, message):
    if message.get('s') == 'OK':
        client.subscribe_touchline('NSE', '22')
        # client.subscribe_touchline('NIFTY', '26009')


@ws.on_message(MessageTopic.TOUCHLINE_FEED)
def msg_handler(client: WsClient, message: Any):
    print(message)


@ws.on_message(MessageTopic.TOUCHLINE_SUB_ACK)
def msg_handler(client: WsClient, message: Any):
    if message.get('s') == 'OK':
        print(message)


@ws.on_connect
def cnc_handler(client: WsClient, message: Any):
    if message.get('s') == 'OK':
        client.subscribe_touchline('NSE', 'NIFTY')
    print(message)


ws.connect(uid='', actid='')
ws.run_forever()
