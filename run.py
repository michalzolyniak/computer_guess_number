if __name__ == '__main__':
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    ATTEMPTS = 10
    min_num = MIN_NUMBER
    max_num = MAX_NUMBER

    print(f"Think of a whole number from range {MIN_NUMBER} to {MAX_NUMBER} "
          f"and I will try to guess it in {ATTEMPTS} tries.")
    user_input = input(f"Click enter when you will be ready:")
    computer_attempt = 1
    bad_answer = False
    guess = 0

    while True:
        print("computer_attempt", computer_attempt)
        if computer_attempt > ATTEMPTS:
            print("Sorry. I have not guess your number:(")
            break
        if not bad_answer:
            guess = int((max_num - min_num) / 2) + min_num
        bad_answer = False
        print(f"I am guessing the number {guess}")
        user_input = input(f"Enter too many or too small or guessed:")
        if user_input == "guessed":
            print("I have won!!!")
            break
        elif user_input == "too many":
            max_num = guess
            computer_attempt += 1
            continue
        elif user_input == "too small":
            min_num = guess
            computer_attempt += 1
            continue
        else:
            print("Do not cheat!!!")
            bad_answer = True
