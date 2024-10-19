#use global

global_var = 0

def use_global():
    global global_var
    print(f"Before modification: {global_var}")
    global_var = 10
    print(f"After modification: {global_var}")
    return global_var