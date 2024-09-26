<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="teal900">
      Список работников гостиницы
      <mu-button flat @click="goHome"> На главную страницу </mu-button>
      </mu-appbar>
      <div v-for="worker in workers" :key="worker.id">
        <mu-col class="worker">
        <h3>Работник: {{worker.attributes.full_name}}</h3>
        <Timetable v-bind:worker="worker.id"> </Timetable>
        <mu-button round @click="DelWorker(worker.id)">Удалить работника</mu-button>
        </mu-col>
      </div>
    <p> </p>
        <mu-button color="success" @click="ChangeTime">Изменить расписание</mu-button>
        <ChangeTT v-if="show"></ChangeTT>
        <mu-button color="success" @click="Addworker">Добавить работника</mu-button>
        <AddWorker v-if="show2"> </AddWorker>
  </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Timetable from './Timetable'
    import AddWorker from "./AddWorker";
    import ChangeTT from "./ChangeTT";

    export default {
        name: "Workers_view",
        components: {
          AddWorker,
          Timetable, ChangeTT
        },
        data() {
          return {
            workers: '',
            show: false,
            show2: false
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadWorkers()
        },
        methods: {
          loadWorkers() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/workers/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.workers = response.data
              }
            })
          },
          Addworker() {
            this.show2 = true
          },
          DelWorker(id) {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/del_worker/" + id,
              type: "POST",
              success: (response) => {
                  alert("Работник удален");
              },
              error: (response) => {
                  alert("Ошибка")
              }
          })
          },
          ChangeTime() {
            this.show = true
          },
          goHome() {
            this.$router.push({name: "Home"})
          }
        }
    }
</script>

<style scoped>

</style>
