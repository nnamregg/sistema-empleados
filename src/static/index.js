// Clases dinámicas para links de navbar
const navLinks = document.querySelectorAll(".nav-link")
for (let link of navLinks) {
    if (link.href == window.location.href) {
       link.classList.add('active')
       link.setAttribute('aria-current','page')
    }
}

// Prompt de confirmación delete()
const btnsConfirm = document.querySelectorAll("#btnBorrar")

if (btnsConfirm.length) {
    for (const btn of btnsConfirm) {
        btn.addEventListener("click", event => {
            const resp = confirm("Esta opción no tiene marcha atrás")
            if (!resp) event.preventDefault()
        })
    }
}