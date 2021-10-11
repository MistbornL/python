'''Create a function that takes a list of
and returns a list with the items from the original list stored into
sublists. Items of the same value should be in the same sublist.


sort([2, friends, 2, friends]) ➞ [[2, 2], [friends, friends]]


sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]


sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]'''

def sublist(x):
    L = []
    for number in set(x):
        L.append([number] * x.count(number))
    print(L)


x = [1, 3, 4, 4, 6, 7, 3,2,4]
sublist(x)

