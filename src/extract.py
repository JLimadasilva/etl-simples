import pandas as pd
import json
import csv
from pathlib import Path
from config import RAW_DIR

class DataExtractor:
    """Classe responsável pela extração de dados de diferentes fontes"""
    
    @staticmethod
    def extract_from_csv(file_path: Path) -> pd.DataFrame:
        """Extrai dados de um arquivo CSV"""
        try:
            df = pd.read_csv(file_path)
            print(f"Dados extraídos de {file_path}: {len(df)} registros")
            return df
        except Exception as e:
            print(f"Erro ao extrair CSV: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def extract_from_json(file_path: Path) -> pd.DataFrame:
        """Extrai dados de um arquivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            df = pd.DataFrame(data)
            print(f"Dados extraídos de {file_path}: {len(df)} registros")
            return df
        except Exception as e:
            print(f"Erro ao extrair JSON: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def generate_sample_data():
        """Gera dados de exemplo para demonstração"""
        import numpy as np
        
        np.random.seed(42)
        dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
        
        data = {
            'data': dates,
            'valor': np.random.randint(100, 1000, size=len(dates)),
            'categoria': np.random.choice(['Vendas', 'Marketing', 'TI', 'RH'], size=len(dates)),
            'departamento': np.random.choice(['A', 'B', 'C'], size=len(dates))
        }
        
        df = pd.DataFrame(data)
        
        # Salvar dados de exemplo
        csv_path = RAW_DIR / "dados_brutos.csv"
        df.to_csv(csv_path, index=False)
        print(f"Dados de exemplo gerados em {csv_path}")
        
        return df