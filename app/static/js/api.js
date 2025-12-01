export const API = {
    async getProdutos() {
        return fetchJSON('https://amazon-price-tracker-50qq.onrender.com/produtos/');
    },

    async getProdutosPorNome(nome) {
        return fetchJSON(`https://amazon-price-tracker-50qq.onrender.com/produtos/nome/${nome}`);
    },

    async getProdutoPorAsin(asin) {
        return fetchJSON(`https://amazon-price-tracker-50qq.onrender.com/produtos/asin/${asin}`);
    },

    async getHistorico(asin) {
        return fetchJSON(`https://amazon-price-tracker-50qq.onrender.com/historico/${asin}`);
    },

    async executeScraping() {
        return fetchJSONPost('https://amazon-price-tracker-50qq.onrender.com/scrap/monitorar', { method: 'POST' });
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