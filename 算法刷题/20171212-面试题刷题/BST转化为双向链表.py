'''问题描述：
输入一棵二元查找树,将该二元查找树转换成一个排序的双向链表。
要求不能创建任何新的结点,只调整指针的指向
'''
'''问题分析：
1)中序遍历完成转换，升序排序
2)plast指向双向链表尾部，要保持对双向链表尾部的跟踪
3)pcu节点的leftchild指向小值
4)plast节点的righchild指向大值
5)plast指向pcur，保持链表尾部跟踪
'''

#树节点结构
class treeNode(object):
	def __init__(self, value=None, leftchild=None, rightchild=None):
		self.value = value
		self.leftchild = leftchild
		self.rightchild = rightchild

# --------------------------------solution-------------------------
plast = treeNode()
def inorder_transform(tree, plast):
	# 若为空，则返回
	if not tree: 
		return 

	# 指向当前节点
	pcur = tree 

	# 递归转化左子树
	if pcur.leftchild:
		inorder_transform(pcur.leftchild,plast)
	
	# 将节点置入双向链表中，plast始终指向尾部，pcur较plast高一层
	pcur.leftchild = plast

	if plast:
		plast.rightchild = pcur
	plast = pcur # 调整至尾部

	# 递归转化右子树
	if plast.rightchild:
		inorder_transform(pcur.rightchild,plast)
# ------------------------------solution end------------------------

# 测试用例
root = treeNode(10, None, None)

left = treeNode(4, treeNode(3, None, None), treeNode(5, None, None))

right = treeNode(12, treeNode(11, None, None), treeNode(13, None, None))

root.leftchild = left
root.rightchild = right

def show(tree):
	if tree:
		show(tree.leftchild)
		print(tree.value)
		show(tree.rightchild)

def show(node):
    rst = [node.value]
    leftCur, rightCur = node, node
    while leftCur.leftchild != None:
        rst.insert(0, leftCur.leftchild.value)
        leftCur = leftCur.leftchild
    while rightCur.rightchild != None:
        rst.append(rightCur.rightchild.value)
        rightCur = rightCur.rightchild
    print(rst)