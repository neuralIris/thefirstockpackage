from thefirstock import thefirstock

PC = thefirstock.firstock_ConvertProduct(
    exch="NFO",
    tsym="BANKNIFTY28APR22C37400",
    qty="250",
    prd="I",
    prevprd="M",
    trantype="B",
    postype="CF"
)

print(PC)
