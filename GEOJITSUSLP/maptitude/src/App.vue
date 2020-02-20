<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawerRight"
      app
      clipped
      right
      mobile-break-point="320"
    >
      <v-col></v-col>
      <v-container>
        <v-card class="mx-auto" max-width="400">
          <v-list
            :disabled="false"
            :dense="false"
            :two-line="false"
            :three-line="false"
            :shaped="false"
            :flat="false"
            :subheader="true"
            :sub-group="false"
            :nav="false"
            :avatar="false"
            :rounded="false"
          >
            <v-subheader><v-icon>mdi-map</v-icon> Mapas Base</v-subheader>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item
                v-for="(item, i) in items_list"
                :key="i"
                :inactive="inactive"
              >
                <v-list-item-avatar v-if="avatar">
                  <v-img :src="item.avatar"></v-img>
                </v-list-item-avatar>
                <v-radio></v-radio>
                <v-list-item-content>
                  <v-list-item-title v-html="item.title"></v-list-item-title>
                  <v-list-item-subtitle
                    v-if="twoLine || threeLine"
                    v-html="item.subtitle"
                  ></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-container>

      <v-container>
        <v-card>
          <v-list
            :disabled="false"
            :dense="false"
            :two-line="false"
            :three-line="false"
            :shaped="false"
            :flat="false"
            :subheader="true"
            :sub-group="false"
            :nav="false"
            :avatar="false"
            :rounded="false"
          >
            <v-subheader><v-icon>mdi-layers</v-icon> Capas</v-subheader>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item
                v-for="(item, i) in capas_list"
                :key="i"
                :inactive="inactive"
              >
                <v-checkbox></v-checkbox>
                <v-list-item-avatar v-if="avatar">
                  <v-img :src="item.avatar"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title v-html="item.title"></v-list-item-title>
                  <v-list-item-subtitle
                    v-if="twoLine || threeLine"
                    v-html="item.subtitle"
                  ></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>

        <v-treeview
          :items="items"
          :dense="true"
          :selectable="true"
          :activatable="true"
          :hoverable="true"
          :open-on-click="false"
          :selected-color="false"
          selection-type="independent"
          selectedColor="accent"
        ></v-treeview>
      </v-container>
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

  data: () => ({
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    zoom: 2,
    center: [0, 0],
    rotation: 0,
    geolocPosition: undefined,
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
