from level1 import play_computer
from level3 import play_user





play = True

while play == True:
    mychoice = int(input('Please enter 1 to guess a number or enter 2 to let the computer to guess   '))
    print('this is start',mychoice)
    # import level1 or level2 to run for the game.
    if mychoice == 1:
        play_computer()
        break
    elif mychoice == 2: 
        play_user()
        break
       
        
    else:
        print('This is not avalid choice')
        continue
    


    




