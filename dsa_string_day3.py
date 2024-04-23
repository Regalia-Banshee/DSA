def is_anagram(s,t):
    return sorted(s)==sorted(t)
s="cat"
t="dog"
print(is_anagram(s,t))