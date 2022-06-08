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
x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.FloatTensor([[5, 6], [7, 8]])
print(torch.cat([x, y], dim=0))  # tensor([[1., 2.], [3., 4.], [5., 6.], [7., 8.]])
print(torch.cat([x, y], dim=1))  # tensor([[1., 2., 5., 6.], [3., 4., 7., 8.]])

# 9) 스택킹(Stacking)
x = torch.FloatTensor([1, 4])
y = torch.FloatTensor([2, 5])
z = torch.FloatTensor([3, 6])
print(torch.stack([x, y, z]))  # tensor([[1., 4.], [2., 5.], [3., 6.]])
print(torch.stack([x, y, z], dim=1))  # tensor([[1., 2., 3.], [4., 5., 6.]]) -- 두번째 차원이 증가하도록 쌓아라! 라는 뜻으로 해석하면됨

# 10) ones_like와 zeros_like - 0으로 채워진 텐서와 1로 채워진 텐서
x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
print(x)  # tensor([[0., 1., 2.], [2., 1., 0.]])
print(torch.ones_like(x))  # tensor([[1., 1., 1.], [1., 1., 1.]]) -- 입력 텐서와 크기를 동일하게 하면서 값을 1로 채우기
print(torch.zeros_like(x))  # tensor([[0., 0., 0.], [0., 0., 0.]])

# 11) In-place Operation (덮어쓰기 연산)
x = torch.FloatTensor([[1, 2], [3, 4]])
print(x.mul(2.))  # tensor([[2., 4.], [6., 8.]])
print(x)  # tensor([[1., 2.], [3., 4.]]) -- mul을 수행했지만 저장을 안했으므로 x는 보존
print(x.mul_(2.))  # tensor([[2., 4.], [6., 8.]])
print(x)  # tensor([[2., 4.], [6., 8.]]) -- _mul은 출력하면서 결과를 x에 저장

