# 01_선형 회귀 https://wikidocs.net/53560

import torch

# 1. 데이터에 대한 이해(Data Definition)
# 1) 훈련 데이터셋과 테스트 데이터셋
x_train = torch.FloatTensor([[1], [2], [3]]) # 입력 : 공부한 시간
y_train = torch.FloatTensor([[2], [4], [6]]) # 출력 : 점수
# 2) 가설(Hypothesis) 수립
'''
* 선형 회귀의 가설(직선의 방정식) : y = Wx + b
 - W는 가중치(Weight), b를 편향(bias)라고 한다.
'''
# 3) 비용 함수(Cost function)에 대한 이해
'''
* 비용 함수(cost function) = 손실 함수(loss function) = 오차 함수(error function) = 목적 함수(objective function)
* 평균 제곱 오차(Mean Squared Error, MSE)
* Cost(W,b)를 최소가 되게 만드는 W와 b를 구하면 훈련 데이터를 가장 잘 나타내는 직선을 구할 수 있다.
'''

# 4) 옵티마이저 - 경사 하강법(Gradient Descent)
'''
* 옵티마이저(Optimizer) 알고리즘 = 최적화 알고리즘 : 비용함수의 값을 최소로 하는 W와 b를 찾는 방법.
* 이 옵티마이저 알고리즘을 통해 적절한 W와 b를 찾아내는 과정을 머신 러닝에서 학습(training)이라고 부른다.
* 여기서 가장 기본적인 옵티마이저 알고리즘인 경사 하강법(Gradient Descent)에 대해 배운다.
* 
'''

# 5) 파이토치로 선형 회귀 구현하기
# a. 기본 셋팅
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)  # 코드를 재실행해도 같은 결과가 나오도록 랜덤 시드를 준다.

# b. 변수 선언
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
print(x_train)
print(x_train.shape)
print(y_train)
print(y_train.shape)

# c. 가중치와 편향의 초기화
# 가중치 W를 0으로 초기화하고 학습을 통해 값이 변경된느 변수임을 명시함.
W = torch.zeros(1, requires_grad=True)
# 가중치 W를 출력
print(W)
# 편향 b도 마찬가지
b = torch.zeros(1, requires_grad=True)
print(b)

# d. 가설 세우기
hypothesis = x_train * W + b
print(hypothesis)

# e. 비용 함수 선언하기
# 앞서 배운 torch.mean으로 평균을 구한다.
cost = torch.mean((hypothesis - y_train) ** 2)
print(cost)

# f. 경사 하강법 구현하기
# SGD 는 경사 하강법의 일종, lr은 학습률(learning rate)
optimizer = optim.SGD([W, b], lr=0.01)
# gradient를 0으로 초기화
optimizer.zero_grad()
# 비용 함수를 미분하여 gradient 계산
cost.backward()
# W와 b를 업데이트
optimizer.step()

# g. 전체 코드
'''
# 데이터
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
# 모델 초기화
W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = optim.SGD([W, b], lr=0.01)

nb_epochs = 1999 # 원하는만큼 경사 하강법을 반복
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    hypothesis = x_train * W + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, W.item(), b.item(), cost.item()
        ))
'''
# 에포크(Epoch)는 전체 훈련 데이터가 학습에 한 번 사용된 주기를 말한다. 이번 실습의 경우 2000번 수행했다.
# 최종 훈련 결과를 보면 최적의 기울기 W는 2에 가깝고, b는 0에 가까운 것을 볼 수 있다. 실제 정답은 W = 2, b = 0인 H(x) = 2x 이므로 거의 정답을 찾은 셈이다.

# 6. optimizer.zero_grad()가 필요한 이유
import torch
w = torch.tensor(2.0, requires_grad=True)

nb_epochs = 20
for epoch in range(nb_epochs + 1):
    z = 2*w
    z.backward()
    print('수식을 w로 미분한 값 : {}'.format(w.grad))
    
# 7. torch.manual_seed()를 하는 이유
# torch.manual_seed()는 난수 발생 순서와 값을 동일하게 보장해준다.
import torch
torch.manual_seed(3)
print('랜덤 시드가 3일 때')
for i in range(1,3):
    print(torch.rand(1))
# 0.0043, 0.1056이 나온다.

# 랜덤 시드값을 바꿔본다.
torch.manual_seed(5)
print('랜덤 시드가 5일 때')
for i in range(1,3):
    print(torch.rand(1))
# 0.8303, 0.1261이 나온다.

# 랜덤 시드값을 다시 3으로 돌려본다.
torch.manual_seed(3)
print('랜덤 시드가 다시 3일 때')
for i in range(1,3):
    print(torch.rand(1))
# 다시 동일하게 0.0043, 0.1056이 나온다.
