name = input("Enter Your Name : ")
goal = input("Your today's goal : ")
with open("journal.txt","a") as file:
    file.write(f"Name :{name}\nGoal : {goal} \n")