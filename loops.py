
# increasing value
num1 = 1
while num1 <= 100:
    print(num1)
    num1 += 1
    print(num1)

# decreasing value
count = 10
while count >= 1:
    print(count)
    count -= 1

# break and continue statements
# continue skips a value
x = 100
while x <= 105:
    print(x)
    if x == 103:
        break
    x += 1
    print(x)

y = 199
while y < 205:
    y += 1
    if y == 202:
        continue
    print(y)


# for loop
for myNum in range(8):
    print(myNum)

for num in range(80, 90):
    print(num)

for number in range(1, 10, 3):
     print(number)


# in arrays
languages = ['Python', 'Java', 'C++', 'Javascript']
for lang in languages:
    print(lang)

