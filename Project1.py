print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()

print("Okay! Let's play ")

answer=input("what does CPU stnad for? ")
if answer == "central processing unit":
    print("Correct!")