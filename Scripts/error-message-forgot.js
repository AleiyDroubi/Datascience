document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("forgot-form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");

    const emailError = document.getElementById("error-email");
    const passwordError = document.getElementById("error-password");

    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

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

    emailInput.addEventListener("input", function () {
        validateInput(emailInput, emailError, emailPattern.test(emailInput.value), "Invalid email address");
    });

    passwordInput.addEventListener("input", function () {
        validateInput(passwordInput, passwordError, passwordInput.value.trim() !== "", "Password is required");
    });

    confirmPasswordInput.addEventListener("input", function (){
        validateInput(confirmPasswordInput, passwordError, passwordInput.value === confirmPasswordInput.value, "Passwords do not match");
    });

    form.addEventListener("submit", function (event) {
        let isValid = true;

        isValid = validateInput(emailInput, emailError, emailPattern.test(emailInput.value), "Invalid email address") && isValid;
        isValid = validateInput(passwordInput, passwordError, passwordInput.value.trim() !== "", "Password is required") && isValid;
        isValid = validateInput(confirmPasswordInput, passwordError, passwordInput.value === confirmPasswordInput.value, "Passwords do not match") && isValid;
        if (!isValid) {
            event.preventDefault();
        }
    });

    
});