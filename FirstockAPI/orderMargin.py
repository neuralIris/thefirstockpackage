from thefirstock import thefirstock

oM = thefirstock.firstock_orderMargin(
    exch="NSE",
    tsym="ITC-EQ",
    qty="10",
    prc="260",
    prd="C",
    trantype="B",
    prctyp="LMT",
)

print(oM)
