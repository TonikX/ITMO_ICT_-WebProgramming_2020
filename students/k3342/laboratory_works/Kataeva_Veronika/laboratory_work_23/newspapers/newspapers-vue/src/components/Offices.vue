<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Post Offices</h1>

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.attributes.number }}</td>
                <td class="is-center">{{ scope.row.attributes.address }}</td>
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
        <p>In order to delete a record of post office, please, enter its id.</p>
        <input v-model="pk" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteOffice">Input</mu-button>
        </mu-container>
      </mu-expansion-panel>
      
      <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
        <div slot="header" style="color: #581845">Add</div>
          In order to add a new record of post office, please, enter information about it.
          <br/>
          <br/>
          <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="number" placeholder="Number" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="address" placeholder="Address" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br/>
          <br/>
          <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addOffice">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>

      <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
        <div slot="header" style="color: #581845">Edit</div>
          In order to edit a record of post office, please, enter its id.
          <br/>
          <br/>
          <input v-model="office_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editOffice">Input</mu-button>
          </mu-container>
          <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="office_number" placeholder="Number" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="office_address" placeholder="Address" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br v-if="options"/>

          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitOffice">Input</mu-button>
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
  name: 'Offices',
  data () {
    return {
      panel: '',
      pk: '',
      id: '',
      office_id: '',
      number: '',
      office_number: '',
      office_address: '',
      address: '',
      labelPosition: 'top',
      answers: [],
      options: '',
      columns: [
        { title: 'Post Office ID', name: 'id', width: 150, align: 'center' },
        { title: 'Post Office Number', name: 'number', width: 150, align: 'center' },
        { title: 'Post Office Address', name: 'address', width: 324, align: 'center' },
        ],
      list: [{}],
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadOffices()
  },
  methods: {
    loadOffices() {
      $.ajax({
        url: 'http://127.0.0.1:8000/postoffices/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },
    toggle (panel) {
      this.panel = panel === this.panel ? '' : panel;
    },
    deleteOffice() {
      $.ajax({
        url: 'http://127.0.0.1:8000/postoffices/',
        type: 'DELETE',
        data: {
          pk: this.pk,
        },
        success: (response) => {
          this.loadOffices()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    addOffice() {
      $.ajax({
        url: 'http://127.0.0.1:8000/postoffices/',
        type: 'POST',
        data: {
          id: this.id,
          number: this.number,
          address: this.address

        },
        success: (response) => {
          this.loadOffices()
        }
      })
    },
    editOffice() {
      $.ajax({
        url: 'http://127.0.0.1:8000/postoffice/',
        type: 'GET',
        data: {
          id: this.office_id
        },
        success: (response) => {
          this.options = response.data
          this.office_number = response.data.attributes.number
          this.office_address = response.data.attributes.address
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    submitOffice() {
      $.ajax({
        url: 'http://127.0.0.1:8000/postoffices/',
        type: 'PUT',
        data: {
          id: this.office_id,
          number: this.office_number,
          address: this.office_address

        },
        success: (response) => {
          this.loadOffices()
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
  margin-left: 313px;
  width: 640px;
}

.panel-wrapper {
  width: 640px;
}

.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}
</style>
