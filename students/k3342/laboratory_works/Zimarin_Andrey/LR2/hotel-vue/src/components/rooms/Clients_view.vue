<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="teal900">
      Просмотр клиентов гостиницы
      <mu-button flat @click="ClientFilt">Поиск клиентов по городу</mu-button>
      <mu-button flat @click="goHome"> На главную страницу </mu-button>
      </mu-appbar>
  <mu-row span="4" xl="2" class="clients-list">
    <mu-col v-for="client in clients" :key="client.id">
      <h3>Клиент - {{client.attributes.full_name}}</h3>
      <p> Паспорт: {{client.attributes.passport}}</p>
      <p> Город: {{client.attributes.city}}</p>
    </mu-col>
  </mu-row>
    <mu-col>
      <mu-button round @click="AddCl">Добавить клиента</mu-button>
    </mu-col>
  </mu-container>
</template>

<script>
  import $ from 'jquery'
    export default {
        name: "Clients_view",
        data() {
          return {
            clients: '',
            client_det: '',
            show: false
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadClients()
        },
        methods: {
          loadClients() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/clients/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.clients = response.data
              }
            })
          },
          goHome() {
            this.$router.push({name: "Home"})
          },
          AddCl() {
            this.$router.push({name: "AddClient"})
          },
          ClientFilt() {
            this.$router.push({name: "Client_filter"})
          },
        }
    }
</script>

<style scoped>
  .clients-list {
    margin: 20px;
  }
</style>
