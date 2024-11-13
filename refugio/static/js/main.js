const sliderLine = document.querySelector(".top-content"),
      pagination = document.querySelectorAll(".top__pagination-item"),
      nav = document.querySelector(".header__menu"),
      header = document.querySelector(".header"),
      headerBtn = document.querySelector(".header__btn"),
      link = document.querySelectorAll(".header__menu-list"),
      logo = document.querySelector(".header-img"),
      burger = document.querySelector(".header__burger"),
      aboutImg = document.querySelector(".about-img"),
      popupImg = document.querySelector(".popup-img"),
      body = document.body,
      wrapper = document.querySelector(".wrapper"),
      main = document.querySelector(".main"),
      footer = document.querySelector(".footer"),
      pay = document.querySelector(".pay"),
      blogBtns = document.querySelectorAll(".blog__more-btn"),
      blogVideo = document.querySelectorAll(".blog-video"),
      blogItems = document.querySelectorAll(".blog__more-item"),
      html = document.querySelector("HTML"),
      popup = document.querySelector(".popup"),
      topLines = document.querySelectorAll(".top-line"),
      contactBtn = document.querySelector("#my-form-button"),
      contactInputs = document.querySelectorAll(".contact-input");

// Carousel
if (sliderLine && pagination.length > 0) {
    let offset = 0;
    paginationShow();

    const rightArrow = document.querySelector(".top-arrow-right");
    const leftArrow = document.querySelector(".top-arrow-left");

    if (rightArrow) {
        rightArrow.addEventListener("click", () => {
            offset += 100;
            if (offset > 300) {
                offset = 0;
            };
            sliderLine.style.left = -offset + "%";
            paginationShow();
        });
    }

    if (leftArrow) {
        leftArrow.addEventListener("click", () => {
            offset -= 100;
            if (offset < 0) {
                offset = 300;
            };
            sliderLine.style.left = -offset + "%";
            paginationShow();
        });
    }

    function paginationShow() {
        pagination.forEach(pag => {
            if (+pag.getAttribute('data-page') == (offset / 100)) {
                pag.classList.add("top__pagination-item--active");
                topLines.forEach((line, i) => {
                    line.classList.toggle("active", line.getAttribute('data-offset') == +pag.getAttribute('data-page') * 100);
                });
            } else {
                pag.classList.remove("top__pagination-item--active");
            };
        });
    };

    pagination.forEach(circle => {
        circle.addEventListener("click", () => {
            pagination.forEach(el => el.classList.remove("top__pagination-item--active"));
            offset = circle.getAttribute('data-page') * 100;
            circle.classList.add("top__pagination-item--active");
            sliderLine.style.left = -offset + "%";
            paginationShow();
        });
    });
}

// Burger menu
if (burger && logo && header && nav && headerBtn && link.length > 0) {
    burger.addEventListener("click", () => {
        burger.classList.toggle("active");
        logo.classList.toggle("active");
        header.classList.toggle("active");
        nav.classList.toggle("active");
        headerBtn.classList.toggle("disactive");
        sectionsToggle(disableArray);
    });

    link.forEach(li => {
        li.addEventListener("click", () => {
            burger.classList.remove("active");
            logo.classList.remove("active");
            header.classList.remove("active");
            nav.classList.remove("active");
            headerBtn.classList.remove("disactive");
            sectionsOn(disableArray);
        });
    });
}

// Events
if (aboutImg && popup && popupImg) {
    aboutImg.addEventListener("click", (e) => {
        popupImg.src = e.target.src;
        popup.classList.add("active");
        html.classList.add("unscroll");
    });

    popup.addEventListener("click", () => {
        popup.classList.remove("active");
        html.classList.remove("unscroll");
    });
}

// Popups
if (headerBtn && pay) {
    headerBtn.addEventListener("click", () => {
        sectionsOff(disableArray);
        pay.classList.add("active");
    });
}

