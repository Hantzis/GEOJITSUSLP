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
              :overlay="true == true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true == true"
            ></vl-source-wms>
          </vl-layer-tile>
          <vl-layer-tile>
            <vl-source-wms
              url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
              layers="PARCELASSLP:ejidos"
              format="image/png"
              :overlay="true == true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true == true"
            ></vl-source-wms>
          </vl-layer-tile>
          <vl-layer-tile>
            <vl-source-wms
              url="https://api.parcelas-slp.maptitude.xyz/geoserver/gwc/service/wms?"
              layers="PARCELASSLP:parcelas"
              format="image/png"
              :overlay="true == true"
              projection="EPSG:4326"
              version="1.1.1"
              :visible="true == true"
            ></vl-source-wms>
          </vl-layer-tile>

          <!-- interactions -->
          <vl-interaction-select
            :features.sync="selectedFeatures"
            v-if="drawType == null"
          >
            <template slot-scope="select">
              <!-- select styles -->
              <vl-style-box>
                <vl-style-stroke color="#423e9e" :width="7"></vl-style-stroke>
                <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
                <vl-style-circle :radius="5">
                  <vl-style-stroke color="#423e9e" :width="7"></vl-style-stroke>
                  <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
                </vl-style-circle>
              </vl-style-box>
              <vl-style-box :z-index="1">
                <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
                <vl-style-circle :radius="5">
                  <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
                </vl-style-circle>
              </vl-style-box>
              <!--// select styles -->

              <!-- selected feature popup -->
              <vl-overlay
                class="feature-popup"
                v-for="feature in select.features"
                :key="feature.id"
                :id="feature.id"
                :position="pointOnSurface(feature.geometry)"
                :auto-pan="true"
                :auto-pan-animation="{ duration: 300 }"
              >
                <template slot-scope="popup">
                  <section class="card">
                    <header class="card-header">
                      <p class="card-header-title">
                        Feature ID {{ feature.id }}
                      </p>
                      <a
                        class="card-header-icon"
                        title="Close"
                        @click="
                          selectedFeatures = selectedFeatures.filter(
                            f => f.id !== feature.id
                          )
                        "
                      >
                        <b-icon icon="close"></b-icon>
                      </a>
                    </header>
                    <div class="card-content">
                      <div class="content">
                        <p>
                          Overlay popup content for Feature with ID
                          <strong>{{ feature.id }}</strong>
                        </p>
                        <p>Popup: {{ JSON.stringify(popup) }}</p>
                        <p>
                          Feature:
                          {{
                            JSON.stringify({
                              id: feature.id,
                              properties: feature.properties
                            })
                          }}
                        </p>
                      </div>
                    </div>
                  </section>
                </template>
              </vl-overlay>
              <!--// selected popup -->
            </template>
          </vl-interaction-select>
          <!--// interactions -->

          <!-- map panel, controls -->
          <div class="map-panel">
            <b-collapse class="panel box is-paddingless" :open.sync="panelOpen">
              <div slot="trigger" class="panel-heading">
                <div class="columns">
                  <div class="column is-11">
                    <strong>Map panel</strong>
                  </div>
                  <div class="column">
                    <b-icon
                      :icon="panelOpen ? 'chevron-up' : 'chevron-down'"
                      size="is-small"
                    ></b-icon>
                  </div>
                </div>
              </div>
              <p class="panel-tabs">
                <a
                  @click="showMapPanelTab('state')"
                  :class="mapPanelTabClasses('state')"
                  >State</a
                >
                <a
                  @click="showMapPanelTab('layers')"
                  :class="mapPanelTabClasses('layers')"
                  >Layers</a
                >
                <a
                  @click="showMapPanelTab('draw')"
                  :class="mapPanelTabClasses('draw')"
                  >Draw</a
                >
              </p>

              <div class="panel-block" v-show="mapPanel.tab === 'state'">
                <table class="table is-fullwidth">
                  <tr>
                    <th>Map center</th>
                    <td>{{ center }}</td>
                  </tr>
                  <tr>
                    <th>Map zoom</th>
                    <td>{{ zoom }}</td>
                  </tr>
                  <tr>
                    <th>Map rotation</th>
                    <td>{{ rotation }}</td>
                  </tr>
                  <tr>
                    <th>Device coordinate</th>
                    <td>{{ deviceCoordinate }}</td>
                  </tr>
                  <tr>
                    <th>Selected features</th>
                    <td>{{ selectedFeatures.map(f => f.id) }}</td>
                  </tr>
                </table>
              </div>

              <div
                class="panel-block"
                v-for="layer in layers"
                :key="layer.id"
                @click="showMapPanelLayer"
                :class="{ 'is-active': layer.visible }"
                v-show="mapPanel.tab === 'layers'"
              >
                <b-switch :key="layer.id" v-model="layer.visible">
                  {{ layer.title }}
                </b-switch>
              </div>

              <div
                class="panel-block draw-panel"
                v-show="mapPanel.tab === 'draw'"
              >
                <div class="buttons">
                  <button
                    v-for="control in drawControls"
                    :key="control.type || -1"
                    @click="drawType = control.type"
                    :class="
                      drawType && drawType === control.type ? 'is-info' : ''
                    "
                    class="button"
                  >
                    <b-icon :icon="control.icon"></b-icon>
                    <span>{{ control.label }}</span>
                  </button>
                </div>
              </div>
            </b-collapse>
          </div>
          <!--// map panel, controls -->
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

