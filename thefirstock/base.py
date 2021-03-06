from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockLogin(self, uid, pwd, factor2, vc, appkey):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockClientDetails(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockLogout(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockPlaceOrder(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockGetOrderMargin(self, exch, tsym, qty, prc, prd, trantype, prctyp):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockOrderBook(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockCancelOrder(self, norenordno):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockModifyOrder(self, qty, norenordno, trgprc, prc):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockSingleOrderHistory(self, norenordno):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockTradeBook(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockPositionBook(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockConvertProduct(self,  exch, tsym, qty, prd, prevprd, trantype, postype):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockHoldings(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockLimits(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockGetQuotes(self, exch, token):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockSearchScrips(self, stext):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockGetSecurityInfo(self, exch, token):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockGetIndexList(self, exch):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockGetOptionChain(self, tsym, exch, strprc, cnt):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockSpanCalculator(self, exch, instname, symname, expd, optt, strprc, netqty, buyqty, sellqty):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockTimePriceSeries(self, exch, token, et, st):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockConnection(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockDepth(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockOrder(self):
        """
        :return:
        """
        pass

    @abstractmethod
    def firstockTouchline(self):
        """
        :return:
        """
        pass
