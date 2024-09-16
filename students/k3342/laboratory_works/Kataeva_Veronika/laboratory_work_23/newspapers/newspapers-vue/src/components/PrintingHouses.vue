<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>Printing Houses</h1>

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.attributes.name }}</td>
                <td class="is-center">{{ scope.row.attributes.address }}</td>
                <td class="is-center">{{ scope.row.attributes.status }}</td>
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
        <p>In order to delete a record of printing house, please, enter its id.</p>
        <input v-model="pk" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteHouse">Input</mu-button>
        </mu-container>
      </mu-expansion-panel>
      
      <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
        <div slot="header" style="color: #581845">Add</div>
          In order to add a new record of printing house, please, enter information about it.
          <br/>
          <br/>
          <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="name" placeholder="Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="address" placeholder="Address" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          Please, also choose a status: &nbsp;
          <mu-select class="options-wrapper" v-model="status">
            <mu-option v-for="status,status_i in statuses" :key="status" :label="status" :value="status"></mu-option>
          </mu-select>
          <br/>
          <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addHouse">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>

      <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
        <div slot="header" style="color: #581845">Edit</div>
          In order to edit a record of printing house, please, enter its id.
          <br/>
          <br/>
          <input v-model="house_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editHouse">Input</mu-button>
          </mu-container>
          <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="house_name" placeholder="Name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
              <mu-text-field v-model="house_address" placeholder="Address" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>

          <mu-select v-if="options" class="options-wrapper" v-model="house_status">
            <mu-option v-for="house_status,house_status_i in statuses" :key="house_status" :label="house_status" :value="house_status"></mu-option>
          </mu-select>
          <br v-if="options"/>

          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitHouse">Input</mu-button>
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
      number: '',
      name: '',
      address: '',
      status: '',
      house_name: '',
      house_address: '',
      house_id: '',
      house_status: '',
      house_statuses: '',
      labelPosition: 'top',
      answers: [],
      options: '',
      columns: [
        { title: 'Printing House ID', name: 'id', width: 150, align: 'center' },
        { title: 'Printing House Name', name: 'name', width: 200, align: 'center' },
        { title: 'Printing House Address', name: 'address', width: 300, align: 'center' },
        { title: 'Printing House Status', name: 'status', width: 160, align: 'center' }
        ],
      list: [{}],
      statuses: ['Working', 'Closed']
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadHouses()
  },
  methods: {
    loadHouses() {
      $.ajax({
        url: 'http://127.0.0.1:8000/printinghouses/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },
    toggle (panel) {
      this.panel = panel === this.panel ? '' : panel;
    },
    deleteHouse() {
      $.ajax({
        url: 'http://127.0.0.1:8000/printinghouses/',
        type: 'DELETE',
        data: {
          pk: this.pk,
        },
        success: (response) => {
          this.loadHouses()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    addHouse() {
      $.ajax({
        url: 'http://127.0.0.1:8000/printinghouses/',
        type: 'POST',
        data: {
          id: this.id,
          name: this.name,
          address: this.address,
          status: this.status

        },
        success: (response) => {
          this.loadHouses()
        }
      })
    },
    editHouse() {
      $.ajax({
        url: 'http://127.0.0.1:8000/printinghouse/',
        type: 'GET',
        data: {
          id: this.house_id
        },
        success: (response) => {
          this.options = response.data
          this.house_name = response.data.attributes.name
          this.house_address = response.data.attributes.address
          this.house_status = response.data.attributes.status
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No printinghouse was found')
          }
        }
      })
    },
    submitHouse() {
      $.ajax({
        url: 'http://127.0.0.1:8000/printinghouses/',
        type: 'PUT',
        data: {
          id: this.house_id,
          name: this.house_name,
          address: this.house_address,
          status: this.house_status

        },
        success: (response) => {
          this.loadHouses()
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
  margin-left: 240px;
  width: 826px;
}

.panel-wrapper {
  width: 640px;
}

.options-wrapper {
  font-size: 90%
}
</style>
