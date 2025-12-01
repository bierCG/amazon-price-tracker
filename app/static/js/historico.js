import { el } from './helpers.js'
import { API } from './api.js'
import { showProdutos } from './produtos.js';
import { setContent } from './dashboard.js'

export async function showHistorico(asin) {
    const historico = await API.getHistorico(asin);
    const produto = await API.getProdutoPorAsin(asin);

    const labels = historico.map(h => h.data);
    const valores = historico.map(h => h.preco);

    const header = el("div", { className: "header_historico" },
        el("img", { src: "/static/images/seta.png", onclick: showProdutos }),
        el("p", { textContent: `Histórico ${produto.nome}` })
    );

    const canvas1 = el("canvas", { id: "chartCanvas" });
    const canvas2 = el("canvas", { id: "chartCanvas2" });

    const body = el("div", { className: "HistoricoConteudo" },
        el("div", { className: "canvas" },
            el("div", { className: "HistoricoConteudoLine" },
                canvas1,
                canvas2
            )
        )
    );

    setContent(header, body);

    // Cria gráficos normalmente
    renderChartLine(canvas1, labels, valores);
    renderChartBar(canvas2, labels, valores);
}

function renderChartLine(canvas, labels, dados) {
    new Chart(canvas, {
        type: "line",
        data: {
            labels,
            datasets: [{
                label: "Preço (R$)",
                data: dados,
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            animation: false,
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function renderChartBar(canvas, labels, dados) {
    new Chart(canvas, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Preço",
                data: dados,
                borderWidth: 1
            }]
        },
        options: {
            animation: false,
            responsive: true,
            maintainAspectRatio: false
        }
    });
}