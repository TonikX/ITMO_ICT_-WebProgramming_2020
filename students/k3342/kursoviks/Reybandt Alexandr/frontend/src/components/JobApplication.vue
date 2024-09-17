<template>
    <div class="container">
        <h3>Для подачи заявки заполните следующие поля</h3>
        <div class="form-group">
            <label for="education">Образование</label>
            <input class="form-control" id="education" v-model="education" type="text"
                   required="" placeholder="Введите свое образование"/>
        </div>

        <div class="form-group mb-3">
            <label for="position">Желаемая должность</label>
            <select class="browser-default custom-select" id="position" v-model="positionSelected">
                <option disabled value="">Выберите желаемую должность</option>
                <option v-for="option in positionOptions">
                    {{option}}
                </option>
            </select>
        </div>
        <button type="button" class="btn btn-primary" @click="applyForJob()">Подать заявку</button>
<!--        <p>{{education}}, {{positionSelected}}</p>-->
    </div>
</template>

<script>
    export default {
        name: "JobApplication",
        data() {
            return {
                positionOptions: [
                    'Главный пилот',
                    'Второй пилот',
                    'Стюардесса',
                    'Стюард'
                ],
                education: '',
                positionSelected: ''
            }
        },
        methods: {
            async applyForJob() {
                let data = {
                    education: this.education,
                    position: this.positionSelected,
                    status: 'На рассмотрении'
                }
                const token = localStorage.getItem('token');
                const id = localStorage.getItem('id');
                console.log(token)
                fetch(`${this.$store.getters.getServerUrl}/flight/profile/${id}/`,
                    {
                        method: "PUT",
                        headers: {
                            'Authorization': 'Token '+ token,
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    this.clearForm()
                    alert('Ваша заявка успешно подана!')
                    this.$router.push({name: "Profile"})
                })
            },
            clearForm() {
                this.education = ''
                this.positionSelected = ''
            }
        }
    }
</script>

<style scoped>

</style>