<template><div>
  <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
  <h2>Worker who tidied the specific room during a chosen day of the week</h2>
<p>Room: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select class="options-wrapper" v-model="room">
            <mu-option v-for="room,index in rooms" :key="room.number" :label="room.number" :value="room.number"></mu-option>
          </mu-select>
          </p>
  <mu-paper :z-depth="1">
              <mu-text-field v-model="weekday" placeholder="Day of the week (e.g. Monday)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
          </mu-container>
  <mu-container class="asa" v-if="list">
      <li v-for="thing in list">
        The room was being cleaned by {{thing.attributes.fio}}
        <br/>
    </li>
  </mu-container></div>
</template>

<script>
     import $ from 'jquery'
  export default {
    name: 'Request3',
    data () {
      return {
        labelPosition: 'top',
        weekday:'',
        id:'',
        room:'',
        rooms:[],
        records:[],
        list:NaN,
      }
    },
    created () {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      }),
      this.loadJournal()
      this.loadRooms()
      this.loadWorkers()
      this.loadWorktable()
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
      loadWorkers() {
        $.ajax({
          url: 'http://127.0.0.1:8000/workers/',
          type: 'GET',
          success: (response) => {
            this.records = response.data
          }
        })
      },
      loadWorktable() {
        $.ajax({
          url: 'http://127.0.0.1:8000/worktable/',
          type: 'GET',
          success: (response) => {
            this.records = response.data
          }
        })
      },
      loadAnswer() {
        $.ajax({
          url: 'http://127.0.0.1:8000/request3/',
          type: 'GET',
          data: {
            room: this.room,
            weekday:this.weekday,
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
    font-size: 170%;
    margin-bottom: 100px;
  }

</style>
