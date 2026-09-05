valid_currency = ["usd",'eur','cad']
while True:
    user_input =(input("Enter the amount:"))
    if user_input.isdigit() and int(user_input) > 0:
        amount = int(user_input)
        source_currency = input('Source Currency (USD/EUR/CAD): ')
        if source_currency in valid_currency :
            target_currency = input('Target Currency (USD/EUR/CAD): ')
            if target_currency in valid_currency :
                if source_currency == target_currency:
                    print(amount)
                elif source_currency == 'usd' and target_currency == 'cad':
                    print(amount * 1.38)
                elif source_currency == 'usd' and target_currency == 'eur':
                    print(amount * 0.86)
                elif source_currency == 'cad' and target_currency == 'usd':
                    print(amount * 0.72)
                elif source_currency == 'cad' and  target_currency == 'eur':
                    print(amount * 1.61)
                elif source_currency == 'eur' and target_currency == 'usd':
                    print(amount * 1.16)
                elif source_currency == 'eur' and target_currency == 'cad':
                    print(amount * 0.62)
            else:
                print('Invalid currency')
        else :
            print('Invalid currency')
        
    else:
        print('Invalid amount')
