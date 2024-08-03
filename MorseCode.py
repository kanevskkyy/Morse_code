from random import randint

words = ["breeze", "sunset", "whisper", "gentle", "mystery"]
size = len(words)
answers = []

morse = {
    "breeze": "-... .-. . . --.. .",
    "sunset": "... ..- -. ... . -",
    "whisper": ".-- .... .. ... .--. . .-.",
    "gentle": "--. . -. - .-.. .",
    "mystery": "-- -.-- ... - . .-. -.--"
}

def line():
    print("===================================================")


def morse_encode(sentence):
    return morse[sentence]


def get_word():
    random_index = randint(0, len(words) - 1)
    random_word = words.pop(random_index)
    return random_word


def print_statistic(answers):
    count_of_True = answers.count(True)
    count_of_False = answers.count(False)
    print(f"Total tasks = {len(answers)}")
    print(f"Number of correct answers = {count_of_True}")
    print(f"Number of incorrect answers = {count_of_False}")


print("Today we will practice decoding Morse code.\nPress Enter and we'll get started")
input()

for index in range(size):
    line()
    random_word = get_word()
    morse_word = morse_encode(random_word)
    print(f"Word {index + 1}: {morse_word}")

    answer_of_user = input("Your answer: ")
    if random_word == answer_of_user:
        answers.append(True)
        print(f"That's right, {answer_of_user}!")
    else:
        answers.append(False)
        print(f"Wrong, the correct word was: {random_word}")


line()
print_statistic(answers)