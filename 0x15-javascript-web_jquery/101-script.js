$(document).ready(function() {
    // Add item
    $('#add_item').click(function() {
        $('ul.my_list').append('<li>Item</li>');
    });

    // Remove last item
    $('#remove_item').click(function() {
        $('ul.my_list li:last').remove();
    });

    // Clear all items
    $('#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});
