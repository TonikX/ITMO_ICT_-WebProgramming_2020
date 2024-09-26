<template>
  <mu-container>
      <mu-appbar style="width: 100%;" color="teal900">
      Поселить клиента
      <mu-button flat slot="right" @click="goHome"> На главную страницу </mu-button>
      </mu-appbar>
    <div>
      <p></p>
    </div>
    <div>
      <mu-form :model="form" label-width="100">
        <mu-form-item label="Комната">
          <mu-select v-model="form.room">
            <mu-option v-for="room in rooms" :key="room.id" :label="room.room_number"
                    :value="room.id">
            </mu-option>
          </mu-select>
        </mu-form-item>

        <mu-form-item label="Клиент">
          <mu-select v-model="form.client">
            <mu-option v-for="client in clients" :key="client.attributes.id" :label="client.attributes.full_name"
                  :value="client.id">
            </mu-option>
          </mu-select>
        </mu-form-item>

        <mu-form-item label="Дата заезда">
          <label>
            <input type="date" v-model="form.date_in"></input>
          </label>
        </mu-form-item>

        <mu-form-item label="Дата выезда">
          <label>
            <input type="date" v-model="form.date_out"></input>
          </label>
        </mu-form-item>

       <mu-button class="btn-send" round @click="AddCh"> Подтвердить заселение</mu-button>
      </mu-form>
    </div>

  </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
      name: "Add_checkin",
      data() {
          return {
            clients: '',
            rooms: '',
            form: {
              room: '',
              client: '',
              date_in: '',
              date_out: '',
                }
          }
      },
      created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadClients();
          this.loadRooms()
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
        loadRooms() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/rooms/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.rooms = response.data.data
              }
            })
        },
        AddCh() {
          $.ajax({
            url: "http://127.0.0.1:8000/app/hotel/checkin/",
            type: "POST",
            data: {
              room: this.form.room,
              client: this.form.client,
              date_in: this.form.date_in,
              date_out: this.form.date_out
            },
            success: (response) => {
              alert("Клиент заселен успешно");
              this.$router.push({name: "Home"})
            },
            error: (response) => {
              alert("Ошибка при заселении");
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
