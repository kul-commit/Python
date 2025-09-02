"""
number of games  played in a tournament. Ask the user number of games won and number of games loss. calculate number of tie and total points( 1 win = 4 points , 1 tie = 2points)
"""

Total_games = int(input("Enter no of games played:"))
Game_won = int(input("Enter no of games won:"))
Game_loss = int(input("Enter no of game loss:"))

game_tie =  Total_games - Game_won - Game_loss

print(f"game tied: {game_tie}")

total_points =  (Game_won*4)+(game_tie*2)

print(f"Total Points :{total_points}")