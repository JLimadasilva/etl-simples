import os
from pathlib import Path

# Diretórios
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = DATA_DIR / "output"

# Criar diretórios se não existirem
for dir_path in [RAW_DIR, PROCESSED_DIR, OUTPUT_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Configurações de dados
DATE_COLUMN = "data"
VALUE_COLUMN = "valor"
CATEGORY_COLUMN = "categoria"