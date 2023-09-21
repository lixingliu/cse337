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
# isBalanced("{[]()}")

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
                if bracket_dictionary.get(valid_bracket_array[-1]) in invalid_bracket_array:
                    invalid_bracket_array.append(valid_bracket_array.pop())
                if bracket_dictionary.get(valid_bracket_array[-1]) == ch:
                    valid_bracket_array.pop()
                else:
                    invalid_bracket_array.append(ch)
            else:
                valid_bracket_array.pop()
    print(len(invalid_bracket_array))
 

# countValidStrings_3("()())()") #1
# countValidStrings_3("({[(])})") # 2
# countValidStrings_3("({[({{{])})") #5
# countValidStrings_3("({[({{{)])})") #3

# countValidStrings_3("{[[([}])]]") #2
# countValidStrings_3("((({{]}])]}})))")





class Node:
    def __init__(self, label, left_child = None, right_child = None, left_child_seen = False, right_child_seen = False, level = 0):
        self.label = label
        self.left_child = left_child
        self.right_child = right_child
        self.level = level

    def preOrderHelper(self, order = None):        
        if order is None:
            order = []
        order.append(self.label)
        if self.left_child:
            self.left_child.preOrderHelper(order)
        if self.right_child:
            self.right_child.preOrderHelper(order)
        return order
        
    def preOrder(self, order = None):
        print(self.preOrderHelper(order))

    def inOrderHelper(self, order = None):
        if order is None:
            order = []
        if self.left_child:
            self.left_child.inOrderHelper(order)
        order.append(self.label)
        if self.right_child:
            self.right_child.inOrderHelper(order)
        return order

    def inOrder(self, order = None):
        print(self.inOrderHelper(order))

    def postOrderHelper(self, order = None):
        if order is None:
            order = []
        if self.left_child:
            self.left_child.postOrderHelper(order)
        if self.right_child:
            self.right_child.postOrderHelper(order)
        order.append(self.label)
        return order
    
    def postOrder(self, order = None):
        print(self.postOrderHelper(order))

    def getHeightHelper(self, value):
        result = -1
        if self.label == value:
            return self.level
        if self.left_child:
            self.left_child.level = self.level + 1
            result = self.left_child.getHeightHelper(value)
        if self.right_child:
            self.right_child.level = self.level + 1
            result = self.right_child.getHeightHelper(value)
        return result

    def getHeight(self, value):
        print(self.getHeightHelper(value))

    def sumTreeHelper(self):
        print(self.label)
        if self.label is None:
            return 0
        

    def sumTree(self, order = None):
        # print(self.sumTreeHelper())
        if self.label is None:
            return 0
        
        result = self.inOrderHelper(order)
        print(sum(result))
        return sum(result)

root = Node(2, Node(1, Node(6), Node(3)), Node(3, None, Node(9)))
# root.preOrder()
# root.inOrder()
# root.postOrder()
# root.getHeight(9)
root.sumTree()


# print("\n")
root = Node(1, Node(2, Node(3)), Node(4,None,(Node(5, None, Node(6, None, Node(7))))))
# root.preOrder()
# root.inOrder()
# root.postOrder()
root.sumTree()
