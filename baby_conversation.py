#baby keeps asking questions untill it gets answer starting with just because

from random import choice

questions=['why the sky is blue? ', 'why lord shiva called the greatest? ',
           'why virat kohli is called king? ']

question=choice(questions)

answer=input(question).lower().strip()

while answer.startswith("just because")!=True:
    answer=input("why?: ").strip().lower()
    
    
