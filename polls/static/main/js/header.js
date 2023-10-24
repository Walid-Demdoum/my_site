document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            console.log(document.getElementById("header"));
            document.getElementById("header").classList.add('navbar-scrolled');
        } else if (window.scrollY < 50) {
            document.getElementById("header").classList.remove('navbar-scrolled');
        }
    });
});

function search_bar_toglle(){
    console.log(document.getElementById('search-bar'));
    document.getElementById("search-bar").classList.add('hidden');
}