if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        cmd_parts = input().split()
        command = cmd_parts[0]

        if command == 'insert':
            i, e = int(cmd_parts[1]), int(cmd_parts[2])
            my_list.insert(i, e)
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            e = int(cmd_parts[1])
            my_list.remove(e)
        elif command == 'append':
            e = int(cmd_parts[1])
            my_list.append(e)
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
