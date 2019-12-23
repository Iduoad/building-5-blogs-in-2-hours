<template>
    <div>
        <h1>Update Post</h1>

        <form  method="post">
        <p>
            <label for="title">Title</label>
            <input type="text" id="title" v-model="post.title">
        </p>
        <p>
            <label for="content">Content</label>
            <textarea name="content" id="content" v-model="post.content">

            </textarea>
        </p>
        <input  type="submit" value="Submit" @click.prevent="update_post" />
        </form>
        <div class="grid-item">
            <router-link to="/">
                <button class="btn btn--cyan">Post list</button>
            </router-link>
        </div>
        <h1>{{ status }}</h1>
    </div>
</template>

<script>
export default {
  name: 'UpadtePost',
  props: {
    id: Number
  },
  data () {
      return {
        post: {
            title: '',
            content: ''
        },
        status: ""    
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
      },
      update_post () {
          let url = "http://localhost:5000/post";
          let json_data = JSON.stringify( 
          {
            "id": this.id,
            "title": this.post.title,
            "content": this.post.content
          });
        
          this.$http({
              method: 'put',
              url: url,
              data: json_data,
              headers: {
                'Content-Type': 'application/json'
              }
          })
          .then(response => {
              this.status = response.data.status;
          })
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
