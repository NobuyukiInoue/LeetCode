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
    def construct(self, grid):
        if len(grid) == 1:
            return Node(grid[0][0]==1, True, None, None, None, None)
        else:
            half_len = len(grid)//2
            topLeft = self.construct([elem[:half_len] for elem in grid[:half_len]])
            topRight = self.construct([elem[half_len:] for elem in grid[:half_len]])
            bottomLeft = self.construct([elem[:half_len] for elem in grid[half_len:]])
            bottomRight = self.construct([elem[half_len:] for elem in grid[half_len:]])
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

    def construct_work(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        node = Node(True, False, None, None, None, None)
        quadGrid = self.get_Quad(grid)

        if self.check_Leaf(quadGrid[0]):
            node.topLeft = Node(self.get_gridVal(quadGrid[0]), True, None, None, None, None)
        else:
            node.topLeft = self.construct(quadGrid[0])

        if self.check_Leaf(quadGrid[1]):
            node.topRight = Node(self.get_gridVal(quadGrid[1]), True, None, None, None, None)
        else:
            node.topRight = self.construct(quadGrid[1])

        if self.check_Leaf(quadGrid[2]):
            node.bottomLeft = Node(self.get_gridVal(quadGrid[2]), True, None, None, None, None)
        else:
            node.bottomLeft = self.construct(quadGrid[2])

        if self.check_Leaf(quadGrid[3]):
            node.bottomRight = Node(self.get_gridVal(quadGrid[3]), True, None, None, None, None)
        else:
            node.bottomRight = self.construct(quadGrid[3])

        return node

    def get_Quad(self, grid):
        width = int(len(grid)/2)
        quadGrid = [[[0]*width]*width]*4
        quadGrid[0] = self.get_topLeft(grid, width)
        quadGrid[1] = self.get_topRight(grid, width)
        quadGrid[2] = self.get_bottomLeft(grid, width)
        quadGrid[3] = self.get_bottomRight(grid, width)
        return quadGrid
    
    def check_Leaf(self, grid):
        for i in range(len(grid)):
            for j in range(i + 1, len(grid)):
                if grid[i] != grid[j]:
                    return False
        return True

    def get_gridVal(self, grid):
        if grid[0][0] == 1:
            return True
        else:
            return False


    def get_topLeft(self, grid, width):
        topLeft = [[0]*width]*width
        for i in range(width):
            topLeft[i] = grid[i][0:width]
        return topLeft

    def get_topRight(self, grid, width):
        topRight = [[0]*width]*width
        for i in range(width):
            topRight[i] = grid[i][width:len(grid)]
        return topRight
    
    def get_bottomLeft(self, grid, width):
        bottomLeft = [[0]*width]*width
        for i in range(width):
            bottomLeft[i] = grid[i + width][0:width]
        return bottomLeft

    def get_bottomRight(self, grid, width):
        bottomRight = [[0]*width]*width
        for i in range(width):
            bottomRight[i] = grid[i + width][width:len(grid)]
        return bottomRight

    
    def set_test_nodes(self):
        node0 = Node(False, False, None, None, None, None)
        node0.topLeft = Node(True, True, None, None, None, None)
        node0.topRight = Node(False, False, None, None, None, None)
        node0.topRight.topLeft = Node(True, False, None, None, None, None)
        node0.topRight.topRight = Node(True, False, None, None, None, None)
        node0.topRight.bottomLeft = Node(True, False, None, None, None, None)
        node0.topRight.bottomRight = Node(True, True, None, None, None, None)
        node0.bottomLeft = Node(True, True, None, None, None, None)
        node0.bottomRight = Node(True, False, None, None, None, None)

        return node0

    def get_node_depth(self, node, depth):
        n = [0]*4
        if node.topLeft != None:
            n[0] = self.get_node_depth(node.topLeft, depth + 1)
        if node.topRight != None:
            n[1] = self.get_node_depth(node.topRight, depth + 1)
        if node.bottomLeft != None:
            n[2] = self.get_node_depth(node.bottomLeft, depth + 1)
        if node.bottomRight != None:
            n[3] = self.get_node_depth(node.bottomRight, depth + 1)
        max = depth
        for temp in n:
            if temp > max:
                max = temp
        return max
    
    def output_node(self, node):
        grid_size = 2 ** self.get_node_depth(node, 1)
        grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

        half = int(grid_size/2)
        self.set_val(node.topLeft, grid, 0, 0, half)
        self.set_val(node.topRight, grid, half, 0, half)
        self.set_val(node.bottomLeft, grid, 0, half, half)
        self.set_val(node.bottomRight, grid, half, half, half)

        return grid
    
    def set_val(self, node, grid, x, y, size):
        half = int(size/2)
        if node.val:
            val = 1
        else:
            val = 0
        if node.isLeaf:
            for i in range(y, y + size):
                for j in range(x, x + size):
                    grid[i][j] = val
            return
        if node.topLeft != None:
            self.set_val(node.topLeft, grid, x, y, half)
        if node.topRight != None:
            self.set_val(node.topRight, grid, x + half, y, half)
        if node.bottomLeft != None:
            self.set_val(node.bottomLeft, grid, x, y + half, half)
        if node.bottomRight != None:
            self.set_val(node.bottomRight, grid, x + half, y + half, half)
        return

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

def flds_to_int_array(flds):
    #grid = [[-1]*len(flds)]*len(flds)
    grid = [[-1 for j in range(len(flds))] for i in range(len(flds))]

    if len(flds) <= 0:
        return grid

    for i in range(0, len(flds)):
        grid[i] = [int(n) for n in flds[i].split(",")]

    return grid

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
    var_str = temp.replace("[[","").replace("]]","").rstrip()

    flds = var_str.split("],[")
    grid = flds_to_int_array(flds)
    print("grid = {0}".format(grid))

    sl = Solution()
    time0 = time.time()

    result_node = sl.construct(grid)

    time1 = time.time()

    #result_str = sl.output_node(result_node)
    #print("result = {0}".format(result_str))
    print("\n{0}".format(output_all_TreeNode(result_node)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
