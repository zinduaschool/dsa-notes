'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
def linearsearch(lst,a):
    for i in range(len(lst)):
        if lst[i] == a:
            return i
    return None
    
lst = [12, 34, 45, 72, 81, 98, 112, 200, 1000, 10000]
a = 200
print(linearsearch(lst,a))
