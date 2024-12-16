words=['apple', 'banana', 'cherry', 'apricot', 'blueberry']

def split_list_by_first_char(words):
    result = []  
    keys = []  

    for word in words:
        first_char = word[0]  
        found = False
        for i in range(len(keys)):  
            if keys[i] == first_char:
                result[i].append(word)  
                found = True
                break
        if not found:
            keys.append(first_char)  
            result.append([word]) 
    output = []
    for i in range(len(keys)):
        output.append((keys[i], result[i]))
    return output

print(split_list_by_first_char(words))
