#!/usr/bin/node

const axios = require('axios');

function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  axios.get(apiUrl)
    .then(response => {
      const charactersUrls = response.data.characters;

      charactersUrls.forEach(characterUrl => {
        axios.get(characterUrl)
          .then(characterResponse => {
            console.log(characterResponse.data.name);
          })
          .catch(error => {
            console.error(`Failed to retrieve character data. Error: ${error.message}`);
          });
      });
    })
    .catch(error => {
      console.error(`Failed to retrieve movie data. Error: ${error.message}`);
    });
}

if (process.argv.length !== 3) {
  console.error('Usage: node starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
