import random
import json
import os


class TournamentTable():
    def __init__(self, data_path, save_file):
        self.data_path = data_path
        self.save_file = save_file
        self.players = []

    def create_players(self):
        try:        
            with open(self.data_path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: File Not Found {self.data_path}")
            return 0
        
        if not content.strip():
            print(f"Error: Data Empty in {self.data_path}")
            return 0
        
        for line in content.splitlines():
            if not line.strip():
                continue
            
            self.players.append(line)
        
        return self.players
    
    def vs_players(self):

        vs = ["", "Vs", ""]
        
        vs[0] = random.choice(self.players)
        vs[2] = random.choice(self.players)
        
        return vs
        
    def create_json_table(self):
        table_len = len(self.players)
        table = {}
        team = 1
        
        if table_len % 2:
            print("Players Must Be Even !")
            return 0

        while True:

            vs_list = self.vs_players()
            
            if vs_list[0] != vs_list[2]:

                table[f"Match {team}"] = [vs_list[0], vs_list[2]]
                team += 1
                
                index_0 = self.players.index(vs_list[0])
                self.players.pop(index_0)

                index_2 = self.players.index(vs_list[2])
                self.players.pop(index_2)
                
                if not self.players:
                    break
                pass
        
        with open(self.save_file, "w") as file:
            json.dump(table, file, indent=2)
        
        print("Sucessfully Matches Saved on:", {self.save_file})
        print("To Print The Output Enter '1337':")
        try:
            x = input()

            if x == '1337':
                self.format_json()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("! Wrong PassKey !")
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Got You ;)\nYou Are Under Arrest By The Campus Law !\033")
            return
    
    def format_json(self):
        
        with open(self.save_file, "r") as file:
            content = file.read()
            content = eval(content)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Matches Output:\n\n")
        
        for _, names in content.items():
            print(" " * 4, "|", names[0], "Vs", names[1])


tournament = TournamentTable(data_path="data.txt", save_file="done.json")
int_error = tournament.create_players()
if int_error != 0:
    tournament.create_json_table()
