class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node,r=''):
    if not node:
        r +='# '
        return r
    r = r + (node.val)+" "
    r = serialize(node.left,r)
    r = serialize(node.right,r)
    return r

i=0
def deserialize(s):
    global i
    if s[i] == "#":
        if(i < len(s)-2):
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space+i
        node = Node(s[i:sp])
        i = sp+1
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
print("String after serializing node: "+serialize(node))
print("Assert: ",deserialize(serialize(node)).left.left.val == 'left.left')
