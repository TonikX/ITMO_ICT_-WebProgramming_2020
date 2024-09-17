<template>
    <div id="app">
        <NavBar />
        <router-view/>
    </div>
</template>

<style scoped>
</style>
<script>
    import NavBar from "./components/NavBar"
    export default {
        components: {NavBar},
        created() {
            const token = localStorage.getItem('token');
            const id = localStorage.getItem('id');
            if (!token) return;
            this.$store.dispatch('loadProfile', {token, id})
                .catch((error) => {
                    console.log('error', error);
                });
        }
    }
</script>
