# Write your code here
import os


class CardExistsException(Exception):
    ...


class FlashCards:
    def __init__(self):
        self.cards = {}
        self.card = None
        self.definition = None

    def start(self):
        while True:
            print("Input the action (add, remove, import, export, ask, exit):")
            action = input()
            if action == "add":
                self.add()
            elif action == "remove":
                self.remove()
            elif action == "import":
                self.importing()
            elif action == "export":
                self.export()
            elif action == "ask":
                self.ask()
            elif action == "exit":
                self.exit()
                break

    def add(self):
        print("The card:")
        while True:
            try:
                self.card = input()
                if self.card in self.cards:
                    raise CardExistsException
                else:
                    break
            except CardExistsException:
                print(f'The term "{self.card}" already exists. Try again:')
        print("The definition of the card:")
        while True:
            try:
                self.definition = input()
                if self.definition in self.cards.values():
                    raise CardExistsException(self.definition)
                else:
                    break
            except CardExistsException:
                print(f'The definition "{self.definition}" already exists. Try again:')

        self.cards[self.card] = self.definition
        print(f'The pair ("{self.card}":"{self.definition}") has been added.', end="\n\n")

    def remove(self):
        print("Which card?")
        card = input()
        if card in self.cards:
            del self.cards[card]
            print('The card has been removed', end='\n\n')
        else:
            print(f'Can\'t remove "{card}": there is no such card.', end='\n\n')

    def importing(self):
        print('File name:')
        filename = input()
        files = os.listdir()
        if filename not in files:
            print('File not found.', end='\n\n')
            return
        with open(filename) as f:
            temp_dict = eval(f.read())
        self.cards.update(temp_dict)
        print(f'{len(temp_dict)} cards have been loaded.', end='\n\n')

    def export(self):
        print("File name:")
        filename = input()
        with open(filename, 'w') as f:
            print(self.cards, file=f)
        print(f'{len(self.cards)} cards have been saved.', end='\n\n')

    def ask(self):
        print("How many times to ask?")
        while True:
            try:
                n = int(input())
                break
            except ValueError:
                print("Enter an integer value.")
        i = 0
        while True:
            full = False
            for card, definition in self.cards.items():
                print(f'Print the definition of "{card}":')
                answer = input()
                if answer == definition:
                    print("Correct!")
                else:
                    for _t, _d in self.cards.items():
                        if answer == _d:
                            print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{_t}".')
                            break
                    else:
                        print(f'Wrong. The right answer is "{definition}"')
                i += 1
                if i == n:
                    full = True
                    break
            if full:
                break
        print()

    @staticmethod
    def exit():
        print("Bye bye!")


FlashCards().start()
