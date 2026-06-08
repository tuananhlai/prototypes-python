if __name__ == '__main__':
    N = int(input())
    a_list = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            a_list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(a_list)
        elif cmd[0] == 'remove':
            a_list.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            a_list.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            a_list.sort()
        elif cmd[0] == 'pop':
            a_list.pop()
        elif cmd[0] == 'reverse':
            a_list.reverse()