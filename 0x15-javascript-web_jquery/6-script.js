/* updates text of <header> to "New Header!!!" on DIV#update_header click */
$(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
