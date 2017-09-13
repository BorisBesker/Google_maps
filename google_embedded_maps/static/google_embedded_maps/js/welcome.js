$(document).ready(function() {

    $("#genButton").click(function() {
        var text = $("iframe").attr('src');
        $('textarea').val(text);
    });

    $("#copyButton").click(function() {
        $('textarea').select();
        document.execCommand('copy');
    });

    $("#locationTextField").keydown(function(e) {
        if (e.keyCode == 13) {
            $('#searchButton').click();
        }
    });

    $("#searchButton").click(function() {
        var place = $("#locationTextField").val();
        var src_iframe = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDY2kqCa1Yk3_9xOICSwiX24W1avKFpvn0&q=';

        src_iframe = src_iframe + place;
        $("iframe").attr("src", src_iframe);
    });

});
