# 🚀 ETL Simples em Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/JLimadasilva/etl-simples)

## 📊 Sobre o Projeto

Este é um pipeline **ETL (Extract, Transform, Load)** desenvolvido em Python para demonstrar conceitos fundamentais de engenharia de dados. O projeto realiza a extração de dados, aplica transformações e limpezas, e gera relatórios em múltiplos formatos.

### 🎯 Funcionalidades

- 📥 **Extração**: Leitura de dados de arquivos CSV, JSON ou geração de dados de exemplo
- 🔄 **Transformação**: Limpeza, validação, remoção de duplicatas e criação de colunas calculadas
- 💾 **Carga**: Salvamento em CSV, JSON e geração de relatórios formatados
- 📈 **Agregações**: Cálculo de totais, médias e sumarizações por categoria
- 📄 **Relatórios**: Geração automática de relatórios em texto simples

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|------------|--------|-------------|
| Python | 3.8+ | Linguagem principal |
| Pandas | 2.0.3 | Manipulação e análise de dados |
| NumPy | 1.24.3 | Operações numéricas |
| Python-dotenv | 1.0.0 | Gerenciamento de variáveis de ambiente |


## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/JLimadasilva/etl-simples.git
cd etl-simples

2. **Instale as dependências**
pip install -r requirements.txt

3. **Execute o pipeline ETL**
python main.py

📊 Exemplo de Saída
🚀 Iniciando Pipeline ETL...
--------------------------------------------------
📥 ETAPA 1: EXTRAÇÃO
Gerando dados de exemplo...
Dados extraídos com sucesso: 365 registros

🔄 ETAPA 2: TRANSFORMAÇÃO
Iniciando transformação dos dados...
Dados transformados: 365 registros

💾 ETAPA 3: CARGA
Dados salvos em CSV: data/output/dados_processados.csv
Relatório salvo em: data/output/relatorio_final.txt

==================================================
✅ ETL CONCLUÍDO COM SUCESSO!
==================================================

📈 Resultados Gerados
Após a execução, os seguintes arquivos são criados:

Arquivo	Formato	Descrição
dados_processados.csv	CSV	Dados limpos e transformados
dados_processados.json	JSON	Mesmos dados em formato JSON
agregacoes.json	JSON	Sumarizações e métricas calculadas
relatorio_final.txt	TXT	Relatório legível em texto plano

🔧 Personalização
Adicionar novos dados
Coloque seu arquivo CSV em data/raw/

Execute python main.py

O pipeline processará automaticamente

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:

Reportar bugs

Sugerir novas funcionalidades

Enviar pull requests

📧 Contato
Autor: JLimadasilva
GitHub: @JLimadasilva
Projeto: ETL Simples em Python

⭐️ Se este projeto foi útil para você, considere dar uma estrela no GitHub!
