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
import xiaoshouinfoList from '../pages/xiaoshouinfo/list'
import xiaoshouinfoDetail from '../pages/xiaoshouinfo/detail'
import xiaoshouinfoAdd from '../pages/xiaoshouinfo/add'
import xiaoshouinfoforecastList from '../pages/xiaoshouinfoforecast/list'
import xiaoshouinfoforecastDetail from '../pages/xiaoshouinfoforecast/detail'
import xiaoshouinfoforecastAdd from '../pages/xiaoshouinfoforecast/add'
import forumtypeList from '../pages/forumtype/list'
import forumtypeDetail from '../pages/forumtype/detail'
import forumtypeAdd from '../pages/forumtype/add'
import forumreportList from '../pages/forumreport/list'
import forumreportDetail from '../pages/forumreport/detail'
import forumreportAdd from '../pages/forumreport/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'
import emailregistercodeList from '../pages/emailregistercode/list'
import emailregistercodeDetail from '../pages/emailregistercode/detail'
import emailregistercodeAdd from '../pages/emailregistercode/add'
import discussxiaoshouinfoList from '../pages/discussxiaoshouinfo/list'
import discussxiaoshouinfoDetail from '../pages/discussxiaoshouinfo/detail'
import discussxiaoshouinfoAdd from '../pages/discussxiaoshouinfo/add'

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
					path: 'xiaoshouinfo',
					component: xiaoshouinfoList
				},
				{
					path: 'xiaoshouinfoDetail',
					component: xiaoshouinfoDetail
				},
				{
					path: 'xiaoshouinfoAdd',
					component: xiaoshouinfoAdd
				},
				{
					path: 'xiaoshouinfoforecast',
					component: xiaoshouinfoforecastList
				},
				{
					path: 'xiaoshouinfoforecastDetail',
					component: xiaoshouinfoforecastDetail
				},
				{
					path: 'xiaoshouinfoforecastAdd',
					component: xiaoshouinfoforecastAdd
				},
				{
					path: 'forumtype',
					component: forumtypeList
				},
				{
					path: 'forumtypeDetail',
					component: forumtypeDetail
				},
				{
					path: 'forumtypeAdd',
					component: forumtypeAdd
				},
				{
					path: 'forumreport',
					component: forumreportList
				},
				{
					path: 'forumreportDetail',
					component: forumreportDetail
				},
				{
					path: 'forumreportAdd',
					component: forumreportAdd
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
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
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
					path: 'emailregistercode',
					component: emailregistercodeList
				},
				{
					path: 'emailregistercodeDetail',
					component: emailregistercodeDetail
				},
				{
					path: 'emailregistercodeAdd',
					component: emailregistercodeAdd
				},
				{
					path: 'discussxiaoshouinfo',
					component: discussxiaoshouinfoList
				},
				{
					path: 'discussxiaoshouinfoDetail',
					component: discussxiaoshouinfoDetail
				},
				{
					path: 'discussxiaoshouinfoAdd',
					component: discussxiaoshouinfoAdd
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
