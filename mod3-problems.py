# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
text = input("Give me a word:")
times = int(input("How many times to repeat word?"))
print(text * times)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("Whats your name?")
age1 = int(input("And what is your age?"))
age2 = age1 + 1
print("Hello,", name,"!" + " You are", age1,"years old. Next year, you will be", age2,"years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sent = input("Give me a sentance: ")
word = input("Give me a special word: ")
print(word in sent)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Give me a word: ")
index1 = int(input("Give me a number: "))
index2 = int(input("Give me another number: "))
print(word[index1:index2])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do
word1 = input("Give me a word:")
word2 = input("And another:")
word3 = input("And another:")
phrase1 = word1, word2, word3
phrase2 = "!".join(phrase1)
print(phrase2)
