$(document).ready(function() {

    //Generates the src of iFrame based on users input
    function generateSrc(mode, options) {
        let currentParams = {};
        let params = {};
        var src_iframe = $("iframe").attr("src");
        var getQueryString = src_iframe.match(/&(.+)/); // Gets querystring after APIkey
        var searchParams = new URLSearchParams(getQueryString[1]);

        // Converts querystring into js object for manipulating
        for (let key of searchParams.keys()) {
            currentParams[key] = searchParams.get(key);
        }

        mode = (mode) ? mode : getCurrentMode();

        Object.assign(currentParams, options);
        // Converts js object into string to form the URL
        params = $.param(currentParams);
        return 'https://www.google.com/maps/embed/v1/' + mode + '?key=AIzaSyDY2kqCa1Yk3_9xOICSwiX24W1avKFpvn0&' + params;
    }

    // Gets the current mode in the src iFrame if (only) place is changed
    function getCurrentMode() {
        var src_iframe = $("iframe").attr("src");
        var mode = src_iframe.substring(37, 43);
        if (mode.substring(0,5) === 'place') {
            mode = 'place'
        }
        if (mode.substring(0,5) === 'searc') {
            mode = 'search'
        }
        return mode;
    }

    $("#genButton").click(function() {
        var text = $("iframe")[0].outerHTML;
        $('textarea').val(text);
    });

    $("select").change(function () {
        var search_mode = $( "select option:selected" ).val();
        $("iframe").attr("src", generateSrc(search_mode));
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
        var options = {q: place};
        $("iframe").attr("src", generateSrc(null, {q: place}));
    });

});
