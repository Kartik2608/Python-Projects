print("Welcome to my computer quiz!")
playing = input("Do you want to play?Type Yes or No ").lower()

if playing != "yes":
    quit()

print("Okkay! Let's Play :)")
score = 0

Answer = input("What does CPU stands for? ").lower()
if Answer == "central processing unit":
    print("Correct answer Man!")
    score += 1
else:
    print("OH! oh.. ")
    print("Incorrect!!")

Answer = input("What does GPU stands for? ").lower()
if Answer == "graphic processing unit":
    print("Correct answer Man!")
    score += 1
else:
    print("OH! oh.. ")
    print("Incorrect!!")

Answer = input("What does RAM stands for? ").lower()
if Answer == "random access memory":
    print("Correct answer Man!")
    score += 1
else:
    print("OH! oh.. ")
    print("Incorrect!!")

Answer = input("What does PSU stands for? ").lower()
if Answer == "power supply":
    print("Correct answer Man!")
    score += 1
else:
    print("OH! oh.. ")
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")