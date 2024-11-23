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

    // Mensaje de bienvenida
    alert("Hola");
});
