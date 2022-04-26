from thefirstock import thefirstock

gQ = thefirstock.firstock_GetQuotes(
    exch="NSE",
    token="26000"
)

print(gQ)
