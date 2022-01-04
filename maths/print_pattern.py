def printPat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print(i*[j])

if __name__ == '__main__':
    printPat(3)