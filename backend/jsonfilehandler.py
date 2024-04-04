import json
import os
class JsonFileHandler:
    def __init__(self):
        self.json_file_path = os.path.join(os.path.dirname(__file__), 'player.json')
        self.player = self.load_json()
        
    def load_json(self):
        try:
            with open(self.json_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
        
    def write_json(self):
        with open(self.json_file_path,'w') as file:
            json.dump(self.player, file, indent=4)
            
    def add_json(self, username, full_name, email, password, wins, draws, loses, total_rounds):
        if username in self.player:
            print('You already create an account!')
            return 0
        self.player[str(username)] = {
            'name': full_name,
            'email':email,
            'password':password,
            'wins':wins,
            'draws':draws,
            'loses':loses,
            'rounds':total_rounds
        }
        self.write_json()
    
    def update_name(self, username, newName):
        if str(username) in self.player:
            x = self.player[str(username)]
            x['name'] = newName
            self.write_json()
        else:
            return 0
    
    def update_password(self, username, password):
        if str(username) in self.player:
            x = self.player[str(username)]
            x['password'] = password
            self.write_json()
        else:
            return 0
    
    def update_email(self, username, newEmail):
        if str(username) in self.player:
            x = self.player[str(username)]
            x['email'] = newEmail
            self.write_json()
        else:
            return 0
    
    def update_wins(self, username, num):
        if str(username) in self.player:
            x = self.player[str(username)]
            current_num = int(x['wins'])
            x['wins'] = current_num + num
            self.write_json()
        else:
            return 0
        
    def update_draws(self, username, num):
        if str(username) in self.player:
            x = self.player[str(username)]
            current_num = int(x['draws'])
            x['draws'] = current_num + num
            self.write_json()
        else:
            return 0
    
    def update_loses(self, username, num):
        if str(username) in self.player:
            x = self.player[str(username)]
            current_num = int(x['loses'])
            x['loses'] = current_num + num
            self.write_json()
        else:
            return 0

    def update_rounds(self, username, num):
        if str(username) in self.player:
            x = self.player[str(username)]
            current_num = int(x['rounds'])
            x['rounds'] = current_num + num
            self.write_json()
        else:
            return 0