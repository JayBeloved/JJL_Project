// Auto-scroll for top pitches
let slider = document.querySelector('.slider-container');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', (e) => {
    isDown = true;
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mouseleave', () => {
    isDown = false;
});

slider.addEventListener('mouseup', () => {
    isDown = false;
});

slider.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 2;
    slider.scrollLeft = scrollLeft - walk;
});

// Auto-advance slider
setInterval(() => {
    slider.scrollBy({
        left: 300,
        behavior: 'smooth'
    });
    
    if (slider.scrollLeft >= (slider.scrollWidth - slider.clientWidth)) {
        slider.scrollTo({
            left: 0,
            behavior: 'smooth'
        });
    }
}, 5000);