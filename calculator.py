#user input numbers for calculation

first=int(input("please enter the number: "))
second=int(input("Please enter the number: "))
operation =input("please enter the operation to be performed: ")


if operation=='+':
    print(first+second)
elif operaton =='-':
    print(first-second)
elif operation=='*':
    print(first*second)
elif operaton=='/':
    print(first/second)
elif operation=='**':
    print(first**second)
elif operation=='%':
    print(first%second)
else:
    print("please enter valid operation to be performed")
