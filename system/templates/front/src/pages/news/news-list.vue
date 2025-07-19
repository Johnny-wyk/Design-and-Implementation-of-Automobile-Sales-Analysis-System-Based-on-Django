<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="category-list">
				<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
				<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
			</div>
			<div class="list10 index-pv1">
				<div v-for="(item,index) in newsList" :key="index" class="list-item animation-box" @click="toNewsDetail(item)">
					<div class="img">
						<img class="image" :src="baseUrl + item.picture" >
					</div>
					<div class="infoBox">
						<div class="infoLeft">
							<div class="name">{{item.title}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label"></span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label"></span>
								<span class="text">{{item.name}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label"></span>
								<span class="text">{{item.thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label"></span>
								<span class="text">{{item.storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label"></span>
								<span class="text">{{item.clicknum}}</span>
							</div>
						</div>
						<div class="desc">{{item.introduction}}</div>
					</div>
				</div>
			</div>
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="false"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>

			<!-- 热门信息 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toNewsDetail(item)">
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
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '公告资讯'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
			}
		},
		created() {
			this.getCategoryList()
			
			this.getHotList()
		},
		watch:{
			$route(newValue){
				this.getCategoryList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {params: {sort: 'typename',order: 'desc'}}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list;
						if(this.$route.query.homeFenlei){
							for(let i=0;i<this.categoryList.length;i++) {
								if(this.$route.query.homeFenlei == this.categoryList[i].typename) {
									this.categoryIndex = i + 1;
									const currentRoute = this.$route;
									const routeWithoutQuery = { ...currentRoute };
									delete routeWithoutQuery.query;
									this.$router.replace(routeWithoutQuery)
									break;
								}
							}
						}
						this.getNewsList(1);
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getNewsList(1);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				border-radius: 20px;
				padding: 0px;
				margin: 40px calc(50% - 600px);
				color: #333;
				background: none;
				display: block;
				width: 1200px;
				font-size: 16px;
				justify-content: flex-start;
				align-items: flex-start;
				position: relative;
				flex-wrap: wrap;
				.list-form-pv {
						padding: 10px;
						margin: 0;
						background: none;
						display: flex;
						width: 101%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						order: 0;
						.search-item {
								margin: 0 0px;
								.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 0px solid #ccc;
										border-radius: 4px;
										padding: 0 10px;
										margin: 0 10px 0 0;
										color: #333;
										background: #fff;
										width: auto;
										font-size: 16px;
										line-height: 42px;
										min-width: 350px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0;
								border-radius: 8px;
								padding: 0px 20px;
								margin: 0 10px 0 0;
								color: #fff;
								background: rgb(25, 190, 212);
								width: auto;
								font-size: inherit;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 3px 0 0;
										color: #fff;
										font-size: inherit;
									}
			}
		}
		.category-list {
						border: 0px solid rgb(45, 50, 64);
						padding: 10px 0px;
						margin: 20px 0 0;
						background: none;
						display: flex;
						gap: 30px;
						width: 101%;
						flex-wrap: wrap;
						height: auto;
						order: 3;
						.item {
								cursor: pointer;
								border: 0px solid rgb(0, 0, 0);
								padding: 0px 20px;
								margin: 0;
								color: rgb(45, 50, 64);
								display: flex;
								font-size: 16px;
								line-height: 40px;
								flex-wrap: wrap;
								border-radius: 4px;
								background: #fff;
								justify-content: center;
								align-items: center;
								min-width: 120px;
							}
			
			.item:hover {
								color: #fff;
								background: linear-gradient(180deg,rgb(39, 103, 205),rgb(25, 190, 212));
								border-color: rgb(213, 103, 147);
							}
			
			.item.active {
								color: #fff;
								background: linear-gradient(180deg,rgb(39, 103, 205),rgb(25, 190, 212));
								border-color: rgb(213, 103, 147);
							}
		}
		.list10 {
						padding: 0;
						margin: 20px 0 0 -10px;
						color: #666;
						background: none;
						display: flex;
						width: calc(100% + 20px);
						font-size: 14px;
						flex-wrap: wrap;
						height: auto;
						order: 8;
						.list-item {
								cursor: pointer;
								border: 0px solid rgb(0, 0, 0);
								padding: 0px;
								margin: 0 10px 20px;
								background: none;
								display: flex;
								width: 48%;
								position: relative;
								flex-wrap: wrap;
								height: auto;
								.img {
										padding: 0;
										overflow: hidden;
										width: 100%;
										height: 261px;
										img {
												object-fit: cover;
												display: block;
												width: 100%;
												height: 100%;
											}
				}
				.infoBox {
										padding: 10px;
										overflow: hidden;
										color: #fff;
										flex: 1;
										background: linear-gradient(180deg,rgba(39, 103, 205, 0.7),rgba(25, 190, 212, 0.7));
										bottom: 0;
										display: flex;
										position: absolute;
										flex-wrap: wrap;
										height: auto;
										.infoLeft {
												padding: 0;
												display: flex;
												gap: 0 20px;
												width: 100%;
												flex-wrap: wrap;
												.name {
														padding: 0;
														overflow: hidden;
														white-space: nowrap;
														font-weight: 600;
														display: inline-block;
														width: 100%;
														font-size: 16px;
														line-height: 30px;
														text-overflow: ellipsis;
													}
						.time_item {
														padding: 0 10px 0 0;
														color: rgb(175, 138, 112);
														display: inline-block;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																line-height: 1.5;
															}
							.text {
																line-height: 1.5;
															}
						}
						.publisher_item {
														padding: 0 10px 0 0;
														display: inline-block;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.like_item {
														padding: 0 10px 0 0;
														display: inline-block;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.collect_item {
														padding: 0 10px 0 0;
														display: inline-block;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.view_item {
														padding: 0 10px 0 0;
														display: inline-block;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
					}
					.desc {
												margin: 10px 0 0;
												overflow: hidden;
												white-space: no-wrap;
												width: 100%;
												font-size: 14px;
												line-height: 24px;
												height: 48px;
											}
				}
			}
			.list-item:hover {
								.infoBox {
					.infoLeft {
						.name {
													}
						.time_item {
							.icon {
															}
							.label {
															}
							.text {
															}
						}
						.publisher_item {
							.icon {
															}
							.label {
															}
							.text {
															}
						}
						.like_item {
							.icon {
															}
							.label {
															}
							.text {
															}
						}
						.collect_item {
							.icon {
															}
							.label {
															}
							.text {
															}
						}
						.view_item {
							.icon {
															}
							.label {
															}
							.text {
															}
						}
					}
					.desc {
											}
				}
			}
		}
		.hot {
						margin: 30px 40px 0 0;
						background: none;
						width: 100%;
						height: auto;
						order: 50;
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
								padding: 20px 0;
								margin: 0;
								background: none;
								display: flex;
								width: 100%;
								flex-wrap: wrap;
								height: auto;
								.hot-item {
										cursor: pointer;
										padding: 10px;
										margin: 0 10px;
										display: flex;
										border-color: rgb(25, 190, 212);
										border-radius: 10px;
										background: #fff;
										width: calc(25% - 20px);
										border-width: 0 0 4px;
										align-items: center;
										border-style: solid;
										text-align: center;
										height: auto;
										img {
												border-radius: 10px;
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
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(0.98) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
</style>
