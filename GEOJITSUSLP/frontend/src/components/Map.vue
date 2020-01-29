<template>
  <div id="mapid" class="map"></div>
</template>

<script>
import L from "leaflet";
//import {LMap, LTileLayer, LMarker} from 'vue2-leaflet'

export default {
  name: "Map",
  mounted: () => {
    const mymap = L.map("mapid").setView([51.505, -0.09], 13);
    L.tileLayer("http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", {
      subdomains: ["mt0", "mt1", "mt2", "mt3"],
      maxZoom: 18,
      // language=HTML
      attribution: `Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors,
                    <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a
                    href="https://www.mapbox.com/">Mapbox</a>`,
      id: "mapbox/streets-v11"
    }).addTo(mymap);
  }
};
</script>

<style scoped>
.map {
  height: 100%;
  width: 100%;
  z-index: 0;
}
</style>
