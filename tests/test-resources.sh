#!/bin/bash

##############################################################################
# Script de Teste Automatizado - Repinho Compensados
# Verifica se todos os links, imagens, favicons, CSS e JS estão carregando
#
# Uso:
#   bash test-resources.sh https://estoque.repinho.ind.br/
#   ou
#   bash test-resources.sh http://localhost:8000/
##############################################################################

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Verificar se URL foi fornecida
if [ -z "$1" ]; then
    echo "Uso: bash test-resources.sh <URL_BASE>"
    echo "Exemplo: bash test-resources.sh https://estoque.repinho.ind.br/"
    exit 1
fi

BASE_URL="${1%/}"  # Remove trailing slash
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Função para imprimir cabeçalho
print_header() {
    echo -e "\n${BOLD}${CYAN}$(printf '=%.0s' {1..70})${NC}"
    echo -e "${BOLD}${CYAN}$1${NC}"
    echo -e "${BOLD}${CYAN}$(printf '=%.0s' {1..70})${NC}\n"
}

# Função para imprimir sucesso
print_success() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED_TESTS++))
}

# Função para imprimir erro
print_error() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED_TESTS++))
}

# Função para imprimir aviso
print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Função para imprimir info
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Função para testar URL
test_url() {
    local url="$1"
    local resource_type="$2"
    
    ((TOTAL_TESTS++))
    
    # Usar curl para testar
    http_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$url" 2>/dev/null)
    
    if [ "$http_code" = "200" ]; then
        return 0
    else
        echo "HTTP $http_code"
        return 1
    fi
}

# Função para extrair URLs de um arquivo HTML
extract_resources() {
    local html_file="$1"
    local base_url="$2"
    
    # Extrair imagens
    echo "=== IMAGENS ===" 
    grep -oP 'src="\K[^"]+' "$html_file" | sort -u
    
    # Extrair CSS
    echo "=== STYLESHEETS ===" 
    grep -oP 'href="\K[^"]+\.css' "$html_file" | sort -u
    
    # Extrair Scripts
    echo "=== SCRIPTS ===" 
    grep -oP '<script[^>]+src="\K[^"]+' "$html_file" | sort -u
    
    # Extrair Favicons
    echo "=== FAVICONS ===" 
    grep -oP 'rel="[^"]*icon[^"]*"[^>]+href="\K[^"]+' "$html_file" | sort -u
}

# Função para testar página
test_page() {
    local page_name="$1"
    local page_path="$2"
    local page_url="${BASE_URL}/${page_path}"
    
    print_info "Testando: $page_url"
    
    # Baixar página
    local temp_file=$(mktemp)
    curl -s "$page_url" > "$temp_file"
    
    if [ ! -s "$temp_file" ]; then
        print_error "Falha ao baixar página: $page_name"
        rm "$temp_file"
        return 1
    fi
    
    print_success "Página carregada: $page_name"
    
    # Testar imagens
    print_info "Testando imagens..."
    while IFS= read -r img_src; do
        [ -z "$img_src" ] && continue
        
        # Converter caminho relativo para URL absoluta
        if [[ "$img_src" == http* ]]; then
            img_url="$img_src"
        else
            img_url="${BASE_URL}/${img_src}"
        fi
        
        if test_url "$img_url" "Imagem"; then
            print_success "Imagem: $img_src"
        else
            print_error "Imagem: $img_src - $(test_url "$img_url" "Imagem" 2>&1)"
        fi
    done < <(grep -oP 'src="\K[^"]+' "$temp_file" | sort -u)
    
    # Testar CSS
    print_info "Testando stylesheets..."
    while IFS= read -r css_src; do
        [ -z "$css_src" ] && continue
        
        if [[ "$css_src" == http* ]]; then
            css_url="$css_src"
        else
            css_url="${BASE_URL}/${css_src}"
        fi
        
        if test_url "$css_url" "CSS"; then
            print_success "CSS: $css_src"
        else
            print_error "CSS: $css_src"
        fi
    done < <(grep -oP 'href="\K[^"]+\.css' "$temp_file" | sort -u)
    
    # Testar Scripts
    print_info "Testando scripts..."
    while IFS= read -r script_src; do
        [ -z "$script_src" ] && continue
        
        if [[ "$script_src" == http* ]]; then
            script_url="$script_src"
        else
            script_url="${BASE_URL}/${script_src}"
        fi
        
        if test_url "$script_url" "Script"; then
            print_success "Script: $script_src"
        else
            print_error "Script: $script_src"
        fi
    done < <(grep -oP '<script[^>]+src="\K[^"]+' "$temp_file" | sort -u)
    
    # Testar Favicons
    print_info "Testando favicons..."
    while IFS= read -r favicon_src; do
        [ -z "$favicon_src" ] && continue
        
        if [[ "$favicon_src" == http* ]]; then
            favicon_url="$favicon_src"
        else
            favicon_url="${BASE_URL}/${favicon_src}"
        fi
        
        if test_url "$favicon_url" "Favicon"; then
            print_success "Favicon: $favicon_src"
        else
            print_error "Favicon: $favicon_src"
        fi
    done < <(grep -oP 'href="\K[^"]+' "$temp_file" | grep -E 'favicon|icon|apple' | sort -u)
    
    # Testar Links Internos
    print_info "Testando links internos..."
    while IFS= read -r link_href; do
        [ -z "$link_href" ] && continue
        [[ "$link_href" == \#* ]] && continue  # Pular âncoras
        [[ "$link_href" == http* ]] && continue  # Pular links externos
        
        if [[ "$link_href" == /* ]]; then
            link_url="${BASE_URL}${link_href}"
        else
            link_url="${BASE_URL}/${link_href}"
        fi
        
        if test_url "$link_url" "Link"; then
            print_success "Link: $link_href"
        else
            print_error "Link: $link_href"
        fi
    done < <(grep -oP 'href="\K[^"]+' "$temp_file" | sort -u | head -20)
    
    rm "$temp_file"
}

# Função para gerar relatório
generate_report() {
    print_header "Relatório Final de Testes"
    
    echo -e "${BOLD}Resumo Geral:${NC}"
    echo "  Total de recursos testados: $TOTAL_TESTS"
    echo -e "  ${GREEN}✓ Sucesso: $PASSED_TESTS${NC}"
    echo -e "  ${RED}✗ Falhas: $FAILED_TESTS${NC}"
    
    if [ $TOTAL_TESTS -gt 0 ]; then
        success_rate=$((PASSED_TESTS * 100 / TOTAL_TESTS))
        echo -e "\n  ${BOLD}Taxa de Sucesso: ${success_rate}%${NC}"
    fi
    
    if [ $FAILED_TESTS -eq 0 ]; then
        echo -e "\n${GREEN}${BOLD}✓ Todos os testes passaram com sucesso!${NC}"
        return 0
    else
        echo -e "\n${RED}${BOLD}✗ $FAILED_TESTS recursos falharam no teste${NC}"
        return 1
    fi
}

# Executar testes
print_header "Teste Automatizado de Recursos - Repinho Compensados"
print_info "URL Base: $BASE_URL"
print_info "Data/Hora: $(date '+%d/%m/%Y %H:%M:%S')"

# Testar páginas
test_page "Página Inicial" "index.html"
test_page "Estoque" "estoque.html"
test_page "Entenda Produtos" "entenda-produtos.html"
test_page "Qualidades" "nc-qualidades.html"

# Gerar relatório
generate_report

# Retornar status
if [ $FAILED_TESTS -eq 0 ]; then
    exit 0
else
    exit 1
fi
