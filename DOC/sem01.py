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
print('##############################################')

# Calculo de Ganho de Informação
### Ganho de Informação: redução esperada no valor da Entropia, devido à ordenação no conjunto de treino segundo os valores do atributo A. Exemplo: Para responder a pergunta: Qual o melhor atributo para iniciar a árvore ? Resposta: utiliza-se o ganho. No exemplo dado: 

# Caculo ASPECTO
# Atributo ASPECTO - SOL [5 instâncias: 2 "sim", 3 "nao"]
entropia_aspecto_sol = -((2/5) * log2(2/5) + (3/5) * log2(3/5))
print(f"ENTROPIA ASPECTO SOL: {entropia_aspecto_sol:.3f}")

# Atributo ASPECTO - NUVENS [4 instâncias: 3 "sim", 1 "nao"]
entropia_aspecto_nuvens = -((3/4) * log2(3/4) + (1/4) * log2(1/4))
print(f"ENTROPIA ASPECTO NUVENS: {entropia_aspecto_nuvens:.3f}")

# Atributo ASPECTO - CHUVA [5 instâncias: 4 "sim", 1 "nao"]
entropia_aspecto_chuva = -((4/5) * log2(4/5) + (1/5) * log2(1/5))
print(f"ENTROPIA ASPECTO CHUVA: {entropia_aspecto_chuva:.3f}")

# Cálculo do ganho de informação para o atributo ASPECTO
ig_aspecto = entropia - ((5/14) * entropia_aspecto_sol + (4/14) * entropia_aspecto_nuvens + (5/14) * entropia_aspecto_chuva)
print(f"GANHO DE INFORMAÇÃO ASPECTO: {ig_aspecto:.3f}")

print('##############################################')

# Caculo TEMPERATURA
# Atributo TEMPERATURA - QUENTE [4 instâncias: 2 "sim", 2 "nao"]
entropia_temperatura_quente = -((2/4) * log2(2/4) + (2/4) * log2(2/4))
print(f"ENTROPIA TEMPERATURA QUENTE: {entropia_temperatura_quente:.3f}")

# Atributo TEMPERATURA - AMENO [6 instâncias: 4 "sim", 2 "nao"]
entropia_temperatura_ameno = -((4/6) * log2(4/6) + (2/6) * log2(2/6))
print(f"ENTROPIA TEMPERATURA AMENO: {entropia_temperatura_ameno:.3f}")

# Atributo TEMPERATURA - FRESCO [4 instâncias: 3 "sim", 1 "nao"]
entropia_temperatura_fresco = -((3/4) * log2(3/4) + (1/4) * log2(1/4))
print(f"ENTROPIA TEMPERATURA FRESCO: {entropia_temperatura_fresco:.3f}")

# Cálculo do ganho de informação para o atributo TEMPERATURA
ig_temperatura = entropia - ((4/14) * entropia_temperatura_quente + (6/14) * entropia_temperatura_ameno + (4/14) * entropia_temperatura_fresco)
print(f"GANHO DE INFORMAÇÃO TEMPERATURA: {ig_temperatura:.3f}")

print('##############################################')

# Caculo UMIDADE
# Atributo UMIDADE - ELEVADA [7 instâncias: 3 "sim", 4 "nao"]
entropia_umidade_elevada = -((3/7) * log2(3/7) + (4/7) * log2(4/7))
print(f"ENTROPIA UMIDADE ELEVADA: {entropia_umidade_elevada:.3f}")

# Atributo UMIDADE - NORMAL [7 instâncias: 4 "sim", 3 "nao"]
entropia_umidade_normal = -((4/7) * log2(4/7) + (3/7) * log2(3/7))
print(f"ENTROPIA UMIDADE NORMAL: {entropia_umidade_normal:.3f}")

# Cálculo do ganho de informação para o atributo UMIDADE
ig_umidade = entropia - ((7/14) * entropia_umidade_elevada + (7/14) * entropia_umidade_normal)
print(f"GANHO DE INFORMAÇÃO UMIDADE: {ig_umidade:.3f}")

print('##############################################')

# Caculo VENTO
# Atributo VENTO - FRACO [8 instâncias: 5 "sim", 3 "nao"]
entropia_vento_fraco = -((5/8) * log2(5/8) + (3/8) * log2(3/8))
print(f"ENTROPIA VENTO FRACO: {entropia_vento_fraco:.3f}")

# Atributo VENTO - FORTE [6 instâncias: 4 "sim", 2 "nao"]
entropia_vento_forte = -((4/6) * log2(4/6) + (2/6) * log2(2/6))
print(f"ENTROPIA VENTO FORTE: {entropia_vento_forte:.3f}")

# Cálculo do ganho de informação para o atributo VENTO
ig_vento = entropia - ((8/14) * entropia_vento_fraco + (6/14) * entropia_vento_forte)
print(f"GANHO DE INFORMAÇÃO VENTO: {ig_vento:.3f}")

print('##############################################')
