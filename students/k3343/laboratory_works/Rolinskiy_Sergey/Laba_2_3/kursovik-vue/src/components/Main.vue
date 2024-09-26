<template>
    <div>
      <h1>Welcome!</h1>
      <h2>Choose an action:</h2>
      <mu-container>
  <mu-tabs class="demo-text" :value.sync="active1" inverse color="black" text-color="rgba(0, 0, 0, .54)" indicator-color="#e6ddde" center>
    <mu-tab>Clients</mu-tab>
    <mu-tab>Workers</mu-tab>
    <mu-tab>Worktable</mu-tab>
    <mu-tab>Journal</mu-tab>
    <mu-tab>Rooms</mu-tab>
    <mu-tab>Report</mu-tab>
    <mu-tab>Requests</mu-tab>
  </mu-tabs>
    <div v-if="active1 === 0">
      <br/>
         <br/>
      <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goClients">Show all clients</mu-button>
    </mu-container></div>
        <div v-if="active1 === 1">
          <br/>
         <br/>
       <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goWorkers">Show all workers</mu-button>
       </mu-container></div>
        <div v-if="active1 === 2">
          <br/>
         <br/>
       <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goWorktable">Show the worktable</mu-button>
       </mu-container></div>
        <div v-if="active1 === 3">
          <br/>
         <br/>
       <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goJournal">Show the reception journal</mu-button>
       </mu-container></div>
        <div v-if="active1 === 4">
          <br/>
         <br/>
       <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRooms">Show all rooms</mu-button>
       </mu-container></div>
        <div v-if="active1 === 5">
          <br/>
         <br/>
       <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goReport">Compile a report of a chosen date interval</mu-button>
       </mu-container></div>
        <div v-if="active1 === 6">
          <br/>
         <br/>
<mu-container class="button-wrapper2">
  <p>Choose an request you would like to perform:</p>
      <mu-button flat textColor="#581845" @click="goRequest1">Clients that lived in a room during specified time</mu-button>
    </mu-container>
      <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRequest2">Number of clients from a specific city</mu-button>
    </mu-container>
      <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRequest3">Worker who tidied the specific room during a chosen day of the week</mu-button>
    </mu-container>
      <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRequest4">What rooms are empty right now</mu-button>
    </mu-container>
      <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRequest5">Clients who lived in the same time with a chosen client</mu-button>
      </mu-container></div>
      </mu-container></div>
</template>

<script>
import $ from 'jquery'
export default {
  data() {
    return {
      active1: 0
    };
  },
  name: "Main",
    created() {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    })
  },
  methods: {
    logout() {
      sessionStorage.removeItem("auth_token")
      window.location = '/'
    },
    goRequest1() {
      this.$router.push({name: "request1"})
    },
    goRequest2() {
      this.$router.push({name: "request2"})
    },
    goRequest3() {
      this.$router.push({name: "request3"})
    },
    goRequest4() {
      this.$router.push({name: "request4"})
    },
    goRequest5() {
      this.$router.push({name: "request5"})
    },
    goReport() {
      this.$router.push({name: "report"})
    },
    goRooms() {
      this.$router.push({name: "rooms"})
    },
    goClients() {
      this.$router.push({name: "clients"})
    },
    goWorkers() {
      this.$router.push({name: "workers"})
    },
    goJournal() {
      this.$router.push({name: "journal"})
    },
    goWorktable() {
      this.$router.push({name: "worktable"})
    }
  }
    }
</script>

<style scoped>
  .demo-text{
    background:#64e867;
  }
 h1 {
        margin-top: 50px;
        font-size: 200%;
        line-height: 100px;
        color: #000000;
        text-align: center;

}.button-wrapper {
  text-align: right;
  .mu-button{font-size: 500%;
    margin: 8px;
  }
}
</style>
