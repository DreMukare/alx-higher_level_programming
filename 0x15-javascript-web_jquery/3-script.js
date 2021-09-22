/* adds class red to <header> when #red_header is clicked */
$(() => {
  $('DIV#red_header').click(() => {
    $('header').addClass('red');
  });
});
