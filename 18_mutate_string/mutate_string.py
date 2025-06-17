# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    print("Welcome to the String Mutator!")
    s = input("Enter the original string: ")
    while True:
        try:
            i = int(input(f"Enter the position to mutate (0 to {len(s)-1}): "))
            if 0 <= i < len(s):
                break
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Please enter a valid integer.")
    c = input("Enter the new character: ")[0]
    s_new = mutate_string(s, i, c)
    print(f"Mutated string: {s_new}")
