window.onscroll = function() {
    let navbar = document.getElementById("navbar");
    if (window.scrollY > 50) { // Bisa disesuaikan untuk menentukan kapan warna berubah
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  };
  