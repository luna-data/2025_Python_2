class ExchangeRate:
    def __init__(self,currency,rate):
        self.currency=currency
        self.rate=rate

    def to_won(self,amount):

    def to_dollar(self,amount):

    def update_rate(self,new_rate):

    def info(self):

usd = ExchangeRate("USD", 1440)
usd.info()
print("100달러=", usd.to_won(100), "원")
print("270000원=", round(usd.to_dollar(270000), 2), "달러")
usd.update_rate(1440)
print("100달러=", usd.to_won(100), "원")