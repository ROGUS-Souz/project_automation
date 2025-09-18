import pyautogui as pa
import time
import pandas as pd

# Lendo a base de dados

tabela = pd.read_csv('produto.csv')

pa.PAUSE = 1

# Começar abrindo o sistema e o navegador

pa.press('win')
time.sleep(2)
pa.write('chrome')
pa.press('enter')
time.sleep(2)

pa.click(x=290, y=640) # Clicar no modo visitante
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')
time.sleep(1)

# Dentro do Sistema

time.sleep(1)
pa.click(x=503, y=372) # Clicar no campo do usuário
pa.write('pythonimpressionador@gmail.com')
pa.press('tab') # Passar para o campo de senha
pa.write('sua senha')
pa.press('enter') # Entrar no sistema
time.sleep(2)

# Dentro do sistema, clicar em produtos
for linha in tabela.index:
    pa.click(x=529, y=259) # Clicar em produtos
    time.sleep(2)
    codigo = tabela.loc[linha, 'codigo']
    pa.write(str(codigo))
    pa.press('tab') # Passar para o campo de marca
    marca = tabela.loc[linha, 'marca']
    pa.write(marca)
    pa.press('tab') # Passar para o campo de tipo
    tipo = tabela.loc[linha, 'tipo']
    pa.write(tipo)
    pa.press('tab') # Passar para o campo de categoria
    categoria = tabela.loc[linha, 'categoria']
    pa.write(str(categoria))
    pa.press('tab') # Passar para o campo de preço unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pa.write(str(preco_unitario))
    pa.press('tab') # Passar para o campo de custo
    custo = tabela.loc[linha, 'custo']
    pa.write(str(custo))
    pa.press('tab') # Passar para o campo de obs
    obs = tabela.loc[linha, 'obs']
    pa.write(str(obs))
    pa.press('tab') # Passar para o botão de salvar
    pa.press('enter') # Clicar em salvar
    time.sleep(2) # Esperar 2 segundos para salvar
    pa.scroll(10000) # Voltar para o topo da página
