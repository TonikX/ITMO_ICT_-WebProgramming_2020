<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">

    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>

    <h1>At what addresses are newspapers of the given name printed?</h1>
    
    <mu-select v-model="name">
      <mu-option v-for="option,index in options" :key="option" :label="option" :value="option"></mu-option>
    </mu-select>
   
    <mu-container class="button-wrapper3" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="loadAnswer">Input</mu-button>
    </mu-container>

    <div v-for="answer in answers">
      <mu-container style="text-align: center">
        <mu-paper class="demo-paper" :z-depth="1" style="padding: 15px">{{ answer.attributes.address }}</mu-paper>
      </mu-container>
    </div>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Request1',
  data () {
    return {
      options: [],
      labelPosition: 'top',
      name: '',
      answers: []
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    }),
    this.loadNewspapers()
  },
  methods: {
    loadNewspapers() {
      $.ajax({
        url: 'http://127.0.0.1:8000/newspapers/',
        type: 'GET',
        success: (response) => {
          this.options = response.data
          }
      })
    },
    loadAnswer() {
      $.ajax({
        url: 'http://127.0.0.1:8000/request1/',
        type: 'GET',
        data: {
          name: this.name,
        },
        success: (response) => {
          this.answers = response.data
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
  line-height: 100px;
  color: #000000;
  font-family: 'Questrial', sans-serif;
  text-align: center;
}

.demo-paper {
  width: 200px;
  position: relative;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 50px;
  margin-bottom: 10px;
}

.mu-demo-form {
  width: 100%;
  max-width: 460px;
}

.button-wrapper4 {
  text-align: left;
  .mu-button{
    margin: 8px;
  }
}

</style>
