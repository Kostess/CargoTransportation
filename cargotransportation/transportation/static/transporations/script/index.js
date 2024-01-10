document.querySelector('.burger-menu').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('.list-menu-burger').classList.toggle('active');
});