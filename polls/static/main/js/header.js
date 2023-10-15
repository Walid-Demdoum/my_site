$( document ).ready(function() {
    console.log( "ready!" );
});

$(document).ready(function() {
    const headerE1 = document.getElementById("header");
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            console.log(headerE1);
            headerE1.classList.add('navbar-scrolled');
        } else if (window.scrollY < 50) {
            headerE1.classList.remove('navbar-scrolled');
        }
    });
});