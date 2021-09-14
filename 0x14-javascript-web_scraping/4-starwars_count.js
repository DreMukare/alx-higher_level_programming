#!/usr/bin/node
/*
    prints the number of movies with Wedge Antilles
*/

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

// let count = 0;
request(url, (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  const wedgeFilms = films.map(film => film.characters)
    .filter(arr => arr.find(str => str.search('18') !== -1));
  console.log(wedgeFilms.length);
  /*
  for (const film in films) {
    for (const character in films[film].characters) {
      if (films[film].characters[character].includes(id)) {
        count++;
        break; 
      }
    }
  }
  console.log(count);
  */
});
