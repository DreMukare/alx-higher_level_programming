/* various onClick interactions */
$(() => {
  $('DIV#add_item').click(() => {
    $('UL').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('UL').children().last().remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL').empty();
  });
});
