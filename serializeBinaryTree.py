#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encoded = []
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            if node:
                encoded.append(str(node.val))
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                encoded.append('')
        return ','.join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        encoded = data.split(',')
        ans = TreeNode(encoded[0])
        i = 1
        queue = collections.deque([ans])
        while queue:
            # when you pop a node, its children will be at i and i+1
            node = queue.pop()
            if i < len(encoded) and encoded[i]:
                node.left = TreeNode(int(encoded[i]))
                queue.appendleft(node.left)
            i += 1
            if i < len(encoded) and encoded[i]:
                node.right = TreeNode(int(encoded[i]))
                queue.appendleft(node.right)
            i += 1
        return ans
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))