export default {
	baseUrl: 'http://localhost:8080/djangod07x7d4j/',
	name: '/djangod07x7d4j',
	indexNav: [
		{
			name: '销售信息',
			url: '/index/xiaoshouinfo',
		},
		{
			name: '用户社区',
			url: '/index/forum'
		}, 
		{
			name: '公告资讯',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '用户社区',
			refTable: 'forumtype',
			refColumn: 'typename',
		},
		{
			name: '公告资讯',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
