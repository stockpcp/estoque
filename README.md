# 🌳 Repinho Compensados - Site de Estoque

**Versão**: 2.0 (Otimizado e Corrigido)  
**Data**: 28 de Novembro de 2025  
**Status**: ✅ Pronto para Produção

---

## 📋 Sobre o Projeto

Site institucional e de estoque da **Repinho Compensados**, empresa especializada em compensados certificados. O site oferece:

- ✅ Página inicial com informações da empresa
- ✅ Página de estoque com **86 produtos** em tempo real
- ✅ Filtros dinâmicos por composição, portfólio, qualidade, espessura e dimensão
- ✅ Integração com WhatsApp para cotações
- ✅ Responsividade mobile-first
- ✅ Meta tags SEO completas
- ✅ Favicon em 6 formatos diferentes

---

## 📁 Estrutura do Repositório

```
estoque/
├── 📄 index.html                    # Página inicial
├── 📄 estoque.html                  # Página de estoque (DINÂMICA)
├── 📄 entenda-produtos.html         # Página de produtos
├── 📄 nc-qualidades.html            # Página de qualidades
├── 📄 liststock_data.json           # Dados de 86 produtos
├── 📄 composicao.json               # Dados de composição
├── 📄 grades.json                   # Dados de qualidade
├── 📄 portfolio.json                # Dados de portfólio
├── 📄 CNAME                         # Configuração de domínio
├── 📄 LICENSE                       # Licença MIT
├── 📄 README.md                     # Este arquivo
├── 📄 .gitignore                    # Arquivos ignorados pelo Git
│
├── 📁 css/                          # Estilos CSS
│   └── styles.css                   # Stylesheet principal
│
├── 📁 favicon/                      # Favicons (6 formatos)
│   ├── favicon.ico
│   ├── favicon-96x96.png
│   ├── apple-touch-icon.png
│   ├── android-chrome-192x192.png
│   ├── android-chrome-512x512.png
│   └── favicon.svg
│
├── 📁 fonts/                        # Fontes web
│   └── inter.css                    # Google Fonts Inter
│
├── 📁 img/                          # Imagens
│   ├── logo.png
│   ├── logo.webp
│   └── bg-2.png
│
├── 📁 docs/                         # Documentação
│   ├── CORRECOES_FINAIS.md
│   ├── PLANO_IMPLEMENTACAO_PRODUCAO.md
│   ├── ESTRUTURA_REORGANIZADA.md
│   ├── SCRIPTS_TESTE_RESUMO.md
│   └── ESTRUTURA_PROJETO.txt
│
└── 📁 tests/                        # Scripts de teste
    ├── test-resources.py            # Teste em Python
    ├── test-resources.sh            # Teste em Bash
    ├── test-resources.js            # Teste em JavaScript
    ├── TEST_GUIDE.md                # Guia de testes
    └── README.md                    # Instruções de teste
```

---

## 🚀 Como Fazer Deploy

### Opção 1: GitHub Pages (Automático)

1. **Ativar GitHub Pages** no repositório
   - Vá para Settings → Pages
   - Selecione "Deploy from a branch"
   - Escolha branch `main` e pasta raiz `/`
   - Clique em Save

2. **O site será publicado automaticamente** em:
   ```
   https://stockpcp.github.io/estoque/
   ```

### Opção 2: Upload Manual via FTP/SFTP

1. **Conecte ao servidor** via FTP/SFTP
2. **Faça upload dos arquivos** da raiz do repositório:
   - `index.html`
   - `estoque.html`
   - `entenda-produtos.html`
   - `nc-qualidades.html`
   - `liststock_data.json` e outros JSONs
   - Pastas: `css/`, `favicon/`, `fonts/`, `img/`

3. **Não faça upload** das pastas `docs/` e `tests/`

### Opção 3: Deploy com Git (SSH)

```bash
# Clone o repositório
git clone https://github.com/stockpcp/estoque.git
cd estoque

# Faça suas alterações
# ...

# Envie para o repositório
git add .
git commit -m "Atualização de produtos"
git push origin main
```

