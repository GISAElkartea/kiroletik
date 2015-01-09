function split_list(list) {
    var elements = list.children('li');
    var split = Math.floor(elements.length/2);
    var left = $('<ul class="left"></ul>'),
        right = $('<ul class="right"></ul>');
    left.append(elements.slice(0, split));
    right.append(elements.slice(split));
    right.insertAfter(list);
    left.insertAfter(list);
    list.remove();
}

$(function() {
    split_list($('ul#mainNav'));
    $('#others > a').click(function(event)  {
        event.preventDefault();
        $('#subNav').toggleClass('active');
    });
});
