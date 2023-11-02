#!/usr/bin/node
/**
  * fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from the fetch in the HTML tag DIV#hello
  * you must use JQuery
  */
$(document).ready(function() {
  // Use jQuery to fetch data from the URL
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr' 
  $.get(url, function(data) {
    const translation = data.hello;
    $('DIV#hello').text(translation);
  });
});

