export const API = {
    async getProdutos() {
        return fetchJSON('http://127.0.0.1:8000/produtos/');
    },

    async getProdutosPorNome(nome) {
        return fetchJSON(`http://127.0.0.1:8000/produtos/nome/${nome}`);
    },

    async getProdutoPorAsin(asin) {
        return fetchJSON(`http://127.0.0.1:8000/produtos/asin/${asin}`);
    },

    async getHistorico(asin) {
        return fetchJSON(`http://127.0.0.1:8000/historico/${asin}`);
    },

    async executeScraping() {
        return fetchJSONPost('http://127.0.0.1:8000/scrap/monitorar', { method: 'POST' });
    }
};

// Helper
async function fetchJSON(url) {
    const res = await fetch(url);
    return res.json();
}

async function fetchJSONPost(url) {
    const res = await fetch(url, { method: 'POST' });
    return res.json();
}