import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros do sistema
a = 1.5
b = 3.0
u1_const = 10.0 

# Amplitude do degrau para o volante (u2)
A = 0.05 

# Intervalo de tempo
t_span = [0, 5]
t_eval = np.linspace(t_span[0], t_span[1], 500)

# Simulação do Sistema NÃO LINEAR
def nonlinear_model(t, x, u1, u2):
    x2, x3 = x
    alpha = np.arctan((a * np.tan(u2)) / b)
    dx2_dt = u1 * np.sin(alpha + x3)
    dx3_dt = (u1 * np.sin(alpha)) / a
    return [dx2_dt, dx3_dt]

x0_nonlinear = [0, 0]
sol_nonlinear = solve_ivp(
    lambda t, x: nonlinear_model(t, x, u1_const, A),
    t_span,
    x0_nonlinear,
    t_eval=t_eval
)
x2_nonlinear = sol_nonlinear.y[0]
# x3_nonlinear = sol_nonlinear.y[1]

# Simulação do Sistema Linearizado
# Expressões obtidas a partir do estado de espaços formado após linearização
def funcao_x2_modelo_linear(t, A):
    return (5*t + t**2 * 50/3)*A

# def funcao_x3_modelo_linear(t, A):
#     return (10 * A * t) / 3

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(7, 5))

# Gráfico de X2 (Posição Lateral)
plt.plot(t_eval, x2_nonlinear, 'b-', label='Não Linear', linewidth=2.5)
plt.plot(t_eval, funcao_x2_modelo_linear(t_eval, A), 'r--', label='Linearizado', linewidth=2)
plt.title(f'Comparação das Respostas para um Degrau de Amplitude A = {A} rad', fontsize=14)
plt.ylabel('Posição Lateral $x_2(t)$ (m)', fontsize=12)
plt.xlabel('Tempo $t$ (s)', fontsize=12)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()