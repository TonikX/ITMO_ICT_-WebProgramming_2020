<template>
  <div>
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Number of clients from a specified city</h1>
<mu-paper :z-depth="1">
              <mu-text-field v-model="hometown" placeholder="Enter the city name" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
  </mu-container>
  <mu-container class="asa" v-if="ans">
    {{ans.data.thing}} client(s) from {{hometown}}</mu-container>
  </div>
</template>

<script>
    import $ from 'jquery'
  export default {
    name: 'Request2',
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
          url: 'http://127.0.0.1:8000/request2/',
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
    font-size: 200%;
  }

</style>
