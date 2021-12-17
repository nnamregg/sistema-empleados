const btnsConfirm = document.querySelectorAll("#btnBorrar")

if (btnsConfirm.length) {
    for (const btn of btnsConfirm) {
        btn.addEventListener("click", event => {
            const resp = confirm("Esta opción no tiene marcha atrás")
            if (!resp) event.preventDefault()
        })
    }
}
