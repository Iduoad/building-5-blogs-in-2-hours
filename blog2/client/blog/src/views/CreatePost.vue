<template>
    <div>
        <h1>Create Post</h1>

        <form  method="post">
        <p>
            <label for="title">Title</label>
            <input type="text" id="title" v-model="title">
        </p>
        <p>
            <label for="content">Content</label>
            <textarea name="content" id="content" v-model="content">

            </textarea>
        </p>
        <input  type="submit" value="Submit" @click.prevent="create_post"  />
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
  name: 'CreatePost',
  props: {
  },
  data () {
      return {
        title: "",
        content: "",
        status: ""   
      }
  },
  methods: {
      create_post () {
          let url = "http://localhost:5000/post";
          let json_data = JSON.stringify({
              title: this.title,
              content: this.content
          });
          this.$http({
              method: 'post',
              url: url,
              data: json_data,
              headers: {
                'Content-Type': 'application/json'
              }
          })
          .then(response => {
              console.log(response.data)
              this.status = response.data.status;
              this.$router.push('/');
          })
          
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
