import random
H = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
bucket={
  "movies":["matrix","twilight","battleship","fast"],
  "sport":["cricket","handball","rugby","kabaddi"]
}
bucket['mix']=bucket["movies"]+bucket['sport']
bucket_inp=input("enter your choice:").lower()
word=random.choice(bucket[bucket_inp])
count=0
l=["-" for i in word]
reserved=[]
end_game = True
print(*l)
def ans():
  for i in range(len(word)):
    if word[i]==inp:
      l[i]=inp
while end_game:
  inp=input("enter: ")
  while inp in reserved:
    inp=input("allready given,give another input: ")
  reserved.append(inp)
  if inp in word:
    ans()
    print(*l)
  else:
    print(H[count])
    count+=1
  if(count == 7):
    end_game = False  
    print("you lose")
  if "-" not in l:
    print('you won')
    break