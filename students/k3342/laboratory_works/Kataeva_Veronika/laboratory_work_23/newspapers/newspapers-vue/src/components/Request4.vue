<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>Which newspapers and where (post offices' numbers) are received in quantities less than the specified?</h1>

    <input v-model="print_run" type="text" placeholder="Please, input the value of print-run" style="width: 320px"/>
    <br/>
    <br/>

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
                  <td class="is-center">{{ scope.row.newspaper }}</td>
                  <td class="is-center">{{ scope.row.post_office }}</td>
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
  name: 'Request4',
  data () {
    return {
      print_run: '',
      columns: [
        { title: "Nespaper's Name", name: 'name', width: 226, align: 'center' },
        { title: 'Post Office Number', name: 'number', width: 226, align: 'center' },
        ],
      list: [{}],
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    })
  },
  methods: {
    loadAnswer() {
      $.ajax({
        url: "http://127.0.0.1:8000/request4/",
        type: "GET",
        data: {
          print_run: this.print_run,
        },
        success: (response) => {
            this.list = response.data.data;
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
  line-height: 0px;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center;
  margin-bottom: 70px;
}

.demo-divider-form {
  padding: 0 16px;
}

.table-wrapper {
  text-align: center;
  margin-left: 325px;
  width: 469px;
}
</style>
