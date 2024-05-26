const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');  
});