/* fetches character name from url and displays in DIV#character */
$(() => {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (res) => {
    $('DIV#character').text(res.name);
  });
});
