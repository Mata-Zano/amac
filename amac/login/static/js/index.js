document.addEventListener("DOMContentLoaded", () => {
    // Seleccionar todos los elementos con la clase 'headerLink'
    const headerLinks = document.querySelectorAll(".headerLink");

    headerLinks.forEach(link => {
        // Obtener la ruta de la imagen desde el atributo 'data-bg-image'
        const bgImage = link.dataset.bgImage;
        
        // Aplicar la imagen de fondo si existe
        if (bgImage) {
            link.style.backgroundImage = `url(${bgImage})`;
            link.style.backgroundSize = "cover";
            link.style.backgroundPosition = "center";
        }
    });

});
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".sidebar-item");
    let currentItem = 0;

    const showItem = (index) => {
        items.forEach((item, i) => {
            item.style.display = i === index ? "block" : "none";
        });
    };

    const nextItem = () => {
        currentItem = (currentItem + 1) % items.length;
        showItem(currentItem);
    };

    // Mostrar el primer elemento
    showItem(currentItem);

    // Cambiar de elemento cada 5 segundos
    setInterval(nextItem, 5000);
});