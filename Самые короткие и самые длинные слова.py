class MinMaxWordFinder():
    
    def __init__(self):
        self.minword = 0
        self.maxword = 0
        self.list_word = [ ]
        
    def add_sentence(self,text):
        self.list_word += text.split()
        self.minword = len(min(self.list_word, key = len))
        self.maxword = len(max(self.list_word, key = len))
        
    def shortest_words(self):
        return sorted(list(filter(lambda x : len(x) == self.minword, self.list_word)))
    
    def longest_words(self):
        return sorted(set(filter(lambda x : len(x) == self.maxword, self.list_word)))


