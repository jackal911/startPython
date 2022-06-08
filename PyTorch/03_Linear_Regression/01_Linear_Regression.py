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

