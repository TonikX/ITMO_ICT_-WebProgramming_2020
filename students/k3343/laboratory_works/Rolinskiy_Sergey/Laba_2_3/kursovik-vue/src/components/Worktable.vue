<template>
<div><mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Worktable of the hotel</h1>
    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list.data" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.worker }}</td>
                <td class="is-center">{{ scope.row.floor }}</td>
                <td class="is-center">{{ scope.row.weekday }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
  <br/>
  <h2>To delete an assignment of work, enter its id below:</h2>
        <input v-model="id" type="text" placeholder="Record ID"/>
        <br/>
  <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteWorktable">Delete</mu-button>
        </mu-container>
  <br/> <h2>To add a new assignment, fill out the form below:</h2>
  <br/>
  <mu-select label="Worker name:" class="options-wrapper" v-model="worker">
            <mu-option v-for="worker,index in workers" :key="worker.fio" :label="worker.fio" :value="worker.fio"></mu-option>
          </mu-select>
      <mu-paper :z-depth="1">
              <mu-text-field v-model="floor" placeholder="Floor (1-4)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
      <mu-paper :z-depth="1">
              <mu-text-field v-model="weekday" placeholder="Week day (e.g.Monday)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
  <br/>
  <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addWorktable">Add</mu-button>
          </mu-container>
  <br/> <h2>To edit an existing assignment, enter its ID first:</h2>
  <br/><input v-model="wt_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editWorktable">Input</mu-button>
          </mu-container>
  <br/>
  <mu-container v-if="options">
    <h3>Now, edit the data </h3>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="wt_floor" placeholder="Floor (1-4)" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
  <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="wt_weekday" placeholder="Day of the week" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br v-if="options"/>
          <p v-if="options">Your worker: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select v-if="options" class="options-wrapper" v-model="wt_worker">
            <mu-option v-for="worker in workers" :key="worker.fio" :label="worker.fio" :value="worker.fio"></mu-option>
          </mu-select>
          </p>
          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitWorktable">Submit changes</mu-button>
          </mu-container>

</div>
</template>

<script>
  import $ from 'jquery'
    export default {
        name: "Worktable",
      data(){
          return{
            id:'',
            workers:'',
            wt_id:'',
            worker: '',
            floor:'',
            weekday:'',
            wt_worker:'',
            wt_floor:'',
            wt_weekday:'',
            columns:[
              { title: "ID", name: 'id', width: 130, align: 'center' },
              { title: "Worker", name: 'fio', width: 260, align: 'center' },
              { title: "Floor", name: 'floor', width: 130, align: 'center',sortable:true },
              { title: "Day of the week", name: 'weekday', width: 180, align: 'center' },
            ],
            list:[{}],
            options:''
          }
        },
       created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadWorktable()
         this.loadWorkers()
    },
      methods:{
        loadWorktable() {
      $.ajax({
        url: 'http://127.0.0.1:8000/worktable/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })},
        loadWorkers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/workers/',
        type: 'GET',
        success: (response) => {
          this.workers = response.data.data
          }
      })
    },
        deleteWorktable() {
      $.ajax({
        url: 'http://127.0.0.1:8000/worktable/',
        type: 'DELETE',
        data: {
          id: this.id,
        },
        success: (response) => {
          this.loadWorktable()
        },
        error: (response) => {
          if (response.status === 404) {
            alert('No assignment was found')
          }
        }
      })
    },
        addWorktable() {
      $.ajax({
        url: 'http://127.0.0.1:8000/worktable/',
        type: 'POST',
        data: {
          id: this.id,
          worker:this.worker,
          floor:this.floor,
          weekday:this.weekday,
        },
        success: (response) => {
          this.loadWorktable()
        }
      })
    },
         editWorktable() {
      $.ajax({
        url: 'http://127.0.0.1:8000/worktableq/',
        type: 'GET',
        data: {
          id: this.wt_id
        },
        success: (response) => {
          this.options = response.data
          this.wt_worker = response.data.data.worker
          this.wt_floor = response.data.data.floor
          this.wt_weekday = response.data.data.weekday
        },
        error: (response) => {
          if (response.status === 404) {
            alert('No assignment was found')
          }
        }
      })
    },    submitWorktable() {
      $.ajax({
        url: 'http://127.0.0.1:8000/worktable/',
        type: 'PUT',
        data: {
          id: this.wt_id,
          worker: this.wt_worker,
          floor: this.wt_floor,
          weekday: this.wt_weekday,
        },
        success: (response) => {
          this.loadWorktable()
          this.options = ''
        }
      })
    },handleSortChange ({name, order}) {
      this.list.data = this.list.data.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },goHome() {
      this.$router.push({name: "main"})
    }
    },}
</script>

<style>
.table-wrapper {
  text-align: center;
  margin-left: 313px;
  width: 740px;
}
.panel-wrapper {
  width: 740px;
}
.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}
</style>
