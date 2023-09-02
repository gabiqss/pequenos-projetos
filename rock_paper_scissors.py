import random

# r > s   p > r   s > p

def rock_paper_scissors():
    user = input('rock (r), paper (p), or scissors (s)? ')
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
    if win(user, computer):
        return 'you won'
    return 'you lost'
    
def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(rock_paper_scissors())