import torch
import numpy as np
import pandas as pd
import os

# x=torch.arange(12)
# print(x.shape)
# print(x)
# X=x.reshape(3,4)
# print(X.shape)


# x=torch.arange(12,dtype=torch.float32).reshape(3,4)
# # y=torch.tensor([[2.0,1,3,4],[1,2,3,4],[4,3,2,1]])
# # print(torch.cat((x,y),dim=1))
#
# #转变为numpy
# A=x.numpy()
# print(type(A),A)

# os.makedirs(os.path.join('..','data'),exist_ok=True)
data_file=os.path.join('..','data','house_tiny.csv')
# with open(data_file,'w') as f:
#     f.write('NumRooms,Alley,Price\n')  # 列名
#     f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
#     f.write('2,NA,106000\n')
#     f.write('4,NA,178100\n')
#     f.write('NA,NA,140000\n')

#
# data=pd.read_csv(data_file)
# print(data)
#
# inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
# inputs = inputs.fillna(inputs.mean())
# print(inputs)
# print(outputs)
#
# X = torch.tensor(inputs.to_numpy(dtype=float))
# y = torch.tensor(outputs.to_numpy(dtype=float))

# x=torch.arange(20).reshape(5,2,2)
# print(x)
# A=x.T
# print(A)

# 范数 F2范数
# torch.norm()

#对哪一个维度求和就去消除哪一个维度
# x=torch.ones(3,6)
# print(x,x.shape)
# x.sum(axis=1)
# print(x,x.shape)


# 矩阵求导
x=torch.arange(4.0,requires_grad=True)
y=2*torch.dot(x,x)
y.backward()
print(x.grad,x.grad==4*x)

x.grad.zero_()
y=x*x
