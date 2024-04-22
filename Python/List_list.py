""" Develop a Python script using a list of lists to manage and analyze a basketball team's
performance data, including player names, points, rebounds, and assists per game.
Operations:
1. Populate Data: Prompt for input to add each player's data to a nested list called players_data.
2. Team Averages: Calculate and display the team's average points, rebounds, and assists.
3. Identify Star Player: Determine and print the player with the highest combined score (points + rebounds + assists)."""

players_data=[]

np=int(input("Enter number of players"))

for i in range(np):
                    print(f"Enter the data for player {i+1}")
                    name= input("Enter player name")
                    points=int(input("Enter player points"))
                    rebounds=int(input("Enter player rebounds"))
                    assists=int(input("Enter player assists"))
                    players_data.append([name,points,rebounds,assists])


def average(players_data):
                            avg_points = sum( player[1] for player in players_data )/ len(players_data)
                            avg_rebounds=sum(player[2] for player in players_data)/len(players_data)
                            avg_assists=sum(player[3] for player in players_data)/len(players_data)

                            print(f"The average points is {avg_points: .2f}")
                            print(f"The average rebounds is {avg_rebounds: .2f}")
                            print(f"The average rebounds is {avg_rebounds: .2f}")

def star(players_data):
                          high_score=-1;
                          star_player =" "
                          for player in players_data:
                                                     total_score= player[1] + player[2] + player[3]
                                                     if total_score>high_score:
                                                                                 high_score=total_score
                                                                                 star_player=player[0]
                          print(f"The highest score is {total_score}")
                          print(f"The name of highest scorer is {star_player}")

average(players_data)
star(players_data)
                          
                          
                          
                                                  
                            
 

