<template>
 <mu-container>
    <div>
      <p>{{worker}}</p>
    </div>
    <div>
      <mu-form :model="form" label-width="100">
        <mu-form-item label="Работник">
          <mu-select v-model="form.worker">
            <mu-option v-for="w in workers" :key="w.id" :label="w.attributes.full_name"
                  :value="w.id">
            </mu-option>
          </mu-select>
        </mu-form-item>

        <mu-form-item label="Этаж">
          <mu-select v-model="form.floor">
            <mu-option v-for="fl in floors" :key="fl.id" :label="fl.floor_num"
                  :value="fl.id">
            </mu-option>
          </mu-select>
        </mu-form-item>

        <mu-form-item label="День недели">
          <mu-select v-model="form.day">
              <mu-option label="Понедельник" value="Пон"></mu-option>
              <mu-option label="Вторник" value="Вт"></mu-option>
              <mu-option label="Среда" value="Ср"></mu-option>
              <mu-option label="Четверг" value="Чт"></mu-option>
              <mu-option label="Пятница" value="Пт"></mu-option>
              <mu-option label="Суббота" value="Сб"></mu-option>
              <mu-option label="Воскресенье" value="Вс"></mu-option>
          </mu-select>
        </mu-form-item>

       <mu-button class="btn-send" round @click="AddTime"> Подтвердить расписание</mu-button>
      </mu-form>
    </div>

  </mu-container>
</template>

<script>
  import $ from 'jquery'
  export default {
      name: "ChangeTT",
      data() {
          return {
            floors: '',
            workers: '',
            form: {
              worker: '',
              day: '',
              floor: ''
                }
          }
      },
      created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadFloors();
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
        loadFloors() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/floors/",
              type: "GET",
              success: (response) => {
                console.log(response);
                this.floors = response.data.data
              }
            })
        },
        AddTime() {
          $.ajax({
            url: "http://127.0.0.1:8000/app/hotel/cleanings/" + this.form.worker,
            type: "POST",
            data: {
              worker: this.form.worker,
              day_of_week: this.form.day,
              floor: this.form.floor
            },
            success: (response) => {
              alert("Расписание изменено успешно");
              this.$router.push({name: "Workers_view"})
            },
            error: (response) => {
              alert("Ошибка при изменении расписания");
            }
          })
        }
      }
    }
</script>

<style scoped>

</style>
