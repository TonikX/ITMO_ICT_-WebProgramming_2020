<template>
    <div class="container">
        <h2 class="mt-4 mb-3">Регистрация</h2>
        <div class="form-group">
            <label for="login">Логин</label>
            <input class="form-control" id="login" v-model="username" type="text"
                   required="" placeholder="Придумайте логин"/>
        </div>

        <div class="form-group">
            <label for="first_name">Имя</label>
            <input class="form-control" id="first_name" v-model="first_name" type="text"
                   required="" placeholder="Введите свое имя"/>
        </div>

        <div class="form-group">
            <label for="last_name">Фамилия</label>
            <input class="form-control" id="last_name" v-model="last_name" type="text"
                   required="" placeholder="Введите свою фамилию"/>
        </div>

        <div class="form-group">
            <label for="age">Возраст</label>
            <input class="form-control" id="age" v-model="age" type="text"
                   required="" placeholder="Введите свое возраст"/>
        </div>

        <div class="form-group">
            <label for="passport_number">Паспортные данные</label>
            <input class="form-control" id="passport_number" v-model="passport_number" type="text"
                   required="" placeholder="Введите свои паспортные данные"/>
        </div>

        <div class="form-group">
            <label for="password">Пароль</label>
            <input class="form-control" id="password" v-model="password" type="password"
                   required="" placeholder="Придумайте пароль"/>
        </div>
        <button type="button" class="btn btn-success" @click="userRegistration()">Зарегистрироваться</button>
    </div>
</template>

<script>
    export default {
        name: "Registration",
        data() {
            return {
                username: '',
                password: '',
                first_name: '',
                last_name: '',
                age: '',
                passport_number: '',
            }
        },
        methods: {
            async userRegistration() {
                let data = {
                    username: this.username,
                    password: this.password,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    age: this.age,
                    passport_number: this.passport_number,
                }
                fetch(`${this.$store.getters.getServerUrl}/flight/accounts/register/`,
                    {
                        method: "POST",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    }
                ).then(async response => {
                    const resp = await response.json();
                    localStorage.setItem("id", response.id)
                    console.log(localStorage.getItem("id"))

                    if (resp.response) {
                        alert('Вы успешно зарегистрированы!')
                        this.clearForm();
                        this.$router.push({name: 'Login'});
                    } else {
                        alert('Ууууу-пс! Что-то пошло не так..')
                        console.log(JSON.stringify(resp));
                    }
                })
            },
            clearForm() {
                this.username = ''
                this.password = ''
                this.first_name = '',
                    this.last_name = '',
                    this.age = '',
                    this.passport_number = ''
            }
        },
    }
</script>

<style scoped>

</style>