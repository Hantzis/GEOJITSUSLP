<template>
  <v-app id="inspire">
    <!-- Menú de capas -->
    <v-navigation-drawer
      v-model="drawerRight"
      app
      clipped
      right
      mobile-break-point="320"
      style="width: 284px;"
    >
      <v-tabs icons-and-text :show-arrows="true" grow v-model="vmodel_layertab">
        <v-tab href="#capas">Capas<v-icon>mdi-layers</v-icon></v-tab>
        <v-tab href="#base">Mapas Base<v-icon>mdi-map</v-icon></v-tab>
        <v-tab href="#servidores">
          Servidores WMS<v-icon>mdi-network</v-icon>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="vmodel_layertab">
        <v-tab-item value="capas">
          <!-- CARD Capas -->
          <v-card style="border-radius: 0;">
            <v-card-title style="padding-bottom: 0;">
              <v-row>
                <v-col> <v-icon>mdi-layers</v-icon>Capas</v-col>
                <v-col align="right">
                  <v-btn fab small color="green" style="margin-right: 14px;"
                    ><v-icon color="white">mdi-plus</v-icon></v-btn
                  >
                </v-col>
              </v-row>
            </v-card-title>
          </v-card>
          <map-layer :layers="layers"></map-layer>

          <!-- /CARD Mapas base -->
        </v-tab-item>
        <v-tab-item value="base">
          <!-- CARD Mapas base -->
          <v-card>
            <v-card-title style="padding-bottom: 0;">
              <v-icon>mdi-map</v-icon> Mapas Base
            </v-card-title>
            <v-card-text>
              <v-radio-group v-model="vmodel_capasbase" :mandatory="true">
                <v-radio
                  v-for="(value, key) in mapbox_styles"
                  v-bind:value="key"
                  v-bind:key="key"
                  v-bind:label="value.name"
                  @change="set_style(value.url)"
                />
              </v-radio-group>
            </v-card-text>
          </v-card>
          <!-- /CARD Mapas base -->
        </v-tab-item>
        <v-tab-item value="servidores">
          <!-- CARD Servidores -->
          <map-server :servers="servers"></map-server>
          <!-- /CARD Servidores -->
        </v-tab-item>
      </v-tabs-items>
    </v-navigation-drawer>
    <!-- / Menú de capas -->
    <v-app-bar app clipped-right color="blue-grey" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Maptitude XYZ</v-toolbar-title>
      <v-spacer />
      <v-btn
        icon
        @click.stop="drawerRight = !drawerRight"
        aria-label="Capas de datos"
      >
        <v-icon>mdi-layers</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-information</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app mobile-break-point="320">
      <v-list dense>
        <v-list-item click.stop="left = !left">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Menú de opciones</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer v-model="left" fixed temporary />

    <v-content>
      <v-container fluid fill-height class="container-map">
        <MglMap
          :accessToken="accessToken"
          :mapStyle.sync="mapStyle"
          :zoom.sync="map_zoom"
          :center.sync="map_center"
        >
          <MglRasterLayer
            :sourceId="municipios_lyr.source.id"
            :layerId="municipios_lyr.id"
            :source.sync="municipios_lyr.source"
            :layer.sync="municipios_lyr"
          ></MglRasterLayer>
        </MglMap>
      </v-container>
    </v-content>

    <v-navigation-drawer v-model="right" fixed right temporary />

    <v-footer app color="blue-grey" class="white--text">
      <span>Maptitude XYZ</span>
      <v-spacer />
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
import "@mdi/font/css/materialdesignicons.css";
import "mapbox-gl/dist/mapbox-gl.css";
import Mapbox from "mapbox-gl";
import { MglMap, MglRasterLayer } from "vue-mapbox";
import MapLayer from "./components/MapLayer";
import MapServer from "./components/MapServer";
import axios from "axios";

export default {
  components: {
    MglMap,
    MglRasterLayer,
    MapLayer,
    MapServer
  },
  props: {},
  watch: {
    vmodel_capasbase() {
      console.log("vmodel_capasbase");
    }
  },
  data: () => ({
    municipios_lyr: {
      id: "municipios layer",
      source: {
        id: "municipios id",
        type: "raster",
        tiles: [
          "https://api.parcelas-slp.maptitude.xyz/geoserver/wms?&service=WMS&request=GetMap&layers=SLP%3Amunicipios&styles=&format=image%2Fpng8&transparent=true&version=1.1.1&width=256&height=256&srs=EPSG%3A3857&bbox={bbox-epsg-3857}"
        ],
        tileSize: 256
      },
      paint: {
        "raster-opacity": 1.0
      }
    },
    servers_url: "https://api.parcelas-slp.maptitude.xyz/rest/v2/wms-servers/",
    layers_url: "https://api.parcelas-slp.maptitude.xyz/rest/v2/wms-layers/",
    servers: [],
    layers: [],
    municipios: {
      type: "raster",
      sourceId: "municipios",
      id: "municipios",
      source: "municipios",
      tiles: [
        "https://api.parcelas-slp.maptitude.xyz/geoserver/wms?&service=WMS&request=GetMap&layers=PARCELASSLP%3Amunicipios&styles=&format=image%2Fpng8&transparent=true&version=1.1.1&width=256&height=256&srs=EPSG%3A4326&bbox={bbox-epsg-4326}"
      ],
      tileSize: 256
    },
    accessToken:
      "pk.eyJ1Ijoibml6aGlzYWViYSIsImEiOiJjanZwZXNpeWYwZDcxNDlwOXVhejg1Yno3In0.kqEaQSkVaFMpKKtx0FyNRA",
    mapbox_styles: {
      outdoors_v11: {
        name: "Outdoors",
        url: "mapbox://styles/mapbox/outdoors-v11"
      },
      streets_v11: {
        name: "Streets",
        url: "mapbox://styles/mapbox/streets-v11"
      },
      light_v10: {
        name: "Light",
        url: "mapbox://styles/mapbox/light-v10"
      },
      dark_v10: {
        name: "Dark",
        url: "mapbox://styles/mapbox/dark-v10"
      },
      satellite_v9: {
        name: "Satellite",
        url: "mapbox://styles/mapbox/satellite-v9"
      },
      satellite_streets_v11: {
        name: "Satellite Streets",
        url: "mapbox://styles/mapbox/satellite-streets-v11"
      }
    },
    mapStyle: "mapbox://styles/mapbox/outdoors-v11",
    map_center: Array(-100.96, 22.16),
    map_zoom: 10,
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    vmodel_capasbase: "vmodel_capasbase",
    vmodel_layertab: "layers",
    vmodel_layericontabs: null,
    slider: 80
  }),
  methods: {
    set_style(val) {
      this.mapStyle = val;
    },
    testa(val) {
      alert(val);
    }
  },
  computed: {},
  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
  },
  mounted() {
    axios.get(this.servers_url).then(response => {
      this.servers = response.data;
    });
    axios.get(this.layers_url).then(response => {
      this.layers = response.data;
    });
  }
};
</script>

<style scoped>
.container-map {
  padding: 0;
  margin-bottom: -7px;
}

.white--text {
}

/* This is for documentation purposes and will not be needed in your application */
#create .v-speed-dial {
  position: absolute;
}

#create .v-btn--floating {
  position: relative;
}

.v-speed-dial--bottomG {
  bottom: 72px;
}

.v-button-upper {
  height: 28px;
  min-height: 28px;
  min-width: 28px;
  width: 28px;
}
</style>
