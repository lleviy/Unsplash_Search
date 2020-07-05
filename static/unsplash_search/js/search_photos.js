$(function() {
    $("#search_btn").click(function() {
        q = $("#search").val();
        if (q != '') {
            var s = 'search_photos/'
            $.get(s, {
                'q': q,
                'page': 1
            }).done(function(data) {
                var elements = $();
                $.each(data['photos_url'], function(index, value) {
                    var res = '<button type="button" src=' + value + ' onclick="document.getElementById(\'id_photo_url\').value=\'' + value + '\'"; return false;" style="background-image: url(' + value + '); background-size: cover; height: 90px; width: 160px; border: 0px;border-radius: 10px;"/> </button>'
                    elements = elements.add(res);
                })
                $('#results').html(elements);
                var link = $('#lazyLoadLink');
                link.show();
            });
        } else {

        }
    });
});


(function() {
    $('#lazyLoadLink').on('click', function() {
        var link = $(this);
        var page = link.data('page');
        page = page + 1;
        var s = 'search_photos/'
        $.get(s, {
            'q': q,
            'page': page
        }).done(function(data) {
            link.data('page', page);
            var elements = $();
            $.each(data['photos_url'], function(index, value) {
                var res = '<button type="button" src=' + value + ' onclick="document.getElementById(\'id_photo_url\').value=\'' + value + '\'"; return false;" style="background-image: url(' + value + '); background-size: cover; height: 90px; width: 160px; border: 0px;border-radius: 10px;"/> </button>'
                elements = elements.add(res);
            })
            $('#results').append(elements);
            if (elements.size() == 0) {
                link.hide();
            }
        });
    });
}(jQuery));