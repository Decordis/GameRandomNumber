import random

ai_number = str(random.randint(10, 999))
def game():
    count = 0
    while True:
        count += 1
        if count == 31:
            print("Sorry, but AI win")
            print(f'AI made {ai_number}')
            break
        try:
            answer = int(input('Your idea?'))
            if answer<10 or answer>999:
                print("Sorry, but that's not really the case")
                print('Try again')
                continue

        except ValueError:
            print('Wait, we use numbers! Not symbols or letters!!!')
            continue

        answer = str(answer)


        if answer == ai_number:
            print("WOW, U\'ve done it!! \n Great!!")
            break

        elif answer[:2] in ai_number or answer[1:] in ai_number:
            print('U guessed right 2 int')
            continue


        elif (answer[0] in ai_number or
              answer[1] in ai_number or
              answer[2] in ai_number):
            print('U guessed right 1 int')
            continue

        else:
            print("U didn't guess anything")
            continue