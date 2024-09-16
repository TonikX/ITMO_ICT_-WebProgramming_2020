<template>
    <div> watermellon sugar
        ${{ rooms }}
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    name: "Room",
    data() {
        return {
            rooms: '',
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
                url: 'http://127.0.0.1:8000/postoffices/',
                type: 'GET',
                success: (response) => {
                    this.rooms = response.data
                }
            })
        }
    }
}
</script>

<style scoped>
</style>

