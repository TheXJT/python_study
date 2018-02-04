from collections import namedtuple
import inspect
from promotions import Promotion

Customer=namedtuple('Customer','name fidelity')

class LineItem:

	def __init__(self,product,quantity,price):
		self.product=product
		self.quantity=quantity
		self.price=price

	def total(self):
		return self.price*self.quantity

class Order:

	def __init__(self,customer,cart,promotion=None):
		self.customer=customer
		self.cart=list(cart)
		self.promotion=promotion

	def total(self):
		if not hasattr(self,'__total'):
			self.__total=sum(item.total() for item in self.cart)
		return self.__total

	def due(self):
		if self.promotion is None:
			discount=0
		else:
			discount=self.promotion(self)
		return self.total()-discount

	def __repr__(self):
		fmt='<Order total: {:.2f} due: {:.2f}>'
		return fmt.format(self.total(),self.due())

# def fidelity_promo(order):
# 	return order.total()*.05 if order.customer.fidelity>=1000 else 0

# def bulk_item_promo(order):
# 	discount=0
# 	for item in order.cart:
# 		if item.quantity>=20:
# 			discount+=item.total()*.1
# 	return discount

# def large_order_promo(order):
# 	distinct_items={item.product for item in order.cart}
# 	if len(distinct_items)>=10:
# 		return order.total()*.07
# 	return 0

# promos=[fidelity_promo,bulk_item_promo,large_order_promo]
# promos=[globals()[name] for name in globals()
	# if name.endswith('_promo')
	# and name !='best_promo']
promos=[func for name,func in inspect.getmembers(Promotion,inspect.isfunction)]

def best_promo(order):
	return max(promo(order) for promo in promos)

joe=Customer('John Doe',0)
ann=Customer('Ann Smith',1100)
cart=[LineItem('banana',4,.5),
	LineItem('Apple',10,1.5),
	LineItem('Watermellon',5,5.0)]
# a1=Order(ann,cart,fidelity_promo)
# print(a1)
banana_cart=[LineItem('banana',30,.5),
	LineItem('apple',10,1.5)]
# a2=Order(joe,banana_cart,bulk_item_promo)
# print(a2)
long_order=[LineItem(str(item_code),1,1.0)
	for item_code in range(10)]
# a3=Order(joe,long_order,large_order_promo)
# print(a3)
a4=Order(joe,long_order,best_promo)
print(a4)
a5=Order(joe,banana_cart,best_promo)
print(a5)
a6=Order(ann,cart,best_promo)
print(a6)

print(globals())