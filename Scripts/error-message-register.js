document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("register-form");
    const firstNameInput = document.getElementById("first-name");
    const lastNameInput = document.getElementById("last-name");
    const phoneInput = document.getElementById("phone");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");

    const firstNameError = document.getElementById("error-first-name");
    const lastNameError = document.getElementById("error-last-name");
    const phoneError = document.getElementById("error-phone");
    const emailError = document.getElementById("error-email");
    const passwordError = document.getElementById("error-password");

    // Validation Patterns
    const phonePattern = /^01\d{9}$/;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // Function to validate input fields (for real-time validation)
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

    // First Name Validation (Real-Time)
    firstNameInput.addEventListener("input", function () {
        validateInput(firstNameInput, firstNameError, firstNameInput.value.trim() !== "", "First Name is required");
    });

    // Last Name Validation (Real-Time)
    lastNameInput.addEventListener("input", function () {
        validateInput(lastNameInput, lastNameError, lastNameInput.value.trim() !== "", "Last Name is required");
    });

    // Phone Number Validation (Live Filtering + Validation)
    phoneInput.addEventListener("input", function () {
        phoneInput.value = phoneInput.value.replace(/\D/g, ""); // Remove non-numeric characters
        validateInput(phoneInput, phoneError, phonePattern.test(phoneInput.value), "Phone number must start with 01 and be 11 digits");
    });

    // Email Validation (Real-Time)
    emailInput.addEventListener("input", function () {
        validateInput(emailInput, emailError, emailPattern.test(emailInput.value), "Invalid email address");
    });

    // Password Validation (Real-Time)
    passwordInput.addEventListener("input", function () {
        validateInput(passwordInput, passwordError, passwordInput.value.trim() !== "", "Password is required");
    });


    // Password Matching Validation (Real-Time)
    confirmPasswordInput.addEventListener("input", function (){
        validateInput(confirmPasswordInput, passwordError, passwordInput.value === confirmPasswordInput.value, "Passwords do not match");
    });

    // Prevent form submission if any field is invalid
    form.addEventListener("submit", function (event) {
        let isValid = true;

        isValid = validateInput(firstNameInput, firstNameError, firstNameInput.value.trim() !== "", "First Name is required") && isValid;
        isValid = validateInput(lastNameInput, lastNameError, lastNameInput.value.trim() !== "", "Last Name is required") && isValid;
        isValid = validateInput(phoneInput, phoneError, phonePattern.test(phoneInput.value), "Phone number must start with 01 and be 11 digits") && isValid;
        isValid = validateInput(emailInput, emailError, emailPattern.test(emailInput.value), "Invalid email address") && isValid;
        isValid = validateInput(passwordInput, passwordError, passwordInput.value.trim() !== "", "Password is required") && isValid;
        isValid = validateInput(confirmPasswordInput, passwordError, passwordInput.value === confirmPasswordInput.value, "Passwords do not match") && isValid;
        
        if (!isValid) {
            event.preventDefault();
        }
    });
});
