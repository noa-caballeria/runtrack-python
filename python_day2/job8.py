def season_and_type():
    season = input("Choisis été ou hiver: ")
    type = input("Choisis fruit ou légume: ")
    
    if season == "été" and type == "fruit":
        print("Poire, Fraise, Cassis")
    elif season == "été" and type == "légume":
        print("Artichaut, Aubergine, Navet")
    elif season == "hiver" and type == "fruit":
        print("Orange, Mandarine et Kiwi")
    elif season == "hiver" and type == "légume":
        print("carotte, topinambour, endive")
    else:
        print("Réessaye en respectant les consignes.")
season_and_type()