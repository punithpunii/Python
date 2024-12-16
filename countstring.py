strings= ['abc', 'xyz', 'aba', '1221']

def count_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

print("the num of required strings are:",count_strings(strings))