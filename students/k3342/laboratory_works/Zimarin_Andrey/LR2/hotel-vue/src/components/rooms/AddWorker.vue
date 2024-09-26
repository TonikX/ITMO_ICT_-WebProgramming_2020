<template>
  <div>
      <mu-form :model="form" label-width="100">
        <mu-form-item label="ФИО работника">
          <mu-text-field v-model="form.name"></mu-text-field>
        </mu-form-item>
       <mu-button class="btn-send" round @click="AddWr"> Подтвердить добавление</mu-button>
      </mu-form>
  </div>

</template>

<script>
    import $ from "jquery";

    export default {
        name: "AddWorker",
        data() {
          return {
              form: {
                name: ''
              }
          }
        },
        methods: {
          AddWr() {
            $.ajax({
              url: "http://127.0.0.1:8000/app/hotel/workers/",
              type: "POST",
              data: {
              full_name: this.form.name
              },
              success: (response) => {
                  alert("Работник добавлен");
              },
              error: (response) => {
                  alert("Ошибка")
              }
          })
          },
        }
    }
</script>

<style scoped>

</style>
