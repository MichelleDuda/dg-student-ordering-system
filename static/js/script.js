// Toggles Text and Appearance of View/Hide Order Details Button on past_orders.html
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".toggle-details").forEach(button => {
        button.addEventListener("click", function() {
            const isExpanded = this.getAttribute("aria-expanded") === "true";

            // Delay update to allow Bootstrap's animation to finish
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
