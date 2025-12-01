import { buildSidebar } from './sidebar.js'
import { buildDashboard } from './dashboard.js'
import { showProdutos } from './produtos.js';

let root = null;

document.addEventListener("DOMContentLoaded", init);

function init() {
    root = document.getElementById("root");
    root.append(buildSidebar(), buildDashboard());
    showProdutos();
}
