# 4) 뷰(View) - 원소의 수를 유지하면서 텐서의 크기 변경. 매우 중요함!!
import numpy as np
import torch


t = np.array([[[0, 1, 2],
               [3, 4, 5]],
              [[6, 7, 8],
               [9, 10, 11]]])
ft = torch.FloatTensor(t)
print(ft.shape)

# 4-1) 3차원 텐서에서 2차원 텐서로 변경
print(ft.view([-1, 3]))
print(ft.view([-1, 3]).shape)

# 4-2) 3차원 텐서의 크기 변경
