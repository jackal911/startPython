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

# 5) 파이토치로 선형 회구 구현하기
import torch
import torch.nn as nn

