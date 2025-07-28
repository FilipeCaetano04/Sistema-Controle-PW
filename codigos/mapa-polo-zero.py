import control as ct
import numpy as np
import matplotlib.pyplot as plt

#coeficientes da transfer function
num = [5, 33.33]
den = [1, 0, 0]

sys = ct.TransferFunction(num, den)
print(sys)

plt.figure(figsize=(8,6))

ct.pzmap(sys, plot=True, title='Mapa Polo-Zero')
plt.xlabel('Eixo Real ($\sigma$)')
plt.ylabel('Eixo Imaginario ($j\omega$)')
plt.show()