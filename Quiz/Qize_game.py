


print ("Welcome to this small quiz !")
playing = input ("Do you want to play ? ")
playing = playing.lower()

if playing != "yes":
   quit()

score=0

print(" Okay! Let's play :) ... " )

answer = input ("what does CPU stands for ? ")
answer=answer.lower()
if answer =="central processing unit":
    print ('Correct ')
    score +=1
else:
    print("Sorry you are wrong")


answer = input ("what does GPU stands for ? ")
answer=answer.lower()
if answer=="graphics processing unit":
    print ('Correct ')
    score +=1
else:
    print("Sorry you are wrong")


answer = input ("what does RAM stands for ? ")
answer=answer.lower()
if answer=="random access memory":
    print ('Correct ')
    score +=1
else:
    print("Sorry you are wrong")


answer = input ("what does PSU stands for ? ")
answer=answer.lower()
if answer=="power supply unit":
    print ('Correct ')
    score +=1
else:
    print("Sorry you are wrong")


    print("You Got " + str(score) + " Qustions Right..")