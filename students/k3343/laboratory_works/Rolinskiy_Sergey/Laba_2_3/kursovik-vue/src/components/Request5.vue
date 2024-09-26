<template>
<div> <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
    <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button></mu-container>
    <h2>Clients who lived in the same time with a chosen client</h2>
  <p>Choose a client: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select class="options-wrapper" v-model="client">
            <mu-option v-for="worker,index in clients" :key="worker.fio" :label="worker.fio" :value="worker.fio"></mu-option>
          </mu-select>
          </p>
  <mu-paper :z-depth="1">
              <mu-text-field v-model="firstdate" placeholder="First date" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-paper :z-depth="1">
              <mu-text-field v-model="seconddate" placeholder="Second date" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
          </mu-container>
  <mu-container class="asa" v-if="list">
      <h2>Query results returned:</h2>
  <div v-for="answer in list">
      <mu-container style="text-align: center">
        <mu-paper class="demo-paper" :z-depth="1" style="padding: 15px">{{ answer.attributes.fio}}, from {{ answer.attributes.hometown}}</mu-paper>
      </mu-container>
  </div>
    </mu-container>
</div>
</template>

<script>
    import $ from 'jquery'
  export default {
    name: 'Request5',
    data () {
      return {
        labelPosition: 'top',
        weekday:'',
        client:'',
        firstdate:'',
        seconddate:'',
        clients:[],
        records:[],
        list:NaN,
      }
    },
    created () {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      }),
      this.loadJournal()
      this.loadClient()
    },
    methods: {
      loadJournal() {
        $.ajax({
          url: 'http://127.0.0.1:8000/journal/',
          type: 'GET',
          success: (response) => {
            this.records = response.data
          }
        })
      },
      loadClient() {
        $.ajax({
          url: 'http://127.0.0.1:8000/clients/',
          type: 'GET',
          success: (response) => {
            this.clients = response.data.data
          }
        })
      },
      loadAnswer() {
        $.ajax({
          url: 'http://127.0.0.1:8000/request5/',
          type: 'GET',
          data: {
            client: this.client,
            firstdate:this.firstdate,
            seconddate:this.seconddate
          },
          success: (response) => {
            this.list = response.data},
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
