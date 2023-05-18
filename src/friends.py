def get_name(person):
    return person['name']

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    return food in person["favourites"]["snacks"]

def add_friend(person, friend):
    person["friends"].append("friend")

def remove_friend(person, friend):
    person["friends"].remove("friend")

def total_money(people):
    total = 0
    for peep in people:
        total += peep["monies"]
    
    return(total)

def lend_money(person_1, person_2, money):
    if person_1["monies"] >= money:
        person_1["monies"] -= money
        person_2["monies"] += money

def all_favourite_foods(people):
    all_fav = []

    for peep in people:
        for food in peep["favourites"]["snacks"]:
            all_fav.append(food)
    
    return(all_fav)

def find_no_friends(people):
    loners = []

    for peep in people:
        if len(peep["friends"]) == 0:  # testing if the length of the list is zero
        # if peep["friends"] == []:    testing if list equals the empty list
            loners.append(peep)

    return(loners)

def unique_favourite_tv_shows(people):
    allshows = []

    for peep in people:
        show = peep["favourites"]["tv_show"]
        if show not in allshows:
            allshows.append(show)
        
    return(allshows)


    ########### EXTENSION

def test_set_tv_shows(people):
    allshows = set()
    for peep in people:
         allshows.add(peep["favourites"]["tv_show"])
    return(allshows)




    

