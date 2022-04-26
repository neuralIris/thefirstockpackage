from thefirstock.base import *
from thefirstock.functions import *


class FirstockLogin:
    def __init__(self, uid, pwd, factor2, vc, appkey):
        self.loginDetails = ApiRequests()
        self.uid = uid
        self.pwd = pwd
        self.factor2 = factor2
        self.vc = vc
        self.appkey = appkey

    def firstockLogin(self):
        result = self.loginDetails.firstockLogin(self.uid, self.pwd, self.factor2, self.vc, self.appkey)
        return result


class FirstockClientDetails:
    def __init__(self):
        self.clientDetails = ApiRequests()

    def firstockClientDetails(self):
        result = self.clientDetails.firstockClientDetails()
        return result


class FirstockLogout:
    def __init__(self):
        self.logoutDetails = ApiRequests()

    def firstockLogout(self):
        result = self.logoutDetails.firstockLogout()
        return result


class FirstockPlaceOrder:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc):

        self.placeOrder = ApiRequests()
        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prd = prd
        self.trantype = trantype
        self.prctyp = prctyp
        self.ret = ret
        self.trgprc = trgprc

    def firstockPlaceOrder(self):
        result = self.placeOrder.firstockPlaceOrder(self.exch, self.tsym, self.qty, self.prc, self.prd,
                                                    self.trantype, self.prctyp, self.ret, self.trgprc)
        return result


class FirstockGetOrderMargin:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp):
        self.getOrderMargin = ApiRequests()

        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prd = prd
        self.trantype = trantype
        self.prctyp = prctyp

    def firstockGetOrderMargin(self):
        result = self.getOrderMargin.firstockGetOrderMargin(self.exch, self.tsym, self.qty, self.prc, self.prd,
                                                            self.trantype, self.prctyp)
        return result


class FirstockOrderBook:
    def __init__(self):
        self.orderBook = ApiRequests()

    def firstockOrderBook(self):
        result = self.orderBook.firstockOrderBook()
        return result


class FirstockCancelOrder:
    def __init__(self, norenordno):
        self.cancelOrder = ApiRequests()

        self.norenordno = norenordno

    def firstockCancelOrder(self):
        result = self.cancelOrder.firstockCancelOrder(self.norenordno)
        return result


class FirstockModifyOrder:
    def __init__(self, qty, norenordno, trgprc, prc):

        self.modifyOrder = ApiRequests()
        self.qty = qty
        self.norenordno = norenordno
        self.trgprc = trgprc
        self.prc = prc

    def firstockModifyOrder(self):
        result = self.modifyOrder.firstockModifyOrder(self.qty, self.norenordno, self.trgprc, self.prc)
        return result


class FirstockSingleOrderHistory:
    def __init__(self, norenordno):
        self.singleOrderHistory = ApiRequests()

        self.norenordno = norenordno

    def firstockSingleOrderHistory(self):
        result = self.singleOrderHistory.firstockSingleOrderHistory(self.norenordno)
        return result


class FirstockTradeBook:
    def __init__(self):
        self.tradeBook = ApiRequests()

    def firstockTradeBook(self):
        result = self.tradeBook.firstockTradeBook()
        return result


class FirstockPositionBook:
    def __init__(self):
        self.positionBook = ApiRequests()

    def firstockPositionBook(self):
        result = self.positionBook.firstockPositionBook()
        return result


class FirstockConvertProduct:
    def __init__(self, exch, tsym, qty, prd, prevprd, trantype, postype):
        self.convertProduct = ApiRequests()

        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prd = prd
        self.prevprd = prevprd
        self.trantype = trantype
        self.postype = postype

    def firstockConvertProduct(self):
        result = self.convertProduct.firstockConvertProduct(self.exch, self.tsym, self.qty, self.prd, self.prevprd,
                                                            self.trantype, self.postype)
        return result


class FirstockHoldings:
    def __init__(self):
        self.holdings = ApiRequests()

    def firstockHoldings(self):
        result = self.holdings.firstockHoldings()
        return result


class FirstockLimits:
    def __init__(self):
        self.limits = ApiRequests()

    def firstockLimits(self):
        result = self.limits.firstockLimits()
        return result


class FirstockGetQuotes:
    def __init__(self, exch, token):
        self.getQuotes = ApiRequests()

        self.exch = exch
        self.token = token

    def firstockGetQuotes(self):
        result = self.getQuotes.firstockGetQuotes(self.exch, self.token)
        return result


class FirstockSearchScrips:
    def __init__(self, stext):
        self.searchScrips = ApiRequests()
        self.stext = stext

    def firstockSearchScrips(self):
        result = self.searchScrips.firstockSearchScrips(self.stext)
        return result


class FirstockGetSecurityInfo:
    def __init__(self, exch, token):
        self.getSecurityInfo = ApiRequests()
        self.exch = exch
        self.token = token

    def firstockGetSecurityInfo(self):
        result = self.getSecurityInfo.firstockGetSecurityInfo(self.exch, self.token)
        return result


class FirstockGetIndexList:
    def __init__(self, exch):
        self.getIndexList = ApiRequests()
        self.exch = exch

    def firstockGetIndexList(self):
        result = self.getIndexList.firstockGetIndexList(self.exch)
        return result


class FirstockGetOptionChain:
    def __init__(self, tsym, exch, strprc, cnt):
        self.getOptionChain = ApiRequests()

        self.tsym = tsym
        self.exch = exch
        self.strprc = strprc
        self.cnt = cnt

    def firstockGetOptionChain(self):
        result = self.getOptionChain.firstockGetOptionChain(self.tsym, self.exch, self.strprc, self.cnt)
        return result


class FirstockSpanCalculator:
    def __init__(self, exch, instname, symname, expd, optt, strprc, netqty, buyqty, sellqty):
        self.spanCalculator = ApiRequests()

        self.exch = exch
        self.instname = instname
        self.symname = symname
        self.expd = expd
        self.optt = optt
        self.strprc = strprc
        self.netqty = netqty
        self.buyqty = buyqty
        self.sellqty = sellqty


    def firstockSpanCalculator(self):
        result = self.spanCalculator.firstockSpanCalculator(self.exch, self.instname, self.symname, self.expd, self.optt,
                                                            self.strprc, self.netqty, self.buyqty, self.sellqty)
        return result


class FirstockTimePriceSeries:
    def __init__(self, exch, token, et, st):
        self.timePriceSeries = ApiRequests()

        self.exch = exch
        self.token = token
        self.et = et
        self.st = st

    def firstockTimePriceSeries(self):
        result = self.timePriceSeries.firstockTimePriceSeries(self.exch, self.token, self.et, self.st)
        return result


class FirstockConnection:
    def __init__(self, connection: FirstockAPI):
        self.connection = connection

    def firstockConnection(self):
        result = self.connection.firstockConnection()
        return result


class FirstockDepth:
    def __init__(self, depth: FirstockAPI):
        self.depth = depth

    def firstockDepth(self):
        result = self.depth.firstockDepth()
        return result


class FirstockOrder:
    def __init__(self, order: FirstockAPI):
        self.order = order

    def firstockOrder(self):
        result = self.order.firstockOrder()
        return result


class FirstockTouchline:
    def __init__(self, touchline: FirstockAPI):
        self.touchline = touchline

    def firstockTouchline(self):
        result = self.touchline.firstockTouchline()
        return result
