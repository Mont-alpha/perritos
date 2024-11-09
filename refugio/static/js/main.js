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
	cardBtn = document.querySelector("#card-btn"),
	cardAboutBtn = document.querySelector(".card__about-btn"),
	cardClose = document.querySelector(".card-close"),
	card = document.querySelector(".card"),
	payClose = document.querySelector(".pay-close"),
	html = document.querySelector("HTML"),
	popup = document.querySelector(".popup"),
	topLines = document.querySelectorAll(".top-line"),
	cardAboutButton = document.querySelector(".card__about-btn"),
	contactBtn = document.querySelector("#my-form-button"),
	contactInputs = document.querySelectorAll(".contact-input");

// carousel

let offset = 0;
paginationShow();

document.querySelector(".top-arrow-right").addEventListener("click", () => {
	offset += 100;
	if (offset > 300) {
		offset = 0;
	};
	sliderLine.style.left = -offset + "%";
	paginationShow();
});

document.querySelector(".top-arrow-left").addEventListener("click", () => {
	offset -= 100;
	if (offset < 0) {
		offset = 300;
	};
	sliderLine.style.left = -offset + "%";
	paginationShow();
});

function paginationShow() {
	pagination.forEach(pag => {
		if (+pag.getAttribute('data-page') == (offset / 100)) {
			pag.classList.add("top__pagination-item--active");
			for (let i = 0;i < topLines.length;i++) {
				if (topLines[i].getAttribute('data-offset') == +pag.getAttribute('data-page') * 100) {
					topLines.forEach(line => {
						line.classList.remove("active")
					})
					topLines[i].classList.add("active");
				}
			}
		}
		else {
			pag.classList.remove("top__pagination-item--active");
		};
	});
};

pagination.forEach(circle => {
	circle.addEventListener("click", () => {
		pagination.forEach(el => {
			el.classList.remove("top__pagination-item--active");
		});
		offset = circle.getAttribute('data-page') * 100;
		circle.classList.add("top__pagination-item--active");
		sliderLine.style.left = -offset + "%";
		paginationShow()
	});
});

// /carousel

// burger

burger.addEventListener("click", () => {
	burger.classList.toggle("active");
	logo.classList.toggle("active");
	header.classList.toggle("active");
	nav.classList.toggle("active");
	headerBtn.classList.toggle("disactive");
	sectionsToggle(disableArray)
});

link.forEach(li => {
	li.addEventListener("click", () => {
		burger.classList.remove("active");
		logo.classList.remove("active");
		header.classList.remove("active");
		nav.classList.remove("active");
		headerBtn.classList.remove("disactive");
		sectionsOn(disableArray)
	});
});

// /burger

// Events

aboutImg.addEventListener("click", (e) => {
	popupImg.src = e.target.src;
	popup.classList.add("active");
	html.classList.add("unscroll");
});

popup.addEventListener("click", () => {
	popup.classList.remove("active");
	html.classList.remove("unscroll");
});

// /Events

// popups

headerBtn.addEventListener("click", () => {
	sectionsOff(disableArray);
	pay.classList.add("active");
});

payClose.addEventListener("click", () => {
	sectionsOn(disableArray);
	pay.classList.remove("active");
	card.classList.remove("active");
});

cardBtn.addEventListener("click", () => {
	pay.classList.remove("active");
	card.classList.add("active");
});

cardClose.addEventListener("click", () => {
	sectionsOn(disableArray);
	header.classList.remove("popup");
	main.classList.remove("popup");
	footer.classList.remove("popup");
	pay.classList.remove("active");
	card.classList.remove("active");
});

cardAboutBtn.addEventListener("click", (e) => {
	paymentAppear()
	card.classList.remove("active")
	sectionsOn(disableArray)
})

// /popups

// scroll animation

const animItems = document.querySelectorAll(".anim-items");

if (animItems.length > 0) {
	window.addEventListener("scroll", animOnScroll);
	function animOnScroll() {
		for (let index = 0;index < animItems.length;index++) {
			const animItem = animItems[index];
			const animItemHeight = animItem.offsetHeight;
			const animItemOffset = getHeight(animItem).top;
			const animStart = 8;
			let animItemPoint = window.innerHeight - animItemHeight / animStart;
			if (animItemHeight > window.innerHeight) {
				animItemPoint = window.innerHeight - window.innerHeight / animStart;
			};
			if ((scrollY > animItemOffset - animItemPoint) && scrollY < (animItemOffset + animItemHeight)) {
				animItem.classList.add("_active");
			} else {
				if (!animItem.classList.contains("_anim-no-hide")) {
					animItem.classList.remove("_active");
				};
			};
		};
	};
	function getHeight(el) {
		const rect = el.getBoundingClientRect(),
			scrollTop = window.pageYOffset || document.documentElement.scrollTop;
		return { top: rect.top + scrollTop };
	};
	animOnScroll();
};

// /scroll animation

// button animation

function btnAnimation(element) {
	element.addEventListener("mousemove", (e) => {
		const x = e.pageX - element.offsetLeft;
		const y = e.pageY - element.offsetTop;

		element.style.setProperty("--x", x + "px");
		element.style.setProperty("--y", y + "px");
	});
}

