from thefirstock import thefirstock

placeOrder = thefirstock.firstock_placeOrder(
    exch="NSE",
    tsym="ITC-EQ",
    qty="10",
    prc="260",
    prd="C",
    trantype="B",
    prctyp="LMT",
    ret="DAY",
    trgprc=""
)

print(placeOrder)
