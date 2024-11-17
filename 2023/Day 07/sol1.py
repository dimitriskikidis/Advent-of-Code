cardsMap = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
handTypeMap = {'5': 6, '41': 5, '32': 4, '311': 3, '221': 2, '2111': 1, '11111': 0}

def calcHandRank(hand):
    cards = hand[0]
    s = {}
    for card in cards:
        s1 = s.get(card, 0) + 1
        s[card] = s1
    s = [[card, freq] for card, freq in s.items()]
    s.sort(key=lambda pair: pair[1], reverse=True)

    s = ''.join([str(freq) for _, freq in s])
    handType = handTypeMap[s]

    handRank = 0
    handRank |= handType << (5 << 2)
    for i in range(0, 5):
        cardValue = cardsMap.get(cards[i], 0)
        handRank |= cardValue << ((4 - i) << 2)
    
    return handRank

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

hands = []
for line in lines:
    hand = line[0 : -1].split()
    hands.append([hand[0], hand[1], calcHandRank(hand)])
hands.sort(key=lambda hand: hand[2])

result = 0
for i, hand in enumerate(hands):
    result += int(hand[1]) * (i + 1)

print(result)
    