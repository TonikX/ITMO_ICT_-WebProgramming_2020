<template>
  <div>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat+Subrayada&display=swap" rel="stylesheet">
    <mu-container class="button-wrapper">
    <mu-button color="#e6ddde" textColor="black" v-if="auth" @click="logout">Sign Out</mu-button>
    </mu-container>
    <h1>NEWSPAPERS SYSTEM</h1>

    <mu-container>
  <mu-tabs :value.sync="active1" inverse color="black" text-color="rgba(0, 0, 0, .54)" indicator-color="#e6ddde" center>
    <mu-tab>Post Offices</mu-tab>
    <mu-tab>Newspapers</mu-tab>
    <mu-tab>Printing Houses</mu-tab>
    <mu-tab>In-Stocks</mu-tab>
    <mu-tab>Requests</mu-tab>
    <mu-tab>Certificate</mu-tab>
    <mu-tab>Report</mu-tab>
  </mu-tabs>
  <div class="demo-text" v-if="active1 === 0">
    <p>In order to view, edit or delete elements of Post Office data, please, click below.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goOffices">Continue with Post Offices</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 1">
    <p>In order to view, edit or delete elements of Newspapers data, please, click below.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goNewspapers">Continue with Newspapers</mu-button>
    </mu-container>
    <p>If you want to specifically  view, edit or delete instances of Editors information, please, click below.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goEditors">Continue with Editors</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 2">
    <p>In order to view, edit or delete elements of Printing Houses data, please, click below.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goHouses">Continue with Printing Houses</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 3">
    <p>In order to view, edit or delete elements of In-Stocks data, please, click below.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goStocks">Continue with In-Stocks</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 4">
    <p>If you need to get the following information, please, click the link below the request respectively.</p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goRequest1">At what addresses are newspapers of the given name printed?</mu-button>
    </mu-container>
    <mu-container class="button-wrapper2" @click="goRequest2">
      <mu-button flat textColor="#581845">What is the name of the editor of the newspaper, which is printed in the indicated printing house in the largest circulation?</mu-button>
    </mu-container>
    <mu-container class="button-wrapper2" @click="goRequest3">
      <mu-button flat textColor="#581845">Which post offices (addresses) receive newspapers with a price higher than the indicated?</mu-button>
    </mu-container>
    <mu-container class="button-wrapper2" @click="goRequest4">
      <mu-button flat textColor="#581845">Which newspapers and where (post offices' numbers) are received in quantities less than the specified?</mu-button>
    </mu-container>
    <mu-container class="button-wrapper2" @click="goRequest5">
      <mu-button flat textColor="#581845">Where does the requested newspaper go, which is printed at the given address?</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 5">
    <p>To create a certificate of the index and price of the newspaper, click below.</p>
    <mu-container class="button-wrapper2" @click="goCertificate">
      <mu-button flat textColor="#581845">Get a Certificate</mu-button>
    </mu-container>
  </div>
  <div class="demo-text" v-if="active1 === 6">
    <p>This section will help you create a report on the work of printing houses with the post offices of the city. The report should contain the following information for each printing house:
    <ul class="dash">
      <li> total number of newspapers printed in the printing house; </li>
      <li> number of newspapers of each denomination, which newspapers; </li>
      <li> which newspapers the printing house sends to each post office; </li>
      <li> in what quantity the printing house sends it.</li>
    </ul>
    </p>
    <p> To create a described report, click below. </p>
    <mu-container class="button-wrapper2">
      <mu-button flat textColor="#581845" @click="goReport">Get a Report</mu-button>
    </mu-container>
  </div>
</mu-container>
  </div>

</template>

<script>
import $ from 'jquery'
export default {
  data () {
    return {
      active1: 0
    };
  },
  name: 'Home',
  created() {
    $.ajaxSetup({
      headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
    })
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("auth_token")) {
        return true
      }
    }
  },
  methods: {
    goLogin() {
      this.$router.push({name: "login"})
    },
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
    goCertificate() {
      this.$router.push({name: "certificate"})
    },
    goOffices() {
      this.$router.push({name: "offices"})
    },
    goNewspapers() {
      this.$router.push({name: "newspapers"})
    },
    goEditors() {
      this.$router.push({name: "editors"})
    },
    goHouses() {
      this.$router.push({name: "printinghouses"})
    },
    goStocks() {
      this.$router.push({name: "instocks"})
    }
  }
}
</script>

<style>
body {
  background-color: #FFFFFF;
}
h1 {
  font-size: 180%;
  line-height: 100px;
  color: #000000;
  font-family: 'Montserrat Subrayada', sans-serif;
  text-align: center;
}

.button-wrapper {
  text-align: right;
  .mu-button{
    margin: 8px;
  }
}
ul.dash {
    list-style: none;
    margin-left: 0;
    padding-left: 1em;
}
ul.dash > li:before {
    display: inline-block;
    content: "\2014";
    width: 1em;
    margin-left: -1em;
}
</style>
