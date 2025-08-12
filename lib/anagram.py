# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
        self.word_list = []  

    def match(self, word_list):
        self.word_list = word_list
        matches = []
        for candidate in self.word_list:
            if candidate.lower() == self.word:
                continue
            if sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        return matches