---

## 📊 Principais Mudanças (v2.0)

### ✅ Página de Estoque Reescrita
- **Antes**: 3 produtos hardcoded, filtros não funcionavam
- **Depois**: 86 produtos carregados dinamicamente, filtros 100% funcionais

### ✅ Logo Corrigida
- **Antes**: Não aparecia em `entenda-produtos.html` e `nc-qualidades.html`
- **Depois**: Aparece corretamente em todas as páginas

### ✅ Dados Atualizados
- **Antes**: `liststock_data.json` desatualizado
- **Depois**: Arquivo atualizado com 86 produtos

### ✅ Estrutura Organizada
- **Antes**: Arquivos misturados
- **Depois**: Separação clara entre produção, documentação e testes

---

## 🔧 Funcionalidades

### 1. Filtros Dinâmicos
- **Composição**: Pinus, Eucalipto, Combinado, etc
- **Portfólio**: NC, NS, SS, ST
- **Qualidade**: B/B, BCX, C+/C, CCX, CDX, Falldown, Shop Grade
- **Espessura**: 6mm a 31mm (14 opções)
- **Dimensão**: 2200x1100, 2400x1200, 2440x1220, 2500x1250
- **Destaque**: Oportunidade, Custo-Benefício, Oferta Especial

### 2. Tabela de Produtos
- Exibe 86 produtos com informações completas
- Calcula preço por chapa automaticamente
- Exibe badges de destaque com cores
- Botão "Cotar" integrado com WhatsApp

### 3. Responsividade
- Mobile-first design
- Funciona em smartphones, tablets e desktops
- Tabela com scroll horizontal em mobile

### 4. SEO
- Meta tags completas em todas as páginas
- Open Graph para redes sociais
- Canonical URLs
- Favicon em 6 formatos

---

## 🧪 Testes

### Executar Testes

```bash
# Python (recomendado)
cd tests
pip3 install requests beautifulsoup4
python3 test-resources.py https://estoque.repinho.ind.br/

# Bash
bash test-resources.sh https://estoque.repinho.ind.br/
```

### O que é Testado
- ✅ Imagens (logo, background)
- ✅ Stylesheets (CSS, Google Fonts)
- ✅ Favicons (6 formatos)
- ✅ Links internos
- ✅ Meta tags
- ✅ Estrutura HTML

---

## 📚 Documentação

Consulte a pasta `docs/` para:

- **CORRECOES_FINAIS.md** - Resumo das correções implementadas
- **PLANO_IMPLEMENTACAO_PRODUCAO.md** - Plano de deploy
- **ESTRUTURA_REORGANIZADA.md** - Estrutura de pastas
- **SCRIPTS_TESTE_RESUMO.md** - Resumo dos scripts de teste

---

## 🔐 Informações de Contato

**Repinho Compensados**
- 📞 Telefone: (42) 3629-8500
- 📧 Email: comercial1@repinho.ind.br
- 📍 Localização: Guarapuava, PR
- 🌐 Site: https://www.repinho.ind.br

---

## 📝 Licença

Este projeto está sob licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuindo

Para contribuir com melhorias:

1. **Faça um fork** do repositório
2. **Crie uma branch** para sua feature
3. **Commit suas mudanças**
4. **Push para a branch**
5. **Abra um Pull Request**

---

## 🐛 Reportar Problemas

Se encontrar bugs ou problemas, abra uma issue no GitHub com detalhes.

---

## ✅ Checklist de Deploy

Antes de fazer deploy, verifique:

- [ ] Todos os arquivos HTML estão presentes
- [ ] Pasta `img/` com imagens existe
- [ ] Pasta `favicon/` com 6 favicons existe
- [ ] Pasta `css/` com styles.css existe
- [ ] Arquivo `liststock_data.json` está atualizado
- [ ] Meta tags estão corretas
- [ ] Filtros funcionam corretamente
- [ ] Site funciona em mobile
- [ ] Sem erros no console

---

**Desenvolvido com ❤️ por Manus AI**  
**Última atualização**: 28 de Novembro de 2025
