/**
 * Script de Teste Automatizado - Repinho Compensados (Navegador)
 * Verifica se todos os recursos estão carregando corretamente
 * 
 * Uso:
 * 1. Abra o console do navegador (F12)
 * 2. Cole o conteúdo deste arquivo
 * 3. Execute: runTests()
 */

class ResourceTester {
    constructor() {
        this.results = {
            images: { ok: [], failed: [] },
            stylesheets: { ok: [], failed: [] },
            scripts: { ok: [], failed: [] },
            favicons: { ok: [], failed: [] },
            links: { ok: [], failed: [] }
        };
        this.totalTests = 0;
        this.passedTests = 0;
        this.failedTests = 0;
    }

    // Cores para console
    getColors() {
        return {
            reset: '\x1b[0m',
            bold: '\x1b[1m',
            green: '\x1b[32m',
            red: '\x1b[31m',
            yellow: '\x1b[33m',
            blue: '\x1b[34m',
            cyan: '\x1b[36m'
        };
    }

    // Imprimir cabeçalho
    printHeader(text) {
        const c = this.getColors();
        console.log(`\n${c.bold}${c.cyan}${'='.repeat(70)}${c.reset}`);
        console.log(`${c.bold}${c.cyan}${text.padStart((text.length + 70) / 2)}${c.reset}`);
        console.log(`${c.bold}${c.cyan}${'='.repeat(70)}${c.reset}\n`);
    }

    // Imprimir sucesso
    printSuccess(text) {
        const c = this.getColors();
        console.log(`${c.green}✓${c.reset} ${text}`);
        this.passedTests++;
    }

    // Imprimir erro
    printError(text) {
        const c = this.getColors();
        console.log(`${c.red}✗${c.reset} ${text}`);
        this.failedTests++;
    }

    // Imprimir aviso
    printWarning(text) {
        const c = this.getColors();
        console.log(`${c.yellow}⚠${c.reset} ${text}`);
    }

    // Imprimir info
    printInfo(text) {
        const c = this.getColors();
        console.log(`${c.blue}ℹ${c.reset} ${text}`);
    }

    // Testar se imagem carregou
    testImage(src) {
        return new Promise((resolve) => {
            const img = new Image();
            img.onload = () => resolve(true);
            img.onerror = () => resolve(false);
            img.src = src;
        });
    }

    // Testar se CSS carregou
    testStylesheet(href) {
        return new Promise((resolve) => {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = href;
            link.onload = () => resolve(true);
            link.onerror = () => resolve(false);
            document.head.appendChild(link);
        });
    }

