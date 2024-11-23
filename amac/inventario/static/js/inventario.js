document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los botones/enlaces que abren el modal
    var openModalButtons = document.querySelectorAll(".open-modal");
    var DeletProduct = document.querySelectorAll(".delete-link"); 

    var btnAT = document.getElementById("myBtn");
    var btnAP = document.getElementById("myBtn2");

    // Obtener el modal
    var modal = document.getElementById("myModal");

    // Obtener el botón de cerrar el modal
    var closeButton = modal.querySelector(".close");

    // When the user clicks the button, open the modal 
    btnAT.onclick = function() {
    modal.style.display = "block";
    };
    btnAP.onclick = function() {
        modal.style.display = "block";
        };
    // Asignar el evento click a cada botón/enlace para abrir el modal
    openModalButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault(); // Prevenir comportamiento por defecto del enlace o botón
            modal.style.display = "block";
        });
    });
    DeletProduct.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            // Obtener el ID del producto del atributo data-id
            var productId = button.getAttribute("id");


            if (confirm( "Esta seguro que desea eliminar" + productId + "?")) {
                window.location.href = "/inventario/delete/";
            }
        });

    // Asignar el evento click para cerrar el modal cuando se hace clic en el botón "cerrar"
    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });

})});