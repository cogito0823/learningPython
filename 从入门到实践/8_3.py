def make_shirt(size, slogon="I love Python"):
    print(f"Your shirt's size is {size}, and says \"{slogon}\"")

def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

a = 1

def modify():
    a += 1

if __name__ == "__main__":
    a = 1
    modify()
