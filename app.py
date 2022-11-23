import pandas
import openpyxl
from twilio.rest import Client

account_sid = ""
auth_token  = ""
client = Client(account_sid, auth_token)

tabela_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in tabela_meses:
    tabela_vendas = pandas.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 50000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+553465223652",
            from_="323653265645",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
