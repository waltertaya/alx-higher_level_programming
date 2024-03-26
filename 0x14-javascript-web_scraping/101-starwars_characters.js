// 101-starwars_characters.js

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;
    const characters = filmData.characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characters).then(names => {
      names.forEach(name => {
        console.log(name);
      });
    }).catch(error => {
      console.error('Error:', error);
    });
  }
});
