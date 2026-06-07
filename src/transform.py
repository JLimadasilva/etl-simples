import pandas as pd
import numpy as np
from config import DATE_COLUMN, VALUE_COLUMN, CATEGORY_COLUMN

class DataTransformer:
    """Classe responsável pela transformação e limpeza dos dados"""
    
    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """Limpa os dados (remove nulos, duplicatas, etc.)"""
        if df.empty:
            return df
        
        # Remover duplicatas
        initial_len = len(df)
        df = df.drop_duplicates()
        print(f"Removidas {initial_len - len(df)} duplicatas")
        
        # Remover linhas com valores nulos críticos
        df = df.dropna(subset=[DATE_COLUMN, VALUE_COLUMN])
        
        # Remover valores negativos ou zero na coluna de valor
        if VALUE_COLUMN in df.columns:
            df = df[df[VALUE_COLUMN] > 0]
        
        return df
    
    @staticmethod
    def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Adiciona colunas calculadas"""
        if df.empty:
            return df
        
        # Garantir que a coluna de data está no formato datetime
        if DATE_COLUMN in df.columns:
            df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
            df['ano'] = df[DATE_COLUMN].dt.year
            df['mes'] = df[DATE_COLUMN].dt.month
            df['trimestre'] = df[DATE_COLUMN].dt.quarter
        
        # Adicionar coluna de valor categorizado
        if VALUE_COLUMN in df.columns:
            df['nivel_valor'] = pd.cut(df[VALUE_COLUMN], 
                                       bins=[0, 200, 500, 1000, float('inf')],
                                       labels=['Baixo', 'Médio', 'Alto', 'Muito Alto'])
        
        return df
    
    @staticmethod
    def aggregate_data(df: pd.DataFrame) -> dict:
        """Cria agregações dos dados"""
        if df.empty:
            return {}
        
        # Agregações principais
        aggregations = {
            'total_geral': float(df[VALUE_COLUMN].sum()),
            'media_geral': float(df[VALUE_COLUMN].mean()),
            'total_por_categoria': df.groupby(CATEGORY_COLUMN)[VALUE_COLUMN].sum().to_dict(),
            'total_por_mes': df.groupby('mes')[VALUE_COLUMN].sum().to_dict(),
            'total_por_departamento': df.groupby('departamento')[VALUE_COLUMN].sum().to_dict()
        }
        
        return aggregations
    
    @staticmethod
    def run_full_transformation(df: pd.DataFrame) -> pd.DataFrame:
        """Executa todas as transformações"""
        print("Iniciando transformação dos dados...")
        
        df_cleaned = DataTransformer.clean_data(df)
        df_transformed = DataTransformer.add_calculated_columns(df_cleaned)
        
        print(f"Dados transformados: {len(df_transformed)} registros")
        return df_transformed