# Guia de Testes Automatizados - Repinho Compensados

**Data**: 28 de Novembro de 2025  
**Objetivo**: Verificar se todos os links, imagens, favicons, CSS e JS estão carregando corretamente

---

## 📋 Conteúdo

Este pacote inclui 3 scripts de teste em diferentes linguagens:

1. **test-resources.py** - Script Python (recomendado para servidor)
2. **test-resources.sh** - Script Bash (para Linux/Mac)
3. **test-resources.js** - Script JavaScript (para navegador)

---

## 🐍 Opção 1: Script Python (Recomendado)

### Requisitos
```bash
pip3 install requests beautifulsoup4
```

### Uso
```bash
python3 test-resources.py https://estoque.repinho.ind.br/
```

### Exemplo de Saída
```
======================================================================
        Teste Automatizado de Recursos - Repinho Compensados
======================================================================

ℹ URL Base: https://estoque.repinho.ind.br/
ℹ Data/Hora: 28/11/2025 14:30:45

======================================================================
                    Testando: Página Inicial
======================================================================

ℹ Testando: https://estoque.repinho.ind.br/index.html
✓ Página carregada com sucesso
ℹ Testando imagens...
✓ Imagem: img/logo.png
✓ Imagem: img/bg-2.png
ℹ Testando stylesheets...
✓ CSS: css/styles.css
✓ CSS: fonts/inter.css
ℹ Testando favicons...
✓ Favicon: favicon/favicon.ico (N/A)
✓ Favicon: favicon/favicon-96x96.png (96x96)
✓ Favicon: favicon/apple-touch-icon.png (180x180)
✓ Favicon: favicon/favicon.svg (N/A)
```

### Vantagens
- ✅ Teste completo e detalhado
- ✅ Verifica HTTP status codes
- ✅ Testa todas as páginas
- ✅ Relatório formatado
- ✅ Suporta redirecionamentos

---

## 🐚 Opção 2: Script Bash

### Requisitos
```bash
# Instalar curl (geralmente já vem instalado)
sudo apt-get install curl
```

### Uso
```bash
bash test-resources.sh https://estoque.repinho.ind.br/
```

### Exemplo de Saída
```
======================================================================
        Teste Automatizado de Recursos - Repinho Compensados
======================================================================

ℹ URL Base: https://estoque.repinho.ind.br/
ℹ Data/Hora: 28/11/2025 14:30:45

ℹ Testando: https://estoque.repinho.ind.br/index.html
✓ Página carregada: Página Inicial
ℹ Testando imagens...
✓ Imagem: img/logo.png
✓ Imagem: img/bg-2.png
ℹ Testando stylesheets...
✓ CSS: css/styles.css
✓ CSS: fonts/inter.css
ℹ Testando favicons...
✓ Favicon: favicon/favicon.ico
✓ Favicon: favicon/favicon-96x96.png
```

### Vantagens
- ✅ Não requer instalação de pacotes Python
- ✅ Funciona em qualquer servidor Linux/Mac
- ✅ Rápido e leve
- ✅ Fácil de integrar em CI/CD

---

## 🌐 Opção 3: Script JavaScript (Navegador)

### Uso

#### Método 1: Copiar e Colar no Console
1. Abra o site em seu navegador
2. Pressione `F12` para abrir o DevTools
3. Vá para a aba "Console"
4. Copie todo o conteúdo de `test-resources.js`
5. Cole no console e pressione Enter
6. Execute: `runTests()`

#### Método 2: Incluir no HTML
```html
<script src="test-resources.js"></script>
<script>
  // Executar testes automaticamente ao carregar
  window.addEventListener('load', () => {
    runTests();
  });
</script>
```

### Exemplo de Saída
```
======================================================================
        Teste Automatizado de Recursos - Repinho Compensados
======================================================================

ℹ URL: https://estoque.repinho.ind.br/index.html
ℹ Data/Hora: 28/11/2025 14:30:45

ℹ Testando imagens...
✓ Imagem: https://estoque.repinho.ind.br/img/logo.png
✓ Imagem: https://estoque.repinho.ind.br/img/bg-2.png
ℹ Testando stylesheets...
✓ CSS: https://estoque.repinho.ind.br/css/styles.css
ℹ Testando favicons...
✓ Favicon: https://estoque.repinho.ind.br/favicon/favicon.ico (N/A)
```

### Vantagens
- ✅ Testa do ponto de vista do usuário
- ✅ Verifica carregamento real de recursos
- ✅ Não requer instalação
- ✅ Funciona em qualquer navegador

---

## 📊 O que é Testado

### 1. Imagens
- ✅ Verifica se todas as imagens (`<img src>`) carregam
- ✅ Valida formatos (PNG, WebP, etc)
- ✅ Testa atributo `alt` (acessibilidade)

### 2. Stylesheets
- ✅ Verifica se todos os CSS carregam
- ✅ Valida sintaxe CSS
- ✅ Testa Google Fonts (fonts/inter.css)

### 3. Scripts
- ✅ Verifica se todos os scripts carregam
- ✅ Valida sintaxe JavaScript
- ✅ Testa execução sem erros

