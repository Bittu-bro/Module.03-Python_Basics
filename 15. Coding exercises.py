#Area of a right triangle = 1/2 × base × height


base = float(input("Enter the base of trangle .!"))
height = float(input("Enter the height of trangle .!"))

area_of_right_triangle = 1/2 * base * height


print("Area of right angle trangle is: ", area_of_right_triangle, ".")




a = float(input("Enter the 1st side of trangle: "))
b = float(input("Now ! Enter the 2nd side of trangle: "))
c = float(input("One last ! Enter the 3rd side of trangle: "))




semi_perimeter = s = (a+b+c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("--------""Here is the your all calculation""----------")
print(" ** Semiperimeter of the trangle is" , semi_perimeter, ".")
print(" ** Area of the trangle is:", round(area, 3), ".", )
print("-------""Thank you for choosing Bittu's tolls""---------- ")




a = float(input("Enter the 1st side of trangle: "))
b = float(input("Now ! Enter the 2nd side of trangle: "))
c = float(input("One last ! Enter the 3rd side of trangle: "))




semi_perimeter = s = (a+b+c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("--------""Here is the your all calculation""----------")
print(" ** Semiperimeter of the trangle is" , semi_perimeter, ".")
print(" ** Area of the trangle is:", round(area, 3), ".", )
print("-------""Thank you for choosing Bittu's tolls""---------- ")





#if you want decimal table then use fun1
                   #fun1 
num = float(input("Enter your \'Decimal\' number: "))




# #if you want integer table then use fun2
#                    #fun2
# num = int(input("Enter your \'Integer\' number: "))





print(f"Here is the your table \n\t{num * 1}\n\t{num * 2}\n\t{num * 3}\n\t{num * 4}\n\t{num * 5}\n\t{num * 6}\n\t{num * 7}\n\t{num * 8}\n\t{num * 9}\n\t{num * 10}")