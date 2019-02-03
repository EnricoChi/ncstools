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

        <v-list three-line subheader fluid>
          <v-layout row wrap>
            <v-flex xs8>
              <v-subheader>Files</v-subheader>
            </v-flex>
          </v-layout>
        </v-list>
      </v-card-text>


      <v-card>
        <v-layout row wrap align-center fill-height>
          <v-flex xs1 ml-4>
            <v-switch
              label="User`s/All"
              color="info"
              hide-details
              v-model="filterForUser"
            ></v-switch>
          </v-flex>
          <v-flex xs2>
            <v-card-title>
              <v-text-field
                v-model="search"
                append-icon="search"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
          </v-flex>
          <v-flex>
            <v-checkbox v-model="selectAll" @change="select" class="mt-5">
              <div slot="label">
                Select All
              </div>
            </v-checkbox>
          </v-flex>
          <v-flex xs12>
            <v-data-table
              hide-actions
              :headers="headers"
              :items="files"
              :search="search"
              :custom-filter="fileSearch"
              class="elevation-1">
              <template slot="items" slot-scope="props">
                <tr v-bind:class="{ 'grey--text': !isShowedForUser(props.item.user) }"
                    v-if="!isShowedForUser(props.item.user) ? filterForUser : isShowedForUser(props.item.user)">
                  <td class="py-4">{{ props.item.name }}</td>
                  <td>{{ props.item.info }}</td>
                  <td>
                    <v-layout
                      v-if="isShowedForUser(props.item.user)"
                      align-center xs1 flex>
                      <v-checkbox v-model="selected" :value="props.item.name" class="mt-3 pt-2"></v-checkbox>
                      <v-icon
                        @click="deleteItem(props.item)">
                        delete
                      </v-icon>
                    </v-layout>
                  </td>
                </tr>
              </template>
            </v-data-table>
            <v-toolbar flat color="white">
              <v-spacer></v-spacer>
              <v-btn class="mb-2" @click="close(dialog.name)">
                Cansel
              </v-btn>
              <v-btn color="primary" class="mb-2">
                Delete {{ selected.length ? selected.length : '' }} files
              </v-btn>
            </v-toolbar>
          </v-flex>
        </v-layout>
      </v-card>


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
                        info: 'info1',
                        user: 1
                    },
                    {
                        name: 'file2',
                        info: 'info2',
                        user: 2
                    },
                    {
                        name: 'file3',
                        info: 'info3',
                        user: 1
                    },
                ]
            },
            close(dialogName) {
                this.toggleDialog(dialogName);
                this.selected = [];
                this.selectAll = false;
            },
            deleteItem(item) {
                const index = this.files.indexOf(item);
                confirm('Are you sure you want to delete this item?') && this.files.splice(index, 1)
            },

            isShowedForUser(file_user) {
                return this.user === file_user;
            },

            select() {
                this.selected = [];
                if (this.selectAll) {
                    for (let i in this.files) {
                        if (this.isShowedForUser(this.files[i].user)) {
                            this.selected.push(this.files[i].name);
                        }
                    }
                }
            },

            fileSearch(items, search, filter) {
                search = search.toString().toLowerCase();
                return items.filter(row => filter(row.name, search));
            }
        },
        data() {
            return {
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
                selected: [],
                selectAll: false,
                search: '',
                filterForUser: true,
            }
        },
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