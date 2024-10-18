import random
def RPS():
    user = input("What's your choice? 'r' for Rock, 'p' for paper, 's' for scissors \n").lower()
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        print("Match Tied!!")
    if who_wins(user, computer):
        return "You win!"
    else:
        return "You lose!"

def who_wins(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
            
    
print(RPS())