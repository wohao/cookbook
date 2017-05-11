from collections import Counter



words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


word_counters = Counter(words)
top_three = word_counters.most_common(3)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
# for word in morewords:
# 	word_counters[word] += 1



word_counters.update(morewords)
print(word_counters['eyes'])