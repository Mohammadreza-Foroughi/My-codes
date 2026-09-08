ls = [['.', '.', '.'], 
      ['.', '.', '.'],
      ['.', '.', '.']]



for row in range(3):
    for col in range(3):

#Here it gets the first item in the list which its a row and then
#in the fisrt row(item) it gets the other items which is coloums
        ls[row][col] = input("x or o")
        

print(f'''---+---+---\n {ls[0][0]} | {ls[0][1]} | {ls[0][2]} \
        \n---+---+---\n {ls[1][0]} | {ls[1][1]} | {ls[1][2]} \
        \n---+---+---\n {ls[2][0]} | {ls[2][1]} | {ls[2][2]} \
        \n---+---+---''')

