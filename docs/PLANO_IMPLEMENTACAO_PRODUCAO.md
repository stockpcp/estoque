# Plano de Implementação em Produção: Otimização do Site Repinho

**Data do Documento**: 28 de Novembro de 2025  
**Projeto**: Migração do Código Otimizado para o Ambiente de Produção  
**Status**: Documento Preliminar

---

## 1. Visão Geral e Objetivos

Este documento descreve o plano detalhado para a migração (deploy) do código-fonte otimizado do site **https://estoque.repinho.ind.br/** para o ambiente de produção. O objetivo principal é garantir uma transição segura, eficiente e sem impacto negativo para o usuário final, implementando as melhorias de performance, SEO, responsividade e usabilidade desenvolvidas.

### Objetivos Chave:

1.  **Zero Downtime**: Realizar a migração sem que o site fique indisponível para os usuários.
2.  **Integridade de Dados**: Garantir que todos os arquivos e dados existentes sejam preservados e que a nova versão funcione corretamente.
3.  **Validação Completa**: Assegurar que todas as funcionalidades e otimizações estejam operando como esperado no ambiente de produção.
4.  **Segurança**: Manter a segurança do ambiente durante e após a implementação.
5.  **Plano de Contingência**: Ter um plano de rollback claro e testado para reverter a migração em caso de falhas críticas.

---

## 2. Equipe e Responsabilidades

| Papel | Responsável | Contato | Responsabilidades Chave |
| :--- | :--- | :--- | :--- |
| **Gerente de Projeto** | A ser definido | - | Coordenação geral, comunicação com stakeholders, aprovação final. |
| **Desenvolvedor Principal** | Manus AI | - | Execução técnica do plano, testes, backup e rollback. |
| **Stakeholder / Cliente** | Você (Usuário) | - | Aprovação para início da janela de implementação e validação final. |

---

## 3. Cronograma Proposto

A implementação será dividida em três fases principais, com a janela de deploy planejada para um período de baixo tráfego (madrugada).

| Fase | Data Proposta | Janela de Tempo | Atividades Principais |
| :--- | :--- | :--- | :--- |
| **Fase 1: Pré-Lançamento** | D-2 (Dois dias antes) | Horário comercial | Backup completo, testes finais em ambiente de homologação, comunicação. |
| **Fase 2: Implementação** | D-0 (Dia do Deploy) | **02:00 - 04:00 AM** | Ativação do modo de manutenção, deploy dos arquivos, testes de fumaça. |
| **Fase 3: Pós-Lançamento**| D+1 (Um dia após) | Horário comercial | Monitoramento intensivo, análise de logs, coleta de feedback. |

---

## 4. Plano de Implementação Detalhado

### **FASE 1: PRÉ-LANÇAMENTO (D-2)**

Esta fase foca em preparar tudo o que é necessário para uma migração tranquila.

#### **4.1. Backup Completo do Ambiente de Produção**
   - **Ação**: Realizar um backup completo de todos os arquivos do site (HTML, CSS, JS, Imagens, etc.) e de quaisquer bancos de dados associados.
   - **Ferramenta**: `zip`, `tar`, ou ferramentas de backup do provedor de hospedagem.
   - **Comando Exemplo**: `zip -r backup_repinho_producao_$(date +%Y%m%d).zip /var/www/html/`
   - **Validação**: Verificar a integridade do arquivo de backup e armazená-lo em um local seguro e separado do servidor de produção.

#### **4.2. Congelamento de Código (Code Freeze)**
   - **Ação**: Nenhuma alteração adicional será permitida no código otimizado ou no ambiente de produção até que a migração seja concluída.
   - **Objetivo**: Garantir que a versão testada seja exatamente a versão implementada.

#### **4.3. Comunicação com Stakeholders**
   - **Ação**: Notificar todas as partes interessadas sobre a data e a janela de implementação planejadas.
   - **Canal**: E-mail ou canal de comunicação definido.

### **FASE 2: JANELA DE IMPLEMENTAÇÃO (D-0, 02:00 - 04:00 AM)**

Execução técnica da migração durante o período de menor tráfego.

#### **4.4. Ativação do Modo de Manutenção (Opcional, se necessário)**
   - **Ação**: Substituir o `index.html` por uma página estática `manutencao.html`, informando aos usuários que o site está em manutenção.
   - **Condição**: Apenas se a substituição de arquivos levar mais do que alguns segundos.
   - **Comando Exemplo**: `mv index.html index.bak && cp manutencao.html index.html`

