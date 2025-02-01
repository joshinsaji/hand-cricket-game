import random

def hand_cricket():
    print("Welcome to Hand Cricket!")
    # Toss
    user_toss = input("Choose heads or tails: ").strip().lower()
    computer_toss = random.choice(["heads", "tails"])

    print(f"Computer chose: {computer_toss}")

    if user_toss == computer_toss:
        print("You won the toss!")
        toss_choice = random.choice(["bat", "bowl"])
        print(f"You randomly chose to {toss_choice} first.")
    else:
        print("Computer won the toss!")
        toss_choice = random.choice(["bat", "bowl"])
        print(f"Computer chose to {toss_choice} first.")

    if toss_choice == 'bat':
        print("You are batting first!")
        player_score = play_innings(player_bats=True)
        print(f"Your score: {player_score}")
        print("Computer is chasing!")
        computer_score = play_innings(player_bats=False, target=player_score)
    else:
        print("Computer is batting first!")
        computer_score = play_innings(player_bats=False)
        print(f"Computer's score: {computer_score}")
        print("You are chasing!")
        player_score = play_innings(player_bats=True, target=computer_score)

    # Results
    if player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("You lose!")
    else:
        print("It's a tie!")


def play_innings(player_bats, target=None):
    score = 0
    while True:
        try:
            if player_bats:
                player_run = int(input("Enter your run (1-6): "))
                if player_run not in range(1, 7):
                    print("Invalid input! Please enter a number between 1 and 6.")
                    continue
            else:
                player_run = random.randint(1, 6)

            if player_bats:
                computer_run = random.randint(1, 6)
            else:
                computer_run = int(input("Enter your run (1-6): "))
                if computer_run not in range(1, 7):
                    print("Invalid input! Please enter a number between 1 and 6.")
                    continue

            print(f"You: {player_run}, Computer: {computer_run}")

            if player_run == computer_run:
                print("Out!")
                break

            score += player_run if player_bats else computer_run

            if target and score > target:
                print("Target achieved!")
                break

            print(f"Score: {score}")

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 6.")

    return score


if __name__ == "__main__":
    hand_cricket()
