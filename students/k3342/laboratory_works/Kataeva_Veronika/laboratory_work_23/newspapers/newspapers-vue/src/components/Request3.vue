<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper4" style="margin-bottom: 50px ">
      <mu-button color="#e6ddde" textColor="black" @click="goHome">Home</mu-button>
    </mu-container>
    <h1>Which post offices (addresses) receive newspapers with a price higher than the indicated?</h1>
    <br/>

    <input v-model="price" type="text" placeholder="Please, input the value of price" style="width: 240px"/>
    <br/>
    <br/>
    <br/>
   
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
  name: 'Request3',
  data () {
    return {
      options: [],
      labelPosition: 'top',
      price: '',
      answers: []
    }
  },
  created () {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    })
  },
  methods: {
    loadAnswer() {
      $.ajax({
        url: 'http://127.0.0.1:8000/request3/',
        type: 'GET',
        data: {
          price: this.price,
        },
        success: (response) => {
          this.answers = response.data
          },
        error: (response) => {
          if (response.status === 404) {
            alert('No post office was found')
          }
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
