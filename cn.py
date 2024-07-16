import numpy as np
# BIBLIOTECA MODELO para o método de Crank-Nicolson
def crank_nicolson(u, nx, m, b, r, ti, tf):
    lu_l = np.zeros(nx+1, dtype=complex)  # iniciação de l (LU)
    lu_u = np.zeros(nx+1, dtype=complex)  # iniciação de u (LU)

    # Decomposição LU para CN: (Método de Crout)
    for x in range(1, nx):
        lu_l[x] = m[x] + r * lu_u[x-1]
        lu_u[x] = -r / lu_l[x]

    # Iteração do alg de CN para nt etapas de tempo
    z = np.zeros(nx+1, dtype=complex)  # iniciação de z
    for t in range(ti, tf):
        # Solução do sistema tridiagonal pelo método de Crout
        for x in range(1, nx):
            z[x]=(b[x]*u[x]+r*(u[x+1]+u[x-1]+z[x-1]))/lu_l[x]
        # Substituição reversa
        for x in range(nx-1, 0, -1):
            u[x] = z[x] - lu_u[x] * u[x+1]

    return u;
