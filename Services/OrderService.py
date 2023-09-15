
import robin_stocks.robinhood as rh
class Order:

    def __init__(self, name):
        self.name = name
    
    def BuyFractionalPriceByDollars(self, amount):
        purchase = rh.orders.order_buy_fractional_by_price(self.name, amount)
        print(purchase)

    def BuyFractionalPriceByPercent(self, amount):
        purchase = rh.orders.order_buy_fractional_by_quantity(self.name, amount)
        print(purchase)

    def SellFractionalPriceByDollars(self, amount):
        purchase = rh.orders.order_sell_fractional_by_price(self.name, amount, extendedHours=True)
        print(purchase)
        
    def SellFractionalPriceByPercent(self, amount):
        purchase = rh.orders.order_sell_fractional_by_quantity(self.name, amount)
        print(purchase)

    def CancelAllStockOrders(self):
        cancel = rh.orders.cancel_all_stock_orders()
        print(cancel)

    
    
