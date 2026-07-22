document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.getElementById("mainNav");

    // Listen for scroll events on the window
    window.addEventListener("scroll", function() {
        if (window.scrollY > 50) {
            // User scrolled down -> add solid background & shrink
            navbar.classList.add("scrolled");
        } else {
            // User is at the top -> make transparent again
            navbar.classList.remove("scrolled");
        }
    });

    // year for the footer.updates automatically!
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});
