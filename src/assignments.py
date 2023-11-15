# define your methods here.
# ex1() - ex10()

from dataclasses import dataclass
import random
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

class TaxMan:
    def __init__(self, itemList, taxRate):
        self.itemList = itemList
        self.taxRate = taxRate
        self.tax = float(taxRate[:len(taxRate)-1]) /100
        self.total = 0
    def calc_total(self):
        for item in self.itemList:
            self.total += item['price'] * (1 + self.tax)
    def get_Total(self):
        return self.total
class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.result = None
    def add(self):
        self.result = self.x + self.y
    def sub(self):
        self.result = self.x - self.y
    def mul(self):
        self.result = self.x * self.y
    def div(self):
        if self.y == 0:
            raise ValueError("Division by zero not allowed.")
        else:
            self.result = self.x / self.y
    def modulus(self):
        self.result = self.x % self.y
    def power(self):
        self.result = self.x ** self.y
    def get_result(self):
        return self.result
class CarCollector:
    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        return list(map(CarCollector._combine, CarCollector.car_list))
    
    @staticmethod
    def _combine(c):
        # Todo...
        retval = {
            'id': c['id'],
            'make': CarCollector.car_dict[c['id']],
            'price': c['price']
        }
        return retval
class Character:

    def __init__(self, hit_points):
        self.hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 20)
        if character.hit_points >= random_number:
            character.hit_points -= random_number
        
    def __repr__(self):
        return f"Character: {self.hit_points} hit points."
class Fighter(Character):
    pass
    def __repr__(self):
        return f"Fighter: {self.hit_points} hit points."
class Dwarf(Character):
    pass
    def __repr__(self):
        return f"Dwarf: {self.hit_points} hit points."
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

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
    
def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print("%.2f"%tm.get_Total())

def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
    lst = CarCollector.get_data()
    for items in lst:
        print(items)

def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)


@dataclass(frozen=False, order=True)
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str

    def __repr__(self) -> str:
        return f"Invoice(invoice_id={self.invoice_id}, user_id={self.user_id}, amount={self.amount}, paid={self.paid})"
def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]

    inv_list = []
    for ele in data:
        #inv = Invoice(*ele.split(", "))
        #print(inv)
        invoice_item = ele.split(", ")
        i_id = invoice_item[0]
        u_id = invoice_item[1]
        amount = invoice_item[2]
        is_paid = invoice_item[3]
        inv = Invoice(i_id,u_id, amount, is_paid)
        inv_list.append(inv)

    print(inv_list)
    