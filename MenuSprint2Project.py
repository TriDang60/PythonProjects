"""Menu of What I learned in COP 1500"""
__author__ = "Tri Dang"

import math


def main():
    """
    All the functions of the menu
    Every individual set of  the menu is under main

    """
    print(
        "Welcome to my summary of what I've learned expressed through a menu!")
    continue_program = True
    while continue_program:

        print(
            "Enter number for which program you would like to use at the "
            "bottom.")
        print(
            "1. Average Sports Points Calculator")  # Enter scores from your
        # favorite teams over the season to
        # see how many points they averaged
        print(
            "2. Reverse Input Staircase")  # Upside down staircase with
        # numbers of your input
        print("3. Area of a Triangle")
        print("4. Surprise!")
        print("5. Square root")  # no bad input allowed through the use of try
        print(
            "6. Even and Negative Number Detector")  # detects and
        # determines if number is even and negative.
        print(
            "7. Factor Checker")  # takes user input and sees if the second
        # user input is an factor of that number
        print(
            "8. Guess the correct words")  # If the word meets the
        # requirement it is valid
        print(
            "9. Simple Scorekeeper")  # sprint 1, easy scorekeeper changed
        # for more efficiency and less redundancy
        print("10. Close the program.")
        good_input = False
        user_choice = 0
        while not good_input:  # cannot enter a letter or word, only numbers
            try:
                user_choice = int(input("Number: "))
                good_input = True
            except ValueError:
                print("That was not a valid number. Please try again.")

        if user_choice == 1:  # average points calculation
            good_input = False
            total_average = 0
            total_num = 0
            while not good_input:
                average_accumulator = input(
                    "Enter a score or enter a -1 when you "
                    "are finished entering scores:")
                # they keep adding numbers to the average and
                # divide by the total amount of times they inputted
                while input_validation(average_accumulator):
                    if int(average_accumulator) > 0:
                        total_average += int(average_accumulator)
                        total_num += 1
                        average_accumulator = input(
                            "Enter a score or enter a -1 when you "
                            "are finished entering scores:")
                        # -1 indicates end of the code
                    else:
                        average = total_average / total_num
                        good_input = True
                        print("Average points are "
                              "about: {:,.0f} ".format(average))
                        break
                else:
                    print("That was not a valid number. Please try again.")
        elif user_choice == 2:  # inverted stairs
            good_input = False
            while not good_input:
                try:
                    row = int(
                        input(
                            "Enter number of rows:"))  # rows and columns
                    # are affected by the arguments and the input
                    good_input = True
                    for column in range(1, row + 1):
                        for height in range(1, row - column + 2):
                            print(height, end=" ")
                        print()
                except ValueError:
                    print("That was not a valid number. Please try again.")
        elif user_choice == 3:  # triangle area (square units)
            base = int(input("Please enter the base:"))
            height_tri = int(input("Please enter the height:"))
            print("The area of this triangle is: ",
                  calculate_area(base, height_tri))
        elif user_choice == 4:  # surprise (heart)
            heart_input = input(
                "Enter the word, epic , for a surprise!: ")  # epic triggers
            # the heart
            while heart_input != "epic":  # getting rid of bad input
                heart_input = input("Please enter the valid word: ")
            if heart_input == "epic":
                print("  __---__      __---__  ")  # heart
                print("|        ______         |")
                print("|                       |")
                print("|                       |")
                print("|                       |")
                print(" --                   --")
                print("   --               --")
                print("     --           --")
                print("        --      --")
                print("           ----")
                print(" I LOVE PYTHON!!!!!!!!!")
        elif user_choice == 5:  # square root
            good_input = False
            while not good_input:  # cannot enter a letter or word, only
                # numbers
                try:
                    num = int(input(
                        "Please enter a number you want to find the square "
                        "root of: "))  # simple square root problem
                    good_input = True
                    print(square_root(num))
                except ValueError:
                    print("That was not a valid number. Please try again.")
        elif user_choice == 6:  # pos, neg, and odd or even
            good_input = False  # prevent words form being entered
            while not good_input:
                try:
                    user_num = int(input(
                        "Checking for positive,negative and even or odd, "
                        "please enter a number: "))
                    good_input = True
                    if user_num > 0 and user_num % 2 == 0:
                        print("The number" + " " + str(
                            user_num) + " " "is positive and even.")
                        # all possible outcomes of positive, negative,even,
                        # or odd
                    elif user_num < 0 and user_num % 2 == 0:
                        print("The number" + " " + str(
                            user_num) + " " "is negative and even.")
                    elif user_num > 0 and user_num % 2 != 0:
                        print("The number" + " " + str(
                            user_num) + " " "is positive and odd.")
                    elif user_num < 0 and user_num % 2 != 0:
                        print("The number" + " " + str(
                            user_num) + " " "is negative and odd.")
                except ValueError:
                    print("That was not a valid number. Please try again.")
        elif user_choice == 7:  # factorisable numbers
            good_input = False
            while not good_input:
                try:
                    integer = int(input(
                        "Pick the number that is going to be determined if "
                        "it is factorisable: "))
                    factor = int(input(
                        "Pick the number it is going to possibly be factored "
                        "by: "))
                    good_input = True
                    if not integer % factor != 0:  # shows that it is
                        # factorisable because there is no remainder
                        print(str(factor) + " " + "is a factor of" + " " + str(
                            integer) + ".")
                    if not integer % factor == 0:  # if there is a remainder
                        # it is not a factor, if not makes it true
                        # when integer % factor is not == 0 which triggers
                        # the print function
                        print(str(
                            factor) + " " + "is not a factor of" + " " + str(
                            integer) + ".")
                except ValueError:
                    print("That was not a valid number. Please try again.")
        elif user_choice == 8:  # guess the word
            print(
                "Guess the valid word, if it is the correct answer, it will "
                "be valid! ")
            # word to be guessed is specifically pear
            print(
                "There is one specific word that will automatically be "
                "accepted, it is a fruit.")
            user_word = input("Enter a word: ")
            while user_word != "pear" or user_word.isdigit():
                # if any digits are found it is incorrect
                user_word = input(
                    "Incorrect! Hint: The specific word is a fruit"
                    "Take another guess: ")
            if user_word == "pear":
                print("Correct! The specific word was pear!")
        elif user_choice == 9:  # old code new and improved
            # intro and welcoming
            print("Hello, Welcome to Scorekeeper!", sep='')
            start = input("Enter a name: ")
            print("Introducing contestant," + " " + start + "!")

            # final score
            fi_score = 1 // 1
            print("Welcome to Scorekeeper" + " " + str(fi_score) + ".0")

            good_input = False
            while not good_input:  # cannot enter a letter or word, only number
                try:
                    # initial score variable
                    initial = 0
                    in_score = 0
                    print("Initial Score:" + str(in_score))
                    good_input = True
                    f_score = input("Enter a 1 to begin: ")
                    while int(f_score) == 1:
                        initial = initial + 1 ** 1
                        f_score = input("Enter 1 for right answer: ")
                        print("Score:" + str(initial))
                    print(
                        "Congrats" + " " + start + "!" +
                        "\nYou've reached the end!")
                    print("Thank you for using this program", end='')
                    print(" " + start + "!")
                    print("Goodbye" * 5)
                except ValueError:
                    print("That was not a valid number. Please try again.")

        elif user_choice == 10:  # quit program
            continue_program = False
        else:
            print("Please enter a valid number.")


def calculate_area(base, height_tri):
    """
    Calculates the area of a triangle
    Base is the base of the triangle
    Height refers to the height of the triangle
    :param base:
    :param height_tri:
    :return:
    """
    return (base * height_tri) / 2


def square_root(num):
    """
    Takes the square of a user inputted number
    Num is user inputted number that is going to be square rooted
    :param num:
    :return:
    """
    return math.sqrt(num)


def input_validation(average_accumulator):
    """
    Validate the input of average accumulator so only good input is detected
    :param average_accumulator: points that are inputted & will be calculated
    in the total average
    :return:
    """
    try:
        int(average_accumulator)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    main()
