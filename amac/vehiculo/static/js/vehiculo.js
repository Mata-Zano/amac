document.addEventListener("DOMContentLoaded", function() {

    var generalModal = document.getElementById("myModal");
    var modalContent = document.getElementById("modalFormContent");
    var closeButton = document.querySelector(".close");
    var DeletProduct = document.querySelectorAll(".delete-link"); 

    // Botones para abrir el modal
    var btnAP = document.getElementById("myBtn2");
    var btnMA = document.getElementById("myBtn");
    var btnMO = document.getElementById("myBtn3");
    var editButtons = document.querySelectorAll("#myBtnE");

    // Mostrar el formulario de agregar producto en el modal
    btnAP.onclick = function() {
        modalContent.innerHTML = document.getElementById("productoFormContainerP").innerHTML;
        generalModal.style.display = "block";

    };
    btnMA.onclick = function() {
        modalContent.innerHTML = document.getElementById("productoFormContainerMA").innerHTML;
        generalModal.style.display = "block";
    };

    btnMO.onclick = function() {
        modalContent.innerHTML = document.getElementById("productoFormContainerMO").innerHTML;
        generalModal.style.display = "block";

    };


    DeletProduct.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            // Obtener el ID del producto del atributo data-id
            var productId = button.getAttribute("id");
            var productName = button.getAttribute("data-id");

            if (confirm( "Esta seguro que desea eliminar vehiculo con patente " + productName + "?")) {
                window.location.href = "/eliminarVehiculo/"+ productId;
            }
        });

    // Cerrar el modal al hacer clic en la "x"
    closeButton.addEventListener("click", function() {
        generalModal.style.display = "none";
        modalContent.innerHTML = ""; // Limpiar el contenido del modal al cerrarlo
    });


})});
