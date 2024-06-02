$('document').ready(function() {
    let add_item = $('#add_item');
    let remove_item = $('#remove_item');
    let clear_list = $('#clear_list');
    let list = $('.my_list');
    let item = "<li>Item</li>"

    add_item.click(function() {
        list.append(item);
    });
    remove_item.click(function() {
        list.children().last().remove();
    });
    clear_list.click(function(){
        list.children().remove();
    })
    
});
