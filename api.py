import requests
import pandas as pd
import base64
from datetime import datetime

# Configurações
login = "V043"
chave = "6f937c12b71f47a3a76104c159e38105"

codigos_setor = ["V02Y", "VS40", "V043", "V044", "V045", "V046", "V047"]

# Anos e meses até o mês anterior ao atual
ano_atual = datetime.now().year
mes_atual = datetime.now().month

anos = list(range(2019, ano_atual + 1))  # do primeiro ano que você quiser até o atual
meses = list(range(1, 13))

# Credenciais
credenciais = f"{login}:{chave}"
token = base64.b64encode(credenciais.encode()).decode()
headers = {"Authorization": f"Basic {token}"}

# Lista para guardar resultados
registros = []

# Loop em setores, anos e meses
for setor in codigos_setor:
    for ano in anos:
        for mes in meses:
            # Evita meses futuros
            if (ano > ano_atual) or (ano == ano_atual and mes >= mes_atual):
                continue

            url = f"https://areacliente.prorad.com.br/ACP/api/v1/DosesMes/{setor}/{ano}/{mes}"
            try:
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    dados = r.json()
                    for dose in dados.get("Doses", []):
                        registros.append({
                            "CodigoSetor": dados.get("CodigoSetor"),
                            "NomeSetor": dados.get("NomeSetor"),
                            "PeriodoInicio": dados.get("PeriodoInicio"),
                            "PeriodoFim": dados.get("PeriodoFim"),
                            "Ano": ano,
                            "Mes": mes,
                            **dose
                        })
            except Exception as e:
                print(f"Erro em {setor}/{ano}/{mes}: {e}")

# Converte para DataFrame
df = pd.DataFrame(registros)

# Resultado para o Power BI
dataset = df
