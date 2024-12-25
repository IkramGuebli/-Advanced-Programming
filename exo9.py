
cities_population = []

while True:
    city = input("Enter the name of a city (or 'stop' to end): ")
    
    if city.lower() == 'stop':
        break
    
    population = len(city) * 1000000
    
    cities_population.append((city, population))


    cities_population.sort(key=lambda x: x[1], reverse=True)

    print("\nCities and their populations (from largest to smallest):")
for city, population in cities_population:
       print(f"{city}: {population:,} citizens")
