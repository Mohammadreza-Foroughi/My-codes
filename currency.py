
valid_currency = ["usd",'eur','cad']

while True:

    user_input =(input("Enter the amount:"))
    if user_input.isdigit():
        amount = int(user_input)
        source_currency = input('Source Currency (USD/EUR/CAD): ')
        if source_currency in valid_currency :
            continue
        else :
            print('Invalid amount')
        
    else:
        print('Invalid amount')

    