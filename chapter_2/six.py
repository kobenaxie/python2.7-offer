# -*- coding:utf-8 -*-
"""
问题描述：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
         例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
思路：首先根据前序遍历第一个节点确定根节点，然后在中序遍历中找到根节点，这样就可以得到左子树与右子树各自的长度；
然后前序遍历和中序遍历根据长度分割出前序【左子树、右子树】和中序遍历的【左子树、右子树】，递归即可。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # pre and tin are list.
        if not pre or not tin:
            return
        root = TreeNode(pre[0])
        i = tin.index(root.val) #中序遍历中根节点的位置
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root
