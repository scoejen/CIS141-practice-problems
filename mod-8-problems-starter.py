'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
with open("gardening_tips.txt", "r") as file:
    print(file.read())
'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
# I didn't want the user to lose past entries, which is why I didn't do a "w" before the with function

file = open("hiking_trips.txt", "a")
while True:
    name = input("Name of hike?: (enter 0 to exit program) ")
    if name == "0":
        break
    miles = input("How many miles?: (enter 0 to exit program) ")
    if miles == "0":
        break
    file.write(name + ":\t" + miles + "\n")

file.close()

with open("hiking_trips.txt", "r") as file:
    print(file.read())
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
lyrics = {}
with open("song_lyrics.txt", "r") as file:
    lyric_count = input("List 5 words to lookup and count: ").split()
    content = file.read().lower()
    for word in lyric_count:
        lyrics[word] = content.count(word.lower())

print("Word frequency:", lyrics)
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", "r") as file:
    content = file.read().lower()
    word1 = "yea"
    word2 = "nay"
    count1 = content.count(word1)
    count2 = content.count(word2)

print({word1}, {count1})
print({word2}, {count2})
