document.querySelector('#scroll').addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector('#contact-form').scrollIntoView({
            behavior: 'smooth'
        });
});

document.querySelector('.burger-menu').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('.list-menu-burger').classList.toggle('active');
});