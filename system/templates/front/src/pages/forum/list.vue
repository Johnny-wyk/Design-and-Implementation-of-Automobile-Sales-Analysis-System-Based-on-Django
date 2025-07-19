<template>
	<div class="forum-preview">
		<div class="forum-title">
			<div>用户社区</div>
		</div>
		<el-form :inline="true" :model="formSearch" class="list-form-pv">
			<el-form-item class="search-item">
				<el-input v-model="title" placeholder="标题"></el-input>
			</el-form-item>
			<div class="search-btn-item">
				<el-button class="searchBtn" type="primary" @click="getForumList(1)">
					<span class="icon iconfont "></span>
					查询
				</el-button>
				<el-button class="pubBtn" type="primary" @click="toForumAdd">
					<span class="icon iconfont "></span>
					发布帖子
				</el-button>
			</div>
		</el-form>
		<div class="category-list">
			<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
			<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
		</div>
		<div class="z-box">
			<div class="section-content" v-for="item in forumList" :key="item.id" @click.stop="toForumDetail(item)">
				<img class="item-img" :src="$config.baseUrl + item.cover.split(',')[0]" @click.stop="imgPreView($config.baseUrl + item.cover.split(',')[0])" />
				<div class="item-title">{{item.title}}</div>
				<div class="item-user">发布人：{{item.isanon==1&&item.userid!=userid?'匿名':item.username}}</div>
				<div class="item-time">{{item.addtime}}</div>
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
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				formSearch: {},
				title: '',
				layouts: '',
				forumList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				previewImg: '',
				previewVisible: false,
				userid: Number(localStorage.getItem('frontUserid')),
				categoryIndex: 0,
				categoryList: [],
			}
		},
		created() {
			this.getCategoryList()
		},
		watch:{
			$route(newValue){
				this.getCategoryList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('forumtype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list
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
						this.getForumList(1);
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getForumList()
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			getForumList(page) {
				let params = {page, limit: this.pageSize, isdone: '开放', sort: 'istop,toptime', order: 'desc,desc',delflag: 0};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('forum/flist', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.forumList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getForumList(page);
			},
			prevClick(page) {
				this.getForumList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getForumList(1);
			},
			nextClick(page) {
				this.getForumList(page);
			},
			toForumAdd() {
				this.$router.push('/index/forumAdd');
			},
			toForumDetail(item) {
				this.$router.push({path: '/index/forumDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.forum-preview {
				padding: 0 calc((100% - 1200px)/2);
				margin: 0 auto;
				align-content: flex-start;
				background: rgb(239, 239, 239);
				display: flex;
				width: 100%;
				font-size: 16px;
				align-items: flex-start;
				position: relative;
				flex-wrap: wrap;
				.forum-title {
						padding: 0 0 0 50px;
						margin: 30px auto 0;
						color: rgb(25, 190, 212);
						background: url(http://codegen.caihongy.cn/20250220/e85584abac2c4b3ebee6d1c211618e75.png) no-repeat center bottom/100% 100%;
						width: 100%;
						position: relative;
						text-align: left;
						height: 70px;
						div {
								font-size: 26px;
								line-height: 60px;
							}
		}
		.list-form-pv {
						padding: 40px 0 20px;
						margin: 0 auto;
						background: none;
						display: flex;
						width: 100%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						order: 2;
						.search-item {
								margin: 0;
								/deep/ .el-form-item__content {
										display: flex;
										align-items: center;
									}
				.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 1px solid #000;
										border-radius: 4px;
										padding: 0 10px;
										margin: 0;
										color: #888;
										background: #fff;
										width: 280px;
										font-size: 15px;
										line-height: 42px;
										height: 42px;
									}
			}
			.search-btn-item {
								display: flex;
								.searchBtn {
										cursor: pointer;
										border: 0;
										border-radius: 4px;
										padding: 0px 20px;
										margin: 0 10px 0 10px;
										color: #fff;
										background: rgb(25, 190, 212);
										width: auto;
										font-size: inherit;
										line-height: 40px;
										height: 40px;
										.icon {
												margin: 0 2px 0 0;
												color: #fff;
											}
				}
				
				.searchBtn:hover {
									}
				
				.pubBtn {
										cursor: pointer;
										border: 0px solid #fcbb78;
										border-radius: 4px;
										padding: 0px 15px;
										margin: 0 10px 0 0;
										color: #fff;
										background: rgb(2, 77, 199);
										width: auto;
										font-size: inherit;
										line-height: 40px;
										height: 40px;
										.icon {
												margin: 0 2px 0 0;
												color: #fff;
												font-size: 16px;
											}
				}
				
				.pubBtn:hover {
									}
			}
		}
		.category-list {
						padding: 0;
						margin: 20px auto 0;
						background: none;
						display: flex;
						width: 100%;
						flex-wrap: wrap;
						height: auto;
						order: 3;
						.item {
								cursor: pointer;
								border: 1px solid #000;
								padding: 0px 20px;
								margin: 0 20px 20px 0;
								color: #000;
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
								background: rgb(25, 190, 212);
								border-color: rgb(25, 190, 212);
							}
			
			.item.active {
								color: #fff;
								background: rgb(25, 190, 212);
								border-color: rgb(25, 190, 212);
							}
		}
		.z-box {
						padding: 20px;
						margin: 0 auto;
						background: url(http://codegen.caihongy.cn/20250220/202138d8ec184491880739c9cee80a3f.png) center/100% 100%;
						display: flex;
						width: 100%;
						justify-content: space-between;
						flex-wrap: wrap;
						order: 3;
						.section-content {
								cursor: pointer;
								padding: 10px 20px 10px;
								margin: 0 0 20px;
								color: #fff;
								display: flex;
								border-color: rgb(0, 0, 0);
								flex-wrap: wrap;
								border-radius: 6px;
								background: url(http://codegen.caihongy.cn/20250220/50f5dea572a74135ae9ea258570dbf72.png) center/ 100% 100%;
								width: 100%;
								border-width: 0px;
								align-items: center;
								position: relative;
								border-style: solid;
								.item-img {
										border-radius: 100%;
										margin: 0 10px 0 0;
										object-fit: cover;
										width: 40px;
										transition: all .4s;
										height: 40px;
										order: 3;
									}
				.item-title {
										margin: 0 0 10px;
										overflow: hidden;
										white-space: nowrap;
										font-weight: 500;
										width: 100%;
										font-size: 16px;
										border-color: #24355915;
										border-width: 0 0 0px;
										line-height: 40px;
										text-overflow: ellipsis;
										border-style: solid;
										order: 20;
									}
				.item-user {
										margin: 0 10px 0 0;
										white-space: nowrap;
										font-size: 15px;
										line-height: 40px;
										position: relative;
										order: 4;
									}
				.item-time {
										margin: 0 0 0 auto;
										font-size: 15px;
										line-height: 1.5;
										position: relative;
										order: 5;
									}
			}
			.section-content:hover {
								.item-title {
										color: #000;
									}
				.item-user {
									}
				.item-time {
									}
			}
		}
	}
</style>
