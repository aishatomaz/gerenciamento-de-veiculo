# fix.ps1 - Script de correção
Write-Host "=== Limpando cache do Python ===" -ForegroundColor Yellow
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force -ErrorAction SilentlyContinue
Write-Host "Cache limpo!" -ForegroundColor Green

Write-Host ""
Write-Host "=== Verificando estrutura ===" -ForegroundColor Yellow
if (Test-Path "service\veiculo_service.py") {
    Write-Host "OK - service\veiculo_service.py encontrado" -ForegroundColor Green
} else {
    Write-Host "ERRO - service\veiculo_service.py NAO encontrado!" -ForegroundColor Red
}

if (Test-Path "service\__init__.py") {
    Write-Host "OK - service\__init__.py encontrado" -ForegroundColor Green
} else {
    Write-Host "ERRO - service\__init__.py NAO encontrado!" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Testando import ===" -ForegroundColor Yellow
python -c "import sys; sys.path.insert(0, '.'); from service.veiculo_service import VeiculoCRUD; print('SUCESSO: VeiculoCRUD importado!')"

Write-Host ""
Write-Host "=== Executando projeto ===" -ForegroundColor Yellow
python -m main

"""
 Para rodar com o código VeiculoCRUD corrigido use: powershell -ExecutionPolicy Bypass -File fix.ps1
"""