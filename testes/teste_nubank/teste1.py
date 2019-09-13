# tags: strings,

def usernamesSystem(u):
    # Write your code here

    if __name__ == '__main__':
        fptr = open(os.environ['input001.txt'], 'w')

        u_count = int(input().strip())

        u = []

        for _ in range(u_count):
            u_item = input()
            u.append(u_item)

        result = usernamesSystem(u)

        fptr.write('\n'.join(result))
        fptr.write('\n')

        fptr.close()

