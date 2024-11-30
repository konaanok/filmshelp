const urlParams = new URLSearchParams(window.location.search);
const genre = urlParams.get('genre');

// Предположим, у нас есть объект с данными о фильмах
const filmsData = {
    action: [
        { director: 'Кристофер Нолан', films: ['Начало', 'Темный рыцарь'] },
        { director: 'Майкл Бэй', films: ['Трансформеры', 'Армагеддон'] }
    ],
    comedy: [
        // Данные для комедийных фильмов
    ],
    drama: [
        // Данные для драматических фильмов
    ]
};

const directorsList = document.getElementById('directors-list');

if (!filmsData[genre]) {
    console.error(`Нет данных для жанра ${genre}`);
}

const currentGenreDirectors = filmsData[genre];
currentGenreDirectors.forEach(director => {
    let button = document.createElement('button');
    button.textContent = director.director;
    button.setAttribute('onclick', `window.location.href='films.html?genre=${genre}&director=${encodeURIComponent(director.director)}'`);
    directorsList.appendChild(button);
});
