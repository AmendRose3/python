# 15. Chocolate Purchase Calculation with Discounts: Develop a program that calculates the 
# total number of chocolates a person can buy, given the cost per chocolate, the amount 
# of money they have, and a discount scheme based on wrappers returned.


def calculate(money, price, wrap) :

	if (money < price) :
		return 0

	#  find number of chocolates we can  buy with that given money
	choc = int(money / price) 

	# add number of chocolates with the chocolates gained by wrapprices 
	choc = choc + (choc - 1) / (wrap - 1) 
	return int(choc )


money = int(input("Total money: "))
price = int(input("Total price:"))
wrap =int(input("Total wrapper needed to get 1 chocolate:"))

print(calculate(money, price, wrap))


