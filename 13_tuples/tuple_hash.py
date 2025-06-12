if __name__ == '__main__':
    n = int(input())                      # Read number of elements
    integer_list = tuple(map(int, input().split()))  # Convert input into a tuple of integers
    print(hash(integer_list))            # Print the hash of the tuple
