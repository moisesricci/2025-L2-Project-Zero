# Functions go here
def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            #check if the response is the entire word
            if response == item:
                return item

            #check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main Routine goes here
levels = ['easy', 'medium', 'hard']

like_coffe = string_check(question="Do you like coffe? ", valid_ans_list=['yes', 'no'])
print(f"You chose {like_coffe}")
choose_level = string_check("Choose a level: ", levels)
print(f"You chose {choose_level}")
next_level = string_check("Choose the next level: ", levels)
print(f"You chose {next_level}")
