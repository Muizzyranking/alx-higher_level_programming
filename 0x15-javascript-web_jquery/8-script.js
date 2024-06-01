$(document).ready(function () {
  var list = $('#list_movies');
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (
    data
  ) {
    $.each(data.results, function (_, movie) {
      list.append('<li>' + movie.title + '</li>');
    });
  });
});
