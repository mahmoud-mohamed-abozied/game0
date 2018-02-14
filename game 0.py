coins = 21
while (coins > 0):
  while True:
    player_one = input("player_one please enter your number")
    if player_one in [1,2,3]:
        break
  coins = coins-player_one
  if(coins <= 0):
    print ("player_two is the winner")
    break
  else:
    print ("coins now is ",coins)
  while True:
    player_two = input("player_two please enter your number")
    if player_two in [1,2,3]:
          break
  coins = coins-player_two
  if(coins <= 0):
    print ("player_one is the winner")
    break
  else:
    print ("coins now is ",coins)
