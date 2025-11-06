# itertools
# from itertools import count
# for i in count(5,2):
#     print(i)
#     if i==15:
#         break

#cycle
# from itertools import cycle
# l=["r","g","b"]
# count=0
# for i in cycle(l):
#     print(i)
#     count+=1
#     if count==10:
#         break

#repeat-same value multiple times
# from itertools import repeat
# for i in repeat("hello hindavi",3):
#     print(i)

# combination-give possible combination without any order
# permutation-order matters
# permutations always more than combination bcoz of their formula
# Permutation (order matters)
# P(n, r) = n! / (n - r)!
# Combination (order does not matter)
# C(n, r) = n! / (r! × (n - r)!)

# from itertools import combinations
# items=['red','green','blue','black','white']
# for combo in combinations(items,2):
#     print(combo)

# from itertools import permutations
# items=['red','green','blue','black','white']
# for permo in permutations(items,2):
#     print(permo)

# cartesian product
# from itertools import product
# colors=['red','green','blue','black','white']
# size=['s','m','xl']
# genders=['male','female']
# for p in product(colors, size, genders):
#     print(p)

# combination_with_replacement
# from itertools import combinations_with_replacement
# items=['a','b']
# for combo in combinations_with_replacement(items,2):
#     print(combo)

# chain-combines multiple iterables into one continous iterable
# from itertools import chain
# list1=[1,2]
# list2=['h','s']
# for i in chain(list1,list2):
#     print(i)

# islice
# from itertools import islice
# list1=[1,2,3,4,5]
# for i in islice(list1,1,6):
#     print(i)

# izip
# accumulate


