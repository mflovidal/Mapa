var map = L.map('map', {
    crs: L.CRS.Simple
});
var bounds = [[0,0], [1000,1000]];
var image = L.imageOverlay('static/imagenes del mapa/Piso uno.png', bounds)
image.addTo(map)



map.fitBounds(bounds);