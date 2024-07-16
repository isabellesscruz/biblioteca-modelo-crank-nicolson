# Biblioteca Modelo para Resolução de Equações Diferenciais Parciais Parabólicas usando Crank-Nicolson 1D

## Visão Geral

Este repositório contém o código fonte da biblioteca desenvolvida como parte do meu Projeto de Conclusão de Curso (TCC) do curso de Ciência da Computação. A biblioteca foi projetada para resolver equações diferenciais parciais parabólicas utilizando o método de Crank-Nicolson 1D, oferecendo uma solução prática e eficiente para problemas físicos e naturais que variam ao longo do tempo.

## Características Principais

- Implementação robusta do método de Crank-Nicolson 1D para EDPs parabólicas.
- Suporte para equações reais e complexas com parametrização flexível.
- Documentação detalhada e exemplos de uso para facilitar a implementação e compreensão.
- Disponibilidade pública para colaboração e contribuições da comunidade.

## Aplicações

A biblioteca é adequada para uma variedade de aplicações, incluindo a modelagem de difusão de calor, propagação de ondas e fenômenos quânticos complexos descritos pela equação de Schrödinger. Ela oferece uma solução precisa e eficaz para simulações numéricas, promovendo avanços em pesquisa científica e desenvolvimento tecnológico.

## Como Utilizar

### Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python 3.11
- NumPy
- Matplotlib (opcional, para visualização de resultados)

### Instalação

1. **Python 3.11**: Se ainda não tiver o Python instalado, você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/).

2. **NumPy**: Para instalar NumPy, você pode usar o gerenciador de pacotes `pip` no terminal: pip install numpy

3. **Matplotlib**: Caso deseje utilizar Matplotlib para visualizar resultados, você pode instalá-lo com o seguinte comando: pip install matplotlib


### Utilização da Biblioteca

1. Clone este repositório: git clone https://github.com/isabellesscruz/biblioteca-modelo-crank-nicolson
cd seu-repositorio

2. Importe a biblioteca `crank_nicolson` no seu código Python:

```python
from cn import crank_nicolson as cn
```

3. Utilize a função crank_nicolson para resolver equações diferenciais parciais parabólicas:

   # Exemplo de utilização
u_final = crank_nicolson(u_inicial, nx, m, b, r, ti, tf)

4. Substitua os parâmetros u_inicial, nx, m, b, r, ti e tf pelos valores específicos do seu problema. Consulte a documentação ou os exemplos fornecidos neste repositório para mais detalhes sobre como configurar os parâmetros corretamente.

5. Neste mesmo repositório existem 3 exemplos de aplicação da biblioteca.


A biblioteca é distribuída sob uma licença de código aberto, encorajando o uso, modificação e contribuições da comunidade científica global.

## Contribuições

Se você encontrar bugs, tiver sugestões de melhorias ou desejar contribuir para o projeto, sinta-se à vontade para abrir um issue ou enviar um pull request. Seu feedback é valorizado e fundamental para o desenvolvimento contínuo da biblioteca.
