from random import randint
# The playerer will generate a number for the answer
# unlimited gusses to get the number




player = int(input('Enter a number between 1 and 10.  '))

play = True

i = 0

while play == True :
    computer = randint(1, 10)
    print(computer)
    i=i+1
    print('this is try number', i)
    if computer == player:
        print('Wow what at guess you nailed it')
        break
    else: continue
   

        
        
    

    


    break

