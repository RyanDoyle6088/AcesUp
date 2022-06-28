"""
    The goal of this project is to make a code that will allow us to play the
    card game Aces Up. We will implement a series of functions to create the
    game deck, and the tableaue where the cards will be put. We will then deal
    cards to the tableau, which will be displayed according to out display
    function. We will then validate the move within tableau and foundation
    in order to see if the move is possible, which will allow the game to be
    played. Lastly, we will develop a main function to show the user the
    rules and the menu, then receive inputs so they can play the game.
"""


import cards

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    
    
    '''
        This function will create the stock, tableau, and foundation. We return
        a tuple in that order according to the game rules. The deck will be
        shuffled and used as the stock of cards. We then deal four cards,
        one to each of the four columns
    '''
    stock = cards.Deck()
    #Creating the deck
    stock.shuffle()
    #Shuffling the deck
    
    tableau=[[],[],[],[]]
    #Creating the empty list for our stock

    for l in tableau:
        #Append the stock to the list, and deal it
        l.append(stock.deal())
    foundation=[]
    
    return (stock, tableau, foundation)
    
def deal_to_tableau( stock, tableau ):
        
    '''
        This function takes two parameters, the stock data and the tableau
        data We will use it to deal four cards.
    '''
    for value in tableau:
        #Each value in the tableau
        
        value.append(stock.deal())
        #Append the dealt card to the stock


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():
    
    '''
        This function takes no parameters and it will prompt the user for an option
        and check that the input supplied by the user is of the form requested
        in the menu.  If the input is not of the required form, the
        function prints an error message and returns None.
    '''
 
    choice_list=[]
    #Creating our list
    
    choice=input("\nInput an option (DFTRHQ): ")
    #Getting the user input
    choice_split=choice.split(' ')
    #Splitting the spaces used for our spec inputs

    
    if choice_split[0]=='H' or choice_split[0]=='Q' or choice_split[0]=='R':
        choice_list.append(choice_split[0])
        #Split at the index
        return choice_list
    
    else:
        if choice_split[0]=='D' or choice_split[0]=='d':
           try:
               if int(choice_split[1])>0:
                   #Try to make int at choice index, append nothing to our 
                   #choice list
                  choice_list.append('None')
           except:
               pass

           choice_list.append(choice_split[0])

        
        elif choice_split[0]=='F' or choice_split[0]=='f':
            #If choice f
               try: 
                   if int(choice_split[1])>0:
                      choice_list.append(choice_split[0])
                      choice_list.append(choice_split[1])
                      #If greater than 0 we will append them
                   else:
                       choice_list.append('None')
               except:

                   choice_list.append('None') 
                
        elif choice_split[0]=='T' or choice_split[0]=='t':

           try: 
               if int(choice_split[1])>0:
                  #Try except for int
                  try:
                      if int(choice_split[2])>0:
                          #Index 2
                         choice_list.append(choice_split[0])
                         choice_list.append(choice_split[1])
                         choice_list.append(choice_split[2])
                        
                      else:
                         choice_list.append('None')

          
                  except:
                      choice_list.append('None')
                
               else:
                  choice_list.append('None')
                  
                   
           except:
               
               choice_list.append('None') 
        else:
             choice_list.append('None') 
    return choice_list
            
def validate_move_to_foundation( tableau, from_col ):
    
    '''
        This function has two parameters, the data structure representing the
        tableau and an int indicating the column whose bottom card should be
        moved. This function will return True if the move is valid, and 
        False otherwise.  If false, it will also print an appropriate error 
        message.  There are two errors that can be caught:
        from_col is empty or move is invalid. 
    '''
 

    card_rank_check=0
    card_suit_check=0
    card_check=''
    #Need to create our checks
    
    if (int(from_col))>=1 and (int(from_col))<=4:
        #Between 1 & 4
        check_index=int(from_col)-1
        #Check index from column minus 1

        #check length of queue
        card_queue=len(tableau[check_index])
        if (card_queue)==0:
            print("Error")
            return False
        #Error message and return False
       

         
        current_card=tableau[check_index][-1]
        card_rank_check=current_card.rank()
        card_suit_check=current_card.suit()
        #Checking the rank and suit
        
             
        if card_rank_check!=1:
            
            for column in tableau:
                if len(column)>0:
                    bottom_card=column[-1]
                    #Setting index for bottom card
                    if bottom_card.rank()==1 or bottom_card.rank()>card_rank_check:
                        if bottom_card.suit()==card_suit_check:
                            return True
                        #Otherwise print error message and return false
    print("Error")
    return False


    
def move_to_foundation( tableau, foundation, from_col ):
    
    '''
        This function takes 3 parameters. If the move is valid, the function
        will update the tableau and foundation, otherwise it will do nothing 
        to them.
    '''
    
        
    card_to_move=tableau[(from_col)-1]
    #Card that will be moved
        
    if validate_move_to_foundation( tableau, from_col )==True:
        #Pass through the validation function to make sure possible
        
        card_to_move = tableau[(from_col)-1].pop()
        #We use the pop to remove the card
        foundation.append(card_to_move)
           
        


