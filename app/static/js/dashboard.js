import {el} from './helpers.js'

export function buildDashboard() {
    return el("div", { id: "corpo_dashboard" },

        // Cabeçalho estático
        el("div", { className: "cabecalho_corpo" },
            el("img", { id: "cabecalho_corpo", src: "/static/images/dashboard_icon.png" }),
            el("h1", { textContent: "Dashboard" })
        ),

        // Área dinâmica
        el("div", { id: "conteudo_dashboard" })
    );
}

export function setContent(...children) {
    const area = document.getElementById("conteudo_dashboard");
    area.innerHTML = "";
    area.append(...children);
}