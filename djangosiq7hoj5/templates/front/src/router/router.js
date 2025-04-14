import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Forum from '../pages/forum/list'
import ForumAdd from '../pages/forum/add'
import ForumDetail from '../pages/forum/detail'
import MyForumList from '../pages/forum/myForumList'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import ziliaoleixingList from '../pages/ziliaoleixing/list'
import ziliaoleixingDetail from '../pages/ziliaoleixing/detail'
import ziliaoleixingAdd from '../pages/ziliaoleixing/add'
import kaoyanziliaoList from '../pages/kaoyanziliao/list'
import kaoyanziliaoDetail from '../pages/kaoyanziliao/detail'
import kaoyanziliaoAdd from '../pages/kaoyanziliao/add'
import yuanxiaoxinxiList from '../pages/yuanxiaoxinxi/list'
import yuanxiaoxinxiDetail from '../pages/yuanxiaoxinxi/detail'
import yuanxiaoxinxiAdd from '../pages/yuanxiaoxinxi/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'
import discusskaoyanziliaoList from '../pages/discusskaoyanziliao/list'
import discusskaoyanziliaoDetail from '../pages/discusskaoyanziliao/detail'
import discusskaoyanziliaoAdd from '../pages/discusskaoyanziliao/add'
import discussyuanxiaoxinxiList from '../pages/discussyuanxiaoxinxi/list'
import discussyuanxiaoxinxiDetail from '../pages/discussyuanxiaoxinxi/detail'
import discussyuanxiaoxinxiAdd from '../pages/discussyuanxiaoxinxi/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'forum',
					component: Forum
				},
				{
					path: 'forumAdd',
					component: ForumAdd
				},
				{
					path: 'forumDetail',
					component: ForumDetail
				},
				{
					path: 'myForumList',
					component: MyForumList
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'ziliaoleixing',
					component: ziliaoleixingList
				},
				{
					path: 'ziliaoleixingDetail',
					component: ziliaoleixingDetail
				},
				{
					path: 'ziliaoleixingAdd',
					component: ziliaoleixingAdd
				},
				{
					path: 'kaoyanziliao',
					component: kaoyanziliaoList
				},
				{
					path: 'kaoyanziliaoDetail',
					component: kaoyanziliaoDetail
				},
				{
					path: 'kaoyanziliaoAdd',
					component: kaoyanziliaoAdd
				},
				{
					path: 'yuanxiaoxinxi',
					component: yuanxiaoxinxiList
				},
				{
					path: 'yuanxiaoxinxiDetail',
					component: yuanxiaoxinxiDetail
				},
				{
					path: 'yuanxiaoxinxiAdd',
					component: yuanxiaoxinxiAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
				{
					path: 'discusskaoyanziliao',
					component: discusskaoyanziliaoList
				},
				{
					path: 'discusskaoyanziliaoDetail',
					component: discusskaoyanziliaoDetail
				},
				{
					path: 'discusskaoyanziliaoAdd',
					component: discusskaoyanziliaoAdd
				},
				{
					path: 'discussyuanxiaoxinxi',
					component: discussyuanxiaoxinxiList
				},
				{
					path: 'discussyuanxiaoxinxiDetail',
					component: discussyuanxiaoxinxiDetail
				},
				{
					path: 'discussyuanxiaoxinxiAdd',
					component: discussyuanxiaoxinxiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
