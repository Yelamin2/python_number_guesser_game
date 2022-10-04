





play = True

while play == True:
    mychoice = int(input('Please enter 1 to guess a number or enter 2 to let the computer to guess   '))
    print('this is start',mychoice)
    # import level1 or level2 to run for the game.
    if mychoice == 1:
        import level1
        break
    elif mychoice == 2: 
        import level3
        break
       
        
    else:
        print('This is not avalid choice')
        continue
    

    




