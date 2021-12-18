// Clases dinámicas para links de navbar
const navLinks = document.querySelectorAll(".nav-link")

for (let link of navLinks) {
    if (link.href == window.location.href) {
       link.classList.add('active')
       link.setAttribute('aria-current','page')
    }
}