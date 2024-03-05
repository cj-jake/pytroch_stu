"""
构建一个颗树 找出树得最深两个路径
电脑可以看成是交换机
"""

#书的节点信息
class TreeNode:
    def __init__(self,value):
        self.chridren=[]
        self.value=value


#读取输入
n,m=map(int,input().split())
switchboard_list=list(map(int,input().split()))
switchboard_list.index(0,0)
computer_list=list(map(int,input().split()))

#构建树
def bulid(self,n,m,switchboard_list:list,computer_list:list):
    nodes=[TreeNode(i+1) for i in range(n+m)]

    #构建交换机之间的连接关系
    for i in (1,n):
        parent=nodes[switchboard_list[i-1]-1]

    #构建交换机和电脑之间的关系


#获得树路径 list 选出最深得两条