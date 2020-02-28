<template>
  <div>
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
                  >
                    <v-icon color="grey lighten-5">mdi-chevron-up</v-icon>
                  </v-btn>
                  <v-btn
                    color="blue-grey"
                    style="height: 28px; width: 28px; min-width: 28px;"
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
                <v-card-title>{{ item.layer_name }}</v-card-title>
              </v-img>
              <v-card-text>
                <v-slider
                  v-model="slider"
                  thumb-label
                  style="min-height: 20px; margin-left: 4px; margin-right: 4px;"
                ></v-slider>
              </v-card-text>
              <v-tabs
                color="black"
                slider-size="3"
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
                      <v-img :contain="false" max-width="213px" min-width="213px" width="213px" :src="get_layer_style(item)" />
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item value="info">
                  <v-card>
                    <v-card-text>
                      info que viene de layer_description
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
  </div>
</template>

<script>
export default {
  name: "MapLayer",
  props: {
    layers: Array
  },
  data: () => ({
    slider: 80,
    vmodel_layericontabs: null
  }),
  methods: {
    testa(val) {
      alert(val);
    },
    add_new_layer() {
      this.layers.push(this.new_layer);
      this.new_layer = {};
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
      console.log("THUMB: ", thumb_url);
      return thumb_url;
    },
    get_layer_style(val) {
      const layer_url =
        val.server +
        "request=GetLegendGraphic&version=" +
        val.version +
        "&format=image/png&width=30&height=30&layer=" +
        val.layers +
        "&legend_options=fontName:Arial;fontAntiAliasing:true;fontSize:16";
      console.log("legend: ", layer_url);
      return layer_url;
    }
  }
};
</script>

<style scoped></style>
