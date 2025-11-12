# #1
# student_grades = {"Matematika": 90, "Fizika": 85, "Informatika": 95}
#
# student_grades["Kimyo"] = 88
# result1 = student_grades
# print("1-vazifa natijasi:", result1)
#
# student_grades["Fizika"] = 87
# result2 = student_grades
# print("2-vazifa natijasi:", result2)
#
# del student_grades["Informatika"]
# result3 = student_grades
# print("3-vazifa natijasi:", result3)
#
# result4 = sum(student_grades.values())
# print("4-vazifa natijasi:", result4)
#
# result5 = sum(student_grades.values()) / len(student_grades)
# print("5-vazifa natijasi:", result5)
#
# result6 = max(student_grades.values())
# print("6-vazifa natijasi:", result6)
#
# result7 = min(student_grades.values())
# print("7-vazifa natijasi:", result7)
#
# result8 = list(student_grades.keys())
# print("8-vazifa natijasi:", result8)
#
# result9 = list(student_grades.values())
# print("9-vazifa natijasi:", result9)
#
# result10 = len(student_grades) == 0
# print("10-vazifa natijasi:", result10)

# #2
# fruits = {"olma": 5000, "banan": 12000, "uzum": 8000}
#
# fruits["anor"] = 10000
# result1 = fruits
# print("1-vazifa natijasi:", result1)
#
# fruits["banan"] = 15000
# result2 = fruits
# print("2-vazifa natijasi:", result2)
#
# del fruits["uzum"]
# result3 = fruits
# print("3-vazifa natijasi:", result3)
#
# result4 = sum(fruits.values())
# print("4-vazifa natijasi:", result4)
#
# result5 = max(fruits, key=fruits.get)
# print("5-vazifa natijasi:", result5)
#
# result6 = min(fruits, key=fruits.get)
# print("6-vazifa natijasi:", result6)
#
# result7 = sorted(fruits.values())
# print("7-vazifa natijasi:", result7)
#
# result8 = len(fruits)
# print("8-vazifa natijasi:", result8)
#
# result9 = fruits.get("olma")
# print("9-vazifa natijasi:", result9)
#
# result10 = sorted(fruits.keys())
# print("10-vazifa natijasi:", result10)

# #3
# cities = {"Toshkent": 2500000, "Samarqand": 550000, "Buxoro": 280000}
#
# cities["Amdijon"] = 600000
# result1 = cities
# print("1. Natija:", result1)
#
# cities["Toshkent"] = 2600000
# result2 = cities
# print("2. Natija:", result2)
#
# del cities["Buxoro"]
# result3 = cities
# print("3. Natija:", result3)
#
# result4 = sum(cities.values())
# print("4. Natija:", result4)
#
# result5 = sum(cities.values()) / len(cities)
# print("5. Natija:", result5)
#
# result6 = max(cities, key=cities.get)
# print("6. Natija:", result6)
#
# result7 = min(cities, key=cities.get)
# print("7. Natija:", result7)
#
# result8 = list(cities.values())
# print("8. Natija:", result8)
#
# result9 = sorted(cities.keys())
# print("9. Natija:", result9)
#
# result10 = len(cities) == 0
# print("10. Natija:", result10)

# #4
# books = {"Alximik": "Paulo Koelyo", "Shaytanat": "Tohir Malik", "1984": "George Orwell"}
#
# books["O‘tkan kunlar"] = "Abdulla Qodiriy"
# result1 = books
# print("1. Natija:", result1)
#
# books["Alximik"] = "Paulo Coelho"
# result2 = books
# print("2. Natija:", result2)
#
# del books["1984"]
# result3 = books
# print("3. Natija:", result3)
#
# result4 = len(books)
# print("4. Natija:", result4)
#
# result5 = list(books.values())
# print("5. Natija:", result5)
#
# result6 = sorted(books.keys())
# print("6. Natija:", result6)
#
# result7 = books.get("Shaytanat")
# print("7. Natija:", result7)
#
# result8 = len(books)
# print("8. Natija:", result8)
#
# if "O'tgan kunlar" in books:
#     print("9. O'tgan kunlar bor")
# else:
#     print("9. O'tgan kunlar yo'q")
#
# result10 = books.clear()
# print("10. Natija:", result10)

# #5
# currencies = {"USD": 12600, "EUR": 13500, "RUB": 140}
#
# currencies["GBP"] = 16000
# result1 = currencies
# print("1. Natija: ", result1)
#
# currencies["USD"] = 12700
# result2 = currencies
# print("2. Natija: ", result2)
#
# del currencies["RUB"]
# result3 = currencies
# print("3. Natija: ", result3)
#
# result4 = sum(currencies.values())
# print("4. Natija: ", result4)
#
# result5 = max(currencies, key=currencies.get)
# print("5. Natija: ", result5)
#
# result6 = min(currencies, key=currencies.get)
# print("6. Natija: ", result6)
#
# result7 = currencies.keys()
# print("7. Natija: ", result7)
#
# result8 = sorted(currencies.values())
# print("8. Natija: ", result8)
#
# result9 = currencies.get("EUR")
# print("9. Natija: ", result9)
#
# result10 = len(currencies) == 0
# print("10. Natija: ", result10)

