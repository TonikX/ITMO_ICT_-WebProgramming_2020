<template>
<div>
  <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>All-time clients list</h1>
    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list.data" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.fio }}</td>
                <td class="is-center">{{ scope.row.hometown }}</td>
                <td class="is-center">{{ scope.row.passport }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
    <br/>
    <br/>

  </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Clients",
        data(){
          return{
            fio:'',
            hometown: '',
            passport:'',
            columns:[
              { title: "Client ID", name: 'id', width: 50, align: 'center' },
              { title: "Client full name", name: 'fio', width: 230, align: 'center' },
              { title: "Client's hometown", name: 'hometown', width: 180, align: 'center' },
              { title: "Passport number", name: 'passport', width: 180, align: 'center' },
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
    this.loadClients()
  },
    methods:{
       loadClients() {
      $.ajax({
        url: 'http://127.0.0.1:8000/clients/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },goHome() {
      this.$router.push({name: "main"})
    }
    }

    }
</script>

<style >
 h1 {
        margin-top: 50px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        font-family: 'Questrial', sans-serif;
        text-align: center;
}
  .demo-divider-form {
  font-size: 90%;
  padding: 0 16px;
  height: 30px;
}
.table-wrapper {
  text-align: center;
  margin-left: 360px;
  width: 640px;
}
.panel-wrapper {
  width: 640px;
}
.button-wrapper4 {
  text-align: left;

 .mu-button {
   margin: 8px;
 }

 }
</style>
