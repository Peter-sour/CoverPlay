// JavaScript
const scrollBottom = document.querySelector('.node-scrollbottom');
const leftButton = document.getElementById('left');
const rightButton = document.getElementById('right');

// Scroll kiri
leftButton.addEventListener('click', () => {
  scrollBottom.scrollBy({
    left: -200, // Scroll ke kiri sebanyak 200px
    behavior: 'smooth' // Animasi smooth
  });
});

// Scroll kanan
rightButton.addEventListener('click', () => {
  scrollBottom.scrollBy({
    left: 200, // Scroll ke kanan sebanyak 200px
    behavior: 'smooth' // Animasi smooth
  });
});