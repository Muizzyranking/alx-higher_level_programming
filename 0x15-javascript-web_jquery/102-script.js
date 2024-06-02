$('document').ready(function () {
  // alert(lang)
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }).fail(function(){
        alert('Error: Failed to translate');
    });
  });
});
