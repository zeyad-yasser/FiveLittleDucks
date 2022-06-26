import random 



userScore=0
computerScore=0
InputList=["rock","paper","scissors"]

while True:
    userOpt=input("Type ( Rock , Paper , Scissors )  OR 'q' for quit: ").lower()
    if userOpt == "q":
        break
    elif userOpt not in InputList:
       continue
    else:
       ComputerIn= random.randint(0,2)
       ComputerOpt=InputList[ComputerIn] 
       print("Computer Picked",ComputerOpt)
       if ComputerOpt == "rock" and userOpt == "paper": 
          userScore+=1
       elif userOpt == "rock" and ComputerOpt == "scissors":
        userScore+=1
       elif userOpt == "paper" and ComputerOpt == "rock":
        userScore+=1
       else:
        computerScore+=1 

    if computerScore > userScore:
        print("You Loss ... ", "Computer Score",computerScore,"Your Socre",userScore)
    elif computerScore < userScore:
        print("You Win ... ", "Computer Score",computerScore,"Your Socre",userScore)
    else:
        print("Draw ... ", "Computer Score",computerScore,"Your Socre",userScore)