# #6
# inventory = {"suv": 50, "non": 100, "shokolad": 20}
#
# inventory["cola"] = 30
# result1 = inventory
# print("1. Natija:", result1)
#
# inventory["non"] = 80
# result2 = inventory
# print("2. Natija:", result2)
#
# del inventory["shokolad"]
# result3 = inventory
# print("3. Natija:", result3)
#
# result4 = sum(inventory.values())
# print("4. Natija:", result4)
#
# result5 = max(inventory.keys(), key=inventory.get)
# print("5. Natija:", result5)
#
# result6 = min(inventory.keys(), key=inventory.get)
# print("6. Natija:", result6)
#
# result7 = inventory.keys()
# print("7. Natija:", result7)
#
# result8 = sorted(inventory.values())
# print("8. Natija:", result8)
#
# result9 = inventory.get("suv")
# print("9. Natija:", result9)
#
# result10 = len(inventory) == 0
# print("10. Natija:", result10)


# #7
# athletes = {"Ali": 150, "Vali": 120, "Sardor": 180}
#
# athletes["Sardor"] = 130
# result1 = athletes
# print("1. Natija:", result1)
#
# athletes["Vali"] = 140
# result2 = athletes
# print("2. Natija:", result2)
#
# del athletes["Sardor"]
# result3 = athletes
# print("3. Natija:", result3)
#
# result4 = sum(athletes.values())
# print("4. Natija:", result4)
#
# result5 = sum(athletes.values()) / len(athletes)
# print("5. Natija:", result5)
#
# result6 = max(athletes.keys(), key=athletes.get)
# print("6. Natija:", result6)
#
# result7 = min(athletes.keys(), key=athletes.get)
# print("7. Natija:", result7)
#
# result8 = athletes.keys()
# print("8. Natija:", result8)
#
# result9 = sorted(athletes.values())
# print("9. Natija:", result9)
#
# result10 = len(athletes) == 0
# print("10. Natija:", result10)


# #8
# menu = {"osh": 25000, "shashlik": 30000, "somsa": 5000}
#
# menu["lag'mon"] = 20000
# result1 = menu
# print("1. Natija:", result1)
#
# menu["somsa"] = 6000
# result2 = menu
# print("2. Natija:", result2)
#
# del menu["shashlik"]
# result3 = menu
# print("3. Natija:", result3)
#
# result4 = sum(menu.values())
# print("4. Natija:", result4)
#
# result5 = max(menu.keys(), key=menu.get)
# print("5. Natija:", result5)
#
# result6 = min(menu.keys(), key=menu.get)
# print("6. Natija:", result6)
#
# result7 = menu.keys()
# print("7. Natija:", result7)
#
# result8 = sorted(menu.values())
# print("8. Natija:", result8)
#
# result9 = menu.get("osh")
# print("9. Natija:", result9)
#
# result10 = len(menu) == 0
# print("10. Natija:", result10)

# #9
# faculties = {"IT": 120, "Matematika": 80, "Filologiya": 60}
#
# faculties['Fikika'] = 90
# result1 = faculties
# print("1. Natija", result1)
#
# faculties['IT'] = 130
# result2 = faculties
# print("2. Natija", result2)
#
# del faculties['Filologiya']
# result3 = faculties
# print("3. Natija", result3)
#
# result4 = sum(faculties.values())
# print("4. Natija", result4)
#
# result5 = sum(faculties.values()) / len(faculties)
# print("5. Natija", result5)
#
# result6 = max(faculties.keys(), key=faculties.get)
# print("6. Natija", result6)
#
# result7 = min(faculties.keys(), key=faculties.get)
# print("7. Natija", result7)
#
# result8 = faculties.keys()
# print("8. Natija", result8)
#
# result9 = sorted(faculties.values())
# print("9. Natija", result9)
#
# result10 = len(faculties) / len(faculties)
# print("10. Natija", result10)

# #10
# destinations = {"Parij": 500, "Dubay": 300, "Istanbul": 200}
#
# destinations["London"] = 450
# result1 = destinations
# print("1. Natija:", result1)
#
# destinations["Istanbul"] = 250
# result2 = destinations
# print("2. Natija:", result2)
#
# del destinations["Dubay"]
# result3 = destinations
# print("3. Natija:", result3)
#
# result4 = sum(destinations.values())
# print("4. Natija:", result4)
#
# result5 = max(destinations.keys(), key=destinations.get)
# print("5. Natija:", result5)
#
# result6 = min(destinations.keys(), key=destinations.get)
# print("6. Natija:", result6)
#
# result7 = destinations.keys()
# print("7. Natija:", result7)
#
# result8 = sorted(destinations.values())
# print("8. Natija:", result8)
#
# result9 = destinations.get("Parij")
# print("9. Natija:", result9)
#
# result10 = len(destinations) == 0
# print("10. Natija:", result10)

#11
phones = {"iPhone 15": 12000000, "Samsung S24": 9000000, "Xiaomi 14": 6000000}

