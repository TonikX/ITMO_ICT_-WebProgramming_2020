<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Newspapers</h1>

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.name }}</td>
                <td class="is-center">{{ scope.row.edition_index }}</td>
                <td class="is-center">{{ scope.row.editor }}</td>
                <td class="is-center">{{ scope.row.price }}</td>
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
        <p>In order to delete a record of newspaper, please, enter its id.</p>
        <input v-model="pk" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deletePaper">Input</mu-button>
        </mu-container>
      </mu-expansion-panel>
      
      <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
        <div slot="header" style="color: #581845">Add</div>
          In order to add a new record of newspaper, please, enter information about it.
          <br/>
          <br/>
          <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="name" placeholder="Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="edition_index" placeholder="Edition Index" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="price" placeholder="Price" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br/>
          Please, also choose an editor: &nbsp;
          <mu-select class="options-wrapper" v-model="editor">
            <mu-option v-for="editor,editor_i in editors" :key="editor" :label="editor" :value="editor"></mu-option>
          </mu-select>
          <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addPaper">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>

      <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
        <div slot="header" style="color: #581845">Edit</div>
          In order to edit a record of post office, please, enter its id.
          <br/>
          <br/>
          <input v-model="paper_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editPaper">Input</mu-button>
          </mu-container>
          <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="paper_name" placeholder="Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="paper_index" placeholder="Edition Index" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="paper_price" placeholder="Price" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <mu-select v-if="options" class="options-wrapper" v-model="paper_editor">
            <mu-option v-for="paper_editor,paper_editor_i in editors" :key="paper_editor" :label="paper_editor" :value="paper_editor"></mu-option>
          </mu-select>
          <br v-if="options"/>

          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitPaper">Input</mu-button>
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
  name: 'Newspapers',
  data () {
    return {
      print_run: '',
      panel: '',
      pk: '',
      id: '',
      paper_id: '',
      paper_name: '',
      paper_price: '',
      paper_index: '',
      paper_editor: '',
      name: '',
      edition_index: '',
      options: '',
      price: '',
      editor: '',
      editors: '',
      columns: [
        { title: 'Newspaper ID', name: 'number', width: 140, align: 'center' },
        { title: 'Nespaper Name', name: 'name', width: 200, align: 'center' },
        { title: 'Newspaper Edition Index', name: 'edition_index', width: 160, align: 'center' },
        { title: 'Newspaper Editor', name: 'editor', width: 226, align: 'center' },
        { title: 'Newspaper Price', name: 'price', width: 140, align: 'center' }
        ],
      list: [{}],
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadPapers()
    this.loadEditors()
  },
  methods: {
    loadPapers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/papers/',
        type: 'GET',
        success: (response) => {
          this.list = response.data.data
          }
      })
    },
    toggle (panel) {
      this.panel = panel === this.panel ? '' : panel;
    },
    deletePaper() {
      $.ajax({
        url: 'http://127.0.0.1:8000/papers/',
        type: 'DELETE',
        data: {
          pk: this.pk,
        },
        success: (response) => {
          this.loadPapers()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    loadEditors() {
      $.ajax({
        url: 'http://127.0.0.1:8000/editorslist/',
        type: 'GET',
        success: (response) => {
          this.editors = response.data
          }
      })
    },
    addPaper() {
      $.ajax({
        url: 'http://127.0.0.1:8000/papers/',
        type: 'POST',
        data: {
          id: this.id,
          name: this.name,
          edition_index: this.edition_index,
          editor: this.editor,
          price: this.price
        },
        success: (response) => {
          this.loadPapers()
        }
      })
    },
    editPaper() {
      $.ajax({
        url: 'http://127.0.0.1:8000/paper/',
        type: 'GET',
        data: {
          id: this.paper_id
        },
        success: (response) => {
          this.options = response.data.data
          this.paper_name = response.data.data.name
          this.paper_index = response.data.data.edition_index
          this.paper_editor = response.data.data.editor
          this.paper_price = response.data.data.price
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    submitPaper() {
      $.ajax({
        url: 'http://127.0.0.1:8000/papers/',
        type: 'PUT',
        data: {
          id: this.paper_id,
          name: this.paper_name,
          edition_index: this.paper_index,
          editor: this.paper_editor,
          price: this.paper_price
        },
        success: (response) => {
          this.loadPapers()
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
  padding: 0 16px;
}

.table-wrapper {
  text-align: center;
  margin-left: 193px;
  width: 882px;
}

.demo-divider-form {
  font-size: 90%;
  padding: 0 16px;
  height: 30px;
}

.panel-wrapper {
  width: 882px;
}

.options-wrapper {
  font-size: 90%
}
</style>
