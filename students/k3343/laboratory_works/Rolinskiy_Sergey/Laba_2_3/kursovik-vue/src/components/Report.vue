<template><div>
  <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#2065f0" textColor="white" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Compile a report over a chosen date interval</h1>
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
  <mu-container v-if="ans">

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="ans.clients" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.client_fio }}</td>
                <td class="is-center">{{ scope.row.client_room}}</td>
                <td class="is-center">{{ scope.row.client_home }}</td>
                <td class="is-center">{{ scope.row.client_days }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
    <h2>Over this date, the hotel accustomed {{ans.totalclients.toString()}} clients, and in total have generated {{ans.totalcost.toString()}} value</h2>
    <h4>More detailed information:</h4>
    <mu-container class="table-wrapper2">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns2" :data="ans.per_room" :sort.sync="sort" @sort-change="handleSortChange">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row[0] }}</td>
                <td class="is-center">{{ scope.row[1]}}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
    <ul><li style="text-align: left" v-for="i in ans.per_room.per_room ">
        {{i}}
    </li>
    </ul>

  </mu-container>
</div>
</template>

<script>
    import $ from 'jquery'
  export default {
    name: 'Report',
    data () {
      return {
        labelPosition: 'top',
        firstdate:'',
        seconddate:'',
        ans:NaN,
        columns:[
              { title: "Client name", name: 'client_fio', width: 230, align: 'center' },
              { title: "Room", name: 'client_room', width: 130, align: 'center' },
              { title: "Hometown", name: 'client_home', width: 180, align: 'center' },
              { title: "Days lived", name: 'client_days', width: 130, align: 'center',sortable:true },
            ],
        columns2:[
              { title: "Room", name: 'room', width: 130, align: 'center',sortable :true },
              { title: "Overall income", name: 'cost', width: 230, align: 'center' ,sortable:true},]
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
      handleSortChange ({name, order}) {
      this.list.data = this.list.data.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
    },
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
          url: 'http://127.0.0.1:8000/report/',
          type: 'GET',
          data: {
            firstdate: this.firstdate,
            seconddate:this.seconddate
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

  }}
.table-wrapper {
  text-align: center;
  align-self: center;
  width: 740px;
}
.table-wrapper2 {
  text-align: center;
  align-self: center;
  width: 400px;
  margin-bottom: 60px;
}
  .asa{
    margin-bottom: 100px;
  }
</style>
