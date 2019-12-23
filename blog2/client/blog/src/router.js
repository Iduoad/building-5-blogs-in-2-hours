import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import GetAllPosts from './views/GetAllPosts.vue'
import GetPost from './views/GetPost.vue'
import CreatePost from './views/CreatePost.vue'
import UpdatePost from './views/UpdatePost.vue'
import DeletePost from './views/DeletePost.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'posts',
      component: GetAllPosts
    },
    {
      path: '/post/:id',
      name: 'get_post',
      component: GetPost,
      props: true
    },
    {
      path: '/create',
      name: 'create_post',
      component: CreatePost
    },
    {
      path: '/update/:id',
      name: 'update_post',
      component: UpdatePost,
      props: true
    },
    {
      path: '/delete/:id',
      name: 'delete_post',
      component: DeletePost,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
