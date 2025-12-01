import { showProdutos } from './produtos.js'
import { initScraping } from './scraping.js'
import { el } from './helpers.js'

export function buildSidebar() {
    return el("div", { className: "menu_lateral" },

        // Logo
        el("div", { className: "logo" },
            el("img", { src: "/static/images/logo.png", className: "logo" })
        ),

        // Botões
        el("div", { className: "menu_botoes" },
            sidebarButton("Produtos", "/static/images/produtos_icon.png", showProdutos),
            sidebarButton("Scraper", "/static/images/scraping_icon.png", initScraping)
        )
    );
}

function sidebarButton(texto, icon, onClick) {
    return el("div", { className: "div_produto", onclick: onClick },
        el("img", { src: icon }),
        el("p", { textContent: texto })
    );
}