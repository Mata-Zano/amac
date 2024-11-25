document.addEventListener("DOMContentLoaded", function() {
    var generalModal = document.getElementById("myModal");
    var modalContent = document.getElementById("modalFormContent");
    var closeButton = document.querySelector(".close");

    // Botones para abrir el modal
    var btnAT = document.getElementById("myBtn");
    var btnAP = document.getElementById("myBtn2");
    var editButtons = document.querySelectorAll("#myBtnE");

    // Mostrar el formulario de agregar producto en el modal
    btnAP.onclick = function() {
        modalContent.innerHTML = document.getElementById("productoFormContainerP").innerHTML;
        generalModal.style.display = "block";
        var form = modalContent.querySelector("form");
        form.action = "{% url 'addProduct' %}";
    };

    // Mostrar el formulario de agregar tipo en el modal
    btnAT.onclick = function() {
        modalContent.innerHTML = document.getElementById("productoFormContainerT").innerHTML;
        generalModal.style.display = "block";
        var form = modalContent.querySelector("form");
        form.action = "{% url 'addTipo' %}";
    };

    editButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            var productId = button.closest(".product-actions").querySelector(".delete-link").getAttribute("id");

            // Cargar el formulario en el modal
            modalContent.innerHTML = document.getElementById("productoFormContainerP").innerHTML;
            generalModal.style.display = "block";

            // Ajustar el formulario para la edición
            var form = modalContent.querySelector("form");
            form.action = "{% url 'editProduct' 0 %}".replace("0", productId);

            // Precargar los datos del producto e inventario en el formulario
            var productItem = button.closest(".horizontal-product-item");
            var productoData = productItem.querySelectorAll(".horizontal-product-details td p");

            // Precargar los campos de tipo `input`
            form.querySelector("#id_nombre").value = productoData[0].innerText.split(": ")[1];
            form.querySelector("#id_descripcion").value = productoData[1].innerText.split(": ")[1];
            form.querySelector("#id_marca").value = productoData[2].innerText.split(": ")[1];
            form.querySelector("#id_unidadMedida").value = productoData[4].innerText.split(": ")[1];

            // Precargar los campos `select`
            var tipoValue = productoData[5].innerText.split(": ")[1]; // Tipo del producto
            var proveedorValue = productoData[3].innerText.split(": ")[1]; // Proveedor del producto

            // Precargar el campo `select` de `tipo`
            var tipoSelect = form.querySelector("#id_tipo");
            for (var i = 0; i < tipoSelect.options.length; i++) {
                if (tipoSelect.options[i].text === tipoValue) {
                    tipoSelect.selectedIndex = i;
                    break;
                }
            }

            // Precargar el campo `select` de `proveedor`
            var proveedorSelect = form.querySelector("#id_proveedor");
            for (var i = 0; i < proveedorSelect.options.length; i++) {
                if (proveedorSelect.options[i].text === proveedorValue) {
                    proveedorSelect.selectedIndex = i;
                    break;
                }
            }

            // Precargar los datos del inventario
            form.querySelector("#id_stock").value = productoData[5].innerText.split(": ")[1];
            form.querySelector("#id_stockMinimo").value = productoData[6].innerText.split(": ")[1];
            form.querySelector("#id_ubicacion").value = productoData[7].innerText.split(": ")[1];
            form.querySelector("#id_fechaVencimiento").value = productoData[8].innerText.split(": ")[1];
        });
    });


    // Cerrar el modal al hacer clic en la "x"
    closeButton.addEventListener("click", function() {
        generalModal.style.display = "none";
        modalContent.innerHTML = ""; // Limpiar el contenido del modal al cerrarlo
    });

    // Cerrar el modal al hacer clic fuera del contenido del modal
    window.addEventListener("click", function(event) {
        if (event.target == generalModal) {
            generalModal.style.display = "none";
            modalContent.innerHTML = ""; // Limpiar el contenido del modal al cerrarlo
        }
    });
});
