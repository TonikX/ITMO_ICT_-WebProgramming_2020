<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Editors</h1>

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.attributes.first_name }}</td>
                <td class="is-center">{{ scope.row.attributes.middle_name }}</td>
                <td class="is-center">{{ scope.row.attributes.last_name }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
    <br/>
    <br/>

    <mu-container class="panel-wrapper">
      <mu-expansion-panel :expand="panel === 'panel1'" @change="toggle('panel1')">
        <div slot="header" style="color: #581845">Delete</div>
        <p>In order to delete an editor, please, enter its id.</p>
        <input v-model="pk" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteEditor">Input</mu-button>
        </mu-container>
      </mu-expansion-panel>

      <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
        <div slot="header" style="color: #581845">Add</div>
          In order to add a new record of editor, please, enter information about it.
          <br/>
          <br/>
          <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="first_name" placeholder="First Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="middle_name" placeholder="Middle Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="last_name" placeholder="Last Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br/>
          <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addEditor">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>
      
      <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
        <div slot="header" style="color: #581845">Edit</div>
          In order to edit a record of editor, please, enter its id.
          <br/>
          <br/>
          <input v-model="editor_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editEditor">Input</mu-button>
          </mu-container>
          <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="first" placeholder="First Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="middle" placeholder="Middle Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="last" placeholder="Last Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br v-if="options"/>
          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitEditor">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>

  </mu-container>
    <br/>
    <br/>
  
  </div>
</template>

<script>

import $ from 'jquery'

export default {
  name: 'Editors',
  data () {
    return {
      panel: '',
      labelPosition: 'top',
      pk: '',
      first_name: '',
      middle_name: '',
      last_name: '',
      first: '',
      middle: '',
      last: '',
      editor_id: '',
      columns: [
        { title: "Editor's ID", name: 'id', width: 130, align: 'center' },
        { title: "Editor's First Name", name: 'first_name', width: 180, align: 'center' },
        { title: "Editor's Middle Name", name: 'middle_name', width: 180, align: 'center' },
        { title: "Editor's Last Name", name: 'last_name', width: 180, align: 'center' }
        ],
      list: [{}],
      options:''
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadEditors()
  },
  methods: {
    loadEditors() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editors/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },
    toggle (panel) {
      this.panel = panel === this.panel ? '' : panel;
    },
    deleteEditor() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editors/',
        type: 'DELETE',
        data: {
          pk: this.pk,
        },
        success: (response) => {
          this.loadEditors()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No editor was found')
          }
        }
      })
    },
    addEditor() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editors/',
        type: 'POST',
        data: {
          first_name: this.first_name,
          middle_name: this.middle_name,
          last_name: this.last_name
        },
        success: (response) => {
          this.loadEditors()
        }
      })
    },
    editEditor() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editor/',
        type: 'GET',
        data: {
          id: this.editor_id
        },
        success: (response) => {
          this.options = response.data
          this.first = response.data.attributes.first_name
          this.middle = response.data.attributes.middle_name
          this.last = response.data.attributes.last_name
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No editor was found')
          }
        }
      })
    },
    submitEditor() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editors/',
        type: 'PUT',
        data: {
          id: this.editor_id,
          first_name: this.first,
          middle_name: this.middle,
          last_name: this.last
        },
        success: (response) => {
          this.loadEditors()
          this.options = ''
        }
      })
    },
    goHome() {
      this.$router.push({name: "home"})
    }
  }
}
</script>

<style>
body {
  background-color: #f4f4f4;
}
h1 {
  font-size: 180%;
  line-height: 0px;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center;
  margin-bottom: 50px;
}

.demo-divider-form {
  font-size: 90%;
  padding: 0 16px;
  height: 30px;
}

.table-wrapper {
  text-align: center;
  margin-left: 290px;
  width: 686px;
}

.panel-wrapper {
  width: 684px;
}
</style>
