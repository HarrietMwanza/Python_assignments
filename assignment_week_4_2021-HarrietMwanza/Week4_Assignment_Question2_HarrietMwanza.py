def play_again():
    play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        print("proceed to next question")
        return True
    else:
        print("Thanks For Playing! We expect you back again!")
        return False


def founder_name():
    name = "Fred Swaniker"
    return name.lower()

def year_founded():
    return 2015


def campus():
    campuses = "Rwanda and Mauritius"
    return campuses.lower()


def number_of_campus():
    return 2

def dean_name():
    dean = "Gaidi Faraj"
    return dean.lower()


def student_life_head():
    name = "Sila Ogidi"
    return name.lower()


def lab_name():
    name_of_lab = "Nigeria"
    return name_of_lab.lower()


def number_of_cs_students():
    return 30


def number_of_degrees():
    return 8


def headquarters():
    name_of_headquarter = "Mauritius"
    return name_of_headquarter.lower()


#our program logic function
def program_logic():
    while True:
        score = 0
        failed = 0

        print("\nWelcome to Hangman game by Africa Board Rwanda\n")
        name = input("Enter your name here: ")
        print("The game is about to start!\n Let's play Hangman!")
        print("Hello " + name + "! Best of Luck to you!")

        # QUESTIONS
        print("Welcome to the hangman game, you will be asked 10 questions about ALU. Good Luck!")
        question_one = int(input("when was ALU founded? "))
        if question_one == year_founded():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        question_two = input("who founded ALU? ")
        if question_two.lower() == founder_name():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        question_three = input("Where are the ALU campuses? ")
        if question_three.lower() == campus():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        question_four = int(input("How many campuses does ALU have? "))
        if question_four == number_of_campus():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        question_five = input("What is the name of ALU Rwanda dean? ")
        if question_five.lower() == dean_name():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        question_six = input("Who is in charge of Student Life? ")
        if question_six.lower() == student_life_head():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        if failed == 6:
            print("You have hang the man 6 times, the man is dead")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        question_seven = input("What is the name of our Lab? ")
        if question_seven.lower() == lab_name():
            score += 1
        else:
            failed += 1
            # score = score
        if failed == 6:
            print("You have hang the man 6 times, the man is dead")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        while True:
            try:
                question_eight = int(input("How many students do we have in year 2 Cs (put the number of students)? "))
                break
            except ValueError:
                print("Enter a number, a valid response")

        if question_eight == number_of_cs_students():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        if failed == 6:
            print("You have hang the man 6 times, the man is dead")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        question_nine = int(input("How many degrees does ALU offer? "))
        if question_nine == number_of_degrees():
            score += 1
        else:
            failed += 1
            # score = score
            print("You have hang the man!")

        if failed == 6:
            print("You have hang the man 6 times, the man is dead")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        question_ten = input("Where are the headquarters of ALU? ")
        if question_ten.lower() == headquarters():
            score += 1
        else:
            failed += 1
            score = score
            print("You have hang the man!")

        if failed == 6:
            print("You have hang the man 6 times, the man is dead")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        if score == 10:
            print("Congratulations! You got all questions right!")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break
        elif score < 10:
            print(f"You scored {score} and failed {failed} questions \n")
            if play_again():
                score = 0
                failed = 0
                continue
            else:
                print(f"You scored {score} and failed {failed} questions \n")
                break

        # return f"Total score = {score}"

program_logic()

