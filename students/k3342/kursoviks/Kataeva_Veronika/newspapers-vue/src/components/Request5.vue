<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">

    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>Where does the requested newspaper go, which is printed at the given address?</h1>

    <mu-select v-model="name">
      <mu-option v-for="name,name_i in names" :key="name" :label="name" :value="name"></mu-option>
    </mu-select>

    <mu-select v-model="address">
      <mu-option v-for="address,address_i in addresses" :key="address" :label="address" :value="address"></mu-option>
    </mu-select>
 
    <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
    </mu-container>

    <mu-container v-if="list">
      <mu-container class="table-wrapper">
        <mu-row gutter>
          <mu-col >
            <mu-paper :z-depth="1">
              <mu-data-table stripe :columns="columns" :data="list">
                <template slot-scope="scope">
                  <td class="is-center">{{ scope.row.attributes.number }}</td>
                  <td class="is-center">{{ scope.row.attributes.address }}</td>
                </template>
              </mu-data-table>
            </mu-paper>
          </mu-col>
        </mu-row>
      </mu-container>
    </mu-container>
    <br/>
    <br/>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Request5',
  data () {
    return {
      names: [],
      addresses: [],
      labelPosition: 'top',
      answers: [],
      name: '',
      address: '',
      columns: [
        { title: "Post Office Number", name: 'name', width: 165, align: 'center' },
        { title: 'Post Office Address', name: 'number', width: 287, align: 'center' },
        ],
      list: [{}],
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadNewspapers()
    this.loadAddresses()
  },
  methods: {
    loadNewspapers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/newspapers/',
        type: 'GET',
        success: (response) => {
          this.names = response.data
          }
      })
    },
    loadAddresses() {
      $.ajax({
        url: 'http://127.0.0.1:8000/addresses/',
        type: 'GET',
        success: (response) => {
          this.addresses = response.data
          }
      })
    },
    loadAnswer() {
      $.ajax({
        url: 'http://127.0.0.1:8000/request5/',
        type: 'GET',
        data: {
          name: this.name,
          address: this.address
        },
        success: (response) => {
          this.list = response.data
          },
        error: (response) => {
          alert("Either newspaper or post office was not found")
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
  line-height: 100px;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center;
}

.demo-divider-form {
  padding: 0 16px;
}

.table-wrapper {
  text-align: center;
  margin-left: 325px;
  width: 468px;
}

.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}
</style>
