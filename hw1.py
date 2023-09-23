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
    # letter_count = list(character_dictionary.values())[0]
    value_dictionary = {}
    for ch in character_dictionary.values():
        if value_dictionary.get(ch) is None:
            value_dictionary[ch] = 1
        else:
            value_dictionary[ch] = value_dictionary[ch] + 1
    
    letter_count = max(value_dictionary, key=value_dictionary.get)

    for key in character_dictionary.keys():
        value = character_dictionary.get(key)
        if value == letter_count:
            continue
        else:
            if deletion_avaliable and (value - 1 == letter_count or value - 1 == 0):
                character_dictionary[key] = value - 1
                deletion_avaliable = False
            else:
                print("NO")
                return
    print("YES")

# print("is valid test cases")
# isValid("aabbcd")
# isValid("aabbcdddeefghi")
# isValid("pabcdefghhgfedcba")
# isValid("aabbcce")
# isValid("ggacc")


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
# isBalanced("{({}{}[][[([{}]){}]])}")
# isBalanced("()())()")
# isBalanced("{[]()}")

def countValidStrings(s):
    open_parenthesis = "("
    close_parenthesis = ")"
    array_of_s = list(s)
    open_dict = {}
    close_dict = {}
    for x, ch in enumerate(array_of_s):
        if ch is open_parenthesis:
            open_dict[x] = ch
        else:
            if open_parenthesis in open_dict.values():
                open_dict.popitem()
            else:
                close_dict[x] = ch
    invalid_dict = {**open_dict, **close_dict}
    print(invalid_dict)
    # for close_index in close_dict.keys():
    #     print(close_index)
    #     for open_index in open_dict.keys():
    #         print(open_index)
    i = 0
    while array_of_s[i] == close_parenthesis and i < close_dict
    pass

# countValidStrings("()())()") #(())() # ()()()
countValidStrings("()())((()()") #(())(()) # ()()()() # (())()()
# countValidStrings("(((((((())())(())((()")

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

    def sumTree(self, order = None):
        # print(self.sumTreeHelper())
        if self.label is None:
            return 0
        result = self.inOrderHelper(order)
        print(sum(result))
        return(sum(result))

# root = Node(2, Node(1, Node(6), Node(3)), Node(3, None, Node(9)))
# root.preOrder()
# root.inOrder()
# root.postOrder()
# root.getHeight(9)
# root.sumTree()


# print("\n")
# root = Node(1, Node(2, Node(3)), Node(4,None,(Node(5, None, Node(6, None, Node(7))))))
# root.preOrder()
# root.inOrder()
# root.postOrder()
# root.sumTree()
