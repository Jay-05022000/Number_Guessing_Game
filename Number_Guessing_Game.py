'''Number guessing game
you have to set default number by yourself
you will give user a limited chance to guess the number and
at each guess u will tell user about remaining attempts and about his/her guess'''

default=36
total_attempts=5
current_attempts=1
while (current_attempts <= total_attempts):
    guess=int(input("enter a number: "))
    if guess==36:
        print("congratulations,you win")
        break

    else:
        print('wrong guess\n')
        left_attempts=total_attempts-current_attempts
        print("left attempts: ",left_attempts)
        if left_attempts==0:
            print("game over")
            break
        else:
            current_attempts += 1
            continue