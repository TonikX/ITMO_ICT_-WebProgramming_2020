<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">

    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>CERTIFICATE</h1>

    <mu-container>
      <mu-paper :z-depth="2">
        <mu-text-field v-model="name" placeholder="Please, enter newspaper's name" solo full-width class="demo-divider-form"></mu-text-field>
        <mu-divider></mu-divider>
      </mu-paper>
    </mu-container>
    <br/>
  
    <mu-container class="button-wrapper" justify-content="center">
      <mu-button color="#e6ddde" textColor="black" @click="getCert">Input</mu-button>
    </mu-container>
    <br/>
    <br/>
    
    <mu-container v-if="certificate">
      <mu-container class="table-wrapper">
        <mu-row gutter>
          <mu-col span="7">
            <mu-paper :z-depth="1">
              <mu-data-table stripe :columns="columns" :data="list.slice(0, 3)">
                <template slot-scope="scope">
                  <td class="is-center">{{ certificate.name }}</td>
                  <td class="is-center">{{ certificate.edition_index }}</td>
                  <td class="is-center">{{ certificate.price }}</td>
                </template>
              </mu-data-table>
            </mu-paper>
          </mu-col>
        </mu-row>
      </mu-container>
    </mu-container>
    <br/>
  
    <br/>
    <br/>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Certificate',
  data() {
    return {
        name: '',
        certificate: '',
        columns: [
          { title: "Nespaper's Name", name: 'name', width: 213, align: 'center' },
          { title: 'Edition Index', name: 'index', width: 213, align: 'center' },
          { title: 'Price ($)', name: 'price', width: 213, align: 'center' }
        ],
        list: [
          {

          }
      ]
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    })
  },
  methods: {
    getCert() {
      $.ajax({
        url: "http://127.0.0.1:8000/certificate/",
        type: "GET",
        data: {
          name: this.name,
        },
        success: (response) => {
            this.certificate = response.data;
        },
        error: (response) => {
          alert("Newspaper with the given name doesn't exist")
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
  margin-bottom: 100px;
}

.demo-divider-form {
  padding: 0 16px;
}

.button-wrapper {
  text-align: right;
}

.table-wrapper {
  text-align: center;
  margin-left: 250px;
}

.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}
</style>
