/* fetches and displays translation of hello from link */
$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (res) => {
    $('DIV#hello').text(res.hello);
    console.log(res);
  });
});
