document.addEventListener("DOMContentLoaded", function () {
    var generalModal = document.getElementById("myModal");
    var modalContent = document.getElementById("modalFormContent");
    var closeButton = document.querySelector(".close");

    // Botón para abrir el modal de agregar tarea
    var btnAgregarTarea = document.getElementById("myBtn");
    btnAgregarTarea.onclick = function () {
        modalContent.innerHTML = document.getElementById("tareaFormContainer").innerHTML;
        generalModal.style.display = "block";
    };

    // Cerrar el modal al hacer clic en la "x"
    closeButton.addEventListener("click", function () {
        generalModal.style.display = "none";
        modalContent.innerHTML = ""; // Limpiar el contenido del modal al cerrarlo
    });

    // Cerrar el modal al hacer clic fuera del contenido del modal
    window.addEventListener("click", function (event) {
        if (event.target == generalModal) {
            generalModal.style.display = "none";
            modalContent.innerHTML = ""; // Limpiar el contenido del modal al cerrarlo
        }
    });
});
