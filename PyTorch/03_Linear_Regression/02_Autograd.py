# 자동 미분 https://wikidocs.net/60754
# 1) 경사 하강법 리뷰
'''
모델이 복잡해질수록 경사 하강법을 넘파이 등으로 직접 코딩하는 것은 까다로운 일이다. 파이토치는 이런 수고를 하지 않도록 자동 미분(Autograd)을 지원한다.
'''
# 2) 자동 미분(Autograd) 실습하기
# 2w**2 + 5를 미분해보자
import torch

# 값이 2인 임의의 스칼라 텐서 w 선언. 이때 required_grad를 True로 설정한다. 이는 이 텐서에 대한 기울기를 저장하겠다는 의미이다.
w = torch.tensor(2.0, requires_grad=True)
y = w**2
z = 2*y+5
z.backward()
print('수식을 w로 미분한 값 : {}'.format(w.grad))
