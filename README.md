# biblioteca-modelo-crank-nicolson
A proposta deste trabalho é construir uma biblioteca modelo para a resolução de equações diferenciais parciais (EDPs) parabólicas, utilizando o método de Crank-Nicolson 1D em um processo iterativo. A linguagem escolhida é a linguagem Python por sua praticidade e facilidade de aprendizado, qualidades apreciada pelos pesquisadores.
As EDPs parabólicas são fundamentais na modelagem de fenômenos físicos e naturais que variam ao longo do tempo, como a difusão de calor, a propagação de ondas e a dispersão de partículas. Esta biblioteca foi projetada para lidar com funções reais e complexas, representando eventos físicos diversos. As EDPs parabólicas podem ser representadas pela seguinte fórmula:

$$\kappa\dfrac{\partial^2{u(x,t)}}{\partial{x}^2} + V(x)u(x,t) = \lambda\dfrac{\partial{u(x,t)}}{\partial{t}}$$

A parametrização da biblioteca é definida por constantes na equação: $\kappa$, $\lambda$, pelo potencial envolvido $V(x)$ e pelas condições iniciais e de contorno. A implementação do método de Crank-Nicolson 1D foi escolhida devido à sua estabilidade e precisão na solução de EDPs parabólicas. Este método combina informações do passado e do futuro para obter uma solução numérica mais precisa, utilizando uma abordagem híbrida implícita e explícita.

Para validar a eficácia da biblioteca, realizamos uma série de estudos de caso, incluindo a resolução da equação do calor, a simulação de sistemas quânticos complexos com a equação de Schrödinger e a aplicação da equação de Wheeler-DeWitt em modelos cosmológicos quânticos.

