def ReadLastRow():
    data = open('text.txt', encoding="utf-8")
    print(data)
    text = data.readlines()
    print(text[-1]) # или так: print(text[len(text)-1])
    data.close()

    