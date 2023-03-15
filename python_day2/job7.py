def langage_in_use():
    langage = input("Choisis un langage de programmation: ")
    
    if langage == "javascript":
        print("Tu es un développeur Web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur Logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur Mobile")
    else:
        print("Un jour tu seras le meilleur développeur...")
langage_in_use()