// Mini-factory para criar elementos facilmente
export function el(tag, props = {}, ...children) {
    const element = Object.assign(document.createElement(tag), props);
    for (const child of children) {
        if (child) element.append(child);
    }
    return element;
}