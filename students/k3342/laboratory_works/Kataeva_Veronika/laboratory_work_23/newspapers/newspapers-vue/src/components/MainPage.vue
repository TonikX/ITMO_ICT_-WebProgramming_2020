<template>
  <div>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat+Subrayada&display=swap" rel="stylesheet">
    <h1>NEWSPAPERS &nbsp; SYSTEM</h1>
    <mu-container class="button-wrapper">
      <mu-button color="#e6ddde" textColor="black" @click=goLogin>Sign In</mu-button>
    </mu-container>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  methods: {
    goLogin() {
      this.$router.push({name: "login"})
    }
  }
}
</script>

<style>
body {
  background-color: #f4f4f4;
}

h1 {
  font-size: 500%;
  line-height: 400px;
  color: #000000;
  font-family: 'Montserrat Subrayada', sans-serif;
  text-align: center;
}
.button-wrapper {
  text-align: center;
  .mu-button{
    margin: 8px;
  }
}

</style>
