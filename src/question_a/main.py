from question_a import get_random_number

def main():
    while True:
        quit = input("Do you want to exit? (Y/N): ").lower()
        if quit == 'n':
            num = get_random_number()
            while True:
                answer = int(input("Guess the random number: "))
                if answer == num:
                    print("congratulations")
                    break
                else:
                    print("try again")
                    continue
        elif quit == 'y':
            print("Quit")
            break
        else:
            print("invalid")
main()