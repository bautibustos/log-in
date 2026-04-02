document.addEventListener("DOMContentLoaded", () => {

    const btnLogin = document.getElementById("btn-login");
    const alertBox = document.getElementById("alert");

    function showAlert(message, isError = true) {
        alertBox.textContent = message;
        alertBox.className   = isError ? "alert alert-error" : "alert alert-success";
        alertBox.style.display = "block";
    }

    btnLogin.addEventListener("click", async () => {
        const email    = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        console.log("Click detectado");
        console.log("Email:", email);
        console.log("Password:", password);

        if (!email || !password) {
            showAlert("Completá todos los campos.");
            return;
        }

        btnLogin.disabled    = true;
        btnLogin.textContent = "Cargando...";

        try {
            const response = await fetch("/api/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password })
            });

            console.log("Status:", response.status);

            const data = await response.json();

            console.log("Respuesta:", data);

            if (response.ok) {
                showAlert(`Bienvenido, ${data.name}!`, false);
            } else {
                showAlert(data.detail || "Error al iniciar sesión.");
            }

        } catch (error) {
            console.log("Error:", error);
            showAlert("No se pudo conectar con el servidor.");
        } finally {
            btnLogin.disabled    = false;
            btnLogin.textContent = "SIGN IN";
        }
    });

});