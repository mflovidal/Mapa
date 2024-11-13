var map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: -1,
    maxZoom: 2,
});
var bounds = [[0,0], [1000,1000]];
var basemap = L.imageOverlay('static/imagenes del mapa/Piso uno.png', bounds);
var secondLayer = L.imageOverlay('static/imagenes del mapa/Piso dos.png', bounds);
var thirdLayer = L.imageOverlay('static/imagenes del mapa/Piso menos uno.png', bounds);

basemap.addTo(map);
map.fitBounds(bounds);

var imageLayers = {
    "Piso Uno": basemap,
    "Piso Dos": secondLayer,
    "Piso Menos Uno": thirdLayer,
};

L.control.layers(imageLayers).addTo(map);

document.addEventListener("DOMContentLoaded", function() {
    const closeButton = document.getElementById("close-info-panel");
    const infoPanel = document.getElementById("info-panel");
    closeButton.addEventListener("click", function() {
        infoPanel.style.display = "none";
    });
});

const areas = [
    {coords: [[50,250], [150,350]], key: 'Hemeroteca'},
    {coords: [[200,200], [300,300]], key: 'Periódicos y Microformatos'}, 
    {coords: [[500,600], [650,750]], key: ' Sala José Toribio Medina'}, 
    {coords: [[300,450], [400,550]], key: 'Archivo de Música'}, 
    {coords: [[50,750], [200,950]], key: 'Archivo del Escritor'}, 
    {coords: [[800,950], [700,850]], key: 'Fondo General'}, 
    {coords: [[150,600], [250,700]], key: 'Referencias y Bibliografía'}, 
    {coords: [[750,50], [650,200]], key: 'Salón de investigadores'}, 
    {coords: [[600,50], [500,200]], key: 'Sección Chilena'}, 
    {coords: [[900,50], [800,200]], key: 'Departamento de Conservación'}, 
    {coords: [[900,250], [800,400]], key: 'Extensión Cultural'}, 
    {coords: [[900,450], [800,600]], key: 'Departamento de Procesos Técnicos'}, 
    {coords: [[900,650], [800,800]], key: 'Depósito Legal'}, 
]
 areas.forEach((area) => {
    const [coord1,coord2] = area.coords;
    const bounds = [coord1,coord2]
    const rectangle = L.rectangle(bounds, {color:"#ff7800", weight:1}).addTo(map)
    rectangle.on('click', function() {
        const translation = translations[area.key];
        document.getElementById('area-title').innerText = translation.title;
        document.getElementById('area-info').innerText = translation.info;
        document.getElementById('info-panel').style.display = 'block'; 
        
    });
 });