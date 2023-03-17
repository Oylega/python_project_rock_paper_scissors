# For this project, you will individually create a program that has a "player" and a "computer" advisary. The computer should randomly choose it's decision based on a 
# list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. If player and computer choose the same decision 
# then display ("Game Tied"), If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if the player chooses "Scissors" and the computer 
# chooses "Rock" display ("You Lose") and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").

# In this project, you will need to use the random.randint function to enable to computer to make a random decision. Full documentation on the use of this function 
# is attached in a link to this assignment.

import random 
# from Ipython.display import clear_output

def playRockPaperScissors():
    player = input("What is your name?\n")
    opponent = 'Computer'
    choices = ['rock', 'paper', 'scissors']
    player_choice = []
    computer_choice = []
   
    
    
    def playerTurn():
        player_choice = input("Make your choice.\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n 4 - Quit\n")        
        for choice in player_choice: 
            while True:                           
                if choice == '1':
                    player_choice = 'rock'
                    print("You chose rock.")
                    break
                elif choice == '2':
                    player_choice = 'paper'
                    print("You chose paper.")
                    break
                elif choice == '3':
                    player_choice = 'scissors'
                    print("You chose scissors.")
                    break
                elif choice == '4':
                    quit == True
                    print("Goodbye")
                    return                            
                else:
                    print('Please try again.')  
                    return playerTurn()                 
            if quit == True:
                print("Goodbye!")
                return    

        def computerTurn():
    
            computer_choice = random.choice(choices)         
    

            def showDown():
                print(f'{player} has chosen {player_choice}. Computer has chosen {computer_choice}.')
            
                if computer_choice == player_choice:
                     print("It's a tie!")  
                        
                elif player_choice == 'scissors' and computer_choice == 'rock':
                    print('Rock beats scissors. Computer wins!')
                        
                elif player_choice == 'paper' and computer_choice == 'rock':
                    print(f"Paper beats rock. {player} wins!")
                    
                elif player_choice == 'rock' and computer_choice == 'paper':
                    print("Paper beats rock. Computer wins!")
                        
                elif player_choice == 'scissors' and computer_choice == 'paper':
                    print(f"Scissors beats paper. {player} wins!")
                        
                elif player_choice == 'paper' and computer_choice == 'scissors':
                    print("Scissors beats paper. Computer wins!")
                        
                elif player_choice == 'rock' and computer_choice == 'scissors':
                    print(f"Rock beats scissors. {player} wins!")
                    

                def playAgain():
                    new_game = input(f"Play again? Y/N\n")
                    while new_game.lower() not in ('y','n'):
                        print("Please try again.")
                        playAgain()
                    if new_game.lower() == 'y':
                            playerTurn()
                    elif new_game.lower() == 'n':
                        quit == True
                        print("Goodbye")
                    else:
                        quit == True
                        print("Goodbye")
                        return
                        
                playAgain()
            showDown()    
        computerTurn()
    playerTurn()
        


playRockPaperScissors()


        

        


    



