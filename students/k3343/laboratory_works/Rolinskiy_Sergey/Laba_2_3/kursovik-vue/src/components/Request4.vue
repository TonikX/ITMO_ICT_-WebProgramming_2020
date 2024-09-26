<template>
<div>
  <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
    <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button></mu-container>
    <h2>Find out what rooms are empty right now</h2>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Find out</mu-button>
  </mu-container>
  <mu-container v-if="ans">
    <h2>Rooms that are empty right now:</h2>
     <mu-container v-for="room in ans">
       <mu-container style="text-align: center; font-size: 150%">
        <mu-paper class="demo-paper" :z-depth="1" style="padding: 15px">{{ room.attributes.number}}</mu-paper>
      </mu-container>
     </mu-container>
  </mu-container></div>
</template>

<script>
    import $ from 'jquery'
  export default {
    name: 'Request4',
    data () {
      return {
        labelPosition: 'top',
        hometown: '',
        clients:[],
        ans:NaN,
      }
    },
    created () {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      }),
      this.loadJournal()
      this.loadRooms()
    },
    methods: {
      loadClients() {
        $.ajax({
          url: 'http://127.0.0.1:8000/clients/',
          type: 'GET',
          success: (response) => {
            this.clients = response.data
          }
        })
      },
      loadAnswer() {
        $.ajax({
          url: 'http://127.0.0.1:8000/request4/',
          type: 'GET',
          data: {
            hometown: this.hometown,
          },
          success: (response) => {
            this.ans = response.data},
           error: (response) => {
            alert("somethings wrong")}
        })
      },goHome() {
      this.$router.push({name: "main"})
    },
    }}
</script>

<style >
.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }}
  .asa{
    margin-bottom: 100px;
  }
</style>
