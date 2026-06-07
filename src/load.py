import pandas as pd
import json
from pathlib import Path
from datetime import datetime
from config import OUTPUT_DIR, PROCESSED_DIR

class DataLoader:
    """Classe responsável pelo carregamento dos dados processados"""
    
    @staticmethod
    def save_to_csv(df: pd.DataFrame, filename: str = "dados_processados.csv") -> Path:
        """Salva dados em CSV"""
        if df.empty:
            print("DataFrame vazio, não foi possível salvar")
            return None
        
        file_path = OUTPUT_DIR / filename
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"Dados salvos em CSV: {file_path}")
        return file_path
    
    @staticmethod
    def save_to_json(df: pd.DataFrame, filename: str = "dados_processados.json") -> Path:
        """Salva dados em JSON"""
        if df.empty:
            print("DataFrame vazio, não foi possível salvar")
            return None
        
        file_path = OUTPUT_DIR / filename
        df.to_json(file_path, orient='records', indent=2, date_format='iso')
        print(f"Dados salvos em JSON: {file_path}")
        return file_path
    
    @staticmethod
    def save_aggregations(aggregations: dict, filename: str = "agregacoes.json") -> Path:
        """Salva as agregações em um arquivo JSON"""
        if not aggregations:
            print("Sem agregações para salvar")
            return None
        
        file_path = OUTPUT_DIR / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(aggregations, f, indent=2, ensure_ascii=False)
        
        print(f"Agregações salvas em: {file_path}")
        return file_path
    
    @staticmethod
    def generate_report(df: pd.DataFrame, aggregations: dict) -> str:
        """Gera um relatório em texto simples"""
        if df.empty:
            return "Sem dados para gerar relatório"
        
        report = []
        report.append("=" * 60)
        report.append("RELATÓRIO ETL - ANÁLISE DE DADOS")
        report.append("=" * 60)
        report.append(f"Data de geração: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total de registros processados: {len(df)}")
        report.append(f"Período: {df['data'].min()} até {df['data'].max()}")
        report.append(f"Valor total: R$ {aggregations.get('total_geral', 0):,.2f}")
        report.append(f"Valor médio: R$ {aggregations.get('media_geral', 0):,.2f}")
        report.append("\n" + "-" * 40)
        report.append("TOTAL POR CATEGORIA:")
        for cat, val in aggregations.get('total_por_categoria', {}).items():
            report.append(f"  {cat}: R$ {val:,.2f}")
        
        report.append("\n" + "-" * 40)
        report.append("TOTAL POR DEPARTAMENTO:")
        for dept, val in aggregations.get('total_por_departamento', {}).items():
            report.append(f"  Departamento {dept}: R$ {val:,.2f}")
        
        report.append("\n" + "=" * 60)
        
        report_text = "\n".join(report)
        
        # Salvar relatório
        report_path = OUTPUT_DIR / "relatorio_final.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print(f"Relatório salvo em: {report_path}")
        return report_text