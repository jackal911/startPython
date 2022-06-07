import numpy as np
import torch
from torch import FloatTensor

# 2. 넘파이로 텐서 만들기(벡터와 행렬 만들기)
# 1) 1D with Numpy
t = np.array([0, 1, 2, 3., 4., 5., 6.])
print(t)
print('Rank of t: ', t.ndim)  # 몇 차원인지
print('Shape of t: ', t.shape)  # 크기
print('t[0] t[1] t[-1] = ', t[0], t[1], t[-1])
print('t[2:5] t[4:-1] = ', t[2:5], t[4:-1])
# 2) 2D with Numpy
t = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
print(t)
print('Rank  of t: ', t.ndim)
print('Shape of t: ', t.shape)

# 3. 파이토치 텐서 선언하기(PyTorch Tensor Allocation)
# 1) 1D with PyTorch
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print(t)
print(t.dim())
print(t.shape)
print(t.size())
print(t[0], t[1], t[-1])
print(t[2:5], t[4:-1])
print(t[:2], t[3:])

# 2) 2D with PyTorch
t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]
                       ])
print(t)
print(t.dim())
print(t.size())
print(t[:, 1])
print(t[:, 1].size())
print(t[:, :-1])

# 3) Broadcasting
m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(m1 + m2)
# Vector + scalar
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([3])  # [3] -> [3, 3]
print(m1 + m2)
# 2 x 1 Vector + 1 x 2 Vector
m1 = torch.FloatTensor([[1, 2]])  # 1 x 2
m2 = torch.FloatTensor([[3], [4]])  # 2 x 1
print(m1 + m2)  # [[1, 2]] ==> [[1, 2], [1, 2]] / [[3],[4]] ==> [[3, 3], [4, 4]]

# 4) 자주 사용되는 기능들
# 행렬 곱셈과 곱셈의 차이
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print('Shape of Matrix 1: ', m1.shape)  # 2 x 2
print('Shape of Matrix 2: ', m2.shape)  # 2 x 1
print(m1.matmul(m2))  # 수학에서의 행렬 곱
print(m1 * m2)  # 요소 곱?
print(m1.mul(m2))  # Broadcasting - m1: [[1], [2]] ==> [[1, 1], [2, 2]]

# 평균(Mean)
t = torch.FloatTensor([1, 2])
print(t.mean())
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)
print(t.mean())  # 단순 평균
print(t.mean(dim=0))  # 행 제거
print(t.mean(dim=1))  # 열 제거
print(t.mean(dim=-1))  # 마지막 차원 제거. 여기선 열 제거

# 3) 덧셈(Sum)
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)
print(t.sum())
print(t.sum(dim=0))
print(t.sum(dim=1))
print(t.sum(dim=-1))

# 4) 최대(Max)와 아그맥스(ArgMax)
print(t.max())  # tensor(4.)
print(t.max(dim=0))  # torch.return_types.max(
                     # values=tensor([3., 4.]),
                     # indices=tensor([1, 1]))
print('Max: ', t.max(dim=0)[0])  # Max:  tensor([3., 4.])
print('Argmax: ', t.max(dim=0)[1])  # Argmax:  tensor([1, 1])
print(t.max(dim=1))  # torch.return_types.max(
                     # values=tensor([2., 4.]),
                     # indices=tensor([1, 1]))                     
print(t.max(dim=-1))  # torch.return_types.max(
                      # values=tensor([2., 4.]),
                      # indices=tensor([1, 1]))
