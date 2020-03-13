<template>
  <div>
    <v-card style="border-radius: 0;">
      <v-card-title style="padding-bottom: 0;">
        <v-row>
          <v-col><v-icon>mdi-layers</v-icon>Capas</v-col>
          <v-col align="right">
            <v-btn
              fab
              small
              color="green"
              @click.stop="add_new_layer_dialog()"
              style="margin-right: 14px; margin-bottom: 14px;"
            >
              <v-icon color="white">mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-title>
    </v-card>
    <v-expansion-panels
      style="border-radius: 0;"
      :accordion="true"
      :multiple="true"
      :hover="true"
      :flat="true"
      :focusable="true"
    >
      <v-expansion-panel v-for="(item, i) in this.layers" :key="i">
        <v-expansion-panel-header>{{
          item.layer_name
        }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row justify="space-between" align="start">
            <v-col pa-0>
              <v-row justify="start">
                <v-switch
                  style="margin-top: 0; bottom: 0;"
                  v-model="item.layer_enabled"
                ></v-switch>
              </v-row>
            </v-col>
            <v-col pa-0>
              <v-row justify="end">
                <v-btn-toggle no-toggle>
                  <v-btn
                    color="blue-grey"
                    style="height: 28px; width: 28px; min-width: 28px;"
                    :disabled="i === 0"
                  >
                    <v-icon color="grey lighten-5">mdi-chevron-up</v-icon>
                  </v-btn>
                  <v-btn
                    color="blue-grey"
                    style="height: 28px; width: 28px; min-width: 28px;"
                    :disabled="i === layers.length - 1"
                  >
                    <v-icon color="grey lighten-5">mdi-chevron-down</v-icon>
                  </v-btn>
                  <v-btn
                    color="red"
                    style="height: 28px; width: 28px; min-width: 28px;"
                    :disabled="item.layer_permanent"
                  >
                    <v-icon color="grey lighten-5">mdi-delete</v-icon>
                  </v-btn>
                </v-btn-toggle>
              </v-row>
            </v-col>
          </v-row>
          <v-row style="margin-top: -20px;">
            <v-card class="mx-auto" max-width="245">
              <v-img
                class="black--text align-end text--secondary"
                height="137px"
                width="245px"
                :src="get_layer_thumb(item)"
                aspect-ratio="1.7"
              >
                <v-card-title
                  ><v-slider
                    v-model="item.layer_opacity"
                    thumb-label
                    track-fill-color="black"
                    track-color="red"
                    :hide-details="true"
                  />
                </v-card-title>
              </v-img>
              <v-tabs
                color="black"
                slider-size="2"
                v-model="vmodel_layericontabs"
              >
                <v-tab
                  href="#legend"
                  style="background-color: #9c27b0; min-width: 48px; max-width: 49px;"
                >
                  <v-icon color="grey lighten-5">mdi-texture</v-icon>
                </v-tab>
                <v-tab
                  href="#info"
                  style="background-color: #00bcd4; min-width: 48px; max-width: 49px;"
                >
                  <v-icon color="grey lighten-5">mdi-information</v-icon>
                </v-tab>
                <v-tab
                  href="#filter"
                  style="background-color: #cddc39; min-width: 48px; max-width: 49px;"
                >
                  <v-icon color="grey lighten-5">mdi-filter</v-icon>
                </v-tab>
                <v-tab
                  href="#settings"
                  style="background-color: #607d8b; min-width: 48px; max-width: 49px;"
                >
                  <v-icon color="grey lighten-5">mdi-settings</v-icon>
                </v-tab>
                <v-tab
                  href="#download"
                  style="background-color: #2196F3; min-width: 48px; max-width: 49px;"
                >
                  <v-icon color="grey lighten-5">mdi-cloud-download</v-icon>
                </v-tab>
              </v-tabs>
              <v-tabs-items v-model="vmodel_layericontabs">
                <v-tab-item value="legend">
                  <v-card>
                    <v-card-text>
                      <v-img
                        :contain="false"
                        width="213px"
                        position="left"
                        :max-height="get_layer_style_height(item)"
                        :min-height="get_layer_style_height(item)"
                        :src="get_layer_style(item)"
                      />
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item value="info">
                  <v-card>
                    <v-card-text>
                      {{ item.layer_description }}
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item value="filter">
                  <v-card>
                    <v-card-text>
                      <v-btn block x-large color="#cddc39" dark
                        >Abrir dialogo</v-btn
                      >
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item value="settings">
                  <v-card>
                    <v-card-text>
                      <v-btn block x-large color="#607d8b" dark
                        >Abrir dialogo</v-btn
                      >
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item value="download">
                  <v-list dense subheader>
                    <v-list-item @click="testa('item list alert')">
                      <v-list-item-content>
                        <v-list-item-title
                          v-text="item.layer_name"
                        ></v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-icon>
                        <v-icon color="primary">mdi-download</v-icon>
                      </v-list-item-icon>
                    </v-list-item>
                    <v-list-item @click="testa('item list alert')">
                      <v-list-item-content>
                        KML
                      </v-list-item-content>
                      <v-list-item-icon>
                        <v-icon color="primary">mdi-download</v-icon>
                      </v-list-item-icon>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        Shapefile
                      </v-list-item-content>
                      <v-list-item-icon>
                        <v-icon color="primary">mdi-download</v-icon>
                      </v-list-item-icon>
                    </v-list-item>
                  </v-list>
                </v-tab-item>
              </v-tabs-items>
            </v-card>
          </v-row>

          <p></p>
          <v-divider></v-divider>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-dialog v-model="new_layer_dialog" max-width="800">
      <v-card>
        <v-card-title>Agregar Capa WMS</v-card-title>
        <v-card-text>
          <p>Detalles de la nueva capa a agregar</p>
          <v-form>
            <v-select
              label="Servidor"
              :outlined="true"
              v-model="new_layer_server"
              :items="servers_select"
              dense
              hint="Versión del servicio"
            />
            <v-select
              label="Versión"
              :outlined="true"
              :disabled="true"
              v-model="new_layer_version"
              :items="['1.1.1', '1.3.0']"
              dense
              hint="Versión del servidor WMS"
            />
            <v-select
              label="Capa"
              :outlined="true"
              dense
              :hint="'Capa a agregar desde el servidor ' + new_layer.server"
            />
            <v-textarea
              label="Descripción"
              :maxlength="255"
              :auto-grow="true"
              :outlined="true"
              v-model="new_layer.server_abstract"
              hint="Descripción breve del servidor WMS, puede ser más especifica que el nombre que es corto"
              :rows="3"
              dense
            />
            <v-row
              align="center"
              style="margin-top: -10px; margin-bottom: -30px;"
            >
              <v-col cols="7">
                <v-select
                  label="Versión"
                  :outlined="true"
                  v-model="new_layer.version"
                  dense
                  hint="Versión del servidor WMS"
                />
              </v-col>
              <v-col cols="5">
                <v-row justify="end" style="margin-right: 2px;">
                  <v-switch
                    label="Activo"
                    dense
                    v-model="new_layer.layer_enabled"
                  />
                </v-row>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
        <v-col style="margin-top: -24px;">
          <v-col
            dense
            align="end"
            :justify="this.$vuetify.breakpoint.width < 333 ? 'center' : 'end'"
          >
            <v-col dense style="margin-top: -10px; margin-bottom: -20px;">
              <v-row
                :justify="
                  this.$vuetify.breakpoint.width < 333 ? 'center' : 'end'
                "
                style="margin-left: -20px; margin-right: -20px;"
              >
                <v-btn
                  class="ma-2"
                  :block="this.$vuetify.breakpoint.width < 333"
                  color="secondary darken-1"
                  tile
                  @click="new_layer_dialog = false"
                >
                  Cancelar
                </v-btn>
                <v-btn
                  class="ma-2"
                  :block="this.$vuetify.breakpoint.width < 333"
                  color="success darken-1"
                  tile
                  @click="add_new_layer()"
                >
                  Agregar
                </v-btn>
              </v-row>
            </v-col>
          </v-col>
        </v-col>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
let wmsclient = require("wms-client");

export default {
  name: "MapLayer",
  props: {
    layers: Array,
    servers: Array
  },
  data: () => ({
    new_layer_dialog: false,
    new_layer_version: undefined,
    new_layer_server: undefined,
    new_layer: {
      layer_enabled: true
    },
    vmodel_layericontabs: null
  }),
  watch: {
    new_layer_server() {
      this.new_layer_version = this.servers[
        this.new_layer_server
      ].server_version;
      console.log("new_layer_server: ", this.new_layer_server);
      console.log("new_layer_version: ", this.new_layer_version);
      let url = this.servers[this.new_layer_server].server_baseurl;
      let wms = new wmsclient(url);
      console.log(url);
      console.log(wms);
      // Get WMS Service Title
      wms.capabilities((err, capabilities) => {
        if (err) return console.log(err);
        console.log(capabilities.service.title);
      });
    },
    new_layer() {
      this.new_layer.version = this.servers[
        this.new_layer.server
      ].server_version;
      /* this.new_layer_server = this.servers[
        this.new_layer.server
      ]; */
      console.log("new_layer.server: ", this.new_layer.server);
      console.log("new_layer.version: ", this.new_layer.version);
      console.log("new_layer: ", this.new_layer);
    }
  },
  computed: {
    servers_select() {
      let names = [];
      for (let item of this.servers) {
        names.push(item.server_name);
      }
      const map_names = names.map(function(val, index) {
        return { value: index, text: val };
      });
      console.log("map_names: ", map_names);
      return map_names;
    }
  },
  methods: {
    testa(val) {
      alert(val);
    },
    add_new_layer_dialog() {
      this.new_layer_dialog = true;
    },
    add_new_layer_cancel() {
      this.new_layer = { layer_enabled: true };
      this.new_layer_dialog = false;
    },
    add_new_layer() {
      this.layers.push(this.new_layer);
      this.new_layer = { layer_enabled: true };
      this.new_layer_dialog = false;
    },
    get_layer_thumb(val) {
      let thumb_server = val.server;
      if (val.server.includes("gwc/service/wms?")) {
        thumb_server = thumb_server.slice(0, -16) + "wms/";
      } else {
        thumb_server = thumb_server.slice(0, -1) + "/";
      }
      const thumb_url =
        thumb_server +
        "reflect?" +
        "layers=" +
        val.layers +
        "&format=image/png&srs=" +
        val.crs;
      return thumb_url;
    },
    get_layer_style_height(val) {
      const layer_url =
        val.server +
        "request=GetLegendGraphic&version=" +
        val.version +
        "&format=image/png&width=30&height=30&layer=" +
        val.layers +
        "&legend_options=fontName:Arial;fontAntiAliasing:true;fontSize:16";
      const img = new Image();
      img.src = layer_url;
      return this.height;
    },
    get_layer_style(val) {
      const layer_url =
        val.server +
        "request=GetLegendGraphic&version=" +
        val.version +
        "&format=image/png&width=30&height=30&layer=" +
        val.layers +
        "&legend_options=fontName:Arial;fontAntiAliasing:true;fontSize:16";
      return layer_url;
    }
  },
  mounted() {
    console.log("mounted");
  }
};
</script>

<style scoped></style>
