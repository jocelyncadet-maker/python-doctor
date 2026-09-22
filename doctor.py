'''
program: doctor.py
Chapter 5 Case Study 2 (Pages 136 - 140)
9/15/2026

Application that simulates a therapy session by modifying user input.
'''

import random

# Global variables that all functions can share

hedges = ("Please, tell me more...", "Many of my patients tell me the same thing.", "Please, continue.", "You don't say...", "Go on, go on...", "That's interesting.")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ", "Is it because ", "Are you that ")

replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours", "am": "are", "you": "I", "are": "am"}

# Definition of the reply() function
def reply(sentence):
    """Builds and returns a reply to the text passed to this function."""
    probability = random.randint(1, 4)

    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

# Definition of the changePerson() function
def changePerson(sentence):
    """Replaces first-person words in the sentence with second-person."""
    words = sentence.split()
    replyWords = []
    # FOR loop that goes through the WORDS list
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

# Definition of the main() function
def main():
    print("Good day, I hope you are well today.")
    print("What can I do for you?")
    print("Enter your response (or 'QUIT' to exit):")
    while True:
        sentence = input("\n>> ")
        # Decide what to do with the sentence input
        if sentence.upper().strip() == "QUIT":
            input("Have a great day! Press ENTER to exit.")
            break
        elif sentence == "":
            print("Did you mean to say something? Or you can type QUIT to exit.")
        else:
            print(reply(sentence))

# Global to call to main() for program entry
main()
