import random
import numpy as np

class LinearRegresssion():
    def __init__(self, eta, howmany):
        self.lr = eta #학습률
        self.howmany = howmany #반복횟수
        self.w = 0.0 #가중치
        self.b = 0.0 #편향

    def MSE(self, X, Y, Weight, Bias): #이때 X,Y는 리스트, Wight, Bias는 상수
        L = len(X) #학습 데이터의 총 개수
        total_MSE = 0.0 #초기 평균제곱 오차 설정
        for i in range(L):
            total_MSE += (Y[i] - (Weight*X[i] + Bias))**2 #MSE값 계산식
        return total_MSE/L #계산한 평균제곱오차를 반환
    
    def update_Weights(self, X, Y, Weight, Bias, learning_rate): #MSE와 받는 것이 동일하지만, learnig_rate 라는 학습률을 추가로 받는다.
        dw = 0 #초기 가중치 설정
        db = 0 #초기 편향 설정
        L = len(X) #학습데이터의 총 개수

        indexs = [] #랜덤으로 데이터를 선정하기 위한 배열을 생성한다.
        for o in range(L): #학습 데이터의 총 개수만큼의 숫자를 랜덤으로 인덱스에 저장한다.
            indexs = np.random.choice(range(0,L),L,replace=False)
        random.shuffle(indexs) #저장한 인덱스를 또 섞어준다. 
        batch_size = 4 #내가 임의로 정할 수 있는 배치 사이즈

        for k in range(batch_size): #배치 사이즈 만큼만 학습한다.
            i = indexs[k] #인덱스에서 랜덤한 배열의 칸( X[랜덤] )의 데이터를 가져와서 학습
            dw += -2 * X[i] * (Y[i] - (Weight * X[i] + Bias))
            db += -2 * (Y[i] - (Weight * X[i] + Bias))

        Weight -= (dw / L) * learning_rate #학습률을 곱해주어 안정성을 높여준다.
        Bias -= (db / L) * learning_rate

        return Weight, Bias #가중치와 편향을 반환
    
    def fit(self, X, Y):
        cost_history = [] #리턴할 때 편하게 하기 위해 배열로 만들었다.

        for i in range(self.howmany): # 경사하강법으로 가중치와 편향을 조정
            self.w, self.b = self.update_Weights(X, Y, self.w, self.b, self.lr)

            cost = self.MSE(X, Y, self.w, self.b) #수정 목적을 위한 계산비용
            cost_history.append(cost) #append를 사용했기때문에 자연스럽게 배열에 추가

            if i % 10 == 0: #i는 이미 self.howmany만큼 커져있기에 10번마다 반복횟수와 가중치 편향 평균제곱 오차를 출력해 줄 것이다.
                print("반복횟수 = {:d}      가중치 = {:.2f}     편향 = {:.4f}       평균제곱오차 = {:.2}".format(i, self.w, self.b, cost))

        return self.w, self.b, cost_history #최종 가중치 편향 최소제곱오차를 반환
    
    def predict(self, x): #예측치를 리턴하는 함수
        x = (x+100) / 300 #나중에 나오겠지만 x값을 데이터 정규화 시키는 과정이다.
        return self.w * x + self.b
    
x = [1, 8, 3, 13, 66, 52, 104, -2, -100, -11, -52, -20] #학습할 x값
y = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0] #학습할 y값

model = LinearRegresssion(0.01, 500) #햑습률을 정하고 몇번 반복할지 결정

X = [(k + 100) / 300 for k in x] #x값인 데이터를 정규화 시키는 과정이다. 닫힌구간 0,1 사이에 값이 존재하기 위해서 +200과 -100 사이 값으로 조정하는 과정이다.

model.fit(X, y) #선형식을 구한다.

test_x = [70, 64, 81, 82, 75, 220, 32, 151, 5, 1, -1, -154, -27, -22, -33, -49, -60, -92] #예측해볼 데이터들

for i in range(len(test_x)): #출력문
    print("input {} =>predict : {}".format(test_x[i], model.predict(test_x[i])))