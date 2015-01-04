function splitmark_elements(elements) {
    var split = Math.floor(elements.length/2);
    elements.slice(0, split).addClass('left');
    elements.slice(split).addClass('right');
}

$(function() {
    splitmark_elements($('#mainNav > li'));
    $('#others').click(function(event)  {
        event.preventDefault();
        $('#subNav').toggle();
    });
});
