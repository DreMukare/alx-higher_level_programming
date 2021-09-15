#!/usr/bin/node
/*
    prints the title of a star wars movie
    given integer supposed to match episode number

*/

const request = require('request');

const num = process.argv.slice(2)[0];
const url = `https://swapi-api.hbtn.io/api/films/${num}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const output = JSON.parse(body).title;
  console.log(output);
});
