function split_list(list) {
    var elements = list.children('li');
    var split = Math.floor(elements.length/2);
    var left = $('<ul class="left"></ul>'),
        right = $('<ul class="right"></ul>');
    left.append(elements.slice(0, split));
    left.insertAfter(list);
    right.append(elements.slice(split));
    right.insertAfter(list);
    list.remove();
}

$(function() {
    split_list($('ul#mainNav'));
    $('#others').click(function(event)  {
        event.preventDefault();
        $('#subNav').toggle();
    });
});
