from random import randint
# The playerer will generate a number and computer will run iterations for the answer
# unlimited gusses to get the number


def play_user():
    player = int(input('Enter a number between 1 and 10.  '))

    # player_input = ['hot', 'cold']
    play = True

    i = 0
    # set parameters for the numbers generated by the computer
    # to set the iteration to narrow the boundries comuter_(ceiling & floor) defined
    # computer = randint(1, 10)
    floor = 1
    ceiling =10

    while play == True :
        
        computer = (floor + ceiling) // 2
        
        i=i+1
        
        # print('this is try number', i)
        if computer == player:
            print('Wow what at guess. The computer won.')
            print(f'The computer guessed your number {player} in {i} tries.')
            break
        elif computer > player:
            ceiling = computer - 1
        elif computer < player:
            floor = computer + 1
            
        player_response = input('If number too low type Cold, if number too high type Hot.  ').lower()
        print(f'The computer got it wrong. The computer guessed {computer}')

        
        # else:
        #     player_response = input('If number low type Cold, if number high type Hot.  ').lower()
        #     while player_response not in player_input:
        #         print('Enter a valid response')
        #         player_response = input('If number low type Cold, if number high type Hot.  ').lower()
        #     if player_response == 'cold':
        #         computer_floor = computer+1
        #         computer = randint(computer_floor, computer_ceiling)
        #         continue
        #     elif player_response == 'hot':
        #         computer_ceiling = computer-1
        #         computer = randint(computer_floor, computer_ceiling)
        #         continue

        #     print(computer_ceiling, computer_floor)



            
            
            # continue
    

            
            
        

        


        # break
if __name__ == "__main__":
    play_user()