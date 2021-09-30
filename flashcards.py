# Write your code here
from random import choice

class FlashCards:
    def __init__(self):
        self.cards = []

    def start(self):
        self.build_deck()
        self.test_user()

    def build_deck(self):
        print("Input the number of cards:")
        n = int(input())

        for i in range(1, n + 1):
            print(f"The term for card #{i}:")
            term = input()
            print(f"The definition for card #{i}:")
            definition = input()
            self.cards.append({'term': term, 'definition': definition})

    def test_user(self):
        for card in self.cards:
            print(f'Print the definition of "{card["term"]}":')
            answer = input()
            if answer == card["definition"]:
                print('Correct!')
            else:
                print(f'Wrong. The right answer is "{card["definition"]}"')


FlashCards().start()
