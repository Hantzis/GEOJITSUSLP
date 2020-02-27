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
          <v-row style="margin-bottom: 20px; margin-top: -20px;">
            {{ item.server_abstract }}
          </v-row>
          <v-row>
            <v-card class="mx-auto" min-width="245" max-width="245">
              <v-card-text>
                <v-form>
                  <v-text-field label="Nombre" v-model="item.server_name" />
                  <v-text-field
                    label="URL Base"
                    v-model="item.server_baseurl"
                  />
                  <v-text-field label="Versión" v-model="item.server_version" />
                  <v-text-field label="Título" v-model="item.server_title" />
                  <v-textarea
                    label="Descripción"
                    maxlength="255"
                    v-model="item.server_abstract"
                  />
                  <v-text-field label="Activo" v-model="item.server_enabled" />
                </v-form>
              </v-card-text>
            </v-card>
          </v-row>

          <p></p>
          <v-divider bold></v-divider>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  name: "MapboxLayer",
  props: {
    servers: Array
  },
  data: () => ({
    slider: 80,
    vmodel_layericontabs: null,
    items: [
      { text: "Real-Time", icon: "mdi-clock" },
      { text: "Audience", icon: "mdi-account" },
      { text: "Conversions", icon: "mdi-flag" }
    ]
  }),
  methods: {
    testa(val) {
      alert(val);
    }
  }
};
</script>

<style scoped></style>
