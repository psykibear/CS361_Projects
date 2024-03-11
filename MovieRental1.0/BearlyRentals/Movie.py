import json
import UI


def listByCategory():
    category = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
    if category == '1':
        cat = "Action and Adventure"
    elif category == '2':
        cat = "Animation"
    elif category == '3':
        cat = "Comedy"
    elif category == '4':
        cat = "Crime"
    elif category == '5':
        cat = "Documentary"
    elif category == '6':
        cat = "Drama"
    elif category == '7':
        cat = "Fantasy"
    elif category == '8':
        cat = "Horror"
    elif category == '9':
        cat = "Romance"
    elif category == '10':
        cat = "Science Fiction"
    elif category == '11':
        cat = "Thriller"
    elif category == '12':
        cat = "Wester"
    else:
        print("INVALID INPUT\n")
        return
    UI.clear()  # clear the screen
    print("For", cat, "category, we have:")
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    for movie in movies['member']:
        if movies['member'][movie]['category'] == cat:
            print('\t', movie, '. ', movies['member'][movie]['name'], '\n\t----',
                  movies['member'][movie]['status'], sep='')
    print("\n")
    return


def add():
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    print("\nPlease type in the movie's name:\n")
    name = input()
    print("\nWhat's the location of this movie?\n")
    location = input()
    print("\nWhich category is this movie?\n")
    cat = input()
    status = "On Shelf at " + location
    movies['number'] += 1
    index = movies['number']
    movies['member'][index] = {'name': name,
                              'location': location,
                              'status': status,
                              'category': cat}
    with open('stock.json', 'w') as outfile:
        json.dump(movies, outfile, indent=4)
    print("\nSystem updated successfully!\nmovie",
          name, "is No.", index, "in the system.\n")


def rent():
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    print("\nDo you know the index number of the movie you want to rent?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the movie list to find the index number.\n")
    elif index in movies['member']:
        if movies['member'][index]['status'] == 'movie rented':
            print("\nI am sorry, the movie is currently rented by other people.\n")
        elif movies['member'][index]['status'] == 'DELETED':
            print("\nI am sorry, the movie is no longer available.\n")
        else:
            movies['member'][index]['status'] = 'movie rented'
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            print("\nYou successfully rented the movie.\nmovie status updated.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        rent()
        return
    print("\nDo you want to rent another movie?")
    rentAnswer = input("Please type in Y/N: ")
    while rentAnswer != 'Y' and rentAnswer != 'N':
        rentAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if rentAnswer == 'Y':
        rent()
    else:
        return


def returnBack():
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    print("\nDo you know the index number of the movie you want to return?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the movie list to find the index number.\n")
    elif index in movies['member']:
        if movies['member'][index]['status'] == 'movie rented':
            movies['member'][index]['location'] = input("\nPlease tell me the location where you put the movie:\n")
            movies['member'][index]['status'] = "On Shelf at " + movies['member'][index]['location']
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            print("\nYou successfully returned the movie.\nmovie status updated.\n")
        else:
            print("\nAre you sure you entered correct information?"
                  "\nThe movie which matches the index number was not rented.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        returnBack()
        return
    print("\nDo you want to return another movie?")
    returnAnswer = input("Please type in Y/N: ")
    while returnAnswer != 'Y' and returnAnswer != 'N':
        returnAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if returnAnswer == 'Y':
        returnBack()
    else:
        return


def delete():
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    print("\nDo you know the index number of the movie you want to delete from the stock?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the movie list to find the index number.\n")
    elif index in movies['member']:
        if movies['member'][index]['status'] == 'DELETED':
            print("\nThe movie status is already deleted in the system.\n")
        else:
            finalCheck = input("\nI have found the movie.\nAre you sure you want to delete it?\n"
                               "Type in Y/N here: ")
            while finalCheck != 'Y' and finalCheck != 'N':
                finalCheck = input("\nINVALID INPUT\nPlease type in Y/N: ")
            if finalCheck == 'Y':
                movies['member'][index]['status'] = 'DELETED'
                with open('stock.json', 'w') as outfile:
                    json.dump(movies, outfile, indent=4)
                print("\nYou successfully deleted the movie.\nmovie status updated.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        delete()
        return
    print("\nDo you want to delete another movie?")
    deleteAnswer = input("Please type in Y/N: ")
    while deleteAnswer != 'Y' and deleteAnswer != 'N':
        deleteAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if deleteAnswer == 'Y':
        delete()
    else:
        return
