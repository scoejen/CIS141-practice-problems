'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
    function body: variable for total, make all letters lower -> return new variable for string,
                    variable for vowels

def count_vowels(input):
    total = 0
    new_input = input.lower()
    vowels = "aeiou"
    for l in new_input:
        if l in vowels:
            total += 1
    return total
string = input("Enter a phrase: ")
print("Vowel count: ", count_vowels(string))

'''
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
    Test: racecar (True), pikachu (False), Racecar (True)
    Input: string (s)
    Output: boolean
    Function body: lowercase s, flip s and save to new varible and then compare s

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s

print(is_palindrome("pikachu"))
print(is_palindrome("Racecar"))
print(is_palindrome("racecar"))

'''
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"

def type_advantage(attacker, defender):
    if ( attacker ) == "Water":
        if (defender) == "Fire":
            return "Super Effective"
    elif (attacker) == "Fire":
        if (defender) =="Water":
            return "Not Very Effective"
    elif attacker == "Electric":
        if defender == "Grass":
            return "Neutral"
    else:
        return "Unknown type."
print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Electric", "Grass"))
'''

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
    def ferry_fare(age, vehicle):
    if age >= 65:
        if vehicle == "y":
            return "Your fee is: $15"
        else:
            return "Your fee is: $5"
    elif age >= 19:
        if vehicle == "y":
            return "Your fee is: $20"
        else:
            return "Your fee is: $10"
    else:
        return "Your fee is: Free"
number = int(input("Enter age: "))
car = input("With vehicle?: Y or N ")
print(ferry_fare(number, car))
'''
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
'''
def level_up(experience):
    if experience >= 200:
        return "Level 3"
    elif experience >= 100:
        return "Level 2"
    else:
        return "Level 1"

number = int(input("How man experience points do you have? "))
print("You are: ", level_up(number))
'''
