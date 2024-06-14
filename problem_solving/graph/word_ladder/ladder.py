import sys

class Edge(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    def __repr__(self):
        return f'src: {self.src} - dst: {self.dst}'
        
    def __str__(self):
        return f'src: {self.src} - dst: {self.dst}'

class Node(object):
    def __init__(self, word):
        self.word = word

class Graph(object):
    def __init__(self):
        self.vertices = {}
    def add(self, key, word):
        if self.vertices.get(key):
            self.vertices[key].append(word)
        else:
            self.vertices[key] = [word]
        
def words_reader():
    words = {}
    with open("words.txt", "r") as f:
        data = f.readline()[0:-2]
        while data:
            words[data] = 1
            data = f.readline()[0:-1]

    return words

def is_word(word, words):
    return words.get(word)

def gen_combi(word, words):
    visited = set()
    res = []
    for i, x in enumerate(word):
        for a in alphabet:
            if a == x: continue
            current = list(word)
            current[i] = a
            current = "".join(current)
            if current in visited: continue
            if is_word(current, words):
                visited.add(current)
                res.append(current)
    return res

alphabet = "abcdefghijklmnopqrstuvwxyz"
def word_generator(beg_word, end_word) :
    
    visited = set()
    visited.add(beg_word)
    words = words_reader()
    
    def inner(word, stock):
        if len(stock) and stock[-1].dst == end_word:
            print("yattttaaaaaaa")
            return stock
        
        for i, x in enumerate(word):
            for a in alphabet:
                if a == x: continue
                current = list(word)
                current[i] = a
                current = "".join(current)
                if current in visited: continue
                if is_word(current, words):
                    visited.add(current)
                    found = inner(current, stock + [Edge(word, current)])
                    return found

    #return inner(big_word, [])
    mem = set()
    def loop(word):
        q = [word]
        gr = {}
        gr[word] = []
        done = False
        keys = [word]
        while len(q):
            pop = q.pop()
            mem.add(pop)
            if pop == end_word:
                print("=========================================")
                return pop
            generated = gen_combi(pop, words)
            gr[pop] = generated 
            keys.append(pop)
            for x in generated:
                if x in mem: continue
                if x == end_word:
                    print("print", gr)
                    print("--------------", gr)
                    print("--------------", keys )

                    return gr
                q.insert(0, x)
        print(gr)
        
    visited = set()

    def find_node(current, keys, graph, trace):
        visited.add(current)
        if end_word in keys: 
            return 12, trace + [end_word]
        for x in keys:
            if not x in visited:
                res = find_node(x, graph.get(x, []), graph, trace + [x])
                if res: print("===>", res)
            else:
                verify = trace + [x, end_word]
                is_path = True
                for i in range(1, len(verify)):
                    if not is_one_letter_diff(verify[i], verify[i - 1]) :
                        is_path = False
                        break
                if is_path: print("**** this is path", verify)
    graphed = loop(beg_word)
    return find_node(beg_word, graphed.get(beg_word), graphed, [beg_word])
            


            


words = words_reader()
def pretty(res):
    #return [x.src for x in res]
    return res

def is_one_letter_diff(dst, src):
    if len(dst) != len(src): return False
    diff = 0
    for i, x in enumerate(dst):
        if x != src[i]:
            diff += 1
    return diff == 1
    
print(pretty(word_generator("cap", "rip")))
        
    
