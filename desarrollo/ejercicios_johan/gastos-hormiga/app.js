// Seleccionamos el botón de hamburguesa y el menú
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

// Agregamos el evento de clic para mostrar/ocultar el menú
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

