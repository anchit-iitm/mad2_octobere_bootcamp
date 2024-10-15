<template>
  <!-- <h2>app.vue start</h2> -->
  <nav>
    <!-- <a href="/">Home</a> | -->
    <router-link to="/">Home</router-link> |
    <router-link :to="{'name': 'about'}">About</router-link> |
    <router-link :to="{'name': 'createCategory'}">createCategory</router-link> |
    <router-link :to="{'name': 'login'}">login</router-link> |
    <router-link to="/test">Test</router-link> |
    <a @click="logout()">Logout</a>
  </nav>
  <!-- <p>app.vue body</p> -->
  <router-view/>
  <!-- <h2>app.vue end</h2> -->
</template>
<script>
export default{
  methods:{
    logout(){
      localStorage.clear()
      this.$router.push({name: 'login'})
    }
  }
}
</script>

<style>
#app123 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
