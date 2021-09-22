/* updates color of <header> to #FF0000 when #red_header is clicked */
$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
