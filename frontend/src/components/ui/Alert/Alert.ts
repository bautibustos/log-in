// alert.ts
export function showAlert(message: string, isError: boolean = true) {
    const alertBox = document.getElementById("mb-alert") as HTMLDivElement;
    alertBox.textContent   = message;
    alertBox.className     = "mb-alert " + (isError ? "error" : "success");
    alertBox.style.display = "block";
}

// Uso:
//showAlert("El correo no existe.");           // error en rojo
//showAlert("Código enviado.", false);          // éxito en verde