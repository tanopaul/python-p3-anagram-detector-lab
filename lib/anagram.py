# your code goes here!


class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, arr):
        anagram_array = []
        for arr_word in arr:
            if sorted([*arr_word]) == sorted([*self.word]):
               anagram_array.append(arr_word)
            else:
                return anagram_array
        
        return anagram_array


listen = Anagram('listen')
listen.match(['enlists', 'google', 'inlets', 'banana'])