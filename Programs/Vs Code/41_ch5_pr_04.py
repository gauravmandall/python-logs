'''
What will be the length of following set s :
    s = set()
    s.add(20)
    s.add(20.0)
    s.add("20")     => Length of s after these operations ?
'''
s = {20, 20.0, "20"}
print(s)
print(len(s))
print(type(s))