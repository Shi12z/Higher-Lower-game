from art import logo,vs
from gamedata import data
import random
print(logo)
score=0
account2=random.choice(data)

game_continue=True
while(game_continue):
    account1=account2
    account2=random.choice(data)
    if account1==account2:
        account2=random.choice(data)


    def format_data(account):
        account_name=account["name"]
        account_dec=account1["description"]
        account_cou=account1["country"]
        return f"{account_name},a {account_dec},from {account_cou}"


    def check_answer(guess,account1,account2):
        if a_follower>b_follower:
            return guess=='A' #CHECKING IF A IS GREATER THAN B AND USER GUESS IS A
        else:
            return guess=='B'


    print(f"Compare A:{format_data(account1)}.")
    print(vs)
    print(f"Against B:{format_data(account2)}.")
    


    guess=input("Who has more followers ?Type 'A' or 'B' ").lower()
    
    a_follower=account1["follower_count"]
    b_follower=account2["follower_count"]


    is_correct=check_answer(guess,a_follower,b_follower)
    if is_correct:
        score+=1
        print("You are correct,Current score is",score)
    else:
        print("You are incorrect.Final Score",score)
        game_continue=False
    