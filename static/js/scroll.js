

window.addEventListener('scroll', function () {
    var footer = document.getElementById('footer');
    var scrollPosition = window.scrollY;
    var windowHeight = window.innerHeight;
    var documentHeight = document.body.offsetHeight;

    var footerHeight = footer.offsetHeight;


    if (scrollPosition + windowHeight >= documentHeight - footerHeight) {
        footer.style.transform = 'translateY(0%)';
    } else {
        footer.style.transform = 'translateY(100%)';
    }
});


/*let menuIcon = document.getElementById("menu-icon");
let navList = document.querySelector(".nav-list");


if (window.matchMedia("(max-width: 400px)").matches) {

    menuIcon.addEventListener("click", function () {

        if (navList.classList.contains("menu-hidden")) {

            navList.classList.remove("menu-hidden");
        } else {

            navList.classList.add("menu-hidden");
        }
    });


    navList.addEventListener("mouseout", function () {

        if (!navList.classList.contains("menu-hidden")) {

            navList.classList.add("menu-hidden");
        }
    });
}

let menuIcon = document.getElementById("menu-icon");
let navList = document.querySelector(".nav-list");

navList.style.display = "none";

menuIcon.addEventListener("click", function () {
    if (navList.style.display === "none" || navList.style.display === "") {
        navList.style.display = "block";
    } else {
        navList.style.display = "none";
    }
});*/

