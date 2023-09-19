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
                invalid_bracket_array.append(ch)
    print(len(invalid_bracket_array))
    
countValidStrings("({[(])})")