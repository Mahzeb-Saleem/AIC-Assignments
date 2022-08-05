rows = int(input('Enter number of rows: '))

# Upper part of diamond
for i in range(1, rows+1):
    for j in range(1,rows-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print((rows+1-i), end="")
        else:
            print(" ", end="")
    print()

# Lower part of diamond
for i in range(rows-1,0, -1):
    for j in range(1,rows-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print((rows+1-i), end="")
        else:
            print(" ", end="")
    print()