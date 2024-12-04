var map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: -1,
    maxZoom: 2,
});
var bounds = [[0,0], [1620,1750]];
var basemap = L.imageOverlay('static/imagenes del mapa/Piso uno.png', bounds);
var secondLayer = L.imageOverlay('static/imagenes del mapa/Piso dos.png', bounds);
var thirdLayer = L.imageOverlay('static/imagenes del mapa/Piso menos uno.png', bounds);

basemap.addTo(map);
map.fitBounds(bounds);
var imageLayers = {
    "1": basemap,
    "2": secondLayer,
    "-1": thirdLayer,
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
    {coords: [[244,1243], [490,1443]], key: 'Hemeroteca', piso: '1'},
    {coords: [[679,620], [1090,1200]], key: 'Periódicos y Microformatos', piso:'-1'}, 
    {coords: [[68,685], [185,1078]], key: ' Sala José Toribio Medina', piso:'2'}, 
    {coords: [[497,333], [245,539]], key: 'Archivo de Música', piso:'1'}, 
    {coords: [[275,334], [535,540]], key: 'Archivo del Escritor', piso:'2'}, 
    {coords: [[1295,332], [1467,553]], key: 'Fondo General', piso:'2'}, 
    {coords: [[1288,335], [1466,710]], key: 'Referencias y Bibliografía', piso:'1'}, 
    {coords: [[272,1244], [538,1438]], key: 'Salón de investigadores', piso:'2'}, 
    {coords: [[1295,1190], [1467,1444]], key: 'Sección Chilena', piso:'2'}, 
    //{coords: [[900,50], [800,200]], key: 'Departamento de Conservación', piso:'1'}, 
    //{coords: [[900,250], [800,400]], key: 'Extensión Cultural', piso:'2'}, 
    //{coords: [[900,450], [800,600]], key: 'Departamento de Procesos Técnicos', piso:'-1'}, 
    //{coords: [[900,650], [800,800]], key: 'Depósito Legal', piso:'-1'}, 
]
const textocasillas = [
    //{textocoords:[100,300], key:'Archivo de Música', piso: '1'},
    //{textocoords:[100,300], key:'Unidad Ediciones Biblioteca Nacional', piso: '1'},
    //{textocoords:[150,300], key:'Archivo de Láminas y Estampas', piso: '1'},
    {textocoords:[85,508], key:'Préstamos a Domicilio', piso: '1'},
    //{textocoords:[250,300], key:'Oficina de Partes', piso: '1'},
    //{textocoords:[300,300], key:'Hemeroteca', piso: '1'},
    //{textocoords:[350,300], key:'Extensión Cultural', piso: '1'},
    //{textocoords:[400,300], key:'Departamento de Atención de Usuarios', piso: '1'},
    //{textocoords:[400,600], key:'Archivo de Referencias Críticas', piso: '1'},
    {textocoords:[545,565], key:'Sección Mapoteca', piso: '1'},
    {textocoords:[545,1210], key:'Galería de Cristal', piso: '1'},
    {textocoords:[838,918], key:'Salón Marta Cruz-Coke', piso: '1'},
    //{textocoords:[650,300], key:'Acceso Catálogo en Línea', piso: '1'},
    {textocoords:[1355,520], key:'Referencias y Bibliografía', piso: '1'},
    //{textocoords:[700,300], key:'Librería Biblioteca Nacional', piso: '1'},
    {textocoords:[1355,1190], key:'Sala América', piso: '1'},
    //{textocoords:[350,275], key:'Archivo del Escritor', piso: '2'},
    //{textocoords:[100,500], key:'Dirección Biblioteca Nacional', piso: '2'},
    {textocoords:[120,500], key:'Sala Ercilla', piso: '2'},
    {textocoords:[108,881], key:' Sala José Toribio Medina', piso: '2'},
    //{textocoords:[500,500], key:'Salón de investigadores', piso: '2'},
    {textocoords:[125,1345], key:'Centro de Investigaciones Barros Arana', piso: '2'},
    {textocoords:[1356,890], key:'Salón Gabriela Mistral', piso: '2'},
    {textocoords:[1356,443], key:'Fondo General', piso: '2'},
    {textocoords:[1356,1315], key:'Sección Chilena', piso: '2'},
    //{textocoords:[200,700], key:'Seguridad', piso: '-1'},
    //{textocoords:[250,700], key:'Departamento de Sistemas de Información Bibliográficas', piso: '-1'},
    //{textocoords:[350,700], key:'Departamento de Procesos Técnicos', piso: '-1'},
    //{textocoords:[400,700], key:'Depósito Legal', piso: '-1'},
    //{textocoords:[450,700], key:'Oficina de Gestión y Desarrollo', piso: '-1'},
    {textocoords:[845,915], key:'Periódicos y Microformatos', piso: '-1'},
]
var capasAreas = [];
function actualizarAreas(piso) {
    capasAreas.forEach(area => map.removeLayer(area));
    capasAreas = [];
    areas.filter(area => area.piso === piso).forEach(area => {
        const bounds = area.coords;
        const rectangle = L.rectangle(bounds, {
            color:"#ff7800", 
            weight:1,
        }).addTo(map);
        rectangle.bringToFront();
        rectangle.on('click', function(){
            const translation = translations[area.key];
            document.getElementById('area-title').innerText = translation.title;
            document.getElementById('area-info').innerText = translation.info;
            document.getElementById('info-panel').style.display = 'block';           
        });
        capasAreas.push(rectangle);       
    });
}
map.on('baselayerchange', function(event) {
    const pisoSeleccionado = event.name;
    casillatexto(pisoSeleccionado);
    actualizarAreas(pisoSeleccionado);
    casillatexto_rotado(pisoSeleccionado);    
});

var capasTexto = [];
function casillatexto(piso) {
    capasTexto.forEach(casilla => map.removeLayer(casilla));
    capasTexto = []
    textocasillas.filter(casilla => casilla.piso === piso).forEach(casilla => {
        const texto = translationstexto[casilla.key].nombrecasilla;
        const tooltip = L.tooltip({ permanent: true, className: 'etiqueta-texto', direction: 'center', offset: [0, -10], opacity: 1 })
            .setLatLng(casilla.textocoords)
            .setContent(texto)
            .addTo(map);
        capasTexto.push(tooltip);
    });
}
var capasTexto_rotado = []
const texto_rotado = [
    {textorotadocoords:[345,445], key:'Archivo de Música', piso: '1'},
    {textorotadocoords:[335,1343], key:'Hemeroteca', piso: '1'},
    {textorotadocoords:[380,445], key:'Archivo del Escritor', piso: '2'},
    {textorotadocoords:[390,1345], key:'Salón de investigadores', piso: '2'},
    //{textorotadocoords:[225,250], key:'Dirección Biblioteca Nacional', piso: '2'},

]
function casillatexto_rotado(piso) {
    capasTexto_rotado.forEach(casilla => map.removeLayer(casilla));
    capasTexto_rotado = []
    texto_rotado.filter(casilla => casilla.piso === piso).forEach(casilla => {
        const texto = translationstexto[casilla.key].nombrecasilla;
        const tooltip = L.tooltip({ permanent: true, className: 'etiqueta-texto-rotado', direction: 'center', offset: [0, -10], opacity: 1 })
            .setLatLng(casilla.textorotadocoords)
            .setContent(texto)
            .addTo(map);
        capasTexto_rotado.push(tooltip);
    });    
}
casillatexto("1");
actualizarAreas("1");
casillatexto_rotado("1");