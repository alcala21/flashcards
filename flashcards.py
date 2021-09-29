# Write your code here
class FlashCards:
    def __init__(self):
        pass

    def start(self):
        term = input()
        definition = input()
        answer = input()
        if answer == definition:
            print('Your answer is right!')
        else:
            print('Your answer is wrong!')

    def print(self):
        print("Card:")
        print('House')
        print('Definition:')
        print('Party')


FlashCards().start()
