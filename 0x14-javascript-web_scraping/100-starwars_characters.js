#!/usr/bin/node
/*
  prints all characters of a star wars movie
*/

const request = require('request');

const id = process.argv.slice(2)[0];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  for (const x in characters) {
    request(characters[x], (err, res, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
});
