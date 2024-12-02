// document.getElementById("myInput").addEventListener("input", function () {
//     if (this.value.length > 5) {
//         this.style.color = "green"; // Warna hijau jika panjang teks > 5
//     } else {
//         this.style.color = "blue"; // Warna biru jika panjang teks ≤ 5
//     }
// });
// document.getElementById("myInput").addEventListener("input", function () {
//     // Ubah warna teks saat mengetik
//     this.style.color = "red"; // Atau warna lain
// });

function myFunction() {
    const input = document.getElementById("myInput");
    if (input.value.length > 0) {
      // Ubah warna teks saat ada input
      input.style.color = "white";
    } else {
      // Kembalikan ke warna default jika kosong
      input.style.color = "black";
    }
  }