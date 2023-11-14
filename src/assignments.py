# define your methods here.
# ex1() - ex10()
def ex1():
    def sort_people(people_list, sorting_key, sorting_order):
        order = True
        if sorting_order == "asc":
            order = False
        return people_list.sort(key=lambda p: p[sorting_key], reverse=order)

    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    
    sort_people(people_list, 'age', 'desc')
    print(people_list)

def ex2():
     def filter_males(people_list):
         return list(filter(lambda p: p['sex'] == 'male', people_list))
     people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
     filtered_list = filter_males(people_list)
     for people in filtered_list:
         print(people)

def ex3():
    def calc_bmi(people_list):
        def add_bmi(person):
            retval = {
                'id' : person['id'],
                'name' : person['name'],
                'weight_kg' : person['weight_kg'],
                'height_meters' : person['height_meters'],
                'bmi' : round(person['weight_kg'] / person['height_meters'] ** 2, 1)
            }
            return retval
        return list(map(add_bmi, people_list))
        
    
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    for p in new_people_list:
        print(p)

def ex4():
    def get_people(people_list):
        return [p['name'] for p in people_list if p['age'] >= 15]
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))

#Create a class called `WordCounter`.  This class is to be consumed in the following manner:

#word_counter = WordCounter(sentence)
#word_counter.count_words()
#print(word_counter.get_word_count())    # Returns the number of all the words.
#print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
#print(word_counter.get_longest_word())  # Returns the length of the longest word.
class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.split_sentence = sentence.lower().split(' ')
        self.word_lengths = []
        self.all_words = set([])
        self.shortest_word = None
        self.longest_word = None
        self.count_words()
    def count_words(self):
        for word in self.split_sentence:
            if len(word) > 0 and not (word[0].isdigit() or word[-1].isdigit()):
                self.word_lengths.append(len(word))
                self.all_words.add(word)
            if self.shortest_word == None or len(word) < self.shortest_word:
                self.shortest_word = len(word)
            elif self.longest_word == None or len(word) > self.longest_word:
                self.longest_word = len(word)
    def get_word_count(self):
        return len(self.all_words)
    def get_shortest_word(self):
        return self.shortest_word
    def get_longest_word(self):
        return self.longest_word
    
def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.