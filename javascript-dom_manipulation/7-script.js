const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

async function displayMoviesList() {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.status);
    const { results } = await res.json();
    const listMovies = document.getElementById('list_movies');

    for (const movie of results) {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      listMovies.appendChild(movieElement)      
    }
  } catch (e) {
    console.log('Error', e)
  }
}

displayMoviesList();