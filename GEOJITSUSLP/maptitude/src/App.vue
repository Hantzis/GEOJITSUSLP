<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawerRight" app clipped right>
      <v-list dense>
        <v-list-item click.stop="right = !right">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Drawer</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-right color="blue-grey" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Toolbar</v-toolbar-title>
      <v-spacer />
      <v-app-bar-nav-icon @click.stop="drawerRight = !drawerRight" />
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app>
      <v-list dense>
        <v-list-item click.stop="left = !left">
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
        <vl-map
          :load-tiles-while-animating="true"
          :load-tiles-while-interacting="true"
          data-projection="EPSG:4326"
          style="height: 100%"
        >
          <vl-view
            :zoom="Number(10)"
            :center="VueLayers.core.projHelper.fromLonLat([-101.08, 22.16])"
          ></vl-view>

          <vl-layer-tile>
            <vl-source-xyz
              url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
            ></vl-source-xyz>
          </vl-layer-tile>
          <vl-layer-tile id="osm">
            <vl-source-osm></vl-source-osm>
          </vl-layer-tile>
          <vl-source-wms
            url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
            layers="PARCELASSLP:municipios"
          ></vl-source-wms>
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

Vue.use(VueLayers);

export default {
  props: {
    source: String
    a = VueLayers.core.
  },

  data: () => ({
    drawer: false,
    drawerRight: false,
    right: false,
    left: false,
    zoom: 2,
    center: [0, 0],
    rotation: 0,
    geolocPosition: undefined
  })
};
</script>

<style scoped>
.container-map {
  padding: 0;
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
