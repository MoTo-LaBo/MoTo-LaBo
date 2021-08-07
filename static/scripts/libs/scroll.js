// ------- identity scroll animation -------
const targetElement = document.querySelectorAll("#animationTarget");
console.log("画面の高さ", window.innerHeight)
document.addEventListener("scroll", function() {
    for (let i = 0; i < targetElement.length; i++) {
        const getElementDistance = targetElement[i].
        getBoundingClientRect().top + targetElement[i].clientHeight * .4
        if (window.innerHeight > getElementDistance) {
            targetElement[i].classList.add("show");
        }
    }
})
