import control as ct
import matplotlib.pyplot as plt
import numpy as np


# A funcao de transferencia calculada foi T(s) = (5s + 33.33) / s^2

#coeficientes
num = [5, 100/3]
den = [1, 0, 0]

T = ct.tf(num, den)

#print(T)

#escolhido por padrao da .step_response degrau de amplitude 1.
t, y = ct.step_response(T)


plt.figure(figsize=(10, 6))
plt.plot(t, y, linewidth=2, label='Resposta ao Degrau')

plt.title('Resposta ao Degrau do Sistema Linearizado', fontsize=16)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Posicao Lateral ($x_2$)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()