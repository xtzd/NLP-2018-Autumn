import random
import collections
import time

def swap(deck,i,j):
    deck[i],deck[j]=deck[j],deck[i]

def shuffler1(deck):
    N=len(deck)
    for i in range(N-1):
        swap(deck,i,random.randrange(i,N))

def shuffler2(deck):
    N=len(deck)
    swapped=[False]*N
    while not all(swapped):
        i,j=random.randrange(N),random.randrange(N)
        swapped[i],swapped[j]=True,True
        swap(deck,i,j)


def test_shuffler(shuffler,deck='abcd',n=10000):
    counts=collections.defaultdict(int)
    for _ in range(n):
        input=list(deck)
        shuffler(input)
        counts[''.join(input)]+=1
    return counts

def test_shufflers(shufflers=[shuffler1,shuffler2],decks=['abc','ab']):
    for deck in decks:
        for sf in shufflers:
            time1=time.time()
            counts=test_shuffler(sf,deck)
            time2=time.time()
            print(sf.__name__,deck,time2-time1,counts)

test_shufflers()
