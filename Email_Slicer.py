#get user email address
email=input("please enter your mail address: ").strip() #strip is to remove any spaces

#sliceout user name
user=email[:email.index('@')]

#slice domain name
domain=email[email.index('@')+1:]

#format message
output=f"Hello, You'r user name is {user}, and domain name is {domain}"

#display output message
print(output)
