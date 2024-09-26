<template>
<mu-container>
      <mu-appbar style="width: 100%;" color="teal900">
      Добавление клиента
      <mu-button flat slot="right" @click="goHome"> На главную страницу </mu-button>
      </mu-appbar>
    <div>
      <p></p>
    </div>
    <div>
      <mu-form :model="form" label-width="100">
        <mu-form-item label="ФИО клиента">
          <mu-text-field v-model="form.name"></mu-text-field>
        </mu-form-item>

        <mu-form-item label="Номер паспорта">
          <mu-text-field v-model="form.passport"></mu-text-field>
        </mu-form-item>

        <mu-form-item label="Город">
          <label>
             <mu-text-field v-model="form.city"></mu-text-field>
          </label>
        </mu-form-item>

       <mu-button class="btn-send" round @click="AddCl"> Подтвердить добавление</mu-button>
      </mu-form>
    </div>

  </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "AddClient",
        data() {
            return {
              form: {
                name: '',
                passport: '',
                city: '',
                  }
            }
        },
        methods: {
          AddCl() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/clients/",
              type: "POST",
              data: {
              full_name: this.form.name,
              passport: this.form.passport,
              city: this.form.city
              },
              success: (response) => {
                  alert("Клиент добавлен");
                  this.$router.push({name: "Clients_view"})
              },
              error: (response) => {
                  alert("Ошибка")
              }
          })
          },
          goHome() {
            this.$router.push({name: "Home"})
          }
        }
    }
</script>

<style scoped>

</style>
