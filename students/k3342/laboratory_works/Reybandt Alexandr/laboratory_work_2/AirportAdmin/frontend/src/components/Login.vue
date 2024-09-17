<template>
    <div class="container">
        <div>
            <h2 class="mt-4 mb-3">Авторизация</h2>
            <div class="form-group">
                <label for="login">Логин</label>
                <input class="form-control" id="login" v-model="login" type="text" placeholder="Введите логин"/>
            </div>
            <div class="form-group">
                <label for="password">Пароль</label>
                <input class="form-control" id="password" v-model="password" type="password"
                       placeholder="Введите пароль"/>
            </div>
            <button class="btn btn-primary" @click="setLogin">Войти</button>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/flight/accounts/login/',
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        localStorage.setItem("token", response.token)
                        localStorage.setItem("id", response.user_id)
                        // console.log(localStorage.getItem('id'))
                        this.$router.push({name: "Profile"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert('Введен неверный логин или пароль.')
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>