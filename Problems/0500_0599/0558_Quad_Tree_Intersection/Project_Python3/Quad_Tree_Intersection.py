import json
import os
import sys
import time

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            return quadTree1.val and quadTree1 or quadTree2
        elif quadTree2.isLeaf:
            return quadTree2.val and quadTree2 or quadTree1
        else:
            tLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None) 
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node

def output_all_TreeNode(node):
    id = 1
    return "{" + output_TreeNode(node, id).replace("True", "true").replace("False", "false") + "}"

def output_TreeNode(node, id):
    if node == None:
        return ":null"

    resultStr = "\"$id\":\"" + str(id) + "\""

    resultStr += ",\"bottomLeft\":"
    if node.bottomLeft == None:
        resultStr += "null"
    else:
        resultStr += "{" + output_TreeNode(node.bottomLeft, id + 3) + "}"

    resultStr += ",\"bottomRight\":"
    if node.bottomRight == None:
        resultStr += "null"
    else:
        resultStr += "{" + output_TreeNode(node.bottomRight, id + 4) +"}"

    resultStr += ",\"isLeaf\":" + str(node.isLeaf)

    resultStr += ",\"topLeft\":"
    if node.topLeft == None:
        resultStr += "null"
    else:
        resultStr += "{" + output_TreeNode(node.topLeft, id + 1) + "}"

    resultStr += ",\"topRight\":"
    if node.topRight == None:
        resultStr += "null"
    else:
        resultStr += "{" + output_TreeNode(node.topRight, id + 2) +"}"

    resultStr += ",\"val\":" + str(node.val)

    return resultStr

def str_to_QuadTree(json_filename):
    print("JSON fileopen = {0}".format(json_filename))
    f = open(json_filename, 'r')
    data = json.load(f)

    if data == None:
        return None

    return json_to_QuadTree(data)

def json_to_QuadTree(data):
    if data == None:
        return None

    node =  Node(data['val'], data['isLeaf'], None, None, None, None)
    if data['topLeft'] != None:
        node.topLeft = json_to_QuadTree(data['topLeft'])
    if data['topRight'] != None:
        node.topRight = json_to_QuadTree(data['topRight'])
    if data['bottomLeft'] != None:
        node.bottomLeft = json_to_QuadTree(data['bottomLeft'])
    if data['bottomRight'] != None:
        node.bottomRight = json_to_QuadTree(data['bottomRight'])
    
    return node

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    json_filenames = temp.rstrip().replace("\"", "").replace("[[", "").replace("]]", "").split("],[")

    quadTree1 = str_to_QuadTree(json_filenames[0])
    quadTree2 = str_to_QuadTree(json_filenames[1])
    print("quadTree1 = \n{0}".format(output_all_TreeNode(quadTree1)))
    print("quadTree2 = \n{0}".format(output_all_TreeNode(quadTree2)))

    sl = Solution()
    time0 = time.time()

    result = sl.intersect(quadTree1, quadTree2)

    time1 = time.time()

    print("result = \n{0}".format(output_all_TreeNode(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
