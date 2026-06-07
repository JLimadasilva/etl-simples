# -*- coding: utf-8 -*- 
import sys 
from pathlib import Path 
sys.path.append(str(Path(__file__).parent)) 
from src.extract import DataExtractor 
from src.transform import DataTransformer 
from src.load import DataLoader 
from config import RAW_DIR 
 
def run_etl_pipeline(): 
    print("🚀 Iniciando Pipeline ETL...") 
    print("-" * 50) 
    try: 
        print("📥 ETAPA 1: EXTRACAO") 
        csv_files = list(RAW_DIR.glob("*.csv")) 
        if not csv_files: 
            print("Gerando dados de exemplo...") 
            df_extracted = DataExtractor.generate_sample_data() 
        else: 
            df_extracted = DataExtractor.extract_from_csv(csv_files[0]) 
        if df_extracted.empty: 
            raise Exception("Falha na extracao dos dados") 
        print(f"Dados extraidos: {len(df_extracted)} registros") 
        print("\n Preview dos dados extraidos:") 
        print(df_extracted.head()) 
        print("\n🔄 ETAPA 2: TRANSFORMACAO") 
        df_transformed = DataTransformer.run_full_transformation(df_extracted) 
        if df_transformed.empty: 
            raise Exception("Falha na transformacao") 
        aggregations = DataTransformer.aggregate_data(df_transformed) 
        print("\n💾 ETAPA 3: CARGA") 
        DataLoader.save_to_csv(df_transformed, "dados_processados.csv") 
        DataLoader.save_to_json(df_transformed, "dados_processados.json") 
        DataLoader.save_aggregations(aggregations, "agregacoes.json") 
        DataLoader.generate_report(df_transformed, aggregations) 
        print("\n✅ ETL CONCLUIDO COM SUCESSO!") 
        return df_transformed, aggregations 
    except Exception as e: 
        print(f"\n❌ ERRO: {e}") 
        return None, None 
 
def main(): 
    df, agg = run_etl_pipeline() 
    if df is not None: 
        print("\n🎉 Pipeline executado com sucesso!") 
        return 0 
    else: 
        print("\n💥 Pipeline falhou!") 
        return 1 
 
if __name__ == "__main__": 
    exit(main()) 
