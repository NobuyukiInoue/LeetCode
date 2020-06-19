# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from .TreeNode import TreeNode

class Codec:
    # 112ms

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                # vals.append('#')
                vals.append('null')
        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            try:
                val = next(vals)
                if val == '#':
                    return None
                elif val == "null":
                    return None
                else:
                    node = TreeNode(int(val))
                    node.left = helper()
                    node.right = helper()
                return node
            except:
                return None
        vals = iter(data.split(","))
        return helper()
