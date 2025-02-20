const slides = document.querySelectorAll('.slide');
const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

let index = 0;

function updateSlide() {
    slider.style.transform = `translateX(-${index * 100}%)`;
}

// Next Button Click
nextBtn.addEventListener('click', () => {
    index = (index + 1) % slides.length;
    updateSlide();
});

// Previous Button Click
prevBtn.addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    updateSlide();
});

// Auto Slide Every 3 Seconds (Optional)
setInterval(() => {
    index = (index + 1) % slides.length;
    updateSlide();
}, 30000);
