<template>
  <v-dialog
    v-model="dialog.show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>

      <v-toolbar card dark color="primary">
        <v-btn icon dark @click="toggleDialog(dialog.name)">
          <v-icon>fa-angle-double-left</v-icon>
        </v-btn>

        <v-spacer></v-spacer>
        <v-toolbar-title>Files</v-toolbar-title>
        <v-spacer></v-spacer>

        <v-toolbar-items class="fab-container">
          <!--<v-btn fab small color="teal accent-3">-->
          <!--<v-icon>fa-plus</v-icon>-->
          <!--</v-btn>-->
          <v-btn fab small color="deep-orange accent-3">
            <v-icon>fa-refresh</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-card-text>

        <v-list three-line subheader>
          <v-subheader>Files</v-subheader>
        </v-list>
      </v-card-text>


      <v-data-table
        :headers="headers"
        :items="files"
        class="elevation-1">
        <template slot="items" slot-scope="props">
          <tr v-bind:class="{ 'grey--text': !isShowedForUser(props.item.user) }">
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.info }}</td>
            <td>
              <v-layout
                v-if="isShowedForUser(props.item.user)"
                align-center xs1 flex>
                <v-checkbox class="mt-3 pt-2"></v-checkbox>
                <v-icon
                  @click="deleteItem(props.item)">
                  delete
                </v-icon>
              </v-layout>
            </td>
          </tr>
        </template>
        <template slot="no-data">
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>


      <div style="flex: 1 1 auto;"></div>
    </v-card>
  </v-dialog>
</template>


<script>
    import {mapActions, mapMutations, mapState} from 'vuex';

    export default {

        computed: {
            ...mapState({
                dialog: state => state.dialogs.files,
            }),
        },

        methods: {
            ...mapMutations(['toggleDialog',]),
            initialize() {
                this.files = [
                    {
                        name: 'file1',
                        info: 'info',
                        user: 1
                    },
                    {
                        name: 'file2',
                        info: 'info',
                        user: 2
                    },
                    {
                        name: 'file3',
                        info: 'info',
                        user: 1
                    },
                ]
            },

            deleteItem(item) {
                const index = this.files.indexOf(item);
                confirm('Are you sure you want to delete this item?') && this.files.splice(index, 1)
            },

            isShowedForUser(file_user) {
                return this.user === file_user;
            }
        },
        data: () => ({
            user: 1,
            headers: [
                {
                    text: 'File name',
                    align: 'left',
                    value: 'name'
                },
                {
                    text: 'Information',
                    value: 'info',
                    sortable: false
                },
                {
                    text: 'Actions',
                    value: 'name',
                    sortable: false
                }
            ],
            files: [],
            editedIndex: -1,
        }),
        created() {
            this.initialize()
        },

    }
</script>

<style scoped>
  .fab-container {
    position: fixed;
    top: 30px;
    left: 50px;
  }
</style>