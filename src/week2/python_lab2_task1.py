"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""




temperatures = [12, 14, 15, 13, 16, 18, 17]  # daily temperatures for a week
city_population = {
    "Riga": 605802,
    "Tallinn": 445259,
    "Vilnius": 592389,
    "Warsaw": 1790658,
    "Berlin": 3769000
}

# 2. 
average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]
total_population = sum(city_population.values())
smallest_city = min(city_population, key=city_population.get)
smallest_population = city_population[smallest_city]

# 3. 
print("Average temperature:", round(average_temperature, 2), "°C")
print("Largest city:", largest_city, "-", largest_population)
print("Smallest city:", smallest_city, "-", smallest_population)
print("Total population:", total_population)
