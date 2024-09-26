<template>
<div><mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Clients that lived in a room during specified time</h1>
  <p>Room: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select class="options-wrapper" v-model="room">
            <mu-option v-for="worker,index in rooms" :key="worker.number" :label="worker.number" :value="worker.number"></mu-option>
          </mu-select>
          </p>
  <mu-paper :z-depth="1">
              <mu-text-field v-model="firstdate" placeholder="First date (YYYY-MM-DD)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-paper :z-depth="1">
              <mu-text-field v-model="seconddate" placeholder="Second date (YYYY-MM-DD)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
          </mu-container>
  <mu-container class="asa" v-if="list">
    <h2>Query results returned:</h2>
  <div v-for="answer in list">
      <mu-container style="text-align: center">
        <mu-paper class="demo-paper" :z-depth="1" style="padding: 15px">{{ answer.attributes.fio}}, from {{ answer.attributes.hometown}}, passport id is {{ answer.attributes.passport}}</mu-paper>
      </mu-container>
  </div></mu-container>
</div>
</template>

<script>
    import $ from 'jquery'
  export default {
    name: 'Request1',
    data () {
      return {
        labelPosition: 'top',
        room: '',
        firstdate:'',
        seconddate:'',
        rooms:[],
        records:[],
        list: NaN,
        columns:[
              { title: "Client", name: 'client', width: 200, align: 'center' },
              { title: "Hometown", name: 'hometown', width: 400, align: 'center' },
              { title: "Passport", name: 'passport', width: 200, align: 'center' },
            ],
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
      loadJournal() {
        $.ajax({
          url: 'http://127.0.0.1:8000/journal/',
          type: 'GET',
          success: (response) => {
            this.records = response.data
          }
        })
      },
      loadRooms() {
        $.ajax({
          url: 'http://127.0.0.1:8000/rooms/',
          type: 'GET',
          success: (response) => {
            this.rooms = response.data.data
          }
        })
      },
      loadAnswer() {
        $.ajax({
          url: 'http://127.0.0.1:8000/request1/',
          type: 'GET',
          data: {
            room: this.room,
            firstdate:this.firstdate,
            seconddate: this.seconddate
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

<style>
  .table-wrapper {
  text-align: center;
  margin-left: 260px;
  width: 900px;
}
.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }}
  .asa{
    margin-bottom: 100px;
  }
</style>
