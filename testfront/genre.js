document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.genres button');

    buttons.forEach(button => {
        button.addEventListener('click', event => {
            const genre = event.target.getAttribute('data-genre');
            window.location.href = `directors.html`;
        });
    });
