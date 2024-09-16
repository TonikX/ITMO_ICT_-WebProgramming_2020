<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>REPORT</h1>

    <div v-for="answer in answers">
      <h2>{{ answer.name }}</h2>
      {{ answer.print_runs }} newspapers in total
      <br/>
      <br/>
      
      <i>For each newspaper:</i>
      <div v-for="paper in answer.papers_run">
        {{ paper.name }}: {{ paper.print_run }} copies
      </div>
    
      <br/>
      <i>Newspapers distribution:</i>
      <div v-for="paper in answer.papers_offices">
        {{ paper.name }}: {{ paper.print_run }} copies for Post Office №{{ paper.number }} ({{ paper.address }})
      </div>
      <br/>
      <br/>
    </div>
    <br/>
    <br/>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Report',
  data () {
    return {
      answers: [],
      name: '',
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadReport()
  },
  methods: {
    loadReport() {
      $.ajax({
        url: 'http://127.0.0.1:8000/report/',
        type: 'GET',
        success: (response) => {
          this.answers = response.data.data
        },
        error: (response) => {
          alert("None of printing houses was found")
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
  margin-bottom: 50px;
}

h2 {
  font-size: 130%;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center; 
}

.demo-divider-form {
  padding: 0 16px;
}

.table-wrapper {
  text-align: center;
  margin-left: 325px;
  width: 468px;
}

.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}
</style>
