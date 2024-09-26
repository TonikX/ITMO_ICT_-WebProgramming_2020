<template>
  <mu-row>
    <h3>Расписание уборок</h3>
    <div v-for="d in days" :key="d">
      <ul>
        <li>День: {{d}}</li>
      </ul>
      <div v-for="cl in cleanings">
      <ul>
        <li v-if="cl.day_of_week===d"> Этаж: {{cl.floor}}</li>
      </ul>
        </div>
    </div>


  </mu-row>
</template>

<script>
  import $ from 'jquery'
    export default {
      name: "Timetable",
      props: ['worker'],
      data() {
          return {
            cleanings: '',
            days: ['Пон', 'Вт', 'Ср', 'Чт','Пт', 'Сб', 'Вс'],
          }
        },
        created() {
          $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadCleanings()
        },
        methods: {
          loadCleanings() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/cleanings/" + this.worker,
              type: "GET",
              success: (response) => {
                console.log(response);
                this.cleanings = response.data.data
              }
            })
          },
        }
    }
</script>

<style scoped>

</style>
