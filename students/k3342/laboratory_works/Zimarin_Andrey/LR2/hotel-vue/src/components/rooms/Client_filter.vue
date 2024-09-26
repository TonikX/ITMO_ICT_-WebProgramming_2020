<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="teal900">
      Поиск клиентов по городу
      <mu-button flat @click="goHome"> На главную страницу </mu-button>
    </mu-appbar>
    <mu-form :model="form" label-width="100" label-position="left">
      <mu-form-item label="Город">
        <mu-text-field v-model="form.city"></mu-text-field>
      </mu-form-item>
     <mu-button class="btn-send" round @click="Filter"> Найти</mu-button>
    </mu-form>
    <mu-col span="4" xl="2" class="clients-list">
      <div v-for="client in clients">
        <h3>Клиент {{client.attributes.full_name}}</h3>
        <p> Паспорт {{client.attributes.passport}}</p>
        <p> Город {{client.attributes.city}}</p>
      </div>
    </mu-col>
  </mu-container>
</template>

<script>
    import $ from "jquery";

    export default {
        name: "Client_filter",
        data() {
          return {
            clients: '',
            form: {
              city: ''
            }
          }
        },
        methods: {
          Filter() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/clients_filter/?city=" + this.form.city,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.clients = response.data;
              }
            })
          },
          goHome() {
            this.$router.push({name: "Home"})
          },
        }
    }
</script>

<style scoped>

</style>
