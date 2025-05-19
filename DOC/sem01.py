from math import log2
# REGRAS DE DIVISÃO POR CLASSIFICAÇÃO

## Entropia
### Entropia é uma medida de incerteza ou aleatoriedade em um conjunto de dados.
### FORMULA: E(Entropia) = -Σ(p_i * log2(p_i))
### S( 9+, 5-)

amostra ='''
| DIA | ASPECTO | TEMPERATURA | UMIDADE | VENTO | JOGAR TÊNIS |
| --- | ------- | ----------- | ------- | ----- | ----------- |
| D1  | sol     | quente      | elevada | fraco | nao         |
| D2  | sol     | quente      | elevada | forte | nao         |
| D3  | nuvens  | quente      | elevada | fraco | sim         |
| D4  | chuva   | ameno       | elevada | fraco | sim         |
| D5  | chuva   | fresco      | normal  | fraco | sim         |
| D6  | chuva   | fresco      | normal  | forte | nao         |
| D7  | nuvens  | fresco      | normal  | fraco | sim         |
| D8  | sol     | ameno       | elevada | fraco | nao         |
| D9  | sol     | fresco      | normal  | fraco | sim         |
| D10 | chuva   | ameno       | normal  | forte | sim         |
| D11 | sol     | ameno       | normal  | forte | sim         |
| D12 | nuvens  | ameno       | elevada | forte | sim         |
| D13 | nuvens  | quente      | normal  | fraco | sim         |
| D14 | chuva   | ameno       | elevada | forte | nao         |
'''

# Formula para calcular a entropia
entropia = -((9/14) * log2(9/14) + (5/14) * log2(5/14))

print(f"ENTROPIA: {entropia:.3f}")

### Ganho de Informação: redução esperada no valor da Entropia, devido à ordenação no conjunto de treino segundo os valores do atributo A. Exemplo: Para responder a pergunta: Qual o melhor atributo para iniciar a árvore ? Resposta: utiliza-se o ganho. No exemplo dado: 
# Ganho(S, Aspecto) = 0,246 
# Ganho(S, Umidade) = 0,151 
# Ganho(S, Vento) = 0,048 
# Ganho(S, Temperatura) = 0,029

# FORMULA: G(S, A) = E(S) - Σ(|S_v|/|S| * E(S_v))
# Onde:
# - G(S, A) é o ganho de informação do atributo A em relação ao conjunto S
# - E(S) é a entropia do conjunto S
# - |S_v| é o número de instâncias do conjunto S que possuem o valor v do atributo A
# - |S| é o número total de instâncias do conjunto S
# - E(S_v) é a entropia do subconjunto S_v, que contém as instâncias do conjunto S que possuem o valor v do atributo A

# Exemplo:
# - S = {D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14}
# - A = {Perspectiva, Umidade, Vento, Temperatura}
# - S_v = {D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14}
# - |S| = 14
# - |S_v| = 14
# - E(S) = 0,940
# - E(S_v) = 0,940
# - G(S, A) = E(S) - Σ(|S_v|/|S| * E(S_v))
# - G(S, A) = 0,940 - Σ(14/14 * 0,940)


# REGRAS DE DIVISÃO POR REGRESSÃO
