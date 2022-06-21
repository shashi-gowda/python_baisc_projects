'''program to take input user's input details and frame sentence as output'''



#ask user for name
name=input("please enter your name: ")

#ask user for age
age=int(input("please enter you'r age: "))

#ask user's city
city=input("please enter the city you live in: ")

#ask user what they enjoy
love=input("please tell us what you love doing: ")

#create output text
output=f"your name is {name} and your age is {age}, you live in {city} and you {love}"

#print output to screen
print(output)
