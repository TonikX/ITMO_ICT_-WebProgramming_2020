<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>In-Stocks</h1>

    <mu-container class="table-wrapper">
      <mu-row gutter>
        <mu-col >
          <mu-paper :z-depth="1">
            <mu-data-table stripe :columns="columns" :data="list">
              <template slot-scope="scope">
                <td class="is-center">{{ scope.row.id }}</td>
                <td class="is-center">{{ scope.row.print_run }}</td>
                <td class="is-center">{{ scope.row.newspaper }}</td>
                <td class="is-center">{{ scope.row.post_office }}</td>
                <td class="is-center">{{ scope.row.printing_house }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-col>
      </mu-row>
    </mu-container>
    <br/>
    <br/>

    <mu-container class="panel-wrapper">
      <mu-expansion-panel :expand="panel === 'panel1'" @change="toggle('panel1')">
        <div slot="header" style="color: #581845">Delete</div>
        In order to delete a record of in-stock, please, enter its id.
        <br/>
        <br/>
        <input v-model="pk" type="text" placeholder=""/>
        <br/>
        <br/>
        <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
          <mu-button color="#e6ddde" textColor="black" @click="deleteStock">Input</mu-button>
        </mu-container>
      </mu-expansion-panel>
      
      <mu-expansion-panel :expand="panel === 'panel2'" @change="toggle('panel2')">
        <div slot="header" style="color: #581845">Add</div>
          In order to add a new record of in-stock, please, enter information about it.
          <br/>
          <br/>
          <mu-container>
            <mu-paper :z-depth="1">
              <mu-text-field v-model="print_run" placeholder="Print Run" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br/>
          <p>Newspaper Name: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select class="options-wrapper" v-model="newspaper">
            <mu-option v-for="newspaper,newspaper_i in newspapers" :key="newspaper" :label="newspaper" :value="newspaper"></mu-option>
          </mu-select>
          </p>
          <p>Post Office Number: &nbsp; &nbsp; &nbsp;
          <mu-select class="options-wrapper" v-model="post_office">
            <mu-option v-for="post_office,post_office_i in post_offices" :key="post_office" :label="post_office" :value="post_office"></mu-option>
          </mu-select>
          </p>
          <p>Printing House Name: &nbsp;
          <mu-select class="options-wrapper" v-model="printing_house">
            <mu-option v-for="printing_house,printing_house_i in printing_houses" :key="printing_house" :label="printing_house" :value="printing_house"></mu-option>
          </mu-select>
          </p>
          <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="addStock">Input</mu-button>
          </mu-container>
      </mu-expansion-panel>

      <mu-expansion-panel :expand="panel === 'panel3'" @change="toggle('panel3')">
        <div slot="header" style="color: #581845">Edit</div>
          In order to edit a record of in-stock, please, enter its id.
          <br/>
          <br/>
          <input v-model="stock_id" type="text" placeholder=""/>
          <br/>
          <br/>
          <mu-container v-if="!options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="editStock">Input</mu-button>
          </mu-container>
          
          <mu-container v-if="options">
            <mu-paper :z-depth="1">
              <mu-text-field v-model="stock_run" placeholder="Print Run" solo full-width class="demo-divider-form"></mu-text-field>
              <mu-divider></mu-divider>
            </mu-paper>
          </mu-container>
          <br v-if="options"/>
          <p v-if="options">Newspaper Name: &nbsp; &nbsp; &nbsp; &nbsp;
          <mu-select v-if="options" class="options-wrapper" v-model="stock_paper">
            <mu-option v-for="stock_paper,stock_paper_i in newspapers" :key="stock_paper" :label="stock_paper" :value="stock_paper"></mu-option>
          </mu-select>
          </p>
          <p v-if="options">Post Office Number: &nbsp; &nbsp; &nbsp;
          <mu-select v-if="options" class="options-wrapper" v-model="stock_office">
            <mu-option v-for="stock_office,stock_office_i in post_offices" :key="stock_office" :label="stock_office" :value="stock_office"></mu-option>
          </mu-select>
          </p>
          <p v-if="options">Printing House Name: &nbsp;
          <mu-select v-if="options" class="options-wrapper" v-model="stock_house">
            <mu-option v-for="stock_house,stock_house_i in printing_houses" :key="stock_house" :label="stock_house" :value="stock_house"></mu-option>
          </mu-select>
          </p>
          <mu-container v-if="options" class="button-wrapper3" style="margin-bottom: 50px ">
            <mu-button color="#e6ddde" textColor="black" @click="submitStock">Input</mu-button>
          </mu-container>

      </mu-expansion-panel>
    </mu-container>
    <br/>
    <br/>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'InStocks',
  data () {
    return {
      labelPosition: 'top',
      panel: '',
      pk: '',
      id: '',
      stock_id: '',
      stock_run: '',
      stock_paper: '',
      stock_office: '',
      stock_house: '',
      print_run: '',
      newspaper: '',
      post_office: '',
      post_offices: '',
      printing_house: '',
      printing_houses: '',
      newspapers: '',
      options: '',
      columns: [
        { title: 'In-Stock ID', name: 'id', width: 130, align: 'center' },
        { title: 'Print Run', name: 'print_run', width: 140, align: 'center' },
        { title: 'Newspaper Name', name: 'newspaper', width: 260, align: 'center' },
        { title: 'Post Office Number', name: 'post_office', width: 135, align: 'center' },
        { title: 'Printing House Name', name: 'printing_house', width: 230, align: 'center' }
        ],
      list: [{}],
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadStocks()
    this.loadPapers()
    this.loadOffices()
    this.loadHouses()
  },
  methods: {
    loadStocks() {
      $.ajax({
        url: 'http://127.0.0.1:8000/instocks/',
        type: 'GET',
        success: (response) => {
          this.list = response.data.data
          }
      })
    },
    toggle (panel) {
      this.panel = panel === this.panel ? '' : panel;
    },
    deleteStock() {
      $.ajax({
        url: 'http://127.0.0.1:8000/instocks/',
        type: 'DELETE',
        data: {
          pk: this.pk,
        },
        success: (response) => {
          this.loadStocks()
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No in-stock was found')
          }
        }
      })
    },
    loadPapers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/newspapers/',
        type: 'GET',
        success: (response) => {
          this.newspapers = response.data
          }
      })
    },
    loadOffices() {
      $.ajax({
        url: 'http://127.0.0.1:8000/offices/',
        type: 'GET',
        success: (response) => {
          this.post_offices = response.data
          }
      })
    },
    loadHouses() {
      $.ajax({
        url: 'http://127.0.0.1:8000/houses/',
        type: 'GET',
        success: (response) => {
          this.printing_houses = response.data
          }
      })
    },
    addStock() {
      $.ajax({
        url: 'http://127.0.0.1:8000/instocks/',
        type: 'POST',
        data: {
          id: this.id,
          newspaper: this.newspaper,
          post_office: this.post_office,
          printing_house: this.printing_house,
          print_run: this.print_run
        },
        success: (response) => {
          this.loadStocks()
        }
      })
    },
    editStock() {
      $.ajax({
        url: 'http://127.0.0.1:8000/instock/',
        type: 'GET',
        data: {
          id: this.stock_id
        },
        success: (response) => {
          this.options = response.data
          this.stock_run = response.data.data.print_run
          this.stock_paper = response.data.data.newspaper
          this.stock_office = response.data.data.post_office
          this.stock_house = response.data.data.printing_house
        }
        ,
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
        }
      })
    },
    submitStock() {
      $.ajax({
        url: 'http://127.0.0.1:8000/instocks/',
        type: 'PUT',
        data: {
          id: this.stock_id,
          print_run: this.stock_run,
          newspaper: this.stock_paper,
          post_office: this.stock_office,
          printing_house: this.stock_house
        },
        success: (response) => {
          this.loadStocks()
          this.options = ''
        }
      })
    },
    goHome() {
      this.$router.push({name: "home"})
    }
  }
}
</script>

<style>
body {
  background-color: #f4f4f4;
}

h1 {
  font-size: 180%;
  line-height: 0px;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center;
  margin-bottom: 60px;
}

p {
  font-size: 90%;
}

.demo-divider-form {
  font-size: 90%;
  padding: 0 16px;
  height: 30px;
}

.table-wrapper {
  text-align: center;
  margin-left: 176px;
  width: 911px;
}

.panel-wrapper {
  width: 911px;
}

.options-wrapper {
  font-size: 100%
}
</style>
