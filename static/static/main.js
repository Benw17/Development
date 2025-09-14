document.addEventListener("DOMContentLoaded", function() {

    /* Blur content on navbar toggle */
    if (document.getElementById("navbar-toggler")) {
        const navbarContent = document.getElementById("navbarContent");
        const pageContent = document.getElementById("pageContent");
        const icon = document.getElementById('dd-i');

        navbarContent.addEventListener("show.bs.collapse", () => {
            pageContent.classList.add("blurred");
            icon.classList.remove('bi-caret-down-fill');
            icon.classList.add('bi-caret-up-fill');
        });

        navbarContent.addEventListener("hide.bs.collapse", () => {
            pageContent.classList.remove("blurred");
            icon.classList.add('bi-caret-down-fill');
            icon.classList.remove('bi-caret-up-fill');
        });

        document.querySelectorAll("#navbarContent .nav-link").forEach(link => {
            link.addEventListener("click", () => {
                pageContent.classList.remove("blurred");
            });
        });  
    }
});
