travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, time_visited, city_visited):
    travel = {}
    travel["country"] = country_visited
    travel["visits"] = time_visited
    travel["cities"] = city_visited
    travel_log.append(travel)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
