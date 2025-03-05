document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");
    const togglePassword = document.getElementById("toggle-password");
    const togglePassword2 = document.getElementById("toggle-password2");
    const hidePassword = document.getElementById("hide-password");
    const hidePassword2 = document.getElementById("hide-password2");

    //Toggle password visibility first input
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

    //confirmepassword second input
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