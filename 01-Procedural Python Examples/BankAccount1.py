account_name = 'Joe'
account_balance = 100
account_password = 'soup'

while True:
    print('\nPress b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit\n')
    
    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    
    if action == 'b':
        print('Getting balance:')
        userPassword = input('Please enter the password')
        if userPassword != account_password:
            print('Incorrect Password')
        else:
            print('Your balance is:', account_balance)
            
    elif action == 'd':
        print('Deposit')
        userDepositAmount = input('Please enter amount to deposit')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password')
        
        if userDepositAmount < 0:
            print('You cannot Deposit a negative amount')
        elif userPassword != account_password:
            print('Incorrect Password')
        else:
            account_balance = account_balance + userDepositAmount
            print('Your new balance is:', account_balance)
            
    elif action == 's':
        print('Show:')
        print('     Name', account_name)
        print('     Balance', account_balance)
        print('     Password', account_password)
    
    elif action == 'q':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter amount to deposit')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password')
        
        if userWithdrawAmount < 0:
            print('You cannot Withdraw a negative amount')
        elif userPassword != account_password:
            print('Incorrect Password')
        
        elif userWithdrawAmount > account_balance:
            print('Insufficient Balance')
        else:
            account_balance = account_balance - userWithdrawAmount
            print('Your new balance is:', account_balance)
    