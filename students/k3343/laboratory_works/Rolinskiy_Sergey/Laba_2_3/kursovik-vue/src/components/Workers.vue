<template>
 <div><mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Workers of the hotel</h1>
    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list.data" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.fio }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
   <h2>To recruit a new worker, enter his full name below:</h2>
   <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="fio" placeholder="Enter the full name here" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br/>
            <mu-button color="#e6ddde" textColor="black" @click="addWorkers">Recruit</mu-button>
        <br/>
   <h2>To fire an existing worker, enter his ID below:</h2>
        <input v-model="id" type="text" placeholder="Worker's ID"/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteWorkers">Delete</mu-button>
        </mu-container>
 </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Workers",
        data(){
          return{
            id:'',
            fio:'',
            columns:[
              { title: "Worker number", name: 'id', width: 200, align: 'center' },
              { title: "Full name", name: 'fio', width: 400, align: 'center' },
            ],
            list:[{}],
            options:''
          }
        },
       created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " +
          sessionStorage.getItem('auth_token')},
    })
       this.loadWorkers()},
     methods: {
      loadWorkers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/workers/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },
       goHome() {
      this.$router.push({name: "main"})
    },
     addWorkers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/workers/',
        type: 'POST',
        data: {
          id: this.id,
          fio: this.fio,
        },
        success: (response) => {
          this.loadWorkers()
        }
      })
    },
      deleteWorkers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/workers/',
        type: 'DELETE',
        data: {
          id: this.id,
        },
        success: (response) => {
          this.loadWorkers()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No worker was found')
          }
        }
      })
    },
     }
    ,}
</script>

<style >
.table-wrapper {
  text-align: center;
  margin-left: 360px;
  width: 640px;
}
.panel-wrapper {
  width: 640px;
}
.button-wrapper4 {
  text-align: left;}
  .mu-button{
    margin: 8px;
  }
  h1 {
        margin-top: 50px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        font-family: 'Questrial', sans-serif;
        text-align: center;
}
</style>
