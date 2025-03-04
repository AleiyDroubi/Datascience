document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("forgot-form");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");
    const togglePassword = document.getElementById("toggle-password");
    const togglePassword2 = document.getElementById("toggle-password2");
    const hidePassword = document.getElementById("hide-password");
    const hidePassword2 = document.getElementById("hide-password2");

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

    //Toggle password visibility
    togglePassword.addEventListener("click", function () {
        passwordInput.type = "password";
        togglePassword.style.display = "none";
        hidePassword.style.display = "inline-block";

        confirmPasswordInput.type = "password";
        togglePassword2.style.display = "none";
        hidePassword2.style.display = "inline-block";
    });

    hidePassword.addEventListener("click", function () {
        passwordInput.type = "text";
        hidePassword.style.display = "none";
        togglePassword.style.display = "inline-block";

        confirmPasswordInput.type = "text";
        hidePassword2.style.display = "none";
        togglePassword2.style.display = "inline-block";
    });

    //confirmepassword 
    togglePassword2.addEventListener("click", function () {
        confirmPasswordInput.type = "password";
        togglePassword2.style.display = "none";
        hidePassword2.style.display = "inline-block";
    });

    hidePassword2.addEventListener("click", function () {
        confirmPasswordInput.type = "text";
        hidePassword2.style.display = "none";
        togglePassword2.style.display = "inline-block";
    });
});