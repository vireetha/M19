price = 2.50

def calculate_change(amount_given):
	return amount_given - price

c = calculate_change(4.00)
print("Change the customer is due", c)