def createCarDictionary(make, model, year, color, price, horsepower):
    car = {'Make': make, 'Model': model, 'Year': year, 'Color': color, 'Price': price, 'Horsepower': horsepower}
    return car

c = createCarDictionary("Porsche", "Cayenne", 2022, "Blue", 100, 650)
print(c)