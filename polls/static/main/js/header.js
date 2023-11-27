document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            document.getElementById("header").classList.add('navbar-scrolled');
        } else if (window.scrollY < 50) {
            document.getElementById("header").classList.remove('navbar-scrolled');
        }
    });
});

function search_bar_toggle(){
    document.getElementById("search-bar").classList.toggle('hidden');
}