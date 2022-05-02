import matplotlib.pyplot as plt
import numpy as np
 
# x값 설정
x = np.arange(1.18, 1.93, 2.95);

# log 예제
amplitude = np.log(np.e)
print(amplitude)
amplitude = np.log10(10)
print(amplitude)
amplitude = np.log2(2)
print(amplitude)
 
# y값 설정
amplitude = np.log(x)
 
print("amp: ", amplitude)
 
# 축 이름 설정
plt.xlabel('x axis')
plt.ylabel('y axis')
 
# 그리드 추가
plt.grid(color = "gray", alpha=.5,linestyle='--')
plt.plot(x,amplitude,label='log(x)')
 
# 범례 작성
plt.legend()
plt.show()