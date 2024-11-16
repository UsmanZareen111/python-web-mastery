# module
def greet (name):
    print(f"welcome {name}")
    
def sum (a , b):
    print(a+b)
    
def divide(a,b,c,d):
    print((a/b)*(c-d))


def converter(type,amount):
    if amount < 0:
        return "your amount not verified"
    if type =="aed":
        return amount*20
    if type == "usd":
        return amount*300
