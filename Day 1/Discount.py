n1 = float(input("Enter a number 1:"))
n2 = float(input("Enter a number 2:"))
d = int(input("Enter a number:"))

price = n1+n2
discount_value = price * 10/100
total_payment = price - discount_value

print(price)
print(discount_value)
print(total_payment)