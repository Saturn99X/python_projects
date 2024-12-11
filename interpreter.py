# store the expression in a variable
expression = input("enter your arithmetic expression")
# break the expression into usable variable
expression_list = list(expression)
x = expression_list[0]
y = expression_list[2]
z = expression_list[4]
# calculations
if y == "/" and z == "0":
 print("math error")
else:
 result = float(eval(expression))
 print(f"{result}")
