from thefirstock import thefirstock

from typing import Any
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.websocket.enums import MessageTopic

login = thefirstock.firstock_login(
    uid='PP1583',
    pwd='Trade@9999',
    factor2='15081983',
    vc='PP1583_API',
    appkey='ncoAPIkey27122021TGDYH1S',
)
print(login)
