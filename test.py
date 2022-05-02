import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
samples = [0,10,20,30,1,11,21,31]
d = []
for i in range(8):
    d.append(digits.images[samples[i]])

plt.figure(figsize=(8, 2))

for i in range(8):
    plt.subplot(1, 8, i+1)
    plt.imshow(d[i], interpolation='nearest', cmap=plt.cm.bone_r)
    plt.grid(False); plt.xticks([]); plt.yticks([])
    plt.title("image {}".format(i+1))
plt.suptitle("숫자 0과 1 이미지")
plt.tight_layout()
plt.show