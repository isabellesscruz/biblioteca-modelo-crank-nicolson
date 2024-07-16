import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from cn import crank_nicolson as cn

# Parâmetros
kappa_ = 1
lambda_ = 1
L = 30.0  # comprimento do domínio em cm
a, b = 0, 30 # limites do domínio
nx = 1000  # número de pontos de dados
dx = L / (nx)  # passo espacial em cm
# V = 0 # potencial
Tf = 500.0  # tempo final em segundos
nt = 10000  # número de passos de tempo
dt = 0.05  # passo de tempo em segundos
times_to_plot = [0, 10, 50, 100, 500] #tempos para plotar

# Temperatura inicial:
def T(x):
    return 20.0

# Passo 1: Configuração inicial dos parâmetros do CN, complexo ou real
x_vals = np.linspace(a, b, nx+1)  # valores de x no domínio
temp = np.array([T(x) for x in x_vals], dtype=complex)  # iniciação da função de onda (psi(x,0))
temp[0] = 0
temp[nx] = 0  # condições de contorno

# Parâmetros para as matrizes de Crank-Nicolson
r = kappa_*dt/(2*lambda_*dx**2)
m = np.array([2*r+1 for x in x_vals])
m[0] = m[nx] = 1
b = np.array([-2*r+1 for x in x_vals])
b[0] = b[nx] = 1

# Intervalos de tempo para gerar as figuras
temp_at_times = {t: np.copy(temp) for t in times_to_plot}
t0 = 0;

for t in times_to_plot[1:]:  # iterações da biblioteca Crank-Nicolson em vários instantes de t:
    temp = cn(temp, nx, m, b, r, int(t0/dt), int(t/dt))
    temp_at_times[t] = np.copy(temp)
    t0 = t;

plt.figure(figsize=(12, 8))
for t in times_to_plot:
    plt.plot(x_vals, abs(temp_at_times[t]), label=f't = {t:.2f}')

plt.xlabel('x')
plt.ylabel('T(x)')
plt.title('Temperatura da barra de alumínio ao longo do tempo')
plt.legend()
plt.grid()
plt.show()
