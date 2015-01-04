$(function() {
    var items = $('#mainNav > li');
    var split = Math.floor(items.length/2);
    items.slice(0, split).addClass('left');
    items.slice(split).addClass('right');
});
