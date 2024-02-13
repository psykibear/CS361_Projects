from os import system, name


def homePage():
    print("Choose what you would like to do:\n"
          "\n\t1. View the movie List by Category\n"
          "\t2. Add a movie\n"
          "\t3. Rent a movie\n"
          "\t4. Return a movie\n"
          "\t5. Delete a movie\n"
          "\t6. Exit the Library\n")  # display options


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("\t\t\t Welcome to Bearly Rentals!!!\n")


def category():
    print("What genre movie are you interested in watching? "
          "\n\n"
          "Choose from the following:"
          "\n\n"
          "\t1. Action and Adventure\n"
          "\t2. Animation\n"
          "\t3. Comedy\n"
          "\t4. Crime\n"
          "\t5. Drama\n"
          "\t6. Horror\n"
          "\t7. SciFi and Fantasy\n"
          "\t8. Thriller\n")
