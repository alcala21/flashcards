# Write your code here
class FlashCards:
    def __init__(self):
        self.cards = {}

    def start(self):
        self.build_deck()
        self.test_user()

    def build_deck(self):
        print("Input the number of cards:")
        n = int(input())

        for i in range(1, n + 1):
            print(f"The term for card #{i}:")
            while True:
                term = input()
                if term in self.cards:
                    print(f'The term "{term}" already exists. Try again:')
                else:
                    break

            print(f"The definition for card #{i}:")
            while True:
                definition = input()
                if definition in self.cards.values():
                    print(f'The definition "{definition}" already exists. Try again:')
                else:
                    break
            self.cards[term] = definition

    def test_user(self):
        for term, definition in self.cards.items():
            print(f'Print the definition of "{term}":')
            answer = input()
            if answer == definition:
                print('Correct!')
            else:
                for _t, _d in self.cards.items():
                    if answer == _d:
                        print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{_t}".')
                        break
                else:
                    print(f'Wrong. The right answer is "{definition}"')


FlashCards().start()
