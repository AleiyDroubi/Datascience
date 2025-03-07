document.addEventListener("DOMContentLoaded", function (){
const phonePattern = /^01\d{9}$/;

const NameInput = document.getElementById("name");
const NameError = document.getElementById("error-name");
const phoneInput = document.getElementById("phone");
const phoneError = document.getElementById("error-phone");

    function validateInput(input, errorElement, condition, errorMessage) {
        if (!condition) {
            errorElement.textContent = errorMessage;
            errorElement.style.display = "block";
            input.style.border = "1px solid red";
            return false;
        } else {
            errorElement.style.display = "none";
            input.style.border = "1px solid green";
            return true;
        }
    }

    NameInput.addEventListener("input", function () {
        validateInput(NameInput, NameError, NameInput.value.trim() !== "", "First Name is required");
    });

    phoneInput.addEventListener("input", function () {
        phoneInput.value = phoneInput.value.replace(/\D/g, "");
        validateInput(phoneInput, phoneError, phonePattern.test(phoneInput.value), "Phone number must start with 01 and be 11 digits");
    });

    this.addEventListener("submit", function (event) {
        let isValid = true; 
        if (!validateInput(NameInput, NameError, NameInput.value.trim() !== "", "Name is required")) {
            isValid = false;
        }
        isValid = validateInput(phoneInput, phoneError, phonePattern.test(phoneInput.value), "Phone number must start with 01 and be 11 digits") && isValid;
        if (!isValid) {
            event.preventDefault();
        }
    });
});