import numpy as np
import matplotlib.pyplot as plt
from cn import crank_nicolson as cn

# Parâmetros para alimentar o método
kappa_ = -0.5
lambda_ = 1j
L = 10.0  # comprimento do domínio
a, b = -5.0, 5.0  # limites do domínio
nx = 500  # número de pontos de dados
dx = L / (nx)  # passo espacial
V = lambda x: 0.5 * x**2  # potencial
dt = 0.02  # passo de tempo
times_to_plot = [0, 0.25, 0.5, 0.75, 1]  # tempos para plotar
nt = int(max(times_to_plot) / dt)  # número total de passos de tempo

# Função para definir a função de onda inicial Psi
def Psi(x):
    return np.exp(-0.5*x**2)/np.sqrt(np.sqrt(np.pi))  # Estado fundamental da função de onda

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
#psi_at_times[0] = np.copy(psi);
t0 = 0;

sum_value = calculate_sum(psi, dx) # função de onda inicial: cálculo da integridade
print(f"Soma de psi*psi * deltax em t = 0: {sum_value}")

for t in times_to_plot[1:]:  # iterações da biblioteca Crank-Nicolson em vários instantes de t:
    psi = cn(psi, nx, m, b, r, int(t0/dt), int(t/dt))
    psi_at_times[t] = np.copy(psi)
    
    # integridade da função de onda nos instantes de t
    sum_value = calculate_sum(psi, dx)
    print(f"Soma de psi*psi * deltax em t = {t}: {sum_value}")
    t0 = t;

plt.figure(figsize=(12, 8))
for t in times_to_plot:
    plt.plot(x_vals, np.abs(psi_at_times[t])**2, label=f't = {t:.2f}')

plt.xlabel('x')
plt.ylabel('|psi(x)|^2')
plt.title('Densidade de Probabilidade da Função de Onda ao Longo do Tempo')
plt.legend()
plt.grid()
plt.show()
