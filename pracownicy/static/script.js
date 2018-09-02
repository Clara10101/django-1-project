// using jQuery
//zabespieczenie csrf
//wystarczy dodac ten kod
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
//alert(csrftoken);
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
//kod csfr


function myFunction() {
    //wszystkie pola inputowe ukryte
    $(".ajax-save").hide();
    $(".ajax-cancel").hide();
    $("input").hide();
    $(".zespol-control").hide();
}
function edycjaPola() {
    $(".ajax-edit").click(function(){
        //znika ajax-edit a pojawia sie save i cancel
        $(this).hide();
        $(".zespol-control").show();
        $(".pracownik-zespol").hide();
        $(this).parent().children(".ajax-save").show();
        $(this).parent().children(".ajax-cancel").show();
        $(this).parent().parent().children("td").children("span").hide();
        $(this).parent().parent().children("td").children("input").show();
    });
    $(".ajax-cancel").click(function(){
        //znika cancel i save, pojawia sie edit i znika pole input
        $(this).hide();
        $(this).parent().children(".ajax-save").hide();
        $(this).parent().children(".ajax-edit").show();
        $(this).parent().parent().children("td").children("span").show();
        $(this).parent().parent().children("td").children("input").hide();
    });
    $(".ajax-save").click(function() {
        var tr = $(this).parent().parent();
        //pk zmienianego obiektu
        var pk = tr.find(".placa_pod-edit").prop("id").substring(9);
        var placa_pod = tr.find(".placa_pod-edit").val();
        var placa_dod = tr.find(".placa_dod-edit").val();
        var zespol_tab = tr.find("option:selected").val().split('-');

        //zapisanie nowej placy podstawowej i dodatkowej do bazy za pomoca ajaxa

        $.post("/ajax/ajaxZapiszPlaca/",
            {
                'pracownik': pk,
                'placa_pod': placa_pod,
                'placa_dod': placa_dod,
                'zespol': zespol_tab[1]
            },
        function(data){
            if (data == '0') {
                tr.find(".placa_pod-view").text(placa_pod);
                tr.find(".placa_dod-view").text(placa_dod);
                tr.find(".pracownik-zespol").text(zespol_tab[0]);
            } else {
                alert("An unknown error has occured");
            }
            //znika input, save, copy, pojawia sie edit
            tr.find(".placa_pod-edit, .placa_dod-edit, .ajax-save, .ajax-cancel").hide();
            tr.find(".placa_pod-view, .placa_dod-view, .ajax-edit").show();
            $(".zespol-control").hide();
            $(".pracownik-zespol").show();
        });
    });
}


function link() {
    $('.clickable-row-pracownicy').click(function() {
        var id = $(this).parent().find("input").prop("id").substring(9);
        window.location.href = "/pracownik-" + id;
});
    $('.clickable-row-etaty').click(function(){
        var id = $(this).prop("id");
        window.location.href = "/etat-" + id;
    });
    $('.clickable-row-zespoly').click(function(){
        var id = $(this).prop("id");
        window.location.href = "/zespol-" + id;
    });
    $('.clickable-row-all-pracownicy').click(function(){
        var id = $(this).prop("id");
        window.location.href = "/pracownik-" + id;
    });
    $('.clickable-row-all-zespoly').click(function(){
        var id = $(this).prop("id");
        window.location.href = "/zespol-" + id;
    });
    $('.clickable-row-all-etaty').click(function(){
        var id = $(this).prop("id");
        window.location.href = "/etat-" + id;
    });
}

$(document).ready(myFunction);
$(document).ready(edycjaPola);
$(document).ready(link);
