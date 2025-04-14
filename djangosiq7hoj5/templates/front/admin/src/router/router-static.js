import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import forum from '@/views/modules/forum/list'
    import news from '@/views/modules/news/list'
    import discussyuanxiaoxinxi from '@/views/modules/discussyuanxiaoxinxi/list'
    import yuanxiaoxinxi from '@/views/modules/yuanxiaoxinxi/list'
    import ziliaoleixing from '@/views/modules/ziliaoleixing/list'
    import systemintro from '@/views/modules/systemintro/list'
    import yonghu from '@/views/modules/yonghu/list'
    import discusskaoyanziliao from '@/views/modules/discusskaoyanziliao/list'
    import kaoyanziliao from '@/views/modules/kaoyanziliao/list'
    import chat from '@/views/modules/chat/list'
    import config from '@/views/modules/config/list'
    import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/forum',
        name: '考研论坛',
        component: forum
      }
      ,{
	path: '/news',
        name: '考研资讯',
        component: news
      }
      ,{
	path: '/discussyuanxiaoxinxi',
        name: '院校信息',
        component: discussyuanxiaoxinxi
      }
      ,{
	path: '/yuanxiaoxinxi',
        name: '院校信息',
        component: yuanxiaoxinxi
      }
      ,{
	path: '/ziliaoleixing',
        name: '资料类型',
        component: ziliaoleixing
      }
      ,{
	path: '/systemintro',
        name: '系统简介',
        component: systemintro
      }
      ,{
	path: '/yonghu',
        name: '用户',
        component: yonghu
      }
      ,{
	path: '/discusskaoyanziliao',
        name: '考研资料评论',
        component: discusskaoyanziliao
      }
      ,{
	path: '/kaoyanziliao',
        name: '考研资料',
        component: kaoyanziliao
      }
      ,{
	path: '/chat',
        name: '报考咨询',
        component: chat
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/newstype',
        name: '考研资讯分类',
        component: newstype
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/board',
    name: 'board',
    component: Board,
    meta: {icon:'', title:'board'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
