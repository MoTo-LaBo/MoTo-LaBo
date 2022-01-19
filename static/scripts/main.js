// ------- identity scroll animation -------
// const targetElement = document.querySelectorAll("#animationTarget");
// console.log("画面の高さ", window.innerHeight)
// document.addEventListener("scroll", function() {
//     for (let i = 0; i < targetElement.length; i++) {
//         const getElementDistance = targetElement[i].
//         getBoundingClientRect().top + targetElement[i].clientHeight * .4
//         if (window.innerHeight > getElementDistance) {
//             targetElement[i].classList.add("show");
//         }
//     }
// })

// ---------- mobile menu ----------
class MobileMenu {
    constructor() {
        this.DOM = {};
        this.DOM.btn = document.querySelector('.mobile-menu_btn');
        this.DOM.container = document.querySelector('#global-container');
        this.eventType = this._getEventType();
        this._addEvent();
    }

    _getEventType() {
        const isTouchCapable =
          "ontouchstart" in window ||
          (window.DocumentTouch && document instanceof window.DocumentTouch) ||
          navigator.maxTouchPoints > 0 ||
          window.navigator.msMaxTouchPoints > 0;

        return isTouchCapable ? "touchstart" : "click";
      }

    _toggle() {
        this.DOM.container.classList.toggle('menu-open');
    }

    _addEvent() {
        this.DOM.btn.addEventListener('click', this._toggle.bind(this));
    }
}

new MobileMenu();
