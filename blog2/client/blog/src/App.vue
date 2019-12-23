<template>
  <div id="app">
      <div class="grid-item">
          <router-view/>
      </div>
  </div>
</template>

<script>
  import GetAllPost from '@/views/GetAllPosts'

  export default {
    name: 'app',
    components: { GetAllPost },
    data () {
      return {
        //
      }
    }
  }
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
