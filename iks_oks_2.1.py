import random
combinations = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def print_table(table):
    print("-------------")
    print("|",table[0],"|",table[1],"|",table[2],"|")
    print("-------------")
    print("|",table[3],"|",table[4],"|",table[5],"|")
    print("-------------")
    print("|",table[6],"|",table[7],"|",table[8],"|")
    print("-------------")
    
def print_winner(combination, table): 
    if table[combination[0]-1] == 'X':
        print(f"Igrac 'X' je pobjednik, spojio je: {combination[0]}-{combination[1]}-{combination[2]}")
    elif table[combination[0]-1] == 'O':
        print(f"Racunar je pobjednik, spojio je: {combination[0]}-{combination[1]}-{combination[2]} ")

def is_valid(field, table): 
    if field < 1 or field > 9:
        return 1 
    elif table[field-1] == 'X' or table[field-1] == 'O':
        return 2  
    else:
        return 0

def table_modification(field, player, table):   
    for i in range(0, len(table) ):
        if table[i] == field:
            table[i] = player

    print_table(table)

def check_combination(table):
    if table[0] == table[1] and table[0] == table[2]:
        return [1,2,3] 
    elif table[0] == table[4] and table[0] == table[8]:
        return [1,5,9]
    elif table[0] == table[3] and table[0] == table[6]:
        return [1,4,7]
    elif table[6] == table[7] and table[6] == table[8]:
        return [7,8,9]
    elif table[2] == table[5] and table[2] == table[8]:
        return [3,6,9]
    elif table[1] == table[4] and table[1] == table[7]:
        return [2,5,8]
    elif table[3] == table[4] and table[3] == table[5]:
        return [4,5,6] 
    elif table[2] == table[4] and table[2] == table[6]:
        return [3,5,7]
    else:
        return 0
        
def check_field_xo(player_xo):
    br2 = 0  
    for i in range(0, len(combinations)):
        for j in range(0, 3):
            x = combinations[i][j]
            if table[x-1] == player_xo:
                br2 += 1     
        if br2 == 2:   
            for j in range(0, 3):
                x = combinations[i][j]
                if table[x-1] != player_xo and table[x-1] > '0' and table[x-1] <= '9':   
                    return table[x-1]
        br2 = 0        
    return -1

def take_field(player, table):
    field = input(f"{player}: ")
    err = is_valid(int(field), table)
    while err > 0:
        if err == 1:
            print("Grska, nepostojece polje!")
            field = input(f"{player}: ")
        elif err == 2:
            print("Greska, uneseno polje je zauzeto!")
            field = input(f"{player}: ")
        err = is_valid(int(field), table)
    return field

def take_field_computer(table):
    field = check_field_xo('O')
    if field == -1:
        field = check_field_xo('X')
        if field == -1:
            field = random.choice(rand_choices)
    return field


table =['1','2','3','4','5','6','7','8','9']
rand_choices = ['1','2','3','4','5','6','7','8','9']
print_table(table)

play_game = True
combination = []
br = 1
while play_game and   br <= 9:

    if br%2 != 0:
        player_x = take_field('player_x', table)
        table_modification(player_x, 'X', table)
        combination = check_combination(table)
        rand_choices.remove(player_x)
        if combination:
            print_winner(combination, table)
            play_game = False
        br += 1

    if br%2 == 0 and br <= 9 and play_game :
        player_o = take_field_computer(table)
        table_modification(player_o, 'O', table)
        rand_choices.remove(player_o)
        print("Racunar..", player_o)
        combination = check_combination(table)
        if combination:
            print_winner(combination, table)
            play_game = False
        br += 1

if br == 10 and combination == 0:
    print("Nerijeseno je!")



