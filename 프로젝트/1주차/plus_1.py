#21
class Player:
    def __init__(self,name,position,jersey_number):
        self.name=name
        self.position=position
        self.jersey_number=jersey_number

class Team:
    def __init__(self,name):
        self.name=name
        self.players=[]

    def add_player(self,player):
        self.players.append(player)


    def get_team_info(self):
        info=f"{self.name} 팀: \n"
        for player in self.players:
            info += f"  {player.jersey_number}번 {player.name} ({player.position})\n"
        return info
 
p1=Player("홍길동","FW",9)
p2=Player("김철수","MF",7)
team=Team("FC")
team.add_player(p1)
team.add_player(p2)

print(team.get_team_info())