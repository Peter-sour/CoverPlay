// Tombol muncul setelah scroll tertentu
// const scrollToTopButton = document.getElementById('scrollToTop');

// window.addEventListener('scroll', () => {
//   if (window.scrollY > 200) {
//     scrollToTopButton.style.display = 'block'; // Tampilkan ikon
//   } else {
//     scrollToTopButton.style.display = 'none'; // Sembunyikan ikon
//   }
// });

// // Scroll ke atas saat ikon diklik
// scrollToTopButton.addEventListener('click', () => {
//     window.scrollTo({
//       top: 0,
//       behavior: 'smooth' // Gulir halus ke atas
//     });
//   });


  const scrollToTopButton = document.getElementById('scrollToTop');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
      scrollToTopButton.style.display = 'block'; // Tampilkan ikon
    } else {
      scrollToTopButton.style.display = 'none'; // Sembunyikan ikon
    }
  });
  
  scrollToTopButton.addEventListener('click', () => {
    const scrollDuration = 500; // Durasi 2 detik
    const scrollStep = -window.scrollY / (scrollDuration / 16); // Langkah scroll tiap frame (~60fps)
    
    const interval = setInterval(() => {
      if (window.scrollY !== 0) {
        window.scrollBy(0, scrollStep); // Scroll secara bertahap
      } else {
        clearInterval(interval); // Hentikan interval saat sudah sampai di atas
      }
    }, 10); // Interval antar frame (16ms = ~60fps)
  });
  