<template>
    <div>
      <h1>Please, enter your username and password:</h1>
      <input v-model="login" type="text" placeholder="Логин"/>
      <input v-model="password" type="password" placeholder="Пароль"/>
      <br/>
      <br/>
      <mu-container class="button-wrapper"><mu-button color="#e6ddde" textColor="#403F3F"@click="setLogin">Sign in</mu-button>
      </mu-container></div>
</template>

<script>
      import $ from 'jquery'
    export default {
        name: "Login",
      data(){
          return {
            login: '',
            password: '',
          }
      },
      methods:{
          setLogin(){
            $.ajax({
              url: "http://127.0.0.1:8000/auth/token/login/",
              type: "POST",
              data:{
                username: this.login,
                password: this.password,
              } ,
              success: (response)=>{
                sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                this.$router.push({name: "main"})
              },
              error: (response)=>{
                if (response.status === 400) {
                    alert('Login or password is incorrect')}
              }})
      }
    },}
</script>

<style >
 h1 {
        margin-top: 180px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        text-align: center;
}
</style>
