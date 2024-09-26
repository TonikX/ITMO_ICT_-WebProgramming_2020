<template>
<div><mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>The journal of all records</h1>
    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list.data" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.room }}</td>
                <td class="is-center">{{ scope.row.client }}</td>
                <td class="is-center">{{ scope.row.checkin }}</td>
                <td class="is-center">{{ scope.row.checkout }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
  <br/>
  <h2>To delete a record of a client's living, enter its id below:</h2>
        <input v-model="id" type="text" placeholder="Record ID"/>
        <br/>
  <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteJournal">Delete</mu-button>
        </mu-container>
  <br/> <h2>To add a new assignment, fill out the form below:</h2>
  <br/>
  <mu-select label="Room number:" class="options-wrapper" v-model="room">
            <mu-option v-for="room,index in rooms" :key="room.number" :label="room.number" :value="room.number"></mu-option>
          </mu-select>
  <mu-select label="Client name:" class="options-wrapper" v-model="client">
            <mu-option v-for="room,index in clients" :key="room.fio" :label="room.fio" :value="room.fio"></mu-option>
          </mu-select>
      <mu-paper :z-depth="1">
              <mu-text-field v-model="checkin" placeholder="Check-in date (YYYY-MM-DD format)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
      <mu-paper :z-depth="1">
              <mu-text-field v-model="checkout" placeholder="Check-out date (YYYY-MM-DD format)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <br/>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addJournal">Add</mu-button>
          </mu-container>
  <br/> <h2>To edit an existing record, enter its ID first:</h2>
  <br/><input v-model="jn_id" type="text" placeholder="Journal ID"/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editJournal">Input</mu-button>
          </mu-container>
  <br/>
  <mu-container v-if="options">
    <h3>Now, edit the data </h3>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="jn_checkin" placeholder="" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
  <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="jn_checkout" placeholder="" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br v-if="options"/>
          <p v-if="options">Client: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select v-if="options" class="options-wrapper" v-model="jn_client">
            <mu-option v-for="worker in clients" :key="worker.fio" :label="worker.fio" :value="worker.fio"></mu-option>
          </mu-select>
          </p>
          <p v-if="options">Room:
            <mu-select v-if="options" class="options-wrapper" v-model="jn_room">
            <mu-option v-for="worker in rooms" :key="worker.number" :label="worker.number" :value="worker.number"></mu-option>
          </mu-select>
          </p>
          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitJournal">Submit changes</mu-button>
          </mu-container>

</div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Journal",
        data(){
          return{
            id:'',
            client: '',
            room:'',
            checkin:'',
            checkout:'',
            jn_id:'',
            jn_client:'',
            jn_room:'',
            jn_checkin:'',
            jn_checkout:'',
            clients:'',
            rooms:'',
            columns:[
              { title: "ID", name: 'id', width: 100, align: 'center' },
              { title: "Room number", name: 'room', width: 100, align: 'center',sortable:true },
              { title: "Client", name: 'client', width: 280, align: 'center' },
              { title: "Check-in date", name: 'checkin', width: 180, align: 'center', sortable:true},
              { title: "Check-out date", name: 'checkout', width: 180, align: 'center',sortable:true },
            ],
            list:[{}],
            options:''
          }
        },
       created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " +
          sessionStorage.getItem('auth_token')},
    }),
      this.loadJournal()
         this.loadClients()
         this.loadRooms()
       },
      methods:{
        loadJournal() {
      $.ajax({
        url: 'http://127.0.0.1:8000/journal/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })},
        loadClients() {
      $.ajax({
        url: 'http://127.0.0.1:8000/clients/',
        type: 'GET',
        success: (response) => {
          this.clients = response.data.data
          }
      })},
        loadRooms() {
      $.ajax({
        url: 'http://127.0.0.1:8000/rooms/',
        type: 'GET',
        success: (response) => {
          this.rooms = response.data.data
          }})},

        deleteJournal() {
      $.ajax({
        url: 'http://127.0.0.1:8000/journal/',
        type: 'DELETE',
        data: {
          id: this.id,
        },
        success: (response) => {
          this.loadJournal()
        },
        error: (response) => {
          if (response.status === 404) {
            alert('No record was found')
          }
        }
      })
    },
        addJournal() {
      $.ajax({
        url: 'http://127.0.0.1:8000/journal/',
        type: 'POST',
        data: {
          id: this.id,
          client:this.client,
          room:this.room,
          checkin:this.checkin,
          checkout:this.checkout,
        },
        success: (response) => {
          this.loadJournal()
        }
      })
    },
          editJournal() {
      $.ajax({
        url: 'http://127.0.0.1:8000/journalq/',
        type: 'GET',
        data: {
          id: this.jn_id
        },
        success: (response) => {
          this.options = response.data
          this.jn_client = response.data.data.client
          this.jn_room = response.data.data.room
          this.jn_checkin = response.data.data.checkin
          this.jn_checkout = response.data.data.checkout
        },
        error: (response) => {
          if (response.status === 404) {
            alert('No record was found')
          }
        }
      })
    },  handleSortChange ({name, order}) {
      this.list.data = this.list.data.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },  submitJournal() {
      $.ajax({
        url: 'http://127.0.0.1:8000/journal/',
        type: 'PUT',
        data: {
          id: this.jn_id,
          client: this.jn_client,
          room: this.jn_room,
          checkin: this.jn_checkin,
          checkout: this.jn_checkout,
        },
        success: (response) => {
          this.loadJournal()
          this.options = ''
        }
      })
    },goHome() {
      this.$router.push({name: "main"})
    }
    }}
</script>

<style >
  .table-wrapper {
  text-align: center;
  width: 860px;
}
p{margin-left: 10px}
.button-wrapper4 {
  text-align: left;}


</style>
