<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawerRight"
      app
      clipped
      right
      mobile-break-point="320"
      style="width: 284px;"
    >
      <v-tabs icons-and-text v-model="vmodel_layertab">
        <v-tab href="#capas">Capas<v-icon>mdi-layers</v-icon></v-tab>
        <v-tab href="#base">Mapas Base<v-icon>mdi-map</v-icon></v-tab>
      </v-tabs>

      <v-tabs-items v-model="vmodel_layertab">
        <v-tab-item value="base">
          <!-- CARD Mapas base -->
          <v-card>
            <v-card-title style="padding-bottom: 0;">
              <v-icon>mdi-map</v-icon> Mapas Base
            </v-card-title>
            <v-card-text>
              <v-radio-group v-model="vmodel_capasbase" :mandatory="true">
                <v-radio label="Open Street Map" value="osm"></v-radio>
                <v-radio
                  label="Google Satellite"
                  value="google_satellite"
                ></v-radio>
                <v-radio
                  label="Google Terrain"
                  value="google_terrain"
                ></v-radio>
                <v-radio
                  label="Google Streets"
                  value="google_streets"
                ></v-radio>
                <v-radio label="Bing Maps" value="bing"></v-radio>
                <v-radio label="Mapbox" value="mapbox"></v-radio>
              </v-radio-group>
            </v-card-text>
          </v-card>
          <!-- /CARD Mapas base -->
        </v-tab-item>
        <v-tab-item value="capas">
          <!-- CARD Capas -->
          <v-card style="border-radius: 0px;">
            <v-card-title style="padding-bottom: 0;">
              <v-icon>mdi-layers</v-icon> Capas
            </v-card-title>
            <v-card-text> </v-card-text>
          </v-card>
          <v-expansion-panels
            style="border-radius: 0px;"
            :accordion="true"
            :multiple="true"
            :hover="true"
            :flat="true"
            :focusable="true"
          >
            <v-expansion-panel>
              <v-expansion-panel-header>Municipios</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row style="margin-top: 14px;">
                  <v-btn-toggle>
                    <v-btn color="blue-grey" class="v-button-upper">
                      <v-icon color="grey lighten-5">mdi-chevron-down</v-icon>
                    </v-btn>
                    <v-btn color="blue-grey" class="v-button-upper">
                      <v-icon color="grey lighten-5">mdi-chevron-up</v-icon>
                    </v-btn>
                    <v-btn color="red" class="v-button-upper">
                      <v-icon color="grey lighten-5">mdi-delete</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-row>
                <v-row>
                  <br />
                  <p>Descripción de la capa de municipios.</p>
                </v-row>
                <v-row>
                  <p style="margin-bottom: 0; margin-top: 16px;">Opacidad</p>
                </v-row>
                <v-row>
                  <v-slider v-model="slider" thumb-label></v-slider>
                </v-row>
                <v-row align="center" justify="center">
                  <v-btn-toggle>
                    <v-btn color="purple">
                      <v-icon color="grey lighten-5">mdi-texture</v-icon>
                    </v-btn>
                    <v-btn color="cyan">
                      <v-icon color="grey lighten-5">mdi-information</v-icon>
                    </v-btn>
                    <v-btn color="lime">
                      <v-icon color="grey lighten-5">mdi-filter</v-icon>
                    </v-btn>
                    <v-btn color="blue-grey">
                      <v-icon color="grey lighten-5">mdi-settings</v-icon>
                    </v-btn>
                    <v-btn color="blue">
                      <v-icon color="grey lighten-5">mdi-cloud-download</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-row>
                <v-divider></v-divider>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header>Ejidos</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <br />
                  <p>Descripción de la capa de municipios.</p>
                </v-row>
                <v-row>
                  <p style="margin-bottom: 0; margin-top: 16px;">Opacidad</p>
                </v-row>
                <v-row>
                  <v-slider v-model="slider" thumb-label></v-slider>
                </v-row>
                <v-row align="center" justify="center">
                  <v-btn-toggle>
                    <v-btn>
                      <v-icon>mdi-view_list</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-info</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-filter</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-settings</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-row>
                <v-divider></v-divider>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header>Parcelas</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <br />
                  <p>Descripción de la capa de municipios.</p>
                </v-row>
                <v-row>
                  <p style="margin-bottom: 0; margin-top: 16px;">Opacidad</p>
                </v-row>
                <v-row>
                  <v-slider v-model="slider" thumb-label></v-slider>
                </v-row>
                <v-row align="center" justify="center">
                  <v-btn-toggle>
                    <v-btn>
                      <v-icon>mdi-view_list</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-information</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-filter</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-settings</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-row>
                <v-divider></v-divider>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-for="(item, i) in 5" :key="i">
              <v-expansion-panel-header>Item</v-expansion-panel-header>
              <v-expansion-panel-content>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>

          <!-- /CARD Mapas base -->
        </v-tab-item>
      </v-tabs-items>
    </v-navigation-drawer>

    <v-app-bar app clipped-right color="blue-grey" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Maptitude</v-toolbar-title>
      <v-spacer />
      <v-btn
        icon
        @click.stop="drawerRight = !drawerRight"
        aria-label="Capas de datos"
      >
        <v-icon>mdi-layers</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="drawerRight = !drawerRight"
        aria-label="Capas de datos"
      >
        <v-icon>mdi-information</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app mobile-break-point="320">
      <v-list dense>
        <v-list-item click.stop="left = !left">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Draweraa</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer v-model="left" fixed temporary />

    <v-content>
      <v-container fluid fill-height class="container-map">
        <MglMap :accessToken="accessToken" :mapStyle.sync="mapStyle">
          <MglRasterLayer
            sourceId="municipios"
            layerId="municipios"
            :layer="municipios"
            :data-src="municipios"
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

export default {
  components: {
    MglMap,
    MglRasterLayer
  },
  props: {},
  watch: {
    model_capasbase(val) {
      console.log("model_capasbase", val);
    }
  },
  data: () => ({
    municipios: {
      type: "raster",
      sourceId: "municipios",
      id: "municipios",
      source: "municipios",
      url:
        "https://api.parcelas-slp.maptitude.xyz/geoserver/wms?&service=WMS&request=GetMap&layers=PARCELASSLP%3Amunicipios&styles=&format=image%2Fpng8&transparent=true&version=1.1.1&width=256&height=256&srs=EPSG%3A4326",
      tiles: [
        "https://api.parcelas-slp.maptitude.xyz/geoserver/wms?&service=WMS&request=GetMap&layers=PARCELASSLP%3Amunicipios&styles=&format=image%2Fpng8&transparent=true&version=1.1.1&width=256&height=256&srs=EPSG%3A4326"
      ],
      tileSize: 256
    },
    accessToken:
      "pk.eyJ1Ijoibml6aGlzYWViYSIsImEiOiJjanZwZXNpeWYwZDcxNDlwOXVhejg1Yno3In0.kqEaQSkVaFMpKKtx0FyNRA",
    mapbox_styles: {
      outdoors_v11: {
        name: "Outdoors",
        url: "mapbox://styles/mapbox/outdoors-v11"
      }
    },
    mapStyle: "mapbox://styles/mapbox/outdoors-v11",
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    zoom: 2,
    center: [0, 0],
    rotation: 0,
    twoLine: false,
    threeLine: false,
    vmodel_capasbase: "osm",
    vmodel_layertab: "osm",
    slider: 80
  }),
  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
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
