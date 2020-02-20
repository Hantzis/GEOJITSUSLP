<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawerRight"
      app
      clipped
      right
      mobile-break-point="320"
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
                <v-row>
                <p style="margin-bottom: 0; margin-top: 16px;">Opacidad</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="slider"
                    thumb-label
                  ></v-slider>
                </v-row>
                <v-row
                  align="center"
                  justify="center"
                >
                  <v-btn-toggle>
                    <v-btn>
                      <v-icon>mdi-map</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-layers</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-phone</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-wifi</v-icon>
                    </v-btn>
                    <v-btn>
                      <v-icon>mdi-alert</v-icon>
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
        <vl-map
          :load-tiles-while-animating="true"
          :load-tiles-while-interacting="true"
          data-projection="EPSG:4326"
          style="height: 100%"
        >
          <vl-view :zoom="Number(10)" :center="Array(-101.08, 22.16)"></vl-view>

          <vl-layer-tile>
            <vl-source-xyz
              name="Google Satellite"
              url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
              :overlay="true == false"
            ></vl-source-xyz>
          </vl-layer-tile>
          <vl-layer-tile name="Open Street Map">
            <vl-source-osm></vl-source-osm>
          </vl-layer-tile>
          <vl-layer-tile>
            <vl-source-wms
              url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
              layers="PARCELASSLP:municipios"
              format="image/png"
              :overlay="true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true"
            ></vl-source-wms>
          </vl-layer-tile>
          <vl-layer-tile>
            <vl-source-wms
              url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
              layers="PARCELASSLP:ejidos"
              format="image/png"
              :overlay="true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true"
            ></vl-source-wms>
          </vl-layer-tile>
          <vl-layer-tile>
            <vl-source-wms
              url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
              layers="PARCELASSLP:parcelas"
              format="image/png"
              :overlay="true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true"
            ></vl-source-wms>
          </vl-layer-tile>
        </vl-map>
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
import Vue from "vue";
import VueLayers from "vuelayers";
import "vuelayers/lib/style.css";
//import * as olExt from "vuelayers/lib/ol-ext";

Vue.use(VueLayers);

export default {
  components: {},
  props: {
    source: String
  },
  watch: {
    model_capasbase(val) {
      console.log("model_capasbase", val);
    }
  },
  data: () => ({
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    zoom: 2,
    center: [0, 0],
    rotation: 0,
    geolocPosition: undefined,
    twoLine: false,
    threeLine: false,
    threeLtwoLinetwoLineine: true,
    nodes: [
      { title: "Item1", isLeaf: true },
      { title: "Item2", isLeaf: true, data: { visible: false } },
      { title: "Folder1" },
      {
        title: "Folder2",
        isExpanded: true,
        children: [
          { title: "Item3", isLeaf: true },
          { title: "Item4", isLeaf: true }
        ]
      }
    ],
    vmodel_capasbase: "osm",
    vmodel_layertab: "osm",
    slider: 80,
    capas_list: [
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Municipios",
        subtitle:
          "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: "Ejidos",
        subtitle:
          "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend."
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Parcelas",
        subtitle:
          "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?"
      }
    ],
    items_list: [
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Google Satellite",
        subtitle:
          "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: "Google Terrain",
        subtitle:
          "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend."
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Open Street Map",
        subtitle:
          "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?"
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Bing Maps",
        subtitle:
          "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?"
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Mapbox",
        subtitle:
          "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos."
      }
    ],
    items: [
      {
        id: 1,
        name: "Municipios",
        children: [
          { id: 2, name: "Calendar : app" },
          { id: 3, name: "Chrome : app" },
          { id: 4, name: "Webstorm : app" }
        ]
      },
      {
        id: 5,
        name: "Documents :",
        children: [
          {
            id: 6,
            name: "vuetify :",
            children: [
              {
                id: 7,
                name: "src :",
                children: [
                  { id: 8, name: "index : ts" },
                  { id: 9, name: "bootstrap : ts" }
                ]
              }
            ]
          },
          {
            id: 10,
            name: "material2 :",
            children: [
              {
                id: 11,
                name: "src :",
                children: [
                  { id: 12, name: "v-btn : ts" },
                  { id: 13, name: "v-card : ts" },
                  { id: 14, name: "v-window : ts" }
                ]
              }
            ]
          }
        ]
      },
      {
        id: 15,
        name: "Downloads :",
        children: [
          { id: 16, name: "October : pdf" },
          { id: 17, name: "November : pdf" },
          { id: 18, name: "Tutorial : html" }
        ]
      },
      {
        id: 19,
        name: "Videos :",
        children: [
          {
            id: 20,
            name: "Tutorials :",
            children: [
              { id: 21, name: "Basic layouts : mp4" },
              { id: 22, name: "Advanced techniques : mp4" },
              { id: 23, name: "All about app : dir" }
            ]
          },
          { id: 24, name: "Intro : mov" },
          { id: 25, name: "Conference introduction : avi" }
        ]
      }
    ]
  })
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
</style>
