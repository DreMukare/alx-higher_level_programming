#!/usr/bin/node
/*
    prints the number of movies with Wedge Antilles
*/

const request = require('request');

const id = '18';
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  const wedgeFilms = films.map(film => film.characters)
    .filter(arr => arr.find(str => str.search(id) !== -1));
  console.log(wedgeFilms.length);
});
