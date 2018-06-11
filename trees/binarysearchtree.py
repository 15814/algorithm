

# 二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树（英语：ordered binary tree），排序二叉树（英语：sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
#
# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
# 没有键值相等的节点。
# 二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为O(log n)。二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、multiset、关联数组等


def isbst_recur(root, predata):

    if root:

        isbst_recur(root.left,predata)

        curdata = root.data

        if curdata < predata:
            print('False')
            return False
        predata = curdata
        print('curdata: ',curdata)
        print('predata: ',predata)
        isbst_recur(root.right,predata)

        return True




def main():
    import binarytree
    from binarytree import BiTreeNode as Node

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(isbst_recur(root,-1))




















if __name__ == '__main__':
    main()
