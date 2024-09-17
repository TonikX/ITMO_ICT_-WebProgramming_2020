<template>
    <div class="container">
        <div class="row">
            <div class="card mt-4 ml-4" style="width: 18rem;" v-for="app in appList">
                <div class="card-body">
                    <h5 class="card-title">{{ app.first_name }} {{ app.last_name }}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Возраст: {{ app.age }} года (лет)</h6>
                    <p class="card-text"><small><b>Образование:</b></small> {{ app.education }} <br>
                        <small><b>Желаемая должность:</b></small> {{ app.position }}
                    </p>
                    <!--                <a href="#" class="card-link">Card link</a>-->
                    <!--                <a href="#" class="card-link">Another link</a>-->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ApplicationList",
        data() {
            return {
                appList: []
            }
        },
        created() {
            this.loadAppList()
        },
        methods: {
            async loadAppList() {
                this.appList = await fetch(
                    `${this.$store.getters.getServerUrl}/flight/profile/job_app/`
                ).then(response => response.json())
                console.log(this.appList);
            }
        }
    }
</script>

<style scoped>

</style>