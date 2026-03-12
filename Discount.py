#Discount value code

n1 = float(input("Enter a n1:"))
n2 = float(input("Enter a n2:"))
d = int(input("Enter a discount:"))

price = n1+n2
discount_value = price * 10/100
paid = price - discount_value

print(price)
print(discount_value)
print(paid)