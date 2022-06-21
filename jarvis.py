'''security system which asks for your name and greets if the name is in
users list or simply asks the user if it can add or remove them'''

known_users=['Shashi','Shiva','Vijay','Niharika', 'Chaithra','Manju','Suguna']

while True:
    print('hi,My name is jarvis')
    name=input("enter your name: ").strip().capitalize()

    if name in known_users:
          print("name recognised")
          print(f"hello {name}")
          remove=input(f"hi {name} do you wish to remove you'r name from users!: ")
          if remove=='yes':
              known_users.remove(name)
          else:
              print("Thank you for staying back!")
    else:
        print("name not recognised")
        ask=input(f"hello {name}, would you like to be added to the users!: ")
        if ask=="yes":
            known_users.append(name)
            print("you are added to the users")
        else:
            print("Thank you for visiting")
        
