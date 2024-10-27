def SquaredValues(beg, end):
	lst = []
	
	for i in range(beg, end):
		
		lst.append(i**2)

	lst_even = []
	lst_odd = []

	
	for i in lst:
		if i%2==0:
			
			lst_even.append(i)
		else:
			
			lst_odd.append(i)
	
	print("Here's a list of even squares within specified range", lst_even)
	print("Here's a list of odd squares within specified range", lst_odd)
	
# Take input from user for range of numbers	
beg = int(input("Enter starting range : "))
end = int(input("Enter end range : "))

# Function call
SquaredValues(beg, end)


