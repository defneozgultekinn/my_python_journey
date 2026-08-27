secret_word= "Unicorn"
guess=""
guess_count= 0

while guess != secret_word:
    if guess_count<3:
        guess = input("Enter your guess: ")
        guess_count+=1

    else:
        print("You lost")
        break     #we need to break the loop otherwise it will be an infite loop


if guess == secret_word:
    print("You win")



