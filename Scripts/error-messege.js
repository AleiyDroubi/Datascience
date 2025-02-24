/* Phone Number Error msg */
document.addEventListener("DOMContentLoaded", function () {
    const phoneInput = document.getElementById("phone");
    const errorMessage = document.getElementById("error-message");

    phoneInput.addEventListener("input", function () {
        // This Allow only digits
        this.value = this.value.replace(/\D/g, "");  

        //  Make it start with "01" and be exactly 11 digits long
        const regex = /^01\d{9}$/;
        if (regex.test(this.value)) {
            errorMessage.style.display = "none";
        } else {
            errorMessage.style.display = "block";
        }
    });
});