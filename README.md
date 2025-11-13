# 📦 Projeto do Site Repinstock

Este pacote contém todos os arquivos para o site institucional e de estoque da Repinstock. O site é composto por 3 páginas principais e é alimentado por arquivos JSON para fácil atualização.

---

## 📂 Estrutura de Arquivos

```
/repinstock-novo
├── 📄 index.html             # Página Inicial
├── 📄 entenda-produtos.html  # Página de Produtos
├── 📄 estoque.html           # Página de Estoque
├── 📁 images/                # Imagens e logos
├── 📁 json/
│   ├── 📄 composicao.json      # Dados da seção "Composição"
│   ├── 📄 grades.json          # Dados da seção "Qualidade"
│   ├── 📄 portfolio.json       # Dados da seção "Portfólio"
│   └── 📄 liststock_data.json  # DADOS PRINCIPAIS DO ESTOQUE
└── 🐍 server.py              # Servidor local para testes
```

---

## 🚀 Como Executar o Site Localmente

Para visualizar e testar o site em sua máquina, você precisa de Python instalado. Siga os passos abaixo:

1.  **Navegue até a pasta do projeto**
    Abra seu terminal (Prompt de Comando, PowerShell, etc.) e use o comando `cd` para entrar na pasta `repinstock-novo`.

    ```bash
    cd caminho/para/repinstock-novo
    ```

2.  **Inicie o servidor local**
    Execute o seguinte comando. Ele iniciará um servidor web simples na porta 8001.

    ```bash
    python3 server.py
    ```
    *(Se o comando `python3` não funcionar, tente usar `python`)*

3.  **Acesse o site no navegador**
    Abra seu navegador (Chrome, Firefox, etc.) e acesse os seguintes endereços:
    - **Página de Estoque:** `http://localhost:8001/estoque.html`
    - **Página Inicial:** `http://localhost:8001/index.html`

---

## 🔄 Como Atualizar o Estoque

A principal vantagem deste sistema é a facilidade de atualização. **Basta editar o arquivo `liststock_data.json`**.

### Editando o JSON

- Abra o arquivo `liststock_data.json` em um editor de texto simples (como Bloco de Notas, VS Code, etc.).
- Cada produto é um bloco de texto entre chaves `{}`.
- Altere os valores (preço, quantidade de paletes, etc.) conforme necessário.
- Salve o arquivo. As alterações aparecerão no site automaticamente ao recarregar a página.

### ✨ Sistema de Destaques (`Featured`)

Para destacar um produto na tabela de estoque, edite o campo `"Featured"` no arquivo `liststock_data.json`.

- **Valores aceitos:**
  - `"Oportunidade"` → Exibe o badge 🔥 Laranja
  - `"Custo-Benefício"` → Exibe o badge 💎 Azul
  - `"Oferta Especial"` → Exibe o badge 💰 Roxo
  - `null` → Nenhum destaque (produto padrão)

**Exemplo:**

```json
{
  "Certificate": "CE4",
  "Grade": "C+/C",
  "Composition": "euca",
  "Portfolio": "SS",
  "Featured": "Custo-Benefício" // <--- Mude aqui
  ...
},
```

---

## 🔮 Próximos Passos (Futuro)

- **Conversor Excel para JSON:** Será desenvolvido um script em Python para converter uma planilha do Excel diretamente para o formato `liststock_data.json`, simplificando ainda mais o processo de atualização.
