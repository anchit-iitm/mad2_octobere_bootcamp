<template>
  <h3>homeview.vue start</h3>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld1 msg="Welcome to Your Vue.js App"/><h3>homeview.vue start</h3>
  </div>
  <h3>homeview.vue end</h3>
</template>

<script>
// @ is an alias to /src
import HelloWorld1 from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld1
  }
}
</script>