    // Testar se script carregou
    testScript(src) {
        return new Promise((resolve) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = () => resolve(true);
            script.onerror = () => resolve(false);
            document.head.appendChild(script);
        });
    }

    // Testar link HTTP
    testLink(href) {
        return fetch(href, { method: 'HEAD', mode: 'no-cors' })
            .then(() => true)
            .catch(() => false);
    }

    // Extrair recursos da página
    extractResources() {
        const resources = {
            images: [],
            stylesheets: [],
            scripts: [],
            favicons: [],
            links: []
        };

        // Imagens
        document.querySelectorAll('img[src]').forEach(img => {
            resources.images.push({
                src: img.src,
                alt: img.alt || 'Sem alt'
            });
        });

        // Stylesheets
        document.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
            resources.stylesheets.push(link.href);
        });

        // Scripts
        document.querySelectorAll('script[src]').forEach(script => {
            resources.scripts.push(script.src);
        });

        // Favicons
        document.querySelectorAll('link[rel*="icon"]').forEach(link => {
            resources.favicons.push({
                href: link.href,
                sizes: link.sizes || 'N/A'
            });
        });

        // Links internos
        document.querySelectorAll('a[href]').forEach(link => {
            const href = link.href;
            if (href && !href.startsWith('#') && !href.startsWith('javascript:')) {
                resources.links.push({
                    href: href,
                    text: link.textContent.trim().substring(0, 50)
                });
            }
        });

        return resources;
    }

    // Testar imagens
    async testImages(resources) {
        this.printInfo('Testando imagens...');
        
        for (const img of resources.images) {
            this.totalTests++;
            const success = await this.testImage(img.src);
            
            if (success) {
                this.printSuccess(`Imagem: ${img.src}`);
                this.results.images.ok.push(img.src);
            } else {
                this.printError(`Imagem: ${img.src}`);
                this.results.images.failed.push(img.src);
            }
        }
    }

    // Testar stylesheets
    async testStylesheets(resources) {
        this.printInfo('Testando stylesheets...');
        
        for (const href of resources.stylesheets) {
            this.totalTests++;
            try {
                const response = await fetch(href, { method: 'HEAD', mode: 'no-cors' });
                if (response.ok || response.status === 0) {
                    this.printSuccess(`CSS: ${href}`);
                    this.results.stylesheets.ok.push(href);
                } else {
                    this.printError(`CSS: ${href} (Status ${response.status})`);
                    this.results.stylesheets.failed.push(href);
                }
            } catch (e) {
                this.printError(`CSS: ${href} (${e.message})`);
                this.results.stylesheets.failed.push(href);
            }
        }
    }

    // Testar scripts
    async testScripts(resources) {
        this.printInfo('Testando scripts...');
        
        for (const src of resources.scripts) {
            this.totalTests++;
            try {
                const response = await fetch(src, { method: 'HEAD', mode: 'no-cors' });
                if (response.ok || response.status === 0) {
                    this.printSuccess(`Script: ${src}`);
                    this.results.scripts.ok.push(src);
                } else {
                    this.printError(`Script: ${src} (Status ${response.status})`);
                    this.results.scripts.failed.push(src);
                }
            } catch (e) {
                this.printError(`Script: ${src} (${e.message})`);
                this.results.scripts.failed.push(src);
            }
        }
    }

    // Testar favicons
    async testFavicons(resources) {
        this.printInfo('Testando favicons...');
        
        for (const favicon of resources.favicons) {
            this.totalTests++;
            try {
                const response = await fetch(favicon.href, { method: 'HEAD', mode: 'no-cors' });
                if (response.ok || response.status === 0) {
                    this.printSuccess(`Favicon: ${favicon.href} (${favicon.sizes})`);
                    this.results.favicons.ok.push(favicon.href);
                } else {
                    this.printError(`Favicon: ${favicon.href} (Status ${response.status})`);
                    this.results.favicons.failed.push(favicon.href);
                }
            } catch (e) {
                this.printError(`Favicon: ${favicon.href} (${e.message})`);
                this.results.favicons.failed.push(favicon.href);
            }
        }
    }

    // Testar links internos
    async testLinks(resources) {
        this.printInfo('Testando links internos...');
        
        // Limitar a 20 links para não sobrecarregar
        const linksToTest = resources.links.slice(0, 20);
        
        for (const link of linksToTest) {
            this.totalTests++;
            try {
                const response = await fetch(link.href, { method: 'HEAD', mode: 'no-cors' });
                if (response.ok || response.status === 0) {
                    this.printSuccess(`Link: ${link.href}`);
                    this.results.links.ok.push(link.href);
                } else {
                    this.printError(`Link: ${link.href} (Status ${response.status})`);
                    this.results.links.failed.push(link.href);
                }
            } catch (e) {
                this.printError(`Link: ${link.href} (${e.message})`);
                this.results.links.failed.push(link.href);
            }
        }
    }

    // Verificar meta tags
    checkMetaTags() {
        this.printHeader('Verificação de Meta Tags');
        
        const requiredTags = ['viewport', 'description', 'robots'];
        const ogTags = ['og:title', 'og:description', 'og:type', 'og:url'];
        
        this.printInfo('Meta tags essenciais:');
        for (const tag of requiredTags) {
            const meta = document.querySelector(`meta[name="${tag}"]`);
            if (meta) {
                this.printSuccess(`${tag}: ${meta.content.substring(0, 50)}`);
            } else {
                this.printWarning(`${tag}: NÃO ENCONTRADA`);
            }
        }
        
        this.printInfo('Open Graph tags:');
        for (const tag of ogTags) {
            const meta = document.querySelector(`meta[property="${tag}"]`);
            if (meta) {
                this.printSuccess(`${tag}: ${meta.content.substring(0, 50)}`);
            } else {
                this.printWarning(`${tag}: NÃO ENCONTRADA`);
            }
        }
    }

    // Gerar relatório
    generateReport() {
        this.printHeader('Relatório Final de Testes');
        
        console.log(`${this.getColors().bold}Resumo Geral:${this.getColors().reset}`);
        console.log(`  Total de recursos testados: ${this.totalTests}`);
        console.log(`  ${this.getColors().green}✓ Sucesso: ${this.passedTests}${this.getColors().reset}`);
        console.log(`  ${this.getColors().red}✗ Falhas: ${this.failedTests}${this.getColors().reset}`);
        
        if (this.totalTests > 0) {
            const successRate = ((this.passedTests / this.totalTests) * 100).toFixed(1);
            console.log(`\n  ${this.getColors().bold}Taxa de Sucesso: ${successRate}%${this.getColors().reset}`);
        }
        
        console.log(`\n${this.getColors().bold}Detalhes por Tipo:${this.getColors().reset}`);
        
        for (const [type, data] of Object.entries(this.results)) {
            const total = data.ok.length + data.failed.length;
            if (total > 0) {
                const status = data.failed.length === 0 ? this.getColors().green : this.getColors().red;
                console.log(`  ${status}${type.charAt(0).toUpperCase() + type.slice(1)}: ${data.ok.length}/${total} OK${this.getColors().reset}`);
                
                if (data.failed.length > 0) {
                    data.failed.forEach(item => {
                        console.log(`    ${this.getColors().red}✗ ${item}${this.getColors().reset}`);
                    });
                }
            }
        }
        
        if (this.failedTests === 0) {
            console.log(`\n${this.getColors().green}${this.getColors().bold}✓ Todos os testes passaram com sucesso!${this.getColors().reset}`);
        } else {
            console.log(`\n${this.getColors().red}${this.getColors().bold}✗ ${this.failedTests} recursos falharam no teste${this.getColors().reset}`);
        }
    }

    // Executar testes
    async run() {
        this.printHeader('Teste Automatizado de Recursos - Repinho Compensados');
        this.printInfo(`URL: ${window.location.href}`);
        this.printInfo(`Data/Hora: ${new Date().toLocaleString('pt-BR')}`);
        
        const resources = this.extractResources();
        
        await this.testImages(resources);
        await this.testStylesheets(resources);
        await this.testScripts(resources);
        await this.testFavicons(resources);
        await this.testLinks(resources);
        
        this.checkMetaTags();
        this.generateReport();
    }
}

// Função global para executar testes
async function runTests() {
    const tester = new ResourceTester();
    await tester.run();
}

// Executar automaticamente se estiver em desenvolvimento
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.log('Teste automatizado disponível. Execute: runTests()');
}
