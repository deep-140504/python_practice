# counting sort using counter
from collections import Counter
def fun(s):
    temp_dict= Counter(s)
    temp_dict= dict(sorted(temp_dict.items()))
    
    print(temp_dict)

    # temp_s = [[key] * value for key, value in temp_dict.items()]
    # this returns a nested list of strings rather than just returning the string and join string accepts only list of strings, not the nested list of strings
    
    temp_s = [key * value for key, value in temp_dict.items()]
    # now this is fine as the strings are stored directly inside of the list and is possible to process upon using the join

    print(temp_s)

    s = "".join(temp_s)
s = "cccbba"
fun(s)
print(s)

# so the join in python is only operational on the strings, any iterable other than that will cause TypeError


words = ["z", "yy", "www"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['z', 'yy', 'www'] # Sorted by length
