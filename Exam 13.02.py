# Task 1

def card_num_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

card = '1234 1234 1234 1234'
print(card_num_hide(card))

# Task 2

def palindrome(word):
    word = word.replace(' ','').lower()
    return 'Палиндром' if word == word[::-1] else 'Не палиндром'

word = 'Заказ'
print(palindrome(word))

# Task 3

class Tomato:
    default_states = 0
    default_states_1 = 1
    default_states_2 = 2

    def __init__(self, index, state):
        self._index = index
        self._state = 0

    def grow(self):
        pass

    def is_rise(self):
        pass

class TomatoBush:

    def __init__(self, count):
        self.count = 10


