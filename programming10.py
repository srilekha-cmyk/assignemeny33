n = int(input("Enter number: "))
s = 0

while n > 0:
    d = n % 10
    s += d
    n //= 10

print(s)

# Input:
# 1234
# Output:
# 10
