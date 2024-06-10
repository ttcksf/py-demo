# セットは論理演算や集合に向いている
set1 = {1,2,3}
set2 = {3,4,5}

# AND 
print(set1 & set2)
print(set1.intersection(set2))
# OR 
print(set1 | set2)
print(set1.union(set2))

# set1 only
print(set1 - set2)
print(set1.difference(set2))
# set2 only
print(set2 - set1)
print(set2.difference(set1))

# XOR
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
