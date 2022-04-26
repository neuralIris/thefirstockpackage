from thefirstock import thefirstock

SP = thefirstock.firstock_SpanCalculator(
    exch="NFO",
    instname="OPTIDX",
    symname="BANKNIFTY",
    expd="2022-04-28",
    optt="CE",
    strprc="37000",
    netqty="-25",
    buyqty="",
    sellqty=""
)

print(SP)
