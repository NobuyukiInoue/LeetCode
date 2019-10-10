import json
import os
import sys
import time

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
#    def postorder(self, root: 'Node') -> List[int]:
    def postorder(self, root):
        output = []
        stack = [root]
        if not root:
            return output
        while stack:
            last = stack.pop()
            if last.children != None:
                stack += last.children
            output += [last.val]
        return output[::-1]

    def set_sample_node(self):
        n1_list = []
        n1_list.append(Node(5, None))
        n1_list.append(Node(6, None))

        n0_list = []
        n0_list.append(Node(3, n1_list))
        n0_list.append(Node(2, None))
        n0_list.append(Node(4, None))

        node = Node(1, n0_list)
        return node

    def output_node(self, node):
        if node == None:
            return ""
        
        self.resultStr = []
        self.resultStr.append(str(node.val))
        self.set_output_node(node, 1)

        if len(self.resultStr) <= 0:
            return ""

        result = "[\n"
        for i in range(0, len(self.resultStr)):
            if i < len(self.resultStr) - 1:
                result += "\t[" + self.resultStr[i] + "],\n"
            else:
                result += "\t[" + self.resultStr[i] + "]\n"
        result += "]"

        return result
                
    def set_output_node(self, node, n):
        if node.children == None:
            return

        tempStr = ""
        for i in range(0, len(node.children)):
            if i == 0:
                tempStr += str(node.children[i].val)
            else:
                tempStr += "," + str(node.children[i].val)

        if len(self.resultStr) <= n:
            self.resultStr.append(tempStr)
        else:
            self.resultStr[n] += tempStr

        for i in range(0, len(node.children)):
            self.set_output_node(node.children[i], n + 1)

def str_to_Node(json_text):
    data = json.loads(json_text)
    if data == None:
        return None
    return json_to_Node(data)

def json_to_Node(data):
    if data == None:
        return None

    node = Node(data['val'], None)
    if len(data['children']) > 0:
        node.children = []
        for children in data['children']:
            node.children.append(json_to_Node(children))
    
    return node

def loop_main(temp):
    json_text = temp.rstrip()

    sl = Solution()

    root = str_to_Node(json_text)
#    root = sl.set_sample_node()
    print("%s" %(sl.output_node(root)))

    time0 = time.time()

    result = sl.postorder(root)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)

if __name__ == "__main__":
    main()
