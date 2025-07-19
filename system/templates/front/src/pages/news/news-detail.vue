<template>
	<div class="news-detail-box">
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="news-detail-view">
			<div class="title-box">
				<div>公告资讯</div>
			</div>
			<div class="news-detail">
				<div class="detail-title">{{detail.title}}</div>
				<div class="infoBox">
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{detail.addtime.split(' ')[0]}}</span>
					</div>
					<div class="publisher_item">
						<span class="icon iconfont icon-touxiang18"></span>
						<span class="label">编辑人员：</span>
						<span class="text">{{detail.name}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞：</span>
						<span class="text">{{detail.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏：</span>
						<span class="text">{{detail.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-liulan13"></span>
						<span class="label">浏览次数：</span>
						<span class="text">{{detail.clicknum}}</span>
					</div>
				</div>
				<div class="operate">
					<div class="zan-btn" @click="zanClick" >
						<span class="icon iconfont" :class="zanType?'icon-guanzhu-zhihui':'icon-guanzhu-zhihui'" ></span>
						<span class="text" >{{zanType?'取消点赞':'点赞'}}</span>
					</div>
					<div class="collect-btn" @click="collectClick" >
						<span class="icon iconfont" :class="collectType?'icon-shoucang10':'icon-shoucang10'" ></span>
						<span class="text" >{{collectType?'取消收藏':'收藏'}}</span>
					</div>
				</div>
				
				<div class="content-detail ql-snow ql-editor" v-html="detail.content"></div>
			</div>
			<!-- option -->
			<div class="option-box">
				<div class="prev-btn" @click="prepDetailClick">
					<span class="text">上一篇</span>
					<span class="icon iconfont "></span>
				</div>
				<div class="next-btn" @click="nextDetailClick">
					<span class="text">下一篇</span>
					<span class="icon iconfont "></span>
				</div>
			</div>

			<!-- 热门文章 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toDetail(item.id)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				id: 0,
				detail: {},
				zanType: false,
				zanForm: {},
				collectType:false,
				collectForm: {},
				baseUrl:'',
				hotList: [],
				categoryList: [],
				currentIndex: 0,
				allList: [],
				storeupType: false,
			}
		},
		created() {
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			this.id = this.$route.query.id
			this.baseUrl = this.$config.baseUrl;
			this.getCategoryList()
			this.getDetail()
			this.getNewsList()
			this.getHotList()
		},
		watch:{
			$route(newValue) {
				this.id = this.$route.query.id
			    this.getDetail()
			}
		},
		methods: {
			backClick() {
				if(this.storeupType){
					history.back()
				}else {
					this.$router.push({path: '/index/news'});
				}
			},
			getNewsList() {
				let params = {page:1, limit: 100,sort:'addtime',order:'desc'};
				this.$http.get('news/list', {params: params}).then(res => {
					if (res.data.code == 0) {
						for(let x in res.data.data.list){
							if(res.data.data.list[x].id == this.id){
								this.currentIndex = Number(x)
								break
							}
						}
						this.allList = res.data.data.list
					}
				});
			},
			// 上一篇
			prepDetailClick(){
				if(this.currentIndex == 0){
					this.$message.error('已经是第一篇了')
					return false
				}
				this.currentIndex--
				this.$router.push({path: '/index/newsDetail', query: {id: this.allList[this.currentIndex].id}});
			},
			// 下一篇
			nextDetailClick(){
				if(this.currentIndex == this.allList.length - 1){
					this.$message.error('已经是最后一篇了')
					return false
				}
				this.currentIndex++
				this.$router.push({path: '/index/newsDetail', query: {id: this.allList[this.currentIndex].id}});
			},
			getCategoryList(){
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data;
					}
				});
			},
			// 获取热门列表
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			// 跳转详情
			toDetail(id){
				this.$router.push({path: '/index/newsDetail', query: {id: id}});
			},
			getDetail(){
				this.$http.get(`news/detail/${this.id}`,{}).then(res=>{
					if(res.data&&res.data.code==0){
						this.detail = res.data.data
						window.scrollTo(0, 100)
						this.getZan()
						this.getCollect()
					}
				})
			},
			getZan() {
				this.$http.get('storeup/list', {
					params: {
						page: 1,
						limit: 1,
						type: '21',
						userid: Number(localStorage.getItem('frontUserid')),
						tablename: 'news',
						refid: this.id
					}
				}).then(res=>{
					if(res.data&&res.data.code==0){
						if(res.data.data.list.length){
							this.zanType = true
							this.zanForm = res.data.data.list[0]
						}else{
							this.zanType = false
						}
					}
				})
			},
			getCollect(){
				this.$http.get('storeup/list', {
					params: {
						page: 1,
						limit: 1,
						type: '1',
						userid: Number(localStorage.getItem('frontUserid')),
						tablename: 'news',
						refid: this.id
					}
				}).then(res=>{
					if(res.data&&res.data.code==0){
						if(res.data.data.list.length){
							this.collectType = true
							this.collectForm = res.data.data.list[0]
						}else{
							this.collectType = false
						}
					}
				})
			},
			zanClick() {
				if(this.zanType){
					this.$http.post('storeup/delete', [this.zanForm.id]).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('取消成功')
							this.detail.thumbsupnum--
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getZan()
						}
					})
				}else{
					let data = {
						name: this.detail.title,
						picture: this.detail.picture,
						refid: this.detail.id,
						type: '21',
						tablename: 'news',
						userid: Number(localStorage.getItem('frontUserid')),
					}
					this.$http.post('storeup/add', data).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('点赞成功')
							this.detail.thumbsupnum++
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getZan()
						}
					})
				}
			},
			collectClick(){
				if(this.collectType){
					this.$http.post('storeup/delete', [this.collectForm.id]).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('取消成功')
							this.detail.storeupnum--
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getCollect()
						}
					})
				}else{
					let data = {
						name: this.detail.title,
						picture: this.detail.picture,
						refid: this.detail.id,
						type: '1',
						tablename: 'news',
						userid: Number(localStorage.getItem('frontUserid')),
					}
					this.$http.post('storeup/add', data).then(res => {
						if (res.data && res.data.code == 0) {
							this.detail.storeupnum++
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.$message.success('收藏成功')
							this.getCollect()
						}
					})
				}
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	
	.news-detail-box {
				padding: 30px calc((100% - 1300px)/2);
				margin: 0px auto;
				color: #333;
				background: rgb(237, 237, 237);
				width: 100%;
				font-size: 15px;
				position: relative;
				.news-detail-view {
						border: 1px solid rgb(25, 190, 212);
						border-radius: 0px;
						padding: 0px;
						align-content: flex-start;
						background: #fff;
						display: flex;
						width: 100%;
						align-items: flex-start;
						position: relative;
						flex-wrap: wrap;
						.title-box {
								background: rgb(25, 190, 212);
								display: none;
								width: 100%;
								height: auto;
								div {
										margin: 10px 0;
										color: #333;
										background: none;
										font-size: 24px;
										line-height: 54px;
										text-align: center;
									}
			}
			.news-detail {
								border: 0px solid rgb(45, 50, 64);
								border-radius: 10px;
								padding: 0px 0px 90px;
								background: #fff;
								display: flex;
								width: 100%;
								position: relative;
								flex-wrap: wrap;
								.detail-title {
										padding: 10px 0;
										color: #fff;
										background: rgb(25, 190, 212);
										font-weight: 500;
										width: 100%;
										font-size: 22px;
										border-color: #fcbb78;
										border-width: 0 0 0px;
										line-height: 1.8;
										border-style: solid;
										text-align: center;
									}
				.infoBox {
										margin: 20px 0 0;
										color: #aaa;
										display: flex;
										width: 50%;
										justify-content: center;
										align-items: center;
										.time_item {
												padding: 0;
												margin: 0 20px 0 0;
												color: #888;
												order: 10;
												.icon {
														margin: 0 2px 0 0;
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
						.label {
														color: inherit;
														display: none;
														font-size: inherit;
														line-height: 1.5;
													}
						.text {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
					}
					.publisher_item {
												padding: 0;
												margin: 0 20px 0 0;
												.icon {
														margin: 0 2px 0 0;
														color: inherit;
														display: none;
														font-size: inherit;
														line-height: 1.5;
													}
						.label {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
						.text {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
					}
					.like_item {
												padding: 0;
												margin: 0 20px 0 0;
												.icon {
														margin: 0 2px 0 0;
														color: inherit;
														display: none;
														font-size: inherit;
														line-height: 1.5;
													}
						.label {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
						.text {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
					}
					.collect_item {
												padding: 0;
												margin: 0 20px 0 0;
												.icon {
														margin: 0 2px 0 0;
														color: inherit;
														display: none;
														font-size: inherit;
														line-height: 1.5;
													}
						.label {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
						.text {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
					}
					.view_item {
												padding: 0;
												margin: 0 20px 0 0;
												.icon {
														margin: 0 2px 0 0;
														color: inherit;
														display: none;
														font-size: inherit;
														line-height: 1.5;
													}
						.label {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
						.text {
														color: inherit;
														font-size: inherit;
														line-height: 1.5;
													}
					}
				}
				.operate {
										padding: 10px;
										display: block;
										width: 50%;
										justify-content: flex-start;
										align-items: center;
										text-align: right;
										.zan-btn {
												border-radius: 0px;
												padding: 0 20px;
												margin: 0 10px 0 0;
												background: rgb(25, 190, 212);
												display: inline-block;
												line-height: 34px;
												height: 34px;
												.icon {
														margin: 0 2px 0 0;
														color: #fff;
														font-size: inherit;
													}
						.text {
														color: #fff;
														font-size: inherit;
													}
					}
					.zan-btn:hover {
												cursor: pointer;
												.icon {
													}
						.text {
													}
					}
					.collect-btn {
												border-radius: 0px;
												padding: 0 20px;
												margin: 0 0 0 10px;
												background: rgb(39, 103, 205);
												display: inline-block;
												line-height: 34px;
												height: 34px;
												.icon {
														margin: 0 2px 0 0;
														color: #fff;
														font-size: inherit;
													}
						.text {
														color: #fff;
														font-size: inherit;
													}
					}
					.collect-btn:hover {
												cursor: pointer;
												.icon {
													}
						.text {
													}
					}
				}
				.content-detail {
										padding: 20px;
										margin: 10px 0 0;
										color: #666;
										text-indent: 2em;
										width: 100%;
										font-size: inherit;
										line-height: 1.8;
										height: auto;
									}
			}
			.option-box {
								padding: 10px 20px 20px;
								margin: -80px auto 0;
								z-index: 9;
								color: #fff;
								display: flex;
								border-color: #fcbb78;
								flex-direction: row;
								background: #fff;
								width: 50%;
								justify-content: center;
								border-width: 0px;
								border-style: solid;
								height: auto;
								.prev-btn {
										border: 0px solid #fcbb78;
										border-radius: 0px;
										padding: 10px 20px;
										margin: 0 20px 0 0;
										background: rgb(25, 190, 212);
										text-align: center;
										min-width: 130px;
										.text {
												color: inherit;
												font-size: inherit;
											}
					.icon {
												color: inherit;
												font-size: inherit;
											}
				}
				.prev-btn:hover {
										cursor: pointer;
										.text {
											}
					.icon {
											}
				}
				.next-btn {
										border: 0px solid #fcbb78;
										border-radius: 0px;
										padding: 10px 20px;
										background: rgb(39, 103, 205);
										min-width: 130px;
										text-align: center;
										.text {
												color: inherit;
												font-size: inherit;
											}
					.icon {
												color: inherit;
												font-size: inherit;
											}
				}
				.next-btn:hover {
										cursor: pointer;
										.text {
											}
					.icon {
											}
				}
			}
			.hot {
								padding: 0 20px;
								margin: 50px auto 20px;
								background: #fff;
								width: 100%;
								height: auto;
								.hot-title {
										padding: 0px 0px 28px 60px;
										margin: 0;
										color: rgb(25, 190, 212);
										background: url("http://codegen.caihongy.cn/20250218/698c52a55fc042a28aacea71589d4e23.png") left center / 700px 100% no-repeat;
										width: 100%;
										font-size: 26px;
										line-height: 40px;
										position: relative;
										text-align: left;
										height: 70px;
									}
				.hot-list {
										padding: 10px 0;
										margin: 0;
										background: none;
										display: flex;
										width: 100%;
										justify-content: space-between;
										flex-wrap: wrap;
										height: auto;
										.hot-item {
												cursor: pointer;
												border: 0px solid #243559;
												padding: 10px;
												margin: 0 10px;
												display: flex;
												border-color: rgb(25, 190, 212);
												border-radius: 10px;
												background: none;
												width: calc(25% - 20px);
												border-width: 1px 1px 6px;
												align-items: center;
												border-style: solid;
												text-align: center;
												height: auto;
												img {
														border-radius: 4px;
														flex-shrink: 0;
														margin: 0 auto;
														object-fit: cover;
														display: block;
														width: 100px;
														height: 125px;
													}
						.hot-name {
														padding: 0px 10px;
														overflow: hidden;
														color: #333;
														white-space: nowrap;
														width: calc(100% - 0px);
														font-size: 15px;
														line-height: 40px;
														text-overflow: ellipsis;
														text-align: center;
													}
						.hot-time {
														padding: 0 5px;
														color: #666;
														display: none;
														width: calc(100% - 0px);
														font-size: 15px;
														line-height: 24px;
														text-align: center;
													}
					}
				}
			}
		}
	}
</style>