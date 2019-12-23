<template>
    <div>
        <h1>Delete post</h1>
        <form  method="post">
        Are you sure you want do delete the post <br>
        <input  type="submit" value="Submit" @click.prevent="delete_post" />
        </form>
        
        <h1>
            {{ status }}
        </h1>
        <div class="grid">
            <div class="grid-item">
                <router-link to="/">
                    <button class="btn btn--cyan">Post list</button>
                </router-link>
            </div>
        
            <div class="grid-item">
                <router-link :to="{name:'get_post', params: {id: id}}">
                    <button class="btn btn--blue">Post Details</button>                    
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'DeletePost',
  props: {
    id: Number
  },
  data () {
      return {
          status: ""
      }
  },
  methods: {
      delete_post() {
          let url = "http://localhost:5000/post";
          let json_data = JSON.stringify({"id": this.id});
          this.$http({
              method: 'delete',
              url: url,
              data: json_data,
              headers: {
                'Content-Type': 'application/json'
              }
          })
          .then(response => {
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
