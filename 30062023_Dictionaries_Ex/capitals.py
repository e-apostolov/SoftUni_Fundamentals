countries = input().split(", ")
capitals = input().split(", ")

# info_dict = {countries[index]: capitals[index] for index in range(len(countries))}
info_dict = dict(zip(countries, capitals))

for country, capital in info_dict.items():
    print(f"{country} -> {capital}")
