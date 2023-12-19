import random

print("\n************** Welcome to the game **************\n\n\t\tRock_Paper_Scissor\n")
pname = input("Please enter your name: ")

options = ["R", "P", "S"]

comp_score = 0
user_score = 0
attempts = 10

while attempts > 0:
    user_inp = input("\nChoose any (R/P/S): ").upper()
    comp_inp = random.choice(options)

    if user_inp not in options:
        print("Invalid input!")
        break

    if user_inp == comp_inp:
        print(f"Turn tie!\n\n{pname} input {user_inp} and Computer input {comp_inp}")

    elif user_inp == 'R' and comp_inp == 'S':
        print(f"{pname} Won!\n\n{pname} input {user_inp} and Computer input {comp_inp}")
        user_score += 1

    elif user_inp == 'P' and comp_inp == 'R':
        print(f"{pname} Won!\n\n{pname} input {user_inp} and Computer input {comp_inp}")
        user_score += 1

    elif user_inp == 'S' and comp_inp == 'P':
        print(f"{pname} Won!\n\n{pname} input {user_inp} and Computer input {comp_inp}")
        user_score += 1

    else:
        print(f"Computer Won!\n\n{pname} input {user_inp} and Computer input {comp_inp}")
        comp_score += 1
    
    attempts -= 1
    print("Remaining attempts: ", attempts)


if user_score > comp_score:
    print("\n*************************************************\n")
    print(f"{pname} Won the game\n{pname} got {user_score} and Computer got {comp_score}")
    print("\n*************************************************\n")
elif comp_score > user_score:
    print("\n*************************************************\n")
    print(f"Computer Won the game\n{pname} got {user_score} and Computer got {comp_score}")
    print("\n*************************************************\n")
else:
    print("\n*************************************************\n")
    print(f"Game tie!\n{pname} got {user_score} and Computer got {comp_score}")
    print("\n*************************************************\n")