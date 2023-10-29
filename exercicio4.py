# 4) Crie utilizando um pandas dataframe a seguinte tabela e salve essa tabela em um arquivo excel (tabela.xlsx):

# | nome | idade | cidade         | profissão |
# |------|-------|----------------|-----------|
# | joão | 22    | Porto Alegre   | professor |
# | ana  | 23    | São Paulo      | jornalista|
# | pedro| 24    | Rio de Janeiro | advogado  |
# | maria| 25    | Belo Horizonte | vendedor  |
# | josé | 26    | Porto Alegre   | engenheiro|

import pandas as pd

dict_data = {
    'nome': ['joão', 'ana', 'pedro', 'maria', 'josé'],
    'idade': [22, 23, 24, 25, 26],
    'cidade': ['Porto Alegre', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre'],
    'profissão': ['professor', 'jornalista', 'advogado', 'vendedor', 'engenheiro']
}

df = pd.DataFrame(data=dict_data)

caminho_xlsx = r'C:\Users\980184\Desktop\QQtech\exercicios6-PythonQQTech\arquivo.xlsx'

df.to_excel(caminho_xlsx, index=False, sheet_name='Planilha1')