def validate_move_within_tableau( tableau, from_col, to_col ):
    
    '''
        This function will take three parameters. the purpose is to make sure
        a move made in the tableau was valid. It will return True if
        it is valid, and return false otherwise.
    '''
 
    valid=False
    
    if int(from_col)>=1 and int(from_col)<=4:
        #int and specifications of column 
        
        if (int(to_col)>=1 and int(to_col)<=4):
            #The move to the column parameters
            
            if int(to_col)!=int(from_col):
                #If the moves are not the same thing

                check_from_index=int(from_col)-1
                check_to_index=int(to_col)-1
                #Create indeces to check these

                card_to_queue=len(tableau[check_to_index])
                #Length of the to column card to queue
                if card_to_queue==0:
                   valid=True
                   return valid
               #We return true if the length is 0
                else:
                   print("Invalid move")
                   return valid
               #Set to return false, and return the error message...
               
            else:
               print("Invalid option.")
               return valid 
        else:
            print("Invalid option.")
            return valid

    else:
        print("Invalid option.")
        return valid



def move_within_tableau( tableau, from_col, to_col ):
    
    '''
        This function has three parameters. The purpose is to see if the 
        move is valid and update the tableau based on that information. 
        If not valid, it won't do anything.  
    '''
    #get card from col
    card_from=''
    card_from_list=tableau[(from_col)-1]
    tableau.pop((to_col)-1)
    #Use the pop function to remove the card
    
    if len(card_from_list)>1:
        #Length of card greater than 1 we set index at second
        
       card_from=card_from_list[-1]
       
    else:
        
       card_from=card_from_list[0]
       #Otherwise we set index 0

    #move card to col
    card_to_list=[]
    card_to_list.insert(0,card_from)

    card_from_list.pop(-1)
    tableau.insert(int(to_col)-1,card_to_list)   

        
def check_for_win( stock, tableau ):
    
    '''
        This function has two parameters, and will return true if the 
        winning conditions are met. For this game, the user must have an empty
        stock and also have 4 aces on their tableau in order to win.
        The function will make sure this is true, and if so we will print
        the winning message.
    '''

    if len(stock)>0:
        #can't win if stock is not 0 
        return False
    count=0
    
    for i in range(4):
        
        #4 cards on board to win
        if len(tableau[i])==1 and tableau[i][0].rank()==1:
            
            count+=1
            
    if count==4 and len(stock)==0:
        return True
    #Meeting the winning conditions
    else:           
        return False
    
def main():
        
    '''
        Our main function will initialize the game. We will display the rules
        and the menu to the user. We will then ask the user for an input
        and check the validity of it. We will use the main to go through
        each user input option from the menu and return it, and it the input
        is invalid, we return the invalid option message. If they input
        q or h, we quit the game or we display the menu. The main will
        repeat until the user wins or quits the program.
    '''

 
    stock, tableau, foundation = init_game()
    print( MENU )
    #display our menu
    if len(tableau[0])==0:

        deal_to_tableau( stock, tableau )
        #initialize our game with the stock and tableau
        
    display( stock, tableau, foundation )
    option_list=get_option()
    #get options

   
    continue_game=True
    while (continue_game):
        if option_list[0]=='H' or option_list[0]=='h':
           print(MENU)
           #H will display the menu
        if option_list[0]=='D' or option_list=='d':
            #D will call the deal to tableau function
           deal_to_tableau( stock, tableau )
                  
        if option_list[0]=='F' or option_list[0]=='f':
            #F will take an input, space, then another input to see
            #from column, then validate the move
           from_col=option_list[1]
           valid_move=validate_move_to_foundation( tableau, from_col )
         
           if (valid_move):
               #If the move is valid, we move it to the foundation
               move_to_foundation(tableau, foundation, from_col)

        if option_list[0]=='T' or option_list=='t':
            #If choice t, we will validate the move within the tableau
           from_col=option_list[1]
           to_col=option_list[2]
           valid_move=validate_move_within_tableau( tableau, from_col, to_col )
           if (valid_move):
               #If move is valid, we run the move within tableau function,
               #as it is possible
               move_within_tableau( tableau, from_col, to_col )
           else:
               print("Invalid move")
               #We return an error message if it is not a valid move

        if option_list[0]=='R' or option_list[0]=='r':
            #If choice r, we will Restart the game and redisplay the rules
            #and menu
           print("=========== Restarting: new game ============")
           print(RULES)
           print()
           print(MENU)
           
           stock, tableau, foundation = init_game()
           #reinitialize the game
           deal_to_tableau( stock, tableau )
                     
        if option_list[0]=='Q' or option_list[0]=='q':
            #We break the code if choice q and print our goodbye message
           print("You have chosen to quit.") 
           break
           
        if option_list[0]=='None':
            #If the user enters none of the above options, we will return
            #the invalid option error message
           print("Invalid option.")
           print()

        win_flag=check_for_win( stock, tableau )
        #Checking for win with our check for win parameters

        if win_flag==False:
            #If they did not win the game, we continue the game
           display( stock, tableau, foundation )
           option_list=get_option()
        else:
            print("You won!")
            #We print the winning mesage and break the code if they have
            #met the winning parameters
            break

if __name__ == "__main__":
    main()
