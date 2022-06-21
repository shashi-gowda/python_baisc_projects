#program to choose and watch movie from available movies and based on available tickets
#films contains movie names and list containing age restriction to watch movie and available no of tickets
films={
    'Kgf':[18,5],
    'Vikrant rona':[12,4],
    'Love mocktail':[10,2]
    }
while True:
    print(f"Choose from the movies available!")
    print(list(films.keys()))
    choice=input("what film would you like to watch?").strip().title()
    if choice in films:
        age=int(input("How old are you? ").strip())
        if age>=films[choice][0]:
            if films[choice][1]>0:
                print('Please enjoy the movie')
                films[choice][1]-=1
                break
        else:
            print('sorry you are too young to watch the movie.\nThank you for visisting!')
            break
    else:
        print("sorry we don't have that film in our collection,please choose from available movies!")
        
