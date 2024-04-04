from backend import jsonfilehandler
from blackjack import gamehandler

jsonHandler = jsonfilehandler.JsonFileHandler()
gameHandler = gamehandler.GameHandler()


def user_account_interface():
    user_name = input('Enter full name: ').lower()
    user_email = input('Enter an email address: ').lower()
    user_id = input('Create a username: ')
    user_password = input('Create a password: ')
    jsonHandler.add_json(user_id,user_name,user_email,user_password,0,0,0,0)
    
    
    
    

    