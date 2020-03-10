produtos = {}

produtos["Chuteira"] = 100.00
produtos["Bola"] = 40.00
produtos["Camisa"] = 80.00
produtos["Shorts"] = 60.00
produtos["Luvas"] = 55.00

for x in produtos:
    if produtos[x] > 50:
        print(produtos[x])
