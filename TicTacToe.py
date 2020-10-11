#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


def display_board(board,clear=False):
    if clear:
        clear_output()
    print(board[7] +'|'+board[8]+'|'+board[9])
    print(board[4] +'|'+board[5]+'|'+board[6])
    print(board[1] +'|'+board[2]+'|'+board[3])
    


# In[2]:


board_values = ['#','1','2','3','4','5','6','7','8','9']
win_comb = [{1,4,7},{1,5,9},{1,2,3},{2,5,8},{3,6,9},{3,5,7},{4,5,6},{7,8,9}]
winner=''
win_status = False
current_player = 1
players=[]


# In[3]:


def player_input(prompt='Player-1 choose your mark - X or O : '):
    global players
    
    player1 = input(prompt).upper()
    #valid = 
    if validate_input(player1):
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        print(f'Player1 takes {player1} and Player2 takes {player2}')
        print('\n')
        print('Let the game begin')
        display_board(board_values)
        players = [player1,player2]
    else:
        player_input('Enter a valid Mark - X or O : ')
    

    
def validate_input(val):
    if val!='X' and val!='O':
        return False
    else:
        return True


# In[4]:


def win_check(mark):
    
    player_pos = []
    global win_status
    global winner
    
    for ind in range(len(board_values)):
        if (board_values[ind] == mark):   
            player_pos.append(ind)      
        
    player_pos = set(player_pos)
    count = 0
    count_list = []

    for comb in win_comb:
        for val in comb:
            for pos in player_pos:
                if pos == val:
                    count += 1
        count_list.append(count)
        count = 0
    
    for c in count_list:
        if c == 3:
            if mark == players[0]:
                winner = 'Bravo!! Player1 has won the game..'
            else:
                winner = 'Bravo!! Player2 has won the game..'
            win_status = True  
            


# In[5]:


def tie_check():
    global winner
    global win_status
    global game_run
    count=0
    for val in board_values:
        if val == 'X' or val == 'O':
            count += 1
    if count == 8:
        winner = "Match Tied!!"
        win_status = True


# In[6]:


def enter_mark(prompt,mark,player):
    position = int(input(prompt))
    if board_values[position] != 'X' and board_values[position] != 'O':
        plot_mark(mark,position)
    else:
        pmpt = 'The position you selected is already plotted..  ' + player +' select another position'
        enter_mark(pmpt,mark,player)
        


# In[7]:


def plot_mark(mark,position):
    global current_player
    global board_values
    
    board_values[position] = mark
    if(mark == players[0]):
        current_player = 2
    elif(mark == players[1]):
        current_player = 1
    display_board(board_values,False)

    win_check(mark)
    tie_check()


# In[8]:


def play_game():
    global win_status
    
    player_input()
        
    while players and win_status == False:
        if current_player == 1:
            prompt = 'Player1 enter your position to mark ' + players[0] + ' : '
            mark = players[0]
            player = 'Player1'
            enter_mark(prompt,mark,player)
        else:
            prompt = 'Player1 enter your position to mark ' + players[1] + ' : '
            mark = players[1]
            player = 'Player2'
            enter_mark(prompt,mark,player)
        
    if win_status:
        print(winner)
        
        replay = input('Mate!! Would you like to replay?? Y or N : ')
        if replay=='Y':
            clear_output()
            play_game()
        else:
            print('Thanks Mate.. See you soon!!')
    


# In[ ]:


play_game()


# In[ ]:




