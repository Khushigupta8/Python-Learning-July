# # set={2,3,4,2}
# # print(set)
# #unordered collection , take unique values 
# # k=set()
# # print(type(k))
# set={"khushi",28,"gupta"}
# for value in set:
#     print(value)
s1={2,5,8}
s2={2,3,7,9}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1,s2)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.add("four")
print(s1)
s1.remove(8)
print(s1)
#remove may raise an error but discard will not
s1.discard(99)
print(s1)
s1.discard("four")
print(s1)
item=s1.pop()
print(item)
print(s1)
# del s1
# print(s1)