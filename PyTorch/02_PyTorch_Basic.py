import numpy as np
import torch

# 2. 넘파이로 텐서 만들기(벡터와 행렬 만들기)
# 1D with Numpy
t = np.array([0, 1, 2, 3., 4., 5., 6.])
print(t)
print('Rank of t: ', t.ndim)  # 몇 차원인지
print('Shape of t: ', t.shape)  # 크기
print('t[0] t[1] t[-1] = ', t[0], t[1], t[-1])
print('t[2:5] t[4:-1] = ', t[2:5], t[4:-1])

# 2D with Numpy
t = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
print(t)
print('Rank  of t: ', t.ndim)
print('Shape of t: ', t.shape)

# 3. 파이토치 텐서 선언하기(PyTorch Tensor Allocation)
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print(t)
