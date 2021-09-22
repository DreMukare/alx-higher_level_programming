/* fetches and lists all movie titles */
$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (res) => {
    res.results.forEach((obj) => {
      $('UL#list_movies').append('<li>' + obj.title + '</li>');
    });
  });
});
