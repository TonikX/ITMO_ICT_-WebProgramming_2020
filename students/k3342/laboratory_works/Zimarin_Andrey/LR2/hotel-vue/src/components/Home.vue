<template>
  <mu-container>
      <mu-appbar style="width: 100%;" color="teal900">
        Система управления гостиницей
      <mu-button flat v-if="auth" @click="goClients">Просмотр клиентов</mu-button>
      <mu-button flat v-if="auth" @click="goWorkers">Просмотр работников</mu-button>
      <mu-button flat v-if="auth" @click="AddCh">Поселить клиента</mu-button>
      <mu-button flat v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat v-else @click="Logout">Выход</mu-button>
      </mu-appbar>
    <mu-row>
      <h1></h1>
    </mu-row>
    <mu-row v-if="auth">
      <mu-button v-if="show" @click="Full">Только занятые</mu-button>
      <mu-button v-if="show" @click="NotFull">Только свободные</mu-button>
    </mu-row>
      <h3 v-if="!auth" > Войдите или зарегистрируйтесь, чтобы начать работу</h3>
      <div v-if="auth" v-for="room in rooms" :key="room.room_number">
        <Rooms v-bind:room="room.room_number"></Rooms>
      </div>
  </mu-container>
</template>

<script>
    import Rooms from './rooms/Rooms'
    import $ from "jquery";
    export default {
        name: "Home",
        components: {
          Rooms
        },
        data() {
          return {
            rooms: '',
            show: false,
          }
        },
        computed: {
          auth() {
            if (sessionStorage.getItem('auth_token')) {
              return true
            }
          }
        },
        created() {
          this.loadRooms()
        },
      methods: {
            async loadRooms() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/rooms/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.rooms = response.data.data
              }
            })
            },
            goLogin() {
                this.$router.push({name: "login"})
            },
            Logout() {
              sessionStorage.removeItem('auth_token');
              window.location = '/'
            },
            goClients() {
                this.$router.push({name: "Clients_view"})
            },
            goWorkers() {
                this.$router.push({name: "Workers_view"})
            },
            AddCh() {
                this.$router.push({name: "Add_checkin"})
            },
        },
    }
</script>

<style scoped>

</style>
