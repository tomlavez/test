#!/bin/bash

# Script para executar o Dashboard Ambiental
echo "🌍 Iniciando Dashboard Ambiental..."

# Verificar se o ambiente virtual existe
if [ ! -d "dashboard_env" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv dashboard_env
    echo "Instalando dependências..."
    source dashboard_env/bin/activate
    pip install -r requirements.txt
else
    echo "Ativando ambiente virtual..."
    source dashboard_env/bin/activate
fi

# Verificar se os dados existem
if [ ! -d "tratado" ]; then
    echo "❌ Erro: Pasta 'tratado' com os dados não encontrada!"
    echo "Por favor, certifique-se de que a pasta 'tratado' com os dados está no diretório atual."
    exit 1
fi

echo "✅ Ambiente configurado com sucesso!"
echo "🚀 Iniciando dashboard em http://localhost:8501"
echo "📝 Para parar o dashboard, pressione Ctrl+C"
echo ""

# Executar o dashboard
streamlit run dashboard_ambiental.py 