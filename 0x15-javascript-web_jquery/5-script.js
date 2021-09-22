/* adds <li> items to UL.my_list everytime DIV#add_item is clicked */
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>item</li>');
  });
});
