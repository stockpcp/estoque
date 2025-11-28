#!/usr/bin/env python3
"""
Script de Teste Automatizado - Repinho Compensados
Verifica se todos os links, imagens, favicons, CSS e JS estão carregando corretamente

Uso:
    python3 test-resources.py https://estoque.repinho.ind.br/
    ou
    python3 test-resources.py http://localhost:8000/
"""

import sys
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import defaultdict
import time
from datetime import datetime

# Cores para terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Imprime um cabeçalho formatado"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}\n")

def print_success(text):
    """Imprime mensagem de sucesso"""
    print(f"{Colors.GREEN}✓{Colors.RESET} {text}")

def print_error(text):
    """Imprime mensagem de erro"""
    print(f"{Colors.RED}✗{Colors.RESET} {text}")

def print_warning(text):
    """Imprime mensagem de aviso"""
    print(f"{Colors.YELLOW}⚠{Colors.RESET} {text}")

def print_info(text):
    """Imprime mensagem informativa"""
    print(f"{Colors.BLUE}ℹ{Colors.RESET} {text}")

class ResourceTester:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = defaultdict(list)
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'warnings': 0
        }

    def check_url(self, url, resource_type=""):
        """Verifica se uma URL está acessível"""
        try:
            response = self.session.head(url, timeout=5, allow_redirects=True)
            
            if response.status_code == 200:
                self.stats['success'] += 1
                return True, response.status_code, None
            elif response.status_code in [301, 302, 303, 307, 308]:
                self.stats['warnings'] += 1
                return True, response.status_code, f"Redirecionado para {response.url}"
            else:
                self.stats['failed'] += 1
                return False, response.status_code, f"Status {response.status_code}"
        except requests.exceptions.Timeout:
            self.stats['failed'] += 1
            return False, None, "Timeout na requisição"
        except requests.exceptions.ConnectionError:
            self.stats['failed'] += 1
            return False, None, "Erro de conexão"
        except Exception as e:
            self.stats['failed'] += 1
            return False, None, str(e)

    def extract_resources(self, html_content, page_url):
        """Extrai todos os recursos de uma página HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        resources = {
            'links': [],
            'images': [],
            'stylesheets': [],
            'scripts': [],
            'favicons': [],
            'meta': []
        }

        # Links
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href and not href.startswith('#'):
                resources['links'].append((href, link.get_text(strip=True)[:50]))

        # Imagens
        for img in soup.find_all('img', src=True):
            resources['images'].append((img['src'], img.get('alt', 'Sem alt')))

        # Stylesheets
        for link in soup.find_all('link', rel='stylesheet'):
            if link.get('href'):
                resources['stylesheets'].append(link['href'])

        # Scripts
        for script in soup.find_all('script', src=True):
            resources['scripts'].append(script['src'])

        # Favicons
        for link in soup.find_all('link'):
            if link.get('rel') and any('icon' in str(r).lower() for r in link.get('rel', [])):
                if link.get('href'):
                    resources['favicons'].append((link['href'], link.get('sizes', 'N/A')))

        # Meta tags
        for meta in soup.find_all('meta'):
            if meta.get('name') or meta.get('property'):
                name = meta.get('name') or meta.get('property')
                content = meta.get('content', '')
                resources['meta'].append((name, content[:60]))

        return resources

    def test_page(self, page_path):
        """Testa uma página específica"""
        page_url = urljoin(self.base_url, page_path)
        print_info(f"Testando: {page_url}")

        try:
            response = self.session.get(page_url, timeout=10)
            
            if response.status_code != 200:
                print_error(f"Página retornou status {response.status_code}")
                return False

            print_success(f"Página carregada com sucesso")
            resources = self.extract_resources(response.content, page_url)
            
            return resources
        except Exception as e:
            print_error(f"Erro ao acessar página: {str(e)}")
            return False

    def test_resources(self, resources, page_url):
        """Testa todos os recursos extraídos"""
        results = {
            'links': {'ok': 0, 'failed': 0, 'details': []},
            'images': {'ok': 0, 'failed': 0, 'details': []},
            'stylesheets': {'ok': 0, 'failed': 0, 'details': []},
            'scripts': {'ok': 0, 'failed': 0, 'details': []},
            'favicons': {'ok': 0, 'failed': 0, 'details': []},
        }

        # Testar imagens
        print_info("Testando imagens...")
        for img_src, alt_text in resources['images']:
            img_url = urljoin(page_url, img_src)
            success, status, error = self.check_url(img_url, "Imagem")
            self.stats['total'] += 1
            
            if success:
                results['images']['ok'] += 1
                print_success(f"Imagem: {img_src}")
            else:
                results['images']['failed'] += 1
                print_error(f"Imagem: {img_src} - {error}")
                results['images']['details'].append((img_src, error))

        # Testar CSS
        print_info("Testando stylesheets...")
        for css_src in resources['stylesheets']:
            css_url = urljoin(page_url, css_src)
            success, status, error = self.check_url(css_url, "CSS")
            self.stats['total'] += 1
            
            if success:
                results['stylesheets']['ok'] += 1
                print_success(f"CSS: {css_src}")
            else:
                results['stylesheets']['failed'] += 1
                print_error(f"CSS: {css_src} - {error}")
                results['stylesheets']['details'].append((css_src, error))

        # Testar Scripts
        print_info("Testando scripts...")
        for script_src in resources['scripts']:
            script_url = urljoin(page_url, script_src)
            success, status, error = self.check_url(script_url, "Script")
            self.stats['total'] += 1
            
            if success:
                results['scripts']['ok'] += 1
                print_success(f"Script: {script_src}")
            else:
                results['scripts']['failed'] += 1
                print_error(f"Script: {script_src} - {error}")
                results['scripts']['details'].append((script_src, error))

        # Testar Favicons
        print_info("Testando favicons...")
        for favicon_src, sizes in resources['favicons']:
            favicon_url = urljoin(page_url, favicon_src)
            success, status, error = self.check_url(favicon_url, "Favicon")
            self.stats['total'] += 1
            
            if success:
                results['favicons']['ok'] += 1
                print_success(f"Favicon: {favicon_src} ({sizes})")
            else:
                results['favicons']['failed'] += 1
                print_error(f"Favicon: {favicon_src} - {error}")
                results['favicons']['details'].append((favicon_src, error))

        # Testar Links Internos
        print_info("Testando links internos...")
        tested_links = set()
        for link_href, link_text in resources['links']:
            if link_href.startswith('http'):
                continue  # Pular links externos
            
            if link_href in tested_links:
                continue
            tested_links.add(link_href)
            
            link_url = urljoin(page_url, link_href)
            success, status, error = self.check_url(link_url, "Link")
            self.stats['total'] += 1
            
            if success:
                results['links']['ok'] += 1
                print_success(f"Link: {link_href}")
            else:
                results['links']['failed'] += 1
                print_error(f"Link: {link_href} - {error}")
                results['links']['details'].append((link_href, error))

        return results

    def test_meta_tags(self, resources):
        """Verifica meta tags importantes"""
        print_header("Verificação de Meta Tags")
        
        required_tags = ['viewport', 'description', 'robots']
        og_tags = ['og:title', 'og:description', 'og:type', 'og:url']
        
        meta_dict = {name: content for name, content in resources['meta']}
        
        print_info("Meta tags essenciais:")
        for tag in required_tags:
            if tag in meta_dict:
                print_success(f"{tag}: {meta_dict[tag]}")
            else:
                print_warning(f"{tag}: NÃO ENCONTRADA")

        print_info("Open Graph tags:")
        for tag in og_tags:
            if tag in meta_dict:
                print_success(f"{tag}: {meta_dict[tag]}")
            else:
                print_warning(f"{tag}: NÃO ENCONTRADA")

    def generate_report(self, all_results):
        """Gera relatório final"""
        print_header("Relatório Final de Testes")
        
        print(f"{Colors.BOLD}Resumo Geral:{Colors.RESET}")
        print(f"  Total de recursos testados: {self.stats['total']}")
        print(f"  {Colors.GREEN}✓ Sucesso: {self.stats['success']}{Colors.RESET}")
        print(f"  {Colors.RED}✗ Falhas: {self.stats['failed']}{Colors.RESET}")
        print(f"  {Colors.YELLOW}⚠ Avisos: {self.stats['warnings']}{Colors.RESET}")
        
        if self.stats['total'] > 0:
            success_rate = (self.stats['success'] / self.stats['total']) * 100
            print(f"\n  {Colors.BOLD}Taxa de Sucesso: {success_rate:.1f}%{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}Detalhes por Tipo:{Colors.RESET}")
        
        for page_name, results in all_results.items():
            print(f"\n  {Colors.BOLD}{page_name}:{Colors.RESET}")
            for resource_type, data in results.items():
                if resource_type in ['links', 'images', 'stylesheets', 'scripts', 'favicons']:
                    total = data['ok'] + data['failed']
                    if total > 0:
                        status = Colors.GREEN if data['failed'] == 0 else Colors.RED
                        print(f"    {status}{resource_type.capitalize()}: {data['ok']}/{total} OK{Colors.RESET}")
                        
                        if data['details']:
                            for resource, error in data['details']:
                                print(f"      {Colors.RED}✗ {resource}: {error}{Colors.RESET}")

    def run_full_test(self, pages):
        """Executa teste completo em todas as páginas"""
        print_header("Teste Automatizado de Recursos - Repinho Compensados")
        print_info(f"URL Base: {self.base_url}")
        print_info(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        all_results = {}
        
        for page_name, page_path in pages.items():
            print_header(f"Testando: {page_name}")
            
            resources = self.test_page(page_path)
            if not resources:
                continue
            
            results = self.test_resources(resources, urljoin(self.base_url, page_path))
            all_results[page_name] = results
            
            # Testar meta tags apenas na primeira página
            if page_name == list(pages.keys())[0]:
                self.test_meta_tags(resources)
        
        self.generate_report(all_results)
        
        # Retornar status final
        if self.stats['failed'] == 0:
            print_success("\n✓ Todos os testes passaram com sucesso!")
            return True
        else:
            print_error(f"\n✗ {self.stats['failed']} recursos falharam no teste")
            return False

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 test-resources.py <URL_BASE>")
        print("Exemplo: python3 test-resources.py https://estoque.repinho.ind.br/")
        sys.exit(1)

    base_url = sys.argv[1]
    
    # Páginas a testar
    pages = {
        'Página Inicial': 'index.html',
        'Estoque': 'estoque.html',
        'Entenda Produtos': 'entenda-produtos.html',
        'Qualidades': 'nc-qualidades.html',
    }
    
    tester = ResourceTester(base_url)
    success = tester.run_full_test(pages)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
