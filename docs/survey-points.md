---
title: Survey Points
---
# Survey Points

<!-- https://stackoverflow.com/questions/15829048/best-way-to-import-coordinates-from-gpx-file-and-display-using-google-maps-api -->

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<div id="map" style="height:525px; width:525px;"></div>
<script>
function initMap() {
    var spainsHall = new google.maps.LatLng(51.970927,0.4396255);
    var mapOptions = {
        center: spainsHall,
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    $.ajax({
        type: "GET",
        url: "https://raw.githubusercontent.com/joejcollins/atlanta-shore/master/data/raw/spains-hall-waypoints-regular-30m.gpx",
        dataType: "xml",
        success: function (xml) {
            var points = [];
            var bounds = new google.maps.LatLngBounds();
            $(xml).find("wpt").each(function () {
                    var lat = $(this).attr("lat");
                    var lon = $(this).attr("lon");
                    var position = new google.maps.LatLng(lat, lon);
                    var label = $(this).text()
                    marker = new google.maps.Marker({
                        position: position,
                        label: label,
                        map: map
                    });
                    bounds.extend(position);
            });
            map.fitBounds(bounds);
        }
    });
}
</script>
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBHCMGq3m39ZUjAw6FbBqZ2L_I9JHGHO2c&callback=initMap"></script>