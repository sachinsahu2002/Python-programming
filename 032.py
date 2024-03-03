# Solution for leetcode Maximum wealth problem
# a = [2,3,4,5,6,7]
# c = sum(a)
# b = 0
# print(max(c,b))
# def maximumWealth(accounts):
#     c = []
#     for items in accounts:
#         a = items
#         b = sum(a)
#         c.append(b)
#     return(max(c))
    
# x = [[1,5],[7,3],[3,5]]
# print(maximumWealth(x))

def maximumWealth(accounts):
    c = 0
    for items in accounts:
        a = items
        b = sum(a)
        c = max(c,b)
    return(c)
    
x = [[1,5],[7,3],[3,5]]
print(maximumWealth(x))