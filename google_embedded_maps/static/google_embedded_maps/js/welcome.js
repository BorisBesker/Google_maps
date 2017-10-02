$(document).ready(function() {

    $("#genButton").click(function() {
        var text = $("iframe")[0].outerHTML;
        $('textarea').val(text);
    });

    $("select").change(function () {
        var search_mode = $( "select option:selected" ).val();
        var src_iframe = $("iframe").attr("src");
        if (search_mode === 'Place mode') {
            src_iframe = src_iframe.replace("search", "place");
        }
        if (search_mode === 'Search mode') {
            src_iframe = src_iframe.replace("place", "search");
        }
        $("iframe").attr("src", src_iframe);
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
        $("iframe").attr("src", changeMode(place));
    });

    function changeMode(place) {
        var src_iframe = $("iframe").attr("src");
        get_location = src_iframe.match(/q=(.+)/);
        src_iframe = src_iframe.replace(get_location[1], place);
        return src_iframe
    }

});
