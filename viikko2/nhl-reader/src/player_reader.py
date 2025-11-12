import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
    
    def get_players(self):
        self.response = requests.get(self.url).json()

        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

        return self.players
