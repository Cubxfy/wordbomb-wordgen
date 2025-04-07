list_ = open("dict.txt").read().split()


while True:
    segment = input("> ").upper()

    for word in list_:
        if segment in word:
            print(word)