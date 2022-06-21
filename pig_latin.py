''' program to take sentence from user and convert it to pig latin'''

#get sentence from user
original=input("please enter you'r sentence: ").lower().strip()

#split sentence into words
words=original.split()
print(words)

#loop through words to convert to pig latin
new_words=[]

#if starts with vowel just add yay else add ay
for word in words:
    if word[0] in 'aeiou':
        word=word+'yay'
        new_words.append(word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos+=1
            else:
                break
            cons=word[:vowel_pos]
            the_rest=word[vowel_pos:]
            new_word=the_rest+cons+'ay'
            new_words.append(new_word)
                
#joining piglet words to form a sentence
output=' '.join(new_words)

#printing the output
print(output)
