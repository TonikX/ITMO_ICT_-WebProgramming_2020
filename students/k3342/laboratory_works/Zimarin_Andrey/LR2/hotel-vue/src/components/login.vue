<template>
  <mu-container>
  <div class="title">
    <h2> Войдите в свой аккаунт </h2>
  </div>
    <div class="login">
      <mu-text-field v-model="username" label="Логин"></mu-text-field>
      <mu-text-field v-model="password" type="password" label="Пароль"></mu-text-field>
        <button @click="setLogin">Войти</button>
    </div>
  <div v-if="show">
    <h4> Либо заполните форму для регистрации </h4>
  </div>
  <div class="registr" v-if="show">
    <mu-form :model="form">
      <mu-form-item label="Ваше ФИО">
        <mu-text-field v-model="form.name"></mu-text-field>
      </mu-form-item>

      <mu-form-item label="Имя пользователя">
        <mu-text-field v-model="form.username"></mu-text-field>
      </mu-form-item>

      <mu-form-item label="Ваш email">
        <label>
           <mu-text-field v-model="form.email"></mu-text-field>
        </label>
      </mu-form-item>

      <mu-form-item label="Пароль">
        <label>
           <mu-text-field type="password" v-model="form.password"></mu-text-field>
        </label>
      </mu-form-item>

     <mu-button class="btn-send" round @click="Registr"> Зарегистрироваться </mu-button>
    </mu-form>
  </div>
  </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                show: true,
                username: '',
                password: '',
                form: {
                  name: '',
                  username: '',
                  email: '',
                  password: '',
                }
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
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                        this.$router.push({name: "Home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
            Registr() {
              $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.form.username,
                        email: this.form.email,
                        password: this.form.password
                    },
                    success: (response) => {
                        this.show = false;
                        this.$router.push({name: "login"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Пароль не соответствует требованиям! (В нем меньше 8 знаков либо он похож на имя пользователя)")
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>
</style>
