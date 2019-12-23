<template>
    <div>
        <div v-for="p in posts" :key="p.id">
            <div class="date">
                {{p.id}}
                <router-link :to="{name:'get_post', params: {id: p.id}}">
                    {{p.created_on}}
                </router-link>
            </div>
            <p class="header">{{ p.title }}</p>

            <div class="blog">
                {{ p.content }}
            </div>

            <hr>

            <div class="grid-item">
                <router-link to="/create">
                    <button class="btn btn--cyan">Create post</button>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'GetAllPost',
  props: {
    msg: String
  },
  data () {
      return {
        posts: []    
      }
  },
  mounted () {
      this.get_all_posts();
  },
  methods: {
      get_all_posts() {          
          this.$http.get("http://localhost:5000/posts")
          .then(response => {               
              this.posts = response.data.posts; 
              })
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
