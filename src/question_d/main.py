from question_d import get_day_of_week

def main():
    while True:
        quit = input("Do you want to exit? (Y/N): ").lower()
        if quit == 'n':
            num = int(input("give number: "))
            result = get_day_of_week(num)
            print(f"The day of {num} is {result}")
        elif quit == 'y':
            print("Quit")
            break
        else:
            print("invalid")
main()