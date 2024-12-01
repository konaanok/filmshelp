const urlParams = new URLSearchParams(window.location.search);
const genre = urlParams.get("genre");

// �����������, � ��� ���� ������ � ������� � �������
const filmsData = {
  action: [
    { director: "��������� �����", films: ["������", "������ ������"] },
    { director: "����� ���", films: ["������������", "����������"] },
  ],
  comedy: [
    // ������ ��� ���������� �������
  ],
  drama: [
    // ������ ��� ������������� �������
  ],
};

const directorsList = document.getElementById("directors-list");

if (!filmsData[genre]) {
  console.error(`��� ������ ��� ����� ${genre}`);
}

const currentGenreDirectors = filmsData[genre];
currentGenreDirectors.forEach((director) => {
  let button = document.createElement("button");
  button.textContent = director.director;
  button.setAttribute(
    "onclick",
    `window.location.href='films.html?genre=${genre}&director=${encodeURIComponent(
      director.director
    )}'`
  );
  directorsList.appendChild(button);
});
