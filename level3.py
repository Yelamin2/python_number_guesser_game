from random import randint
# The computer will generate a number and you have
# three gusses to get the number



player = int(input('Enter a number between 1 and 10.  '))

player_input = ['hot', 'cold']
play = True

i = 0
computer = randint(1, 10)
computer_floor = 1
computer_ceiling =10

while play == True :
    
    print(computer)
    i=i+1
    print('this is try number', i)
    if computer == player:
        print('Wow what at guess you win')
        break
    else:
        player_response = input('If number low type Cold, if number high type Hot.  ').lower()
        while player_response not in player_input:
            print('Enter a valid response')
            player_response = input('If number low type Cold, if number high type Hot.  ').lower()
        if player_response == 'cold':
            computer_floor = computer+1
            computer = randint(computer_floor, computer_ceiling)
            continue
        elif player_response == 'hot':
            computer_ceiling = computer-1
            computer = randint(computer_floor, computer_ceiling)
            continue

        print(computer_ceiling, computer_floor)



         
        
        continue
   

        
        
    

    


    break