// eslint-disable-next-line no-unused-vars
import { createProj, addProj, findPointOnSurface, createStyle, createMultiPointGeom, loadingBBox } from "vuelayers/lib/ol-ext";
import { range, random } from "lodash";

Vue.use(VueLayers);

// Custom projection for static Image layer
let x = 1024 * 10000;
let y = 968 * 10000;
let imageExtent = [-x / 2, -y / 2, x / 2, y / 2];
let customProj = createProj({
  code: "xkcd-image",
  units: "pixels",
  extent: imageExtent
});
// add to the list of known projections
// after that it can be used by code
addProj(customProj);

export default {
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
    selectedFeatures: [],
    drawType: undefined,
    clickCoordinate: undefined,
    deviceCoordinate: undefined,
    mapPanel: {
      tab: "state"
    },
    panelOpen: true,
    mapVisible: true,
    drawControls: [
      {
        type: "point",
        label: "Draw Point",
        icon: "map-marker"
      },
      {
        type: "line-string",
        label: "Draw LineString",
        icon: "minus"
      },
      {
        type: "polygon",
        label: "Draw Polygon",
        icon: "square-o"
      },
      {
        type: "circle",
        label: "Draw Circle",
        icon: "circle-thin"
      },
      {
        type: undefined,
        label: "Stop drawing",
        icon: "times"
      }
    ],
    drawnFeatures: [],
    // base layers
    baseLayers: [
      {
        name: "osm",
        title: "OpenStreetMap",
        visible: true
      },
      {
        name: "sputnik",
        title: "Sputnik Maps",
        visible: false
      },
      // needs paid plan to get key
      // {
      //   name: 'mapbox',
      //   title: 'Mapbox',
      // },
      {
        name: "bingmaps",
        title: "Bing Maps",
        apiKey:
          "ArbsA9NX-AZmebC6VyXAnDqjXk6mo2wGCmeYM8EwyDaxKfQhUYyk0jtx6hX5fpMn",
        imagerySet: "CanvasGray",
        visible: false
      }
    ],
    // layers config
    layers: [
      // Circles
      {
        id: "circles",
        title: "Circles",
        cmp: "vl-layer-vector",
        visible: false,
        source: {
          cmp: "vl-source-vector",
          staticFeatures: range(0, 100).map(i => {
            let coordinate = [random(-50, 50), random(-50, 50)];
            return {
              type: "Feature",
              id: "random-cirlce-" + i,
              geometry: {
                type: "Circle",
                coordinates: coordinate,
                radius: random(Math.pow(10, 5), Math.pow(10, 6))
              }
            };
          })
        }
      },
      // Countries vector layer
      // loads GeoJSON data from remote server
      {
        id: "countries",
        title: "Countries",
        cmp: "vl-layer-vector",
        visible: false,
        source: {
          cmp: "vl-source-vector",
          url:
            "https://openlayers.org/en/latest/examples/data/geojson/countries.geojson"
        },
        style: [
          {
            cmp: "vl-style-box",
            styles: {
              "vl-style-fill": {
                color: [255, 255, 255, 0.5]
              },
              "vl-style-stroke": {
                color: "#219e46",
                width: 2
              },
              "vl-style-text": {
                text: "\uf041",
                font: "24px FontAwesome",
                fill: {
                  color: "#2355af"
                },
                stroke: {
                  color: "white"
                }
              }
            }
          }
        ]
      },
      // Tile layer with WMS source
      {
        id: "wms",
        title: "WMS",
        cmp: "vl-layer-tile",
        visible: false,
        source: {
          cmp: "vl-source-wms",
          url: "https://ahocevar.com/geoserver/wms",
          layers: "topp:states",
          extParams: { TILED: true },
          serverType: "geoserver"
        }
      },
      // Tile layer with WMTS source
      {
        id: "wmts",
        title: "WMTS",
        cmp: "vl-layer-tile",
        visible: false,
        source: {
          cmp: "vl-source-wmts",
          url:
            "https://services.arcgisonline.com/arcgis/rest/services/Demographics/USA_Population_Density/MapServer/WMTS/",
          layerName: "0",
          matrixSet: "EPSG:3857",
          format: "image/png",
          styleName: "default"
        }
      },
      // Vector layer with clustering
      {
        id: "cluster",
        title: "Cluster",
        cmp: "vl-layer-vector",
        renderMode: "image",
        visible: false,
        // Cluster source (vl-source-cluster) wraps vector source (vl-source-vector)
        source: {
          cmp: "vl-source-cluster",
          distance: 50,
          source: {
            cmp: "vl-source-vector",
            // features defined as array of GeoJSON encoded Features
            // to not overload Vue and DOM
            features: range(0, 10000).map(i => {
              let coordinate = [random(-50, 50), random(-50, 50)];
              return {
                type: "Feature",
                id: "random-" + i,
                geometry: {
                  type: "Point",
                  coordinates: coordinate
                }
              };
            })
          }
        },
        style: [
          {
            cmp: "vl-style-func",
            factory: this.clusterStyleFunc
          }
        ]
      },
      {
        id: "wfs",
        title: "WFS (Canada water areas)",
        cmp: "vl-layer-vector",
        visible: false,
        renderMode: "image",
        source: {
          cmp: "vl-source-vector",
          features: [],
          url(extent, resolution, projection) {
            return (
              "https://ahocevar.com/geoserver/wfs?service=WFS&" +
              "version=1.1.0&request=GetFeature&typename=osm:water_areas&" +
              "outputFormat=application/json&srsname=" +
              projection +
              "&" +
              "bbox=" +
              extent.join(",") +
              "," +
              projection
            );
          },
          strategyFactory() {
            return loadingBBox;
          }
        }
      },
      {
        id: "static-image",
        title: "Static Image with custom projection",
        cmp: "vl-layer-image",
        visible: false,
        source: {
          cmp: "vl-source-image-static",
          projection: customProj.getCode(),
          url: "https://imgs.xkcd.com/comics/online_communities.png",
          size: [1024, 968],
          extent: imageExtent
        }
      },
      {
        id: "wms-image",
        title: "Image WMS",
        cmp: "vl-layer-image",
        visible: false,
        source: {
          cmp: "vl-source-image-wms",
          url: "https://ahocevar.com/geoserver/wms",
          layers: "topp:states",
          serverType: "geoserver"
        }
      },
      {
        id: "vector-tiles",
        title: "Vector tiles",
        cmp: "vl-layer-vector-tile",
        visible: false,
        source: {
          cmp: "vl-source-vector-tile",
          url:
            "https://basemaps.arcgis.com/v1/arcgis/rest/services/World_Basemap/VectorTileServer/tile/{z}/{y}/{x}.pbf"
        },
        style: [
          {
            cmp: "vl-style-box",
            styles: {
              "vl-style-stroke": {
                width: 2,
                color: "#2979ff"
              },
              "vl-style-circle": {
                radius: 5,
                stroke: {
                  width: 1.5,
                  color: "#2979ff"
                }
              }
            }
          }
        ]
      }
    ]
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
