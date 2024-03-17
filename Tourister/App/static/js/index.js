const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
  if (body.getAttribute('data-bs-theme') === 'dark') {
    console.log("sss");
      body.removeAttribute('data-bs-theme');
  } else {
      body.setAttribute('data-bs-theme', 'dark');
  }
});