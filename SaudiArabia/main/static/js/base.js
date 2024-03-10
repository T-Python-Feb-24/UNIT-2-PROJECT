document.getElementById('darkModeToggle').addEventListener('change', function(event){
    if(event.target.checked){
      document.documentElement.setAttribute('data-bs-theme', 'dark');
      document.getElementById("darkModeToggle").setAttribute("checked","");
    } else {
      document.documentElement.removeAttribute('data-bs-theme');
      document.getElementById("darkModeToggle").removeAttribute("checked");
    }
  });