<template>
  <div>
    <v-card style="border-radius: 0px;">
      <v-card-title style="padding-bottom: 0;">
        <v-row>
          <v-col cols="8">
            <v-icon>mdi-network</v-icon>Servidores <br />WMS</v-col
          >
          <v-col cols="4" align="right">
            <v-btn
              fab
              small
              color="green"
              @click.stop="dialog = true"
              style="margin-right: 14px;"
              ><v-icon color="white">mdi-plus</v-icon></v-btn
            >
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        Servidores WMS desde dónde conectar capas
      </v-card-text>
    </v-card>
    <v-expansion-panels
      style="border-radius: 0;"
      :accordion="true"
      :multiple="true"
      :hover="true"
      :flat="true"
      :focusable="true"
    >
      <v-expansion-panel v-for="(item, i) in this.servers" :key="i">
        <v-expansion-panel-header>{{
          item.server_name
        }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row justify="space-between" align="start">
            <v-col pa-0>
              <v-row justify="start">
                <v-switch
                  style="margin-top: 0; bottom: 0;"
                  v-model="item.server_enabled"
                  :disabled="item.server_permanent"
                ></v-switch>
              </v-row>
            </v-col>
            <v-col pa-0>
              <v-row justify="end">
                <v-btn
                  :disabled="item.server_permanent"
                  color="red"
                  style="height: 28px; width: 28px; min-width: 28px;"
                  @click="ask_delete_wms_server(i)"
                >
                  <v-icon color="grey lighten-5">mdi-delete</v-icon>
                </v-btn>
              </v-row>
            </v-col>
          </v-row>
          <v-row style="margin-top: -20px;">
            <v-card class="mx-auto" min-width="245" max-width="245">
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Nombre"
                    :maxlength="25"
                    v-model="item.server_name"
                    :disabled="item.server_permanent"
                    hint="Nombre corto del servidor (debe ser único)"
                  />
                  <v-text-field
                    label="URL Base"
                    :maxlength="255"
                    v-model="item.server_baseurl"
                    :disabled="item.server_permanent"
                    hint="URL del servidor WMS; suele estar en la forma https://dominio/uri/wms?"
                  />
                  <v-select
                    label="Versión"
                    v-model="item.server_version"
                    :disabled="item.server_permanent"
                    :items="['1.1.1', '1.3.0']"
                    hint="Versión del servicio"
                  />
                  <v-textarea
                    style="margin-top: 20px;"
                    label="Descripción"
                    v-model="item.server_abstract"
                    :disabled="item.server_permanent"
                    :maxlength="255"
                    :auto-grow="true"
                    hint="Descripción breve del servidor WMS, puede ser más especifica que el nombre que es corto"
                    :rows="4"
                    dense
                  />
                </v-form>
              </v-card-text>
            </v-card>
          </v-row>
          <p></p>
          <v-divider bold></v-divider>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-dialog v-model="dialog" max-width="800">
      <v-card>
        <v-card-title>Agregar servidor WMS</v-card-title>
        <v-card-text>
          <p>Detalles del nuevo servidor a agregar</p>
          <v-form>
            <v-text-field
              label="Nombre"
              :maxlength="25"
              :outlined="true"
              v-model="new_server.server_name"
              hint="Nombre corto del servidor (debe ser único)"
              dense
            />
            <v-text-field
              label="URL Base"
              :maxlength="255"
              :outlined="true"
              v-model="new_server.server_baseurl"
              hint="URL del servidor WMS; suele estar en la forma https://dominio/uri/wms?"
              dense
            />
            <v-textarea
              label="Descripción"
              :maxlength="255"
              :auto-grow="true"
              :outlined="true"
              v-model="new_server.server_abstract"
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
                  v-model="new_server.server_version"
                  :items="['1.1.1', '1.3.0']"
                  dense
                  hint="Versión del servicio"
                />
              </v-col>
              <v-col cols="5">
                <v-row justify="end" style="margin-right: 2px;">
                  <v-switch
                    label="Activo"
                    dense
                    v-model="new_server.server_enabled"
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
                  :block="this.$vuetify.breakpoint.width < 333 ? true : false"
                  color="secondary darken-1"
                  tile
                  @click="dialog = false"
                >
                  Cancelar
                </v-btn>
                <v-btn
                  class="ma-2"
                  :block="this.$vuetify.breakpoint.width < 333 ? true : false"
                  color="success darken-1"
                  tile
                  @click="add_new_server()"
                >
                  Agregar
                </v-btn>
              </v-row>
            </v-col>
          </v-col>
        </v-col>
      </v-card>
    </v-dialog>

    <v-dialog v-model="wms_delete_dialog" max-width="600">
      <v-card>
        <v-card-title>Eliminar servidor WMS</v-card-title>
        <v-card-text>
          <p>
            ¿Está seguro de eliminar el servidor
            <strong>{{ delete_server_name }}</strong
            >?
          </p>
          <v-row>
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
                    :block="this.$vuetify.breakpoint.width < 333 ? true : false"
                    color="secondary darken-1"
                    tile
                    @click="cancel_delete_wms_server()"
                  >
                    Cancelar
                  </v-btn>
                  <v-btn
                    class="ma-2"
                    :block="this.$vuetify.breakpoint.width < 333 ? true : false"
                    color="error darken-1"
                    tile
                    @click="confirm_delete_wms_server(delete_server_index)"
                  >
                    Eliminar
                  </v-btn>
                </v-row>
              </v-col>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "MapServer",
  props: {
    servers: Array
  },
  data: () => ({
    dialog: false,
    wms_delete_dialog: false,
    delete_server_name: "",
    delete_server_index: undefined,
    new_server: {
      server_enabled: true
    },
    slider: 80,
    vmodel_layericontabs: null
  }),
  methods: {
    add_new_server() {
      this.servers.push(this.new_server);
      this.new_server = { server_enabled: true };
      this.dialog = false;
    },
    ask_delete_wms_server(val) {
      this.delete_server_name = this.servers[val].server_name;
      this.delete_server_index = val;
      this.wms_delete_dialog = true;
    },
    confirm_delete_wms_server(val) {
      this.servers.splice(val, 1);
      this.wms_delete_dialog = false;
      this.delete_server_name = "";
      this.delete_server_index = undefined;
    },
    cancel_delete_wms_server() {
      this.wms_delete_dialog = false;
      this.delete_server_name = "";
    }
  }
};
</script>

<style scoped></style>
