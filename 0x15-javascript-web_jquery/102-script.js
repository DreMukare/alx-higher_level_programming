/* says hello depending on the language */
$(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, (res) => {
      $('DIV#hello').text(res.hello);
    });
  });
});
