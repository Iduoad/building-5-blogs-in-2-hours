<template>
    <div>
        <div class="date">{{ post.created_on }}</div>
        <p class="header">{{ post.title }}</p>

        <div class="blog">
            {{ post.content }}
        </div>


        <div class="grid">
            <div class="grid-item">
                <router-link to="/">
                    <button class="btn btn--cyan">Post list</button>
                </router-link>
            </div>
        
            <div class="grid-item">
                <router-link :to="{name:'update_post', params: {id: post.id}}">
                    <button class="btn btn--blue">update list</button>
                </router-link>
            </div>
        
            <div class="grid-item">
                <router-link :to="{name:'delete_post', params: {id: post.id}}">
                    <button class="btn btn--red">Delete list</button>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'GetPost',
  props: ['id'],
  data () {
      return {
          post: {
              created_on: '',
              title: '',
              content: ''
          }
      }
  },
  mounted () {
      this.get_post();
  },
  methods: {
      get_post() {
          if (this.id) {
            let url = "http://localhost:5000/post?id=" + this.id;

            this.$http.get(url)
            .then(response => {
                console.log(response.data);
                
                this.post = response.data.post
                })
          }
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
