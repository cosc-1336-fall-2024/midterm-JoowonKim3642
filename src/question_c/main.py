from question_c import use_global

global_var = 0

def main():

    print(f"Before modification: {global_var}")
    use_global()
    print(f"After modification: {global_var}")

main()