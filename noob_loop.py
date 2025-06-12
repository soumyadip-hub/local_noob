#loops-----> for loop
for num in range(1,21):
    print(num)

    if num % 2 == 0:
        print(f"{num} i even")
    elif num == 4 or num == 13:
        print(f"{num} is unlucky")
    else:
        print(f"{num} is odd")

# loop ------>while loop------
num = 1 
while num < 11:
    print(num)
    num += 2
#------------------
msg = input("whats the secret password? ")
while msg != "bananas":
    print("WRONG!")
    msg = input("what's the secret password?")
print("CORRECCT!")