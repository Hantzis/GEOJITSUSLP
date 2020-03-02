<template>
  <div>
    <v-card style="border-radius: 0px;">
      <v-card-title style="padding-bottom: 0;">
        <v-row>
          <v-col cols="8"> <v-icon>mdi-network</v-icon>Servidores</v-col>
          <v-col cols="4" align="right">
            <v-btn fab small color="green" @click.stop="dialog = true"
              ><v-icon color="white">mdi-plus</v-icon></v-btn
            >
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        Servidores WMS y WFS de dónde conectar capas
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
                <v-btn-toggle no-toggle>
                  <v-btn
                    :disabled="item.server_permanent"
                    color="red"
                    style="height: 28px; width: 28px; min-width: 28px;"
                  >
                    <v-icon color="grey lighten-5">mdi-delete</v-icon>
                  </v-btn>
                </v-btn-toggle>
              </v-row>
            </v-col>
          </v-row>
          <v-row style="margin-top: -20px;">
            <v-card class="mx-auto" min-width="245" max-width="245">
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Nombre"
                    v-model="item.server_name"
                    :disabled="item.server_permanent"
                  />
                  <v-text-field
                    label="URL Base"
                    v-model="item.server_baseurl"
                    :disabled="item.server_permanent"
                  />
                  <v-text-field
                    label="Versión"
                    v-model="item.server_version"
                    :disabled="item.server_permanent"
                  />
                  <v-text-field
                    label="Título"
                    v-model="item.server_title"
                    :disabled="item.server_permanent"
                  />
                  <v-textarea
                    label="Descripción"
                    maxlength="255"
                    v-model="item.server_abstract"
                    :disabled="item.server_permanent"
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
        <v-card-title>Agregar servidor</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Nombre"
              :outlined="true"
              v-model="new_server.server_name"
            />
            <v-text-field
              label="URL Base"
              :outlined="true"
              v-model="new_server.server_baseurl"
            />
            <v-text-field
              label="Versión"
              :outlined="true"
              v-model="new_server.server_version"
            />
            <v-text-field
              label="Título"
              :outlined="true"
              v-model="new_server.server_title"
            />
            <v-textarea
              label="Descripción"
              maxlength="255"
              :auto-grow="true"
              :outlined="true"
              v-model="new_server.server_abstract"
            />
            <v-text-field
              label="Activo"
              :outlined="true"
              v-model="new_server.server_enabled"
            />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false"
            >Cancelar</v-btn
          >
          <v-btn color="green darken-1" text @click="add_new_server()"
            >Agregar servidor</v-btn
          >
        </v-card-actions>
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
    new_server: {},
    slider: 80,
    vmodel_layericontabs: null
  }),
  methods: {
    testa(val) {
      alert(val);
    },
    add_new_server() {
      this.servers.push(this.new_server);
      console.log("NEW SERVER: ", this.new_server);
      this.new_server = {};
      this.dialog = false;
      console.log("SERVERS: ", this.servers);
    }
  }
};
</script>

<style scoped></style>
