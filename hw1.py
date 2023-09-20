def isValid(s):
    if len(s) == 0:
        print("YES")
        return
    character_dictionary = {}
    deletion_avaliable = True
    for ch in s:
        if ch in character_dictionary.keys():
            character_dictionary[ch] = character_dictionary.get(ch) + 1 
        else:
            character_dictionary[ch] = 1
    letter_count = list(character_dictionary.values())[0]
    # print("stuff")
    # print(letter_count)
    # print(character_dictionary)
    for key in character_dictionary.keys():
        value = character_dictionary.get(key)
        if value == letter_count:
            continue
        else:
            if deletion_avaliable and (value - 1 == letter_count or value - 1 == 0):
                character_dictionary[key] = value - 1
            else:
                print("NO")
                return
    print("YES")

# print("is valid test cases")
# isValid("aabbcd")
# isValid("aabbcdddeefghi")
# isValid("abcdefghhgfedecba")
# isValid("aabbcce")
# isValid("")


def isBalanced(s):
    bracket_array = []
    bracket_dictionary = {'{': '}', '[': ']', '(': ')'}
    if (len(s)) % 2 != 0 or s[0] not in bracket_dictionary.keys():
        print("NO")
        return
    else:
        for ch in s:
            if ch in bracket_dictionary.keys():
                bracket_array.append(ch)
            else:
                if bracket_dictionary.get(bracket_array[-1]) == ch:
                    bracket_array.pop()
        if not bracket_array:
            print("YES")
        else:
            print("NO")

# print("is balanced test cases")
# isBalanced("(){[([()][])]}")
# isBalanced("{[()]}")
# isBalanced("{[(])}")
# isBalanced("{{[[(())]]}}")
# isBalanced("[{}][{}]")
# isBalanced(("{({}{}[][[([{}]){}]])}"))
# isBalanced("()())()")
def countValidStrings(s):
    valid_bracket_array = []
    invalid_bracket_array = []
    bracket_dictionary = {'{': '}', '[': ']', '(': ')'}   
    for ch in s:
        if ch in bracket_dictionary.keys():
            valid_bracket_array.append(ch)
        else:
            if valid_bracket_array and bracket_dictionary.get(valid_bracket_array[-1]) == ch:
                valid_bracket_array.pop()
            else:
                list_bracket_dictionary_keys = list(bracket_dictionary.keys())
                list_bracket_dictionary_values = list(bracket_dictionary.values())
                invalid_bracket_array.append(ch)
                key_of_value = list_bracket_dictionary_keys[list_bracket_dictionary_values.index(ch)]
                if key_of_value in valid_bracket_array:
                    invalid_bracket_array.append(key_of_value)
                    del valid_bracket_array[valid_bracket_array.index(key_of_value)]
    print(len(invalid_bracket_array))
    
def countValidStrings_2(s):

    bracket_dictionary = {'{': '}', '[': ']', '(': ')'}   
    list_bracket_dictionary_values = list(bracket_dictionary.values())
    list_bracket_dictionary_keys = list(bracket_dictionary.keys())
    valid_bracket_array = []
    deleted_bracket_array = []
    count_1 = 0
    for ch in s:
        if ch in bracket_dictionary.keys():
            valid_bracket_array.append(ch)
        else:
            key_of_value = list_bracket_dictionary_keys[list_bracket_dictionary_values.index(ch)]
            if valid_bracket_array and bracket_dictionary.get(valid_bracket_array[-1]) == ch:
                valid_bracket_array.pop()
                count_1 += 2
                continue
            if not valid_bracket_array or key_of_value in deleted_bracket_array:
                deleted_bracket_array.append(ch)
                continue
            if not key_of_value in valid_bracket_array:
                deleted_bracket_array.append(ch)
                continue
            i = -1
            while valid_bracket_array[-1] != key_of_value:
                deleted_bracket_array.append(valid_bracket_array.pop())
                # i -= 1
            # deleted_bracket_array.append(valid_bracket_array[i])
            # del valid_bracket_array[i] 
            # if bracket_dictionary.get(valid_bracket_array[-1]) in deleted_bracket_array:
            #     deleted_bracket_array.append(valid_bracket_array.pop())
            # if valid_bracket_array[-1] != key_of_value:
            #     deleted_bracket_array.append(ch)
            #     continue
            if valid_bracket_array[-1] == key_of_value:
                valid_bracket_array.pop()
                count_1 += 2
    if valid_bracket_array:
        deleted_bracket_array += valid_bracket_array
    # print(len(deleted_bracket_array))
    # print(count_1)
    print(min(count_1, len(deleted_bracket_array)))
def countValidStrings_3(s):
    valid_bracket_array = []
    invalid_bracket_array = []
    bracket_dictionary = {'{': '}', '[': ']', '(': ')'}   
    for ch in s:
        if ch in bracket_dictionary.keys():
            valid_bracket_array.append(ch)
        else:
            if not valid_bracket_array:
                invalid_bracket_array.append(ch)
                continue
            if bracket_dictionary.get(valid_bracket_array[-1]) != ch:
                invalid_bracket_array.append(ch)
            else:
                valid_bracket_array.pop()
    print(len(invalid_bracket_array))
 

countValidStrings_3("()())()") #1
countValidStrings_3("({[(])})") # 2
# countValidStrings_3("({[({{{])})") #5
# countValidStrings_3("{[[([}])]]") #2
# countValidStrings_3("((({{]}])]}})))")