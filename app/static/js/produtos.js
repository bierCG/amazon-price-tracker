import { el } from './helpers.js'
import { API } from './api.js'
import { showHistorico } from './historico.js'
import { setContent } from './dashboard.js'

export async function showProdutos() {
    const pesqInput = el("input", {
        placeholder: "Pesquisar...",
        onkeydown: e => {
            if (e.key === "Enter") loadProdutosPesquisa(pesqInput.value);
        }
    });

    const cabecalho = el("div", { id: "barra_1" },
        el("h1", { textContent: "Produtos" }),
        el("div", { className: "div_pesquisa" },
            el("img", { src: "/static/images/search_icon.png" }),
            pesqInput
        )
    );

    const listaContainer = el("div", { className: "lista" },
        el("div", { className: "campos_produto" },
            el("p", { textContent: "Nome" }),
            el("p", { textContent: "Preço" })
        ),
        el("div", { id: "lista_produtos" })
    );

    setContent(cabecalho, listaContainer);

    carregarProdutos(await API.getProdutos());
}

async function loadProdutosPesquisa(valor) {
    const produtos = valor ? await API.getProdutosPorNome(valor) : await API.getProdutos();
    carregarProdutos(produtos);
}

function carregarProdutos(produtos) {
    const lista = document.getElementById("lista_produtos");
    lista.innerHTML = "";

    produtos.forEach(p =>
        lista.append(el("div", { className: "item_lista", onclick: () => showHistorico(p.codigo_asin) },
            el("span", { textContent: p.nome }),
            el("span", { textContent: p.preco })
        ))
    );
}