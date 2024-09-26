<template>
  <div> <link href="https://fonts.googleapis.com/css2?family=Montserrat+Subrayada&display=swap" rel="stylesheet">
    <h1>Hotel administrator management system</h1>
    <mu-container class="button-wrapper"><mu-button @click="goLogin">Вход</mu-button>
    </mu-container>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods:{
    goLogin(){
      this.$router.push({name:"login"})
    }
  }}
</script>

<style>
body {
  background-color: #f4f4f4;
}
h1 {
  font-size: 350%;
  line-height: 100px;
  color: #000000;
  text-align: center;
}
.button-wrapper {
  text-align: center;
  .mu-button{
    margin: 8px;
  }
}
</style>
