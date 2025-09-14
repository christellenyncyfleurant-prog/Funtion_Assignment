#Area of a circle
def area_of_circle(pi, radius):
    return round (pi * (radius ** 2),2)

#Total due
def total_due (money, tax):
  return round(money + (money * tax), 2)

#Converting Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)


#Circle
PI = 3.14159
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(PI, radius)
print("The area of the circle is: ", area)


#Total
money = float(input("Enter the money amount: "))
tax_percentage = float(input("Enter the tax percentage: "))
tax= tax_percentage / 100
total = total_due(money, tax)
print("The total due is: ", total)



#Temperature
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("The temperature in celsius is: ", celsius)


