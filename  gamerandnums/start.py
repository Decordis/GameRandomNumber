from gamefunc import game
import time

def start_or_quit():
    while True:
        try:
            ask = int(input('So, do u want to play? 1 - Yes, 2 - No'))
            if ask not in range(1, 3):
                print('Oh, I don\'t understand')
                print('Try again please')
                continue

        except ValueError:
            print("Sorry, but we use only numbers! :'(")
            continue

        if ask == 1:
            print('Oh, yeh!!')
            print('So, give me 5 second')
            time.sleep(5)
            print('Well, I made a number!')
            print('Good luck!!')
            game()
            continue

        else:
            print('Well, goodbye and have a nice day!;)')
            input("Click 'Enter' to close")
            break