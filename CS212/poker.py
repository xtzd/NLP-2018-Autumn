
import random
import itertools

mydeck=[r+s for r in '23456789TJQKA' for s in 'HSDC']
mydeck+=['?B','?R']
# 13 rankings
# 4 suits: heart-spade-diamond-club

def deal(numhands,n=5,deck=mydeck):
    random.shuffle(mydeck)
    hands=[[0 for i in range(n)] for j in range(numhands)]
    for i in range(n):
        for j in range(numhands):
            hands[j][i]=mydeck.pop()
    return hands


def hand_rank(hand):
    rank=['--23456789TJQKA'.index(r) for r,s in hand]
    freq=[(rank.count(x),x) for x in set(rank)]
    freq.sort(reverse=True)
    counts,ranks=zip(*freq)
    if ranks==(14,5,4,3,2):
        ranks=(5,4,3,2,1)
    straight=len(ranks)==5 and max(ranks)-min(ranks)==4
    flush=len(set([s for r,s in hand]))==1
    return (9 if (5,)==counts else
            8 if straight and flush else
            7 if (4,1)==counts else
            6 if (3,2)==counts else
            5 if flush else
            4 if straight else
            3 if (3,1,1)==counts else
            2 if (2,2,1)==counts else
            1 if (2,1,1,1)==counts else
            0),ranks

def best_hand(hand):
    "select best 5 of 7"
    best=max(itertools.combinations(hand,5),key=hand_rank)
    return best

def replacement(card):
    if card.startswith('?'): return [r+s for r in '23456789TJQKA' for s in 'HSDC']
    else: return [card]

def best_wild_hand(hand):
    "select best 5 of 7 after replace joker to any possible car"
    hands=set(best_hand(h) for h in itertools.product(*map(replacement,hand)))
    return max(hands,key=hand_rank)


def allmax(hands,key=None):

    result,maxval=[],None
    key=key or (lambda x:x)
    for x in hands:
        xval=key(x)
        if not result or xval>maxval:
            result,maxval=[x],xval
        elif xval==maxval:
            result.append(x)
    return result


def poker(hands,key=hand_rank):
    return allmax(hands,key=key)

 
def test():
    hands=deal(5,7)
    print(hands)
    print(poker(hands,key=best_wild_hand))
    

test()