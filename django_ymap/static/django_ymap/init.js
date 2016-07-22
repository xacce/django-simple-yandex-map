(function ($) {
    $(function () {

        var i = 0;
        $('.ymap_field').each(function () {
            var input = $(this);

            var ymap_div = $('<div style="float:left"></div>').attr('id', 'ymap_' + i);
            input.data('ymap_div', ymap_div);

            q = ymap_div.insertAfter(input);
            q.css({'width': parseInt(input.attr('data-size_width')), 'height': parseInt(input.attr('data-size_height'))});
            init_map(input);
            i++;
        })
    })
})(django.jQuery);

function init_map(input) {
    ymaps.ready(function () {

        var map = new ymaps.Map(input.data('ymap_div').attr('id'), {
            center: [41, 82],
            zoom: 13,
            controls: ['zoomControl', 'typeSelector', 'rulerControl']
        });

        var searchControl = new ymaps.control.SearchControl({
            options: {
                noPlacemark: true
            }
        });

        map.controls.add(searchControl);

        map.events.add('click', function (e) {
            var coords = e.get('coords');
            django_ymap_change_mark(input, coords)

        });

        input.data("ymap", map);
        if (input.val().length < 1) {
            django_ymap_set_center_by_query(input.attr('data-start_query'), map)
        }
        else {
            var currcord = input.val().split(',');
            currcord = [parseFloat(currcord[0]), parseFloat(currcord[1])];
            django_ymap_set_center_by_coords(currcord, map);
            django_ymap_change_mark(input, currcord);
        }
    });

}

function django_ymap_set_center_by_coords(coords, map) {

    map.zoomRange.get(coords).then(function (range) {
        map.setCenter(coords, range[13])
    })
}

function django_ymap_change_mark(input, coords, title) {
    console.log(coords);
    var mark = input.data('ymap_mark');
    var map = input.data('ymap');
    if (mark) map.geoObjects.remove(mark);

    mark = new ymaps.Placemark(coords, {'hintContent': title});
    map.geoObjects.add(mark);
    input.data('ymap_mark', mark);

    input.attr('value', coords.join(','))
}

function django_ymap_set_center_by_query(query, map) {

    ymaps.geocode(query, { results: 1 }).then(function (res) {

        var coords = res.geoObjects.get(0).geometry.getCoordinates();
        var firstGeoObject = res.geoObjects.get(0);
        map.setBounds(firstGeoObject.properties.get('boundedBy'));
    });
}
