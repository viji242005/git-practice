a = input("Enter a number: ")

if a %2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 

for i in range(1, 11):
    print(i)
    
while a < 10:
    print("The number is less than 10.")
    a += 1

for i in range(5):
    print("This is iteration number", i)

def number_square(num):
    return num ** 2

print("The square of 5 is", number_square(5))

print("This is a simple program to try switch between commits.")