<template>
    <mu-container>
    <mu-appbar style="width: 100%;" color="teal900">
      Поиск работников
      <mu-button flat @click="goHome"> На главную страницу </mu-button>
    </mu-appbar>
    <mu-form :model="form" label-width="100" label-position="left">
      <mu-form-item label="ФИО Клиента">
        <mu-text-field v-model="form.client"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="День недели">
          <mu-select v-model="form.day">
              <mu-option label="Понедельник" value="1"></mu-option>
              <mu-option label="Вторник" value="2"></mu-option>
              <mu-option label="Среда" value="3"></mu-option>
              <mu-option label="Четверг" value="4"></mu-option>
              <mu-option label="Пятница" value="5"></mu-option>
              <mu-option label="Суббота" value="6"></mu-option>
              <mu-option label="Воскресенье" value="7"></mu-option>
          </mu-select>
        </mu-form-item>
     <mu-button class="btn-send" round @click="Find_cl"> Найти</mu-button>
    </mu-form>
    <mu-col span="4" xl="2" class="worker">
      <div>
        <h3>Работник {{worker.full_name}}</h3>
        <p> Паспорт </p>
      </div>
    </mu-col>
  </mu-container>
</template>

<script>
    import $ from "jquery";
    export default {
      name: "Find_worker",
      data() {
          return {
            worker: '',
            client_id: '',
            floor: '',
            form: {
              client: '',
              day: ''
            }
          }
        },
        methods: {
          Find_cl() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/workers_filter/?full_name=" + this.form.client,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.client_id = response.data.id;
              }
            })
          },
          Find_Cleaning() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/cleanings_view/" + this.form.day,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.floor = response.data.data.floor;
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
