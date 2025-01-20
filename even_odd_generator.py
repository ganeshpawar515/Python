inp=input("Enter 'even' or 'odd' to generate numbers:")
print(inp)

if inp=='even':
    print("generating even numbers")
    count=int(input("Enter Upper limit: "))
    for i in range(count):
        if i%2==0:
            print(i)
elif inp=='odd':
    print("Generating odd numbers")
    count=int(input("Enter Upper limit: "))
    for i in range(count):
        if i%2!=0:
            print(i)
