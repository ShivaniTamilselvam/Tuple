from collections import Counter 
dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 
Cdict = Counter(dict1) + Counter(dict2) 
print(Cdict) 
