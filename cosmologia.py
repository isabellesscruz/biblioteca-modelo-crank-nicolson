import numpy as np
import matplotlib.pyplot as plt
from cn import crank_nicolson as cn

# Parâmetros para alimentar o método
A = 0.001
B = 0.001
kappa_ = -1/12
lambda_ = 1j
L = 50.0  # comprimento do domínio
a, b = 0, 50  # limites do domínio
nx = 5000  # número de pontos de dados
dx = L / (nx)  # passo espacial
dt = 0.005  # passo de tempo
times_to_plot = [5]  # tempo para plotar
nt = int(max(times_to_plot) / dt)  # número total de passos de tempo

# Potencial
def V(x):
    if x == 0:
        return 0
    else:
        return 3 * x**2 - ((x**4 / np.pi) * np.sqrt(A + (B / np.power(x, 6))))

# Função para definir a função de onda inicial Psi
def Psi(a):
    E_m = 220
    return (8 * np.power(2, 1/4) * np.power(E_m, 3/4) * a * np.exp(-4 * a**2 * E_m)) / np.power(np.pi, 1/4)  # Estado fundamental da função de onda

# Função para calcular a soma de psi*psi * deltax: Integridade da função de onda.
def calculate_sum(psi, dx):
    return np.sum(np.abs(psi)**2) * dx

# Passo 1: Configuração inicial dos parâmetros do CN, complexo ou real
x_vals = np.linspace(a, b, nx+1)  # valores de x no domínio
psi = np.array([Psi(x) for x in x_vals], dtype=complex)  # iniciação da função de onda (psi(x,0))
psi[0] = psi[-1] = 0  # condições de contorno

# Parâmetros para as matrizes de Crank-Nicolson
r = kappa_*dt/(2*lambda_*dx**2)
m = np.array([2*r-V(x)*dt/(2*lambda_)+1 for x in x_vals])
b = np.array([-2*r+V(x)*dt/(2*lambda_)+1 for x in x_vals])

# Intervalos de tempo para gerar as figuras
psi_at_times = {t: np.copy(psi) for t in times_to_plot}
t0 = 0

sum_value = calculate_sum(psi, dx) # função de onda inicial: cálculo da integridade
print(f"Soma de psi*psi * deltax em t = 0: {sum_value}")

for t in times_to_plot:  # iterações da biblioteca Crank-Nicolson em vários instantes de t:
    psi = cn(psi, nx, m, b, r, int(t0/dt), int(t/dt))
    psi_at_times[t] = np.copy(psi)
    
    # integridade da função de onda nos instantes de t
    sum_value = calculate_sum(psi, dx)
    print(f"Soma de psi*psi * deltax em t = {t}: {sum_value}")
    t0 = t

# Plotando Vef(a) e a densidade de probabilidade em t = 5
plt.figure(figsize=(12, 8))

# Plotando Vef(a)
vef_vals = np.array([V(x) for x in x_vals])
plt.plot(x_vals, vef_vals, label='$V_{ef}(a)$', color='black')

# Plotando a densidade de probabilidade |psi(a)|^2 para t = 5
plt.plot(x_vals, np.abs(psi_at_times[5])**2, label=f'$|\\psi(a)|^2$ at $t = 5.00$', color='blue')

plt.xlabel('$a$')
plt.ylabel('$V_{ef}(a)$ and $|\\psi(a)|^2$')
plt.title('Densidade de Probabilidade e Potencial Efetivo')
plt.ylim(0, 0.5)  # Definir limites do eixo y para Vef(a)
plt.legend()
plt.grid(True)
plt.show()
