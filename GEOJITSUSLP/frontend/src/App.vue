<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawerRight"
      app
      clipped
      right
      mobile-break-point="320"
    >
      <v-list dense>
        <v-list-item @click.stop="right = !right">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Drawer</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click.stop="right = !right">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Drawer 2</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-right color="blue-grey" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Parcelas SLP</v-toolbar-title>
      <v-spacer />

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-email-outline</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>

      <v-btn icon @click.stop="drawerRight = !drawerRight">
        <v-icon>mdi-layers</v-icon>
      </v-btn>

      <v-menu left bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="n in 5" :key="n" @click="() => {}">
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
          <v-list-item @click="() => {}">
            <v-list-item-title>Menú opción</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      color="blue-grey lighten-5"
      app
      mobile-break-point="320"
    >
      <v-list dense>
        <v-list-item @click.stop="left = !left">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Drawer</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer v-model="left" fixed temporary />

    <v-content>
      <v-container fluid fill-height class="container-map">
        <l-map
          :zoom="zoom"
          :center="center"
          style="z-index: 0"
          @click="get_coordenadas"
        >
          <l-tile-layer
            name="Google Satellite"
            :url="url"
            attribution="Google Maps"
            layer-type="base"
          />
          <l-tile-layer
            name="Open Street Map"
            url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
            attribution="OpenStreetMap"
            layer-type="base"
          />
          <l-w-m-s-tile-layer
            name="Municipios"
            baseUrl="https://api.parcelas-slp.maptitude.xyz/geoserver/PARCELASSLP/ows?"
            layers="municipios"
            layer-type="overlay"
            format="image/png"
          >
            <l-popup></l-popup>
          </l-w-m-s-tile-layer>
          <l-geo-json
            name="Ejidos"
            :geojson="ejidos"
            attribution="INEGI"
            layer-type="overlay"
          />
          <l-control-layers />
        </l-map>
      </v-container>
    </v-content>

    <v-navigation-drawer v-model="right" fixed right temporary />

    <v-footer app class="white--text" color="blue-grey">
      <span>Maptitude XYZ</span>
      <v-spacer />
      <span>&copy; 2020 GeoJitsu</span>
    </v-footer>
  </v-app>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LControlLayers,
  LGeoJson,
  LWMSTileLayer,
  LPopup
} from "vue2-leaflet";
import axios from "axios";

export default {
  name: "App",
  components: {
    LMap,
    LTileLayer,
    LControlLayers,
    LGeoJson,
    LWMSTileLayer,
    LPopup
  },
  props: {
    source: String
  },
  data: () => ({
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    zoom: 10,
    // eslint-disable-next-line no-undef
    center: L.latLng(22.16, -101.08),
    url: "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attribution: `&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors`,
    // eslint-disable-next-line no-undef
    municipios: null,
    parcelas: null,
    ejidos: null
  }),
  methods: {
    get_coordenadas(evt) {
      console.log(evt);
      let coord = evt.latlng;
      let lat = coord.lat;
      let lng = coord.lng;
      console.log(
        "You clicked the map at latitude: " + lat + " and longitude: " + lng
      );
    }
  },
  mounted() {
    this.loading = true;
    axios
      .get("https://api.parcelas-slp.maptitude.xyz/rest/v2/municipios/")
      .then(response => {
        this.municipios = response.data;
        this.loading = false;
      });
    axios
      .get("https://api.parcelas-slp.maptitude.xyz/rest/v2/ejidos/")
      .then(response => {
        this.ejidos = response.data;
        this.loading = false;
      });
    axios
      .get("https://api.parcelas-slp.maptitude.xyz/rest/v2/parcelas/")
      .then(response => {
        this.parcelas = response.data;
        this.loading = false;
      });
  }
};
</script>

<style scoped>
.container-map {
  padding: 0;
}

.white--text {
}
</style>