// Scroll animation
const animItems = document.querySelectorAll(".anim-items");
if (animItems.length > 0) {
    window.addEventListener("scroll", animOnScroll);
    function animOnScroll() {
        animItems.forEach(animItem => {
            const animItemHeight = animItem.offsetHeight;
            const animItemOffset = getHeight(animItem).top;
            const animStart = 8;
            let animItemPoint = window.innerHeight - animItemHeight / animStart;

            if (animItemHeight > window.innerHeight) {
                animItemPoint = window.innerHeight - window.innerHeight / animStart;
            }

            if ((scrollY > animItemOffset - animItemPoint) && scrollY < (animItemOffset + animItemHeight)) {
                animItem.classList.add("_active");
            } else if (!animItem.classList.contains("_anim-no-hide")) {
                animItem.classList.remove("_active");
            }
        });
    }
    
    function getHeight(el) {
        const rect = el.getBoundingClientRect(),
              scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        return { top: rect.top + scrollTop };
    }

    animOnScroll();
}

// Button animation
if (headerBtn) {
    btnAnimation(headerBtn);
    function btnAnimation(element) {
        element.addEventListener("mousemove", (e) => {
            const x = e.pageX - element.offsetLeft;
            const y = e.pageY - element.offsetTop;
            element.style.setProperty("--x", x + "px");
            element.style.setProperty("--y", y + "px");
        });
    }
}

// Video button
if (blogBtns.length > 0 && blogVideo.length > 0 && blogItems.length > 0) {
    blogBtns.forEach((btn, index) => {
        btn.addEventListener("click", (e) => {
            const isPlaying = !blogVideo[index].paused && !blogVideo[index].ended;
            if (!isPlaying) {
                blogVideo[index].play();
                e.target.classList.replace("play", "pause");
                blogBtns[index].src = "./images/blog/pause.svg";
            } else {
                blogVideo[index].pause();
                e.target.classList.replace("pause", "play");
                blogBtns[index].src = "./images/blog/play.svg";
            }
        });
    });

    blogItems.forEach((video, index) => {
        video.addEventListener("mouseleave", () => {
            blogBtns[index].classList.add("disactive");
        });
        video.addEventListener("mouseenter", () => {
            blogBtns[index].classList.remove("disactive");
        });
    });

    blogVideo.forEach(video => video.volume = 0.3);
}

// Sections toggle functions
let disableArray = [".about", ".main", ".footer"];

function sectionsOff(array) {
    array.forEach(el => {
        const element = document.querySelector(el);
        if (element) element.classList.add("disactive");
    });
}

function sectionsOn(array) {
    array.forEach(el => {
        const element = document.querySelector(el);
        if (element) element.classList.remove("disactive");
    });
}

function sectionsToggle(array) {
    array.forEach(el => {
        const element = document.querySelector(el);
        if (element) element.classList.toggle("disactive");
    });
}

// Lazy loading
const lazyImages = document.querySelectorAll("img[data-src], source[data-srcset], div[data-src]");
const windowHeight = document.documentElement.clientHeight;

let lazyImagesPosition = [];
if (lazyImages.length > 0) {
    lazyImages.forEach(img => {
        if (img.dataset.src || img.dataset.srcset) {
            lazyImagesPosition.push(img.getBoundingClientRect().top + scrollY - 250);
            lazyScrollCheck();
        }
    });
}

window.addEventListener("scroll", lazyScroll);

function lazyScroll() {
    if (document.querySelectorAll("img[data-src], source[data-srcset]").length > 0) {
        lazyScrollCheck();
    }
}

function lazyScrollCheck() {
    let imgIndex = lazyImagesPosition.findIndex(item => scrollY > item - windowHeight);
    if (imgIndex >= 0) {
        if (lazyImages[imgIndex].dataset.src) {
            lazyImages[imgIndex].src = lazyImages[imgIndex].dataset.src;
            lazyImages[imgIndex].removeAttribute("data-src");
        } else if (lazyImages[imgIndex].dataset.srcset) {
            lazyImages[imgIndex].srcset = lazyImages[imgIndex].dataset.srcset;
            lazyImages[imgIndex].removeAttribute("data-srcset");
        }
        delete lazyImagesPosition[imgIndex];
    }
}

function getMap() {
	const loadMapBlockPos = contactMap.getBoundingClientRect().top + scrollY;
	if (scrollY > loadMapBlockPos - windowHeight) {
		console.log();
		const loadMapUrl = contactMap.dataset.map;
		console.log(loadMapUrl);
		if (loadMapUrl) {
			contactMap.insertAdjacentHTML("beforeend", `<iframe class="contact-iframe" src="${loadMapUrl}"></iframe>`)
		};
		contactMap.classList.add("_loaded")
	};
};

// /lazy loading