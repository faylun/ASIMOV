import pandas as pd
from pathlib import Path

current_path = Path(__file__).parent
separated_panel = current_path / 'separated_panel'
joining_tables = current_path / 'joining_tables'

separated_panel.mkdir(exist_ok=True)
joining_tables.mkdir(exist_ok=True)


client_table_rs = pd.read_excel(current_path / 'clientes.xlsx', sheet_name='RS')
client_table_sc = pd.read_excel(current_path / 'clientes.xlsx', sheet_name='SC')
client_table_pr = pd.read_excel(current_path / 'clientes.xlsx', sheet_name='PR')
client_table_sp = pd.read_excel(current_path / 'clientes.xlsx', sheet_name='SP')

with pd.ExcelWriter(current_path / 'separated_panel' / 'RS.xlsx') as new_panel:
    client_table_rs.to_excel(new_panel, sheet_name='RS', index=False)

with pd.ExcelWriter(current_path / 'separated_panel' / 'SC.xlsx') as new_panel:
    client_table_sc.to_excel(new_panel, sheet_name='SC', index=False)

with pd.ExcelWriter(current_path / 'separated_panel' / 'PR.xlsx') as new_panel:
    client_table_pr.to_excel(new_panel, sheet_name='PR', index=False)

with pd.ExcelWriter(current_path / 'separated_panel' / 'SP.xlsx') as new_panel:
    client_table_sp.to_excel(new_panel, sheet_name='SP', index=False)

with pd.ExcelWriter(current_path / 'joining_tables' / 'joining_clients.xlsx') as new_panel:
    client_table_rs.to_excel(new_panel, sheet_name='RS', index=False)
    client_table_sc.to_excel(new_panel, sheet_name='SC', index=False)
    client_table_pr.to_excel(new_panel, sheet_name='PR', index=False)
    client_table_sp.to_excel(new_panel, sheet_name='SP', index=False)



''''

from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

tabela_clientes_dict = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name=None)
for nome_aba, tabela in tabela_clientes_dict.items():
    tabela.to_excel(pasta_atual / 'planilhas' / 'planilhas_separadas' / f'{nome_aba}.xlsx', index=False)


with pd.ExcelWriter(pasta_atual / 'planilhas' / 'planilha_consolidada' / 'clientes.xlsx') as consolidada:
    for arquivo in Path(pasta_atual / 'planilhas' / 'planilhas_separadas').glob('*.xlsx'):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)
    
'''