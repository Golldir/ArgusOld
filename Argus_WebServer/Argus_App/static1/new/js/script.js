function resizing() {
    let image = document.querySelector("#scheme"); // Достаем картинку
    let parent = document.querySelector('.grid-cell-scheme')

    parent.style.opacity = '100%';

    if (w1 == undefined) {
        w1 = image.offsetWidth; // Пропорция
    }

    if (h1 == undefined) {
        h1 = image.offsetHeight; // Пропорция
    }

    let w2 = parent.offsetWidth;
    let h2 = parent.offsetHeight;

    let scale = Math.min(w2 / w1, h2 / h1);

    let newWidth = w1 * scale;
    let newHeight = h1 * scale;

    image.style.height = newHeight + "px";
    image.style.width = newWidth + "px";

    parent.style.fontSize = (image.offsetHeight + image.offsetWidth)/ 130 + "px";
}


let w1;
let h1;
// Вызываем resizing() при загрузке страницы
window.addEventListener('load', resizing);
// Вызываем resizing() при изменении размеров окна
window.addEventListener("resize", resizing);