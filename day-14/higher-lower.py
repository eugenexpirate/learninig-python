# Goal: Use my knowlage in python and make a game Higher - Lower
import csv
import random
import os

countries_dictionary = {}
dictionary_size = 0


with open("day-14/countries.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # row[0] - countrie
        # row[1] - population
        # row[2] - land area 
        countries_dictionary[row[0]] = [int(row[1]), int(row[2])]

# game start and contine till player makes error or he compare all the countries
# each turn compare country A with randome one (country B) from dictionary 
# after the turn country A data delete from dictionary
# country B become country A next turn

country_A_name = random.choice(list(countries_dictionary.keys()))
country_A = countries_dictionary.pop(country_A_name)
score = 0

os.system('clear')
print("--==[ Welcome to Higher/Lower game ]==--")

# player can choose what to compare (population or land area)
compare_param = ""
print("Choose what to compare. Land area or Population?")
while compare_param not in ["area", "population"]:
    compare_param = input("Type 'area' or 'population': ")
print(f"You choose to compare {compare_param}")

compare_list_index = 0
if compare_param == "area":
    compare_list_index = 1


while True:
    # let check are we make all countries
    if len(countries_dictionary) <= 1:
        print("Congratulation! You make all the countries!")
        print(f"Your score is {score}!")
        break
    
    country_B_name = random.choice(list(countries_dictionary.keys()))
    country_B = countries_dictionary.pop(country_B_name)
    
    os.system('clear')
    print(f"_______ Your score is {score} _______\n");
    print(f"Is {compare_param} of {country_A_name} higher or lower then {compare_param} of {country_B_name}")
    print("Type L for Lower or H for Higher (or Q for Quit): ")
    
    answer = ""
    while answer not in ['l', 'h', 'q']:
        answer = input().lower()
    
    if answer == 'q':
        break
    
    if answer == 'l':
        if country_A[compare_list_index] < country_B[compare_list_index]:
            print("That is true!")
            score += 1
        else:
            print("That is wrong!")
            break
    
    if answer == 'h':
        if country_A[compare_list_index] > country_B[compare_list_index]:
            print("That is true!")
            score += 1
        else:
            print("That is wrong!")
            break

    country_A_name = country_B_name
    country_A = country_B

print(f"Game over. Your score is {score}.")
print("Thank you for playing! Good luck")
