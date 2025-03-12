// Toggles Text and Appearance of View/Hide Order Details Button on past_orders.html
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".toggle-details").forEach(button => {
        button.addEventListener("click", function() {
            const isExpanded = this.getAttribute("aria-expanded") === "true";

            setTimeout(() => {
                if (isExpanded) {
                    this.textContent = "Hide Order Details";
                    this.classList.remove("btn-primary");
                    this.classList.add("btn-secondary");
                } else {
                    this.textContent = "View Order Details";
                    this.classList.remove("btn-secondary");
                    this.classList.add("btn-primary");
                }
            }, 200);
        });
    });
});

//Event Listener for Order ID for Deletion of Orders
document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll('#delete-initialization-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            // Get the order ID from the clicked button
            const orderId = event.target.getAttribute('data-order-id');
            
            // Find the delete form and set its action to call the delete view with the appropriate orderId
            const deleteForm = document.getElementById('deleteForm');
            const deleteUrl = deleteUrlBase.replace('0', orderId);
            deleteForm.setAttribute('action', deleteUrl);
        });
    });
});

//Event Listener and function to dynamically add new forms to the admin menu creation screen
document.addEventListener("DOMContentLoaded", function () {
    let formsetContainer = document.getElementById("meal-formset");
    let addButton = document.getElementById("add-meal");
    let totalForms = document.getElementById("id_meals-TOTAL_FORMS");

    addButton.addEventListener("click", function (e) {
        e.preventDefault();

        let formCount = parseInt(totalForms.value);
        let newForm = formsetContainer.lastElementChild.cloneNode(true);

        //update form index with a regular expression that matches a sequence of - followed by digits and another -
        //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions 
        newForm.innerHTML = newForm.innerHTML.replace(/-\d+-/g, `-${formCount}-`);
        
        formsetContainer.appendChild(newForm);
        totalForms.value = formCount + 1;
    });
});
