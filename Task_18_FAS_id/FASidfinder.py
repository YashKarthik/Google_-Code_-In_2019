from fedora.client.fas2 import AccountSystem 
from fedora.client import AuthError
from termcolor import colored, cprint

cprint("""
            ____________________            _______              ____________________
           ||___________________|          /       \             |___________________|
           ||                             /         \            |  
           ||________________            /           \           |  
           ||________________|          /             \          |
           ||                          /_______________\         |___________________
           ||                         /_________________\        |__________________ |
           ||                        /                   \                           |
           ||                       /                     \                          |  
           ||                      /                       \      ___________________|
           ||                     /                         \    |___________________|
                      """, 'yellow')

def get_email(username):
    USER_NAME = str(input("Enter your user name: "))
    PASSWORD = str(input("Enter password: "))
    try:
        fas = AccountSystem(username=USER_NAME, password=PASSWORD)
        people = fas.people_by_key(key='username', search=username, fields=['email'])
        if username in people:
            return people[username]['email']
        return 0 
    except AuthError as e:
        print(str(e))
        exit()


def main():
    username = input('Enter The username you wanna search: ')
    email = get_email(username)
    if email:
        cprint(f'User: {username} Email -> {email}', 'green')
    else:
        cprint('The given user doesn\'t exist', 'red')


if __name__ == "__main__":
    main()