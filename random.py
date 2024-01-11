import random

def generate_random_number():
    return random.randint(1, 10)

if __name__ == "__main__":
    random_number = generate_random_number()
    print('The Random Number is: ')
    print("This will be going to be printed...")        
    print("Random number:", random_number)


