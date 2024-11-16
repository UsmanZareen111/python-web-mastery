# def miles_to_kilometer(miles):
#     miles_value = miles/1.6934
#     print(miles_value)
# miles_to_kilometer(5)    





# def print_input(a):
#     return a+"00000";
# a = input("Ente a")
# b = print_input(a)
# print(b)

# def convert_dirham_to_dollar(amount , type):
#     dirham = float(input("enter amount in dirham:"))
#     usd_dollar = dirham*0.272258
#     if type == "dirham":
#         print(usd_dollar)
#     elif type == "euro":
#         return amount *100    
#     # return float (usd_dollar)  

    # print(f"the {dirham} aed in ${usd_dollar}")
    
# dollar_value = convert_dirham_to_dollar()
# print(dollar_value)

# scope in fuction
# x = 10

# def show_scope():
#     x = 5
#     print("insert function :", x)
    
# show_scope();
# print(x)


# x = 30
# def my_function():
#     global x
#     x = 40
#     # # x = 10
#     print("inside function", x)
    
# my_function()
# print("outside function",x)

# currrncy conveter
type_input = input("enter your currency type in usd or aed:")
amount_input = int(input("enter your currency amount:"))
def converter(type,amount):
    if amount < 0:
        return "your amount not verified"
    if type =="aed":
        return amount*20
    if type == "usd":
        return amount*300
result = converter(type_input,amount_input)
print("the amount you entered in pkr =",result)    






# assigement
# global variable
# x = 10
# def my_function(a,b):
#     # local variable
#     c = a+b
#     # updating global variable inside function
#     global x
#     x = c+x
#     return c
# result = my_function(5,3)
# print("result from function:",result)
# print("updated global x:",x)



