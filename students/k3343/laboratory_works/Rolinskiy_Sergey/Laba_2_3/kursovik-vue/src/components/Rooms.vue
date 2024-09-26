<template>
  <div>
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Rooms of the hotel</h1>
    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list.data" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.number }}</td>
                <td class="is-center">{{ scope.row.type }}</td>
                <td class="is-center">{{ scope.row.cost }}</td>
                <td class="is-center">{{ scope.row.phone }}</td>
                <td class="is-center">{{ scope.row.floor }}</td>
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
        name: "Rooms",
        data(){
          return{
            sort: {
        name: '',
        order: 'asc'
      },
            number:'',
            type: '',
            cost:'',
            phone:'',
            floor:'',
            columns:[
              { title: "Room number", name: 'number', width: 100, align: 'center' ,sortable:true},
              { title: "Room type", name: 'type', width: 150, align: 'center' ,sortable:true},
              { title: "Daily cost", name: 'cost', width: 100, align: 'center' ,sortable:true},
              { title: "Room telephone number", name: 'phone', width: 180, align: 'center' },
              { title: "Floor", name: 'floor', width: 80, align: 'center',sortable:true },
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
    this.loadRooms()
  },
    methods:{
          handleSortChange ({name, order}) {
      this.list.data = this.list.data.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
       loadRooms() {
      $.ajax({
        url: 'http://127.0.0.1:8000/rooms/',
        type: 'GET',
        success: (response) => {
          this.list = response.data
          }
      })
    },
      goHome() {
      this.$router.push({name: "main"})
    }
    }
    }
</script>

<style scoped>
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
  .mu-button{
    margin: 8px;
  }
}
</style>
