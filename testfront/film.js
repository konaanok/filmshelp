const urlParams = new URLSearchParams(window.location.search);
const genre = decodeURIComponent(urlParams.get('genre'));
const director = decodeURIComponent(urlParams.get('director'));

const filmsList = document.getElementById('films-list');

// Находим фильмы текущего режиссёра
const directorFilms = filmsData[genre].find(item => item.director === director).films;

directorFilms.forEach(film => {
    const link = document.createElement('a');
    link.textContent = film;
    link.href = `film.html?film=${encodeURIComponent(film)}`;
    filmsList.appendChild(link);
});
