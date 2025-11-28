# Scripts de Teste Automatizado

Este diretório contém scripts para testar se todos os recursos do site estão carregando corretamente.

## 📋 Arquivos

- **test-resources.py** - Script Python (recomendado)
- **test-resources.sh** - Script Bash (Linux/Mac)
- **test-resources.js** - Script JavaScript (Navegador)
- **TEST_GUIDE.md** - Guia completo de uso

## 🚀 Como Usar

### Python
```bash
pip3 install requests beautifulsoup4
python3 test-resources.py https://estoque.repinho.ind.br/
```

### Bash
```bash
bash test-resources.sh https://estoque.repinho.ind.br/
```

### JavaScript (Navegador)
1. Abra o site em seu navegador
2. Pressione F12 para abrir DevTools
3. Vá para Console
4. Cole o conteúdo de `test-resources.js`
5. Execute: `runTests()`

## 📖 Documentação

Veja `TEST_GUIDE.md` para instruções detalhadas.
