$(document).ready(function () {
    $.ajax({
        type: 'POST',
        url: '/test_connection/',
        data: {'app': 'real time'},
        success: function (response) {

        }, error: function (error) {

        }
    })
});