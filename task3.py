from datetime import date
from random import randint


def greetings(msg):
    print(msg)


def register():
    print('Register an Account')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    username = input('Enter your username: ')
    email = input('Enter your email address: ')

    while True:
        password = input('Enter the password you wanna use: ')
        password2 = input('Confirm your password: ')
        if password == password2:
            break
        else:
            print('The password you entered doesnt match, try again')

    account_number = randint(1000000000, 3000000000)
    print(
        f'''
        Congrats user created succesfully, 
        your data is saved and safe.
        Account number generated succesfully {account_number}
        '''
    )

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'email': email,
        'password': password,
        'account_number': account_number
    }

    return data


def login():
    print('Login to the system')

    username = input('Enter you username: ')
    password = input('Enter your password: ')

    data = {
            'username': username,
            'password': password
        }
    return data


def do_bankings(username):
    today = date.today()
    print(f'Welcome {username}')
    print(today.strftime('%B %d, %Y'))
    print('1. Withdrawal')
    print('2. Cash deposit')
    print('3. Complaint')

    while True:
        try:
            selected_option = int(input('Please select an option from the above(Must be a number): '))
        except ValueError:
            print('invalid input, try again')
        else:
            break

    if selected_option == 1:
        while True:
            try:
                withrawal_amount = int(input('How much would you like to withdraw? '))
            except ValueError:
                print('Invalid input, try again')
            else:
                break

        print(f'£{withrawal_amount} cash succesfully withdrawn')
        print('Take your cash!')

    elif selected_option == 2:
        current_balance = 0
        while True:
            try:
                deposit_amount = float(input('How much would you like to deposit? '))
            except ValueError:
                print('Invalid input, try again')
            else:
                break

        current_balance += deposit_amount
        print('Cash deposited successfully')
        print(f'You current balance is: £{current_balance}')

    elif selected_option == 3:
        complaint = input('What issue will you like to report? ')
        print(f'Dear {username}, your report "{complaint}" is under review')
        print('Thank you for contacting us')


def main():
    greetings('Welcome')
    print('Register an account to login to the system')

    # This line execute the function and return sign up info, which is save in the saved_login_data variable
    saved_login_data = register()

    # Get the user username from the saved sign up data
    username = saved_login_data['username']
    # Get the user password from the saved sign up data
    password = saved_login_data['password']

    while True:
        login_in_info = login()
        if login_in_info['username'] == username and login_in_info['password'] == password:
            print('login succesfully')
            do_bankings(username)
            break

        else:
            print('Incorrect username or password, Try again')


main()
