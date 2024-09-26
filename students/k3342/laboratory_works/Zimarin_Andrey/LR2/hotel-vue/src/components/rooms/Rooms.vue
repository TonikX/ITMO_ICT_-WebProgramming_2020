<template>
  <mu-card>
    <mu-row xl="2" class="rooms-list">
      <mu-col class="room_num">
        <mu-card-header style="text-align: center; font-size: 20px"> Комната {{room_det.room_number}}</mu-card-header>
      </mu-col>
      <mu-col class="room_type" color="teal200">
          <h4>Этаж: {{room_det.floor}}</h4>
          <h4>Телефон: {{room_det.phone}}</h4>
          <h4>Цена за сутки: {{room_det.price}}</h4>
          <h4>Тип номера: {{room_det.type}}</h4>
      </mu-col>
      <div class="button">
        <mu-button flat color="success" @click="ShHistory" v-if="!show">История заселений</mu-button>
        <mu-button flat color="success" @click="HideHistory" v-if="show"> Скрыть историю </mu-button>
      </div>
      <mu-col v-for="ch in room_det.checkins" :key="ch.id" v-if="show">
        <ul>
          <li> Клиент: {{ch.client}}</li>
          <li> Дата въезда: {{ch.date_in}}</li>
          <li> Дата выезда: {{ch.date_out}}</li>
        </ul>
      </mu-col>
    </mu-row>
  </mu-card>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Rooms",
      props: ['room'],
        data() {
          return {
            room_det: '',
            checkins: '',
            show: false
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadRoom()
        },
        methods: {
          loadRoom() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/room_detail/" + this.room,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.room_det = response.data.data
              }
            })
          },
          ShHistory() {
            this.show = true
          },
          HideHistory() {
            this.show = false
          }
        }
    }
</script>

<style scoped>
  .button {
    margin: 10px;
  }
  .room_type {
    background: #80cbc4;
    margin: 10px;
  }
</style>