btnAnimation(headerBtn);
btnAnimation(cardAboutBtn);

// /button animation

// video button

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
		};
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

blogVideo.forEach(volumeOf => {
	volumeOf.volume = 0.3
})

// /video button

// languages



// disable

let disableArray = [".about", ".main", ".footer"];

function sectionsOff(array) {
	array.forEach(el => {
		document.querySelector(el).classList.add("disactive");
	});
};

function sectionsOn(array) {
	array.forEach(el => {
		document.querySelector(el).classList.remove("disactive");
	});
};

function sectionsToggle(array) {
	array.forEach(el => {
		document.querySelector(el).classList.toggle("disactive");
	});
};

// disable 



// titl mobile fix

if (window.innerWidth < 1024) {
	const aboutBox = document.querySelector(".about__inner");

	let mobile = document.createElement('div');
	mobile.classList.add('about__img');
	mobile.innerHTML = '<img data-src="./images/about/about-1.webp" src="./images/lazy.png" alt="about images" class="about-img anim-items mobile">';

	aboutBox.removeChild(aboutBox.firstElementChild);
	aboutBox.insertBefore(mobile, aboutBox.firstElementChild);

	const aboutImg = document.querySelector(".about-img");

	aboutImg.addEventListener("click", openImage)

	function openImage() {
		window.open("./images/about/about-1.webp");
	};
};

// /titl mobile fix

// input validation

const inputToValidate = [16, 2, 4, 3, 10];
const cardInputs = document.querySelectorAll(".card__input");

for (let i = 0;i < inputToValidate.length;i++) {
	const currentInput = cardInputs[i];
	currentInput.addEventListener("input", (e) => {
		let input = e.target.value;
		if (input.length > inputToValidate[i]) {
			input = input.slice(0, inputToValidate[i]);
			currentInput.value = input;
		};
	});
};
// /input validation

// forms spree

let form = document.querySelector(".contact-form");

async function handleSubmit(event) {
	event.preventDefault();
	var data = new FormData(event.target);
	fetch(event.target.action, {
		method: form.method,
		body: data,
		headers: {
			'Accept': 'application/json'
		}
	}).then(response => {
		if (response.ok && contactInputs[0].value.match(nameEx) && contactInputs[1].value.match(phoneEx) && contactInputs[2].value.match(emailEx)) {
			paymentAppear()
			contactInputs.forEach(input => input.classList.remove("error"));
			form.reset()
		} else {
			console.log("error");
			contactInputs.forEach(input => input.classList.add("error"));
		}
	}).catch(error => {
		contactInputs.forEach(input => {
			input.classList.add("error");
		});
	});
};
form.addEventListener("submit", handleSubmit);

contactInputs.forEach(inp => {
	inp.addEventListener("input", () => {
		contactInputs.forEach(el => {
			el.classList.remove("error");
		});
	});
});

let nameEx = /^[^\d]\w+$/gm;
let phoneEx = /^(\+?38[ -]?)?\(?(0\d{2}|\d{3})\)?[ -]?(\d{2}[ -]?\d{2}?[ -]?\d{3})$/gm;
let emailEx = /^[^\d]\w+@\w+\.\w+$/gm;

function paymentAppear() {
	payment.classList.add("active");
	html.classList.add("unscroll");
	paymentImage.classList.add("active");
	if (payment.classList.contains("active")) {
		setTimeout(() => {
			paymentImage.classList.remove("active");
			html.classList.remove("unscroll");
			payment.classList.remove("active");
		}, 2500);
	};
};

// /forms spree

// google maps

contactMap.addEventListener("mouseenter", () => {
	contactMap.classList.add("active")
});

contactMap.addEventListener("mouseleave", () => {
	contactMap.classList.remove("active")
});

// /google maps

// lazy loading

const lazyImages = document.querySelectorAll("img[data-src], source[data-srcset], div[data-src]");
const windowHeight = document.documentElement.clientHeight;

let lazyImagesPosition = [];
if (lazyImages.length > 0) {
	lazyImages.forEach(img => {
		if (img.dataset.src || img.dataset.srcset || div.dataset.src) {
			lazyImagesPosition.push(img.getBoundingClientRect().top + scrollY - 250);
			lazyScrollCheck()
		};
	});
};

window.addEventListener("scroll", lazyScroll)

function lazyScroll() {
	if (document.querySelectorAll("img[data-src], source[data-srcset]").length > 0) {
		lazyScrollCheck();
	};
	if (!contactMap.classList.contains("_loaded")) {
		getMap()
	};
};

function lazyScrollCheck() {
	let imgIndex = lazyImagesPosition.findIndex(item => scrollY > item - windowHeight);
	if (imgIndex >= 0) {
		if (lazyImages[imgIndex].dataset.src) {
			lazyImages[imgIndex].src = lazyImages[imgIndex].dataset.src;
			lazyImages[imgIndex].removeAttribute("data-src");
		} else if (lazyImages[imgIndex].dataset.srcset) {
			lazyImages[imgIndex].srcset = lazyImages[imgIndex].dataset.srcset;
			lazyImages[imgIndex].removeAttribute("data-srcset");
		};
		delete lazyImagesPosition[imgIndex];
	};
};

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