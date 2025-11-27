# Print even numbers up to user limit
n = int(input("Enter a number limit: "))
print("Even numbers up to", n, ":")

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")
