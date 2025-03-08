<script>
    {% if messages %}
        var myModal = new bootstrap.Modal(document.getElementById('messageModal'), {
            keyboard: false
        });
        myModal.show();  // Show the modal with messages
    {% endif %}
</script>