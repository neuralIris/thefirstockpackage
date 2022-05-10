from thefirstock import thefirstock

from typing import Any
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.websocket.enums import MessageTopic

login = thefirstock.firstock_login(
    uid='',
    pwd='',
    factor2='',
    vc='',
    appkey='',
)
print(login)
