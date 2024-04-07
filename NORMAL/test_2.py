from collections import Counter

l = ['a','b','a','a']

counter = Counter(l)
most_common, freq = counter.most_common(1)[0]
print(f"The most frequent element in {l} is '{most_common}' with a frequency of {freq}")

