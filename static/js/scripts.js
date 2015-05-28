// overide default submit action to specifiy what to do with res
$('form').submit(function() {
    /* 
    jQuery's 'post' method takes an endpoint, data,
    and optionally a success funtion that says what
    to do with returned data.
    */
    $.post('/crunch', $(this).serialize() , function(res) {
        $('#result > p').text(res);
    });

    return false; // so that form doesn't try to complete post
});