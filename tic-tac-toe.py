ls = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]

print(f'''---+---+---\n {ls[1][1]} | {ls[1][2]} | {ls[1][3]} \
        \n---+---+---\n {ls[2][1]} | {ls[2][2]} | {ls[2][3]} \
        \n---+---+---\n {ls[3][1]} | {ls[3][2]} | {ls[3][3]} \
        \n---+---+---''')

while True:
      while True:
            while True:
                  try :
                        print("Player X's turn: ")
                        player_x_row_input = input('Enter row (1-3): ')
                        if int(player_x_row_input) in range(1,4) :
                              break
                        else: 
                              print('Invalid input!')
                  except ValueError:
                        print('Invalid input!')
                  

            while True:
                  try:
                        player_x_column_input = input('Enter column (1-3): ')
                        if int(player_x_column_input) in range(1,4) :
                              break
                                    
                        else: 
                              print('Invalid input!')
                  except ValueError:
                              print('Invalid input!')

            if (' ') in ls[int(player_x_row_input)][int(player_x_column_input)]:  
                  ls[int(player_x_row_input)][int(player_x_column_input)] = 'X'
                  print(f'''---+---+---\n {ls[1][1]} | {ls[1][2]} | {ls[1][3]} \
                        \n---+---+---\n {ls[2][1]} | {ls[2][2]} | {ls[2][3]} \
                        \n---+---+---\n {ls[3][1]} | {ls[3][2]} | {ls[3][3]} \
                        \n---+---+---''')
                  break
            else:
                  print('This spot is already taken!!')

      if (("X" in ls[1][1]) and ("X" in ls[1][2]) and ("X" in ls[1][3])) or \
      (("X" in ls[2][1]) and ("X" in ls[2][2]) and ("X" in ls[2][3])) or \
            (("X" in ls[3][1]) and ("X" in ls[3][2]) and ("X" in ls[3][3])) or \
                  (("X" in ls[1][1]) and ("X" in ls[2][2]) and ("X" in ls[3][3])) or \
                        (("X" in ls[1][3]) and ("X" in ls[2][2]) and ("X" in ls[3][1])) or \
                              (("X" in ls[1][1]) and ("X" in ls[2][1]) and ("X" in ls[3][1])) or \
                                    (("X" in ls[1][2]) and ("X" in ls[2][2]) and ("X" in ls[3][2])) or \
                                          (("X" in ls[1][3]) and ("X" in ls[2][3]) and ("X" in ls[3][3])):
              print('X is the winner')
              break

      elif ((' ') not in ((ls[1][1]) + (ls[1][2]) + (ls[1][3])\
                  + (ls[2][1]) + (ls[2][2]) + (ls[2][3])\
                  + (ls[3][1]) + (ls[3][2]) + (ls[3][3]))):
             print('its a tie')
             break
      
      while True: 
            while True:
                        try :
                              print("Player O's turn: ")
                              player_o_row_input = input('Enter row (1-3): ')
                              if int(player_o_row_input) in range(1,4) :
                                    break
                              else: 
                                    print('Invalid input!')
                        except ValueError:
                              print('Invalid input!')
                  
            
            while True:
                  try:
                        player_o_column_input = input('Enter column (1-3): ')
                        if int(player_o_column_input) in range(1,4) :      
                              break
                        else: 
                              print('Invalid input!')
                  except ValueError:
                        print('Invalid input!')

            if (' ') in ls[int(player_o_row_input)][int(player_o_column_input)]:
                    ls[int(player_o_row_input)][int(player_o_column_input)] = 'O'
                    print(f'''---+---+---\n {ls[1][1]} | {ls[1][2]} | {ls[1][3]} \
                            \n---+---+---\n {ls[2][1]} | {ls[2][2]} | {ls[2][3]} \
                            \n---+---+---\n {ls[3][1]} | {ls[3][2]} | {ls[3][3]} \
                            \n---+---+---''')
                    break
            else:
             print('This spot is already taken!!')   

      if (("O" in ls[1][1]) and ("O" in ls[1][2]) and ("O" in ls[1][3])) or \
      (("O" in ls[2][1]) and ("O" in ls[2][2]) and ("O" in ls[2][3])) or \
            (("O" in ls[3][1]) and ("O" in ls[3][2]) and ("O" in ls[3][3])) or \
                  (("O" in ls[1][1]) and ("O" in ls[2][2]) and ("O" in ls[3][3])) or \
                        (("O" in ls[1][3]) and ("O" in ls[2][2]) and ("O" in ls[3][1])) or \
                              (("O" in ls[1][1]) and ("O" in ls[2][1]) and ("O" in ls[3][1])) or \
                                    (("O" in ls[1][2]) and ("O" in ls[2][2]) and ("O" in ls[3][2])) or \
                                          (("O" in ls[1][3]) and ("O" in ls[2][3]) and ("O" in ls[3][3])):
              print('O is the winner')
              break
      
      elif ((' ') not in ((ls[1][1]) + (ls[1][2]) + (ls[1][3])\
                  + (ls[2][1]) + (ls[2][2]) + (ls[2][3])\
                  + (ls[3][1]) + (ls[3][2]) + (ls[3][3]))):
             print('its a tie')
             break
      
                  



# for row in range(3):
#     for col in range(3):

# #Here it gets the first item in the list which its a row and then
# #in the fisrt row(item) it gets the other items which is columns
#         ls[row][col] = input("x or o")
        


