const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
const mobileNavLinks = document.querySelector('.mobile-nav ul');

mobileNavToggle.addEventListener('click', () => {
  mobileNavLinks.classList.toggle('show'); // Add/remove 'show' class
});
