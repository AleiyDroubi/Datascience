
document.addEventListener("DOMContentLoaded", function () {
    const phoneInput = document.getElementById("phone");
    const errorMessage = document.getElementById("error-message");

    phoneInput.addEventListener("input", function () {
        this.value = this.value.replace(/\D/g, "");

        if (this.value.length === 11) {
            errorMessage.style.display = "none";
            } else {
            errorMessage.style.display = "block";
        }
    });
});
