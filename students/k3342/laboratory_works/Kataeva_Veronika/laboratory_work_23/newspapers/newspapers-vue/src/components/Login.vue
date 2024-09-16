<template>
  <div>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <h1>Please, input your username and password</h1>
    <input v-model="username" type="text" placeholder="Username"/>
    <input v-model="password" type="password" placeholder="Password"/>
    <br/>
    <br/>
    <mu-container class="button-wrapper">
    <mu-button color="#e6ddde" textColor="#403F3F" @click="setLogin">Sign In</mu-button>
    </mu-container>
    <br/>
    Don't have an account? Please, 
    <a href="http://localhost:8080/#/signup">Sign Up</a>.
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
  name: "Login",
  data() {
    return {
        username: '',
        password: '',

    }
  },
  methods: {
    setLogin() {
        $.ajax({
            url: "http://127.0.0.1:8000/auth/token/login/",
            type: "POST",
            data: {
                        username: this.username,
                        password: this.password
                    },
            success: (response) => {
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
            },
            error: (response) => {
                if (response.status === 400) {
                    alert('Login or password is incorrect')
            }}
        })

    },
  }

}
</script>

<style scoped>
    h1 {
        margin-top: 180px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        font-family: 'Questrial', sans-serif;
        text-align: center;
}
</style>

