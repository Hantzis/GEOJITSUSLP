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
        <!-- <v-list-item @click.stop="overright = !overright"> -->
        <v-list-item>
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Open Temporary Drawer</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
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

      <v-btn icon aria-label="Buscar">
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon aria-label="Mensajes">
        <v-icon>mdi-email-outline</v-icon>
      </v-btn>

      <v-btn icon aria-label="Notificaciones">
        <v-icon>mdi-bell</v-icon>
      </v-btn>

      <v-btn
        icon
        @click.stop="drawerRight = !drawerRight"
        aria-label="Capas de datos"
      >
        <v-icon>mdi-layers</v-icon>
      </v-btn>

      <v-menu left bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on" aria-label="Menú de capas">
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
        <!-- <v-list-item @click.stop="overleft = !overleft"> -->
        <v-list-item>
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Menú de opciones</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer v-model="overleft" fixed temporary />
    <v-content>
      <v-container fluid fill-height class="container-map">
        <l-map
          ref="map"
          :zoom="zoom"
          :center="center"
          style="z-index: 0"
          @click="getFeatureInfo"
        >
          <l-tile-layer
            name="Google Satellite"
            url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
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
            v-for="layer in layers"
            :key="layer.name"
            :name="layer.name"
            :baseUrl="layer.baseUrl"
            :layers="layer.layers"
            layer-type="overlay"
            :format="layer.format"
            :transparent="layer.transparent"
            :visible="layer.visible"
            :options="layer.options"
          />
          <l-control-layers />
        </l-map>
        <v-speed-dial
          v-model="fab"
          :top="top"
          :bottom="bottom"
          :right="right"
          :left="left"
          :direction="direction"
          :open-on-hover="hover"
          :transition="transition"
        >
          <template v-slot:activator>
            <v-btn v-model="fab" color="blue darken-2" dark fab>
              <v-icon v-if="fab">mdi-close</v-icon>
              <v-icon v-else>mdi-plus</v-icon>
            </v-btn>
          </template>
          <v-btn
            fab
            dark
            small
            color="green"
            @click.stop="
              dialog_green = true;
              fab = false;
            "
          >
            <v-icon>mdi-layers</v-icon>
          </v-btn>
          <v-btn fab dark small color="indigo">
            <v-icon>mdi-layers</v-icon>
          </v-btn>
          <v-btn fab dark small color="purple">
            <v-icon>mdi-layers</v-icon>
          </v-btn>
          <v-btn
            fab
            dark
            small
            color="red"
            @click="layers = layers.slice(0, 3)"
          >
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-speed-dial>
      </v-container>
    </v-content>

    <v-navigation-drawer v-model="overright" fixed right temporary />

    <v-footer app class="white--text" color="blue-grey">
      <span>Maptitude XYZ</span><v-spacer /><span>&copy; 2020 GeoJitsu</span>
    </v-footer>

    <v-dialog v-model="dialog_green">
      <v-card>
        <v-card-title class="headline"
          >Agregar capa filtrada de parcelas</v-card-title
        >

        <v-card-text>
          Seleccione el criterio de busqueda para mostrar solo los objetos que
          lo cumplan, como una capa nueva.
          <v-form ref="green-form" v-model="greenvalid" :lazy="lazy">
            <v-select
              v-model="select"
              :items="items"
              rules="[v => !!v || 'Item is required']"
              label="Nombre"
              required
            />
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog_green = false">
            Cancelar
          </v-btn>

          <v-btn color="green darken-1" text @click="putNewLayer('green')">
            Agregar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
    // eslint-disable-next-line vue/no-unused-components
    LGeoJson,
    LWMSTileLayer,
    // eslint-disable-next-line vue/no-unused-components
    LPopup
  },
  props: {
    source: String
  },
  data: () => ({
    loading: null,
    drawer: false,
    drawerRight: false,
    overright: false,
    overleft: false,
    zoom: 10,
    lazy: false,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    // eslint-disable-next-line no-undef
    center: L.latLng(22.16, -101.08),
    attribution: `&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors`,
    municipios: null,
    ejidos: null,
    parcelas: null,
    layers: [
      {
        name: "Municipios",
        layers: "PARCELASSLP:municipios",
        baseUrl:
          "https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?",
        format: "image/png8",
        srs: "EPSG:4326",
        transparent: true,
        visible: true
      },
      {
        name: "Ejidos",
        layers: "PARCELASSLP:ejidos",
        baseUrl:
          "https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?",
        format: "image/png8",
        srs: "EPSG:4326",
        transparent: true,
        visible: false
      },
      {
        name: "Parcelas",
        layers: "PARCELASSLP:parcelas",
        baseUrl:
          "https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?",
        format: "image/png8",
        srs: "EPSG:4326",
        transparent: true,
        visible: false
      }
    ],
    direction: "top",
    fab: false,
    fling: false,
    hover: false,
    tabs: null,
    top: false,
    right: false,
    bottom: true,
    left: true,
    transition: "slide-y-reverse-transition",
    dialog_green: false
  }),
  methods: {
    putNewLayer(layer) {
      console.log(layer);
      this.dialog_green = false;
      const new_layer = {
        name: "Conafor",
        layers: "PARCELASSLP:parcelas",
        baseUrl:
          "http://api.parcelas-slp.maptitude.xyz:8080/geoserver/PARCELASSLP/wms?",
        format: "image/png8",
        srs: "EPSG:4326",
        transparent: true,
        visible: true,
        CQL_FILTER: "programa='Conafor'",
        options: { CQL_FILTER: "programa='Conafor'" }
      };
      this.layers.push(new_layer);
      console.log(this.layers);
    },
    getVisibleLayers() {
      let activas = [];
      for (let layer of Object.entries(this.$refs.map.mapObject._layers)) {
        if (layer[1].wmsParams) {
          activas.push(layer[1]);
        }
      }
      return activas;
    },
    getFeatureInfoUrls(latlng) {
      const point = this.$refs.map.mapObject.latLngToContainerPoint(latlng);
      const size = this.$refs.map.mapObject.getSize();
      const visible_layers = this.getVisibleLayers();
      let urls = [];
      if (visible_layers.length > 0) {
        for (let layer of visible_layers) {
          let srs = "EPSG:4326";
          for (let conflayer of this.layers) {
            if (conflayer.layers === layer.wmsParams.layers)
              srs = conflayer.srs;
          }
          let params = {
            request: "GetFeatureInfo",
            service: "WMS",
            srs: srs,
            format: layer.wmsParams.format,
            bbox: this.$refs.map.mapObject.getBounds().toBBoxString(),
            height: size.y,
            width: size.x,
            layers: layer.wmsParams.layers,
            query_layers: layer.wmsParams.layers,
            info_format: "text/html",
            styles: layer.styles || ""
          };
          params[params.version === "1.3.0" ? "i" : "x"] = point.x;
          params[params.version === "1.3.0" ? "j" : "y"] = point.y;
          const url = [layer._url] + new URLSearchParams(params);
          urls.push(url);
        }
      }
      return urls;
    },
    getFeatureInfo(evt) {
      const urls = this.getFeatureInfoUrls(evt.latlng);
      // eslint-disable-next-line no-undef
      const popup = L.popup();
      let cuerpo = "";
      for (let url of urls) {
        axios
          .get(url)
          .then(response => {
            if (response.data.length > 658) {
              cuerpo += response.data;
            }
          })
          .then(() => {
            if (cuerpo.length > 0) {
              popup
                .setLatLng(evt.latlng)
                .setContent(cuerpo)
                .openOn(this.$refs.map.mapObject);
            }
          });
      }
    }
  },
  computed: {
    activeFab() {
      switch (this.tabs) {
        case "one":
          return { class: "purple", icon: "account_circle" };
        case "two":
          return { class: "red", icon: "edit" };
        case "three":
          return { class: "green", icon: "keyboard_arrow_up" };
        default:
          return {};
      }
    }
  },
  watch: {
    top(val) {
      this.bottom = !val;
    },
    right(val) {
      this.left = !val;
    },
    bottom(val) {
      this.top = !val;
    },
    left(val) {
      this.right = !val;
    }
  },
  created() {
    this.loading = true;
  },
  mounted() {
    this.loading = false;
  }
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

.v-speed-dial--bottom {
  bottom: 72px;
}
</style>
