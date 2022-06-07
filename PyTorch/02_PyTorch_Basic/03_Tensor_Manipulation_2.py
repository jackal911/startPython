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
print(ft.view([-1, 3]))  # -1을 넣은 인덱스의 차원은 numpy가 알아서 맞춰줌
print(ft.view([-1, 3]).shape)

# 4-2) 3차원 텐서의 크기 변경
print(ft.view([-1, 1, 3]))  # -1을 넣은 인덱스의 차원은 numpy가 알아서 맞춰줌
print(ft.view([-1, 1, 3]).shape)

# 5) 스퀴즈(Squeeze) - 1인 차원을 제거한다.
ft = torch.FloatTensor([[0], [1], [2]])
print(ft)  # tensor([[0.], [1.], [2.]])
print(ft.shape) # torch.Size([3, 1])
print(ft.squeeze())  # tensor([0., 1., 2.])
print(ft.squeeze().shape)  # torch.Size([3])

# 6) 언스퀴즈(Unsqueeze) - 특정 위치에 1인 차원을 추가한다.
ft = torch.Tensor([0, 1, 2])
print(ft.shape)  # torch.Size([3])
print(ft.unsqueeze(0))  # tensor([[0., 1., 2.]])
print(ft.unsqueeze(0).shape)  # torch.Size([1, 3])
print(ft.view(1, -1))  # tensor([[0., 1., 2.]])
print(ft.view(1, -1).shape)  # torch.Size([1, 3])
print(ft.unsqueeze(1))  # tensor([[0.], [1.], [2.]])
print(ft.unsqueeze(1).shape)  # torch.Size([3, 1])
print(ft.unsqueeze(-1))  # tensor([[0.], [1.], [2.]])
print(ft.unsqueeze(-1).shape)  # torch.Size([3, 1])

# 7) 타입 캐스팅(Type Casting)
lt = torch.LongTensor([1, 2, 3, 4])
print(lt)  # tensor([1, 2, 3, 4])
print(lt.float())  # tensor([1., 2., 3., 4.]) -- 점을 찍는게 float을 구분하는 의미였구나
bt = torch.ByteTensor([True, False, False, True])
print(bt)  # tensor([1, 0, 0, 1], dtype=torch.uint8)
print(bt.long())  # tensor([1, 0, 0, 1])
print(bt.float())  # tensor([1., 0., 0., 1.])

# 8) 연결하기(concatenate)

