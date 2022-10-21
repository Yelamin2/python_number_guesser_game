from random import randint
# The computer will generate a number and you have
# three gusses to get the number


def play_computer():
    computer = randint(1, 10)

    player = int(input('Guess a number between 1 and 10.  '))

    play = True

    i = 0

    while play == True :
        

        if player == computer and i <3:
            print('Wow what at guess you win!')
            break
        elif player < computer and i <3 :
            if i ==2:
                print('you lose') 
                break
            else:
                print('Too low')
                player = int(input('Make another guess.  '))
                i= i+1
                continue

            
            
        elif player > computer and i <3 :
            if i ==2:
                print('you lose') 
                break
            else: 
                print('Too high')
                player = int(input('Make another guess.  '))
                i=i+1
                continue
        print(i)

        


        break



if __name__ == "__main__":
    play_computer()