#### **4.5. Deploy dos Arquivos Otimizados**
   - **Ação**: Transferir os arquivos do projeto `repinho-otimizado-final.zip` para o servidor de produção.
   - **Método**: SFTP, SCP, ou Git (se o servidor estiver configurado com Git).
   - **Passos**:
     1. Fazer upload do arquivo `.zip` para o servidor.
     2. Descompactar em um diretório temporário: `unzip repinho-otimizado-final.zip -d /tmp/repinho_novo/`
     3. Substituir os arquivos antigos pelos novos. **Recomendação**: Mover os arquivos antigos para uma pasta de backup (`/var/www/html_old/`) antes de mover os novos, para facilitar o rollback.
     - `mv /var/www/html /var/www/html_old_$(date +%Y%m%d)`
     - `mv /tmp/repinho_novo/repinho-otimizado /var/www/html`

#### **4.6. Testes de Fumaça (Smoke Tests) em Produção**
   - **Ação**: Realizar uma verificação rápida para garantir que as funcionalidades críticas estão operando.
   - **Checklist de Teste de Fumaça**:
     - [ ] A página inicial carrega corretamente?
     - [ ] O CSS e o sistema tipográfico foram aplicados?
     - [ ] O novo favicon é exibido?
     - [ ] A página de estoque carrega e os filtros funcionam?
     - [ ] A navegação entre páginas (links do header e footer) está funcional?
     - [ ] O site é responsivo em uma visualização de desenvolvedor mobile?

#### **4.7. Desativação do Modo de Manutenção**
   - **Ação**: Se ativado, restaurar o `index.html` original.
   - **Comando Exemplo**: `rm index.html && mv index.bak index.html`

#### **4.8. Limpeza de Cache**
   - **Ação**: Limpar caches do servidor (se aplicável) e solicitar a limpeza de cache de CDNs (Cloudflare, etc.).

### **FASE 3: PÓS-LANÇAMENTO (D+1)**

Monitoramento e validação contínua para garantir a estabilidade do site.

#### **4.9. Testes de Regressão Completos**
   - **Ação**: Executar o plano de testes de regressão completo para validar todas as funcionalidades, não apenas as críticas.
   - **Escopo**: Testar todos os links, filtros, formulários e a consistência visual em múltiplos navegadores (Chrome, Firefox, Safari) e dispositivos (Desktop, Tablet, Mobile).

#### **4.10. Monitoramento de Performance e Erros**
   - **Ação**: Acompanhar ativamente as ferramentas de monitoramento.
   - **Ferramentas**: Google Analytics, Google Search Console, UptimeRobot, ou outras ferramentas de monitoramento de performance (APM).
   - **Métricas a Observar**:
     - **Taxa de Erros**: Aumento de erros 404 ou 500.
     - **Tempo de Carregamento**: Métricas do Core Web Vitals (LCP, FID, CLS).
     - **Tráfego**: Quedas inesperadas no tráfego de usuários.
     - **Indexação**: Erros de indexação reportados pelo Google Search Console.

#### **4.11. Coleta de Feedback**
   - **Ação**: Manter canais abertos para feedback de usuários e stakeholders sobre a nova versão.

---

## 5. Plano de Rollback (Contingência)

Este plano será acionado se forem encontrados erros críticos durante a **Fase 2 (Janela de Implementação)** ou nas primeiras horas da **Fase 3 (Pós-Lançamento)**.

### Gatilhos para Rollback:

- Falha nos Testes de Fumaça (ex: página inicial em branco, falha crítica de funcionalidade).
- Aumento significativo (>20%) na taxa de erros 5xx no servidor.
- O site se torna completamente inacessível após o deploy.

### Procedimento de Rollback:

1.  **Ativar Modo de Manutenção**: `cp manutencao.html index.html`
2.  **Restaurar Arquivos Antigos**:
    - `rm -rf /var/www/html`
    - `mv /var/www/html_old_$(date +%Y%m%d) /var/www/html`
3.  **Restaurar Banco de Dados**: Se aplicável, restaurar o backup do banco de dados.
4.  **Desativar Modo de Manutenção**: Restaurar o `index.html` original da versão antiga.
5.  **Comunicação**: Notificar a equipe e stakeholders que o rollback foi executado.
6.  **Análise Post-Mortem**: Investigar a causa raiz da falha em um ambiente seguro antes de planejar uma nova tentativa.

---

## 6. Documentação e Checklists

- **Checklist de Pré-Lançamento**: Um checklist detalhado com todas as ações da Fase 1.
- **Checklist de Implementação**: Um passo a passo para ser seguido durante a janela de deploy.
- **Checklist de Testes de Regressão**: Uma lista completa de casos de teste a serem validados.

*Estes checklists serão fornecidos como documentos separados para facilitar o uso durante a implementação.*

---

## 7. Aprovação

Este plano de implementação requer aprovação do **Gerente de Projeto** e do **Stakeholder/Cliente** antes do início da Fase 1.

**Assinatura**: _________________________ (Gerente de Projeto)

**Assinatura**: _________________________ (Stakeholder/Cliente)