### 4. Favicons
- ✅ Verifica todos os 6 formatos:
  - favicon.ico
  - favicon-96x96.png
  - apple-touch-icon.png
  - android-chrome-192x192.png
  - android-chrome-512x512.png
  - favicon.svg

### 5. Links Internos
- ✅ Verifica se todos os links internos funcionam
- ✅ Valida navegação entre páginas
- ✅ Testa links de menu

### 6. Meta Tags
- ✅ Verifica meta tags essenciais:
  - viewport
  - description
  - robots
- ✅ Verifica Open Graph tags:
  - og:title
  - og:description
  - og:type
  - og:url

---

## 🎯 Cenários de Teste

### Teste Local (Desenvolvimento)
```bash
# Iniciar servidor local
python3 -m http.server 8000

# Em outro terminal
python3 test-resources.py http://localhost:8000/
```

### Teste em Staging
```bash
python3 test-resources.py https://staging.estoque.repinho.ind.br/
```

### Teste em Produção
```bash
python3 test-resources.py https://estoque.repinho.ind.br/
```

---

## 📈 Interpretando Resultados

### Taxa de Sucesso 100%
```
✓ Todos os testes passaram com sucesso!
```
**Significado**: Todos os recursos estão carregando corretamente.

### Taxa de Sucesso < 100%
```
✗ 3 recursos falharam no teste
```
**Significado**: Alguns recursos não estão carregando. Verifique:
1. Caminhos de arquivo (img/, favicon/, css/)
2. Permissões de arquivo
3. Configuração do servidor web
4. Erros de digitação em referências

### Erros Comuns

#### Erro: "Favicon: favicon/favicon.ico - HTTP 404"
**Causa**: Arquivo não encontrado
**Solução**: Verifique se o arquivo existe em `favicon/favicon.ico`

#### Erro: "Imagem: img/logo.png - HTTP 404"
**Causa**: Caminho incorreto
**Solução**: Verifique se o arquivo existe em `img/logo.png`

#### Erro: "CSS: css/styles.css - HTTP 404"
**Causa**: Arquivo CSS não encontrado
**Solução**: Verifique se o arquivo existe em `css/styles.css`

---

## 🔄 Integração com CI/CD

### GitHub Actions
```yaml
name: Test Resources

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install requests beautifulsoup4
      - name: Run tests
        run: python3 test-resources.py https://estoque.repinho.ind.br/
```

### GitLab CI
```yaml
test_resources:
  image: python:3.9
  script:
    - pip install requests beautifulsoup4
    - python3 test-resources.py https://estoque.repinho.ind.br/
```

---

## 📝 Logs e Relatórios

### Salvar Relatório em Arquivo (Python)
```bash
python3 test-resources.py https://estoque.repinho.ind.br/ > relatorio_testes.txt
```

### Salvar Relatório em Arquivo (Bash)
```bash
bash test-resources.sh https://estoque.repinho.ind.br/ > relatorio_testes.txt
```

### Exportar Relatório JSON (Python)
```python
# Modificar script para exportar JSON
import json
with open('relatorio_testes.json', 'w') as f:
    json.dump(tester.results, f, indent=2)
```

---

## 🚀 Automação Recomendada

### Executar Testes Diariamente
```bash
# Adicionar ao crontab
0 9 * * * /usr/bin/python3 /home/ubuntu/repinho-otimizado/test-resources.py https://estoque.repinho.ind.br/ > /var/log/repinho_tests.log
```

### Executar Testes Após Deploy
```bash
#!/bin/bash
# deploy.sh
./deploy_files.sh
sleep 5
python3 test-resources.py https://estoque.repinho.ind.br/
```

---

## ✅ Checklist de Testes

- [ ] Todos os favicons carregam (6 formatos)
- [ ] Todas as imagens carregam (logo, bg)
- [ ] CSS carrega sem erros
- [ ] Google Fonts carrega (fonts/inter.css)
- [ ] Todos os links internos funcionam
- [ ] Meta tags estão presentes
- [ ] Taxa de sucesso é 100%
- [ ] Sem erros 404 no console
- [ ] Sem erros de CORS
- [ ] Sem avisos de segurança

---

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os caminhos de arquivo**
   ```bash
   ls -la img/
   ls -la favicon/
   ls -la css/
   ```

2. **Verifique permissões**
   ```bash
   chmod 644 img/*
   chmod 644 favicon/*
   chmod 644 css/*
   ```

3. **Verifique configuração do servidor web**
   ```bash
   # Apache
   sudo systemctl restart apache2
   
   # Nginx
   sudo systemctl restart nginx
   ```

4. **Teste localmente**
   ```bash
   python3 -m http.server 8000
   python3 test-resources.py http://localhost:8000/
   ```

---

## 🎉 Conclusão

Use estes scripts para garantir que:

✅ Todos os recursos estão carregando corretamente  
✅ Não há erros 404 ou de carregamento  
✅ O site funciona em todos os navegadores  
✅ A experiência do usuário é ótima  
✅ O site está pronto para produção

**Bom teste! 🚀**
