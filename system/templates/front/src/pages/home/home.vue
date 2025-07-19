<template>
	<div class="home-preview">



		<!-- 关于我们 -->
		<div id="about" class="animate__animated">
			<div class="about_item">
				<div class="about_title_box">
					<div class="about_title">{{aboutUsDetail.title}}</div>
					<div class="about_subtitle">{{aboutUsDetail.subtitle}}</div>
				</div>
				<div class="about_img">
					<img :src="baseUrl + aboutUsDetail.picture1">
					<img :src="baseUrl + aboutUsDetail.picture2">
					<img :src="baseUrl + aboutUsDetail.picture3">
				</div>
				<div class="about_content ql-snow ql-editor" v-html="aboutUsDetail.content"></div>
				<div class="about_idea1" />
				<div class="about_idea2" />
				<div class="about_idea3" />
				<div class="about_idea4" />
				<div class="about_more" @click="toDetail('aboutusDetail',aboutUsDetail)">
					<span>查看更多</span>
					<span class="icon iconfont icon-jiantou25"></span>
				</div>
			</div>
		</div>
		<!-- 关于我们 -->

		<!-- 系统简介 -->
		<div id="system" class="animate__animated">
			<div class="system_item">
				<div class="system_title_box">
					<div class="system_title">{{systemIntroductionDetail.title}}</div>
					<div class="system_subtitle">{{systemIntroductionDetail.subtitle}}</div>
				</div>
				<div class="system_img">
					<img :src="baseUrl + systemIntroductionDetail.picture1">
					<img :src="baseUrl + systemIntroductionDetail.picture2">
					<img :src="baseUrl + systemIntroductionDetail.picture3">
				</div>
				<div class="system_content ql-snow ql-editor" v-html="systemIntroductionDetail.content"></div>
				<div class="system_idea1" />
				<div class="system_idea2" />
				<div class="system_idea3" />
				<div class="system_idea4" />
				<div class="system_more" @click="toDetail('systemintroDetail',systemIntroductionDetail)">
					<span>查看更多</span>
					<span class="icon iconfont icon-gengduo1"></span>
				</div>
			</div>
		</div>
		<!-- 系统简介 -->
		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">公告资讯</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div v-if="newsList.length" class="list list13 index-pv1">
				<div class="top">
					<div class="left">
						<template v-for="(item,index) in newsList">
							<div v-if="index < 3" @click="toDetail('newsDetail', item)" class="list-item animation-box">
								<div class="name">{{item.title}}</div>
								<div class="desc">{{item.introduction}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
								<div class="publisher_item">
									<span class="icon iconfont icon-geren16"></span>
									<span class="label">发布人：</span>
									<span class="text">{{item.name}}</span>
								</div>
								<div class="like_item">
									<span class="icon iconfont icon-zan10"></span>
									<span class="label">点赞：</span>
									<span class="text">{{item.thumbsupnum}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{item.storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-chakan2"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{item.clicknum}}</span>
								</div>
							</div>
						</template>
					</div>
					<div class="news-swiper13">
						<div v-if="newsList.length > 3" class="swiper-container newsSwiper13 new-list-13news">
							<div class="swiper-wrapper">
								<template v-for="(item,index) in newsList">
									<div v-if="index > 2 && index < 6" class="swiper-slide">
										<div class="list-item" @click="toDetail('newsDetail', item)">
											<img :src="baseUrl + item.picture">
											<div class="infoBox">
												<div class="name">{{item.title}}</div>
											</div>
										</div>
									</div>
								</template>
							</div>
							<!-- Add Pagination -->
							<div class="swiper-pagination"></div>
						</div>
					</div>
				</div>
				<div class="bottom" v-if="newsList.length > 6">
					<template v-for="(item,index) in newsList">
						<div v-if="index > 5" @click="toDetail('newsDetail', item)" class="list-item animation-box">
							<img :src="baseUrl + item.picture">
							<div class="name">{{item.title}}</div>
							<div class="desc">{{item.introduction}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{item.name}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{item.thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{item.storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{item.clicknum}}</span>
							</div>
						</div>
					</template>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendxiaoshouinfo" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">销售信息推荐</span>
				<span class="recommend_subhead">{{'xiaoshouinfo'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div v-if="xiaoshouinfoRecommend.length" class="list list12 index-pv1 list12xiaoshouinfo">
				<div class="list-body">
					<div class="item list-item animation-box" v-for="item,index in xiaoshouinfoRecommend" :key="index" @click="toDetail('xiaoshouinfoDetail', item)">
						<div class="name">厂商:{{item.changshang}}</div>
						<div class="name">车型:{{item.chexing}}</div>
						<div class="name">时间:{{item.tjtime}}</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('xiaoshouinfo')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				aboutUsDetail: {},
				systemIntroductionDetail: {},
				newsList: [],
				xiaoshouinfoRecommend: [],


				newListSwiper13news: null,



			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getAboutUs();
			this.getSystemIntroduction();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				if (this['newListSwiper13news']) this['newListSwiper13news'].destroy()
				setTimeout(()=>{
					this['newListSwiper13news'] = new Swiper(".new-list-13news", {"pagination":{"el":".swiper-pagination","clickable":true}})
				},750)
			},
			recommendIndexClick12(index, name) {
				this['recommendIndex12' + name] = index
				this.getList()
				
				document.querySelectorAll('.recommend .list12' + name + ' .list .item').forEach(el => {
					el.classList.remove("active")
				})
				setTimeout(() => {
					document.querySelectorAll('.recommend .list12' + name + ' .list .item').forEach(el => {
						el.classList.add("active")
					})
				}, 1);
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__fadeInLeftBig'},
					{id:'system',css:'animate__slideInUp'},
					{id:'animate_recommendxiaoshouinfo',css:'animate__zoomIn'},
					{id:'animate_newsnews',css:'animate__lightSpeedInLeft'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getAboutUs() {
				this.$http.get('aboutus/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.aboutUsDetail = res.data.data;
					}
				})
			},
			getSystemIntroduction() {
				this.$http.get('systemintro/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.systemIntroductionDetail = res.data.data;
					}
				})
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 10,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "xiaoshouinfo/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "xiaoshouinfo/autoSort2";
				}
				data = {
					page: 1,
					limit: 10,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.xiaoshouinfoRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		background: #fff;
		display: flex;
		width: 100%;
		#about {
			padding: 170px 0 136px;
			margin: 0 auto;
			background: url(http://codegen.caihongy.cn/20250218/2463e5c21b344582b044a7a4edf122cb.png) no-repeat bottom/100%;
			width: 100%;
			position: relative;
			height: auto;
			order: 2;
			.about_item {
				padding: 0 calc(50% - 600px);
				margin: 0px auto 0px;
				z-index: 9;
				overflow: hidden;
				align-content: flex-start;
				background: linear-gradient(0deg, rgb(39, 102, 205), rgb(25, 190, 212));
				display: flex;
				width: 100%;
				flex-wrap: wrap;
				height: 631px;
				.about_title_box {
					padding: 0 0 28px 60px;
					margin: 0 0 30px;
					top: 40px;
					background: url(http://codegen.caihongy.cn/20250218/698c52a55fc042a28aacea71589d4e23.png) no-repeat left center / 700px 100%;
					width: 1200px;
					position: absolute;
					text-align: left;
					.about_title {
						margin: 0 auto;
						color: rgb(25, 190, 212);
						background: none;
						font-weight: 600;
						display: inline-block;
						width: auto;
						font-size: 28px;
						line-height: 40px;
						text-align: center;
					}
					.about_subtitle {
						margin: 0;
						color: #999;
						display: none;
						width: 100%;
						font-size: 18px;
						line-height: 40px;
						text-align: center;
					}
				}
				.about_img {
					padding: 29px 0 140px 140px;
					margin: 0;
					z-index: 999;
					display: flex;
					right: 0;
					flex-wrap: wrap;
					border-radius: 0px;
					overflow: hidden;
					top: 150px;
					background: url(http://codegen.caihongy.cn/20250218/c939c8d609cd4dcc9061e6141ac3dc18.png) center/100% 100%;
					gap: 45px;
					width: 953px;
					position: absolute;
					height: 759px;
					order: 0;
					img:nth-child(1) {
						margin: 0;
						object-fit: cover;
						display: block;
						width: 50vw;
						height: 600px;
					}
					img:nth-child(2) {
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: none;
						width: 370px;
						height: 100%;
					}
					img:nth-child(3) {
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: none;
						width: 370px;
						height: 100%;
					}
				}
				.about_content {
					padding: 0 50% 30px 0;
					margin: 20px 2% 0 0;
					overflow: hidden;
					color: #fff;
					display: flex;
					width: 100%;
					font-size: 16px;
					line-height: 30px;
					align-items: center;
					height: 100%;
				}
				.about_idea1 {
					z-index: -1;
					top: 0;
					background: #d10602;
					display: none;
					width: 50%;
					position: absolute;
					right: 0;
					height: 400px;
				}
				.about_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_more {
					border: 0px solid rgb(0, 0, 0);
					padding: 0 20px;
					margin: 40px 0 0;
					color: #fff;
					display: block;
					line-height: 60px;
					right: calc(50% - 600px);
					border-radius: 0px;
					top: 30px;
					background: url("http://codegen.caihongy.cn/20250218/eb9fc96db122406ebbd41cc9ddb60a9e.png") center center / 100% 100%;
					width: 130px;
					position: absolute;
					text-align: center;
					order: 3;
					span:nth-child(1) {
						color: inherit;
						font-size: 16px;
					}
					span:nth-child(2) {
						color: inherit;
						display: none;
						font-size: 18px;
					}
				}
				.about_more:hover {
					cursor: pointer;
					opacity: 1;
				}
			}
		}
		#system {
			padding: 50px;
			margin: 0;
			background-repeat: no-repeat;
			background-size: 55% 100%;
			width: 100%;
			background-image: url(http://codegen.caihongy.cn/20250219/ef0c1081b6ae402a987d261568d0e36b.png);
			position: relative;
			background-position: right;
			height: 619px;
			order: 7;
			.system_item {
				padding: 0 0 0 560px;
				margin: 0 auto;
				display: flex;
				width: 1200px;
				flex-wrap: wrap;
				.system_title_box {
					padding: 0 0 28px 60px;
					margin: 0 auto 30px;
					background: url(http://codegen.caihongy.cn/20250218/698c52a55fc042a28aacea71589d4e23.png) no-repeat left center / 700px 100%;
					width: 100%;
					text-align: center;
					.system_title {
						margin: 0;
						color: #fff;
						background: none;
						font-weight: 500;
						width: 100%;
						font-size: 28px;
						line-height: 40px;
						text-align: left;
					}
					.system_subtitle {
						margin: 0;
						color: #999;
						display: none;
						width: 100%;
						font-size: 18px;
						line-height: 40px;
						text-align: center;
					}
				}
				.system_img {
					padding: 0;
					margin: 0;
					background: none;
					display: flex;
					width: 100%;
					justify-content: space-between;
					flex-wrap: wrap;
					height: auto;
					order: 2;
					img:nth-child(1) {
						border-radius: 0px;
						margin: 0;
						top: 0;
						object-fit: cover;
						display: block;
						width: 560px;
						position: absolute;
						right: 55%;
						height: 48%;
					}
					img:nth-child(2) {
						border-radius: 0px;
						margin: 0;
						bottom: 0;
						object-fit: cover;
						display: block;
						width: 560px;
						position: absolute;
						right: 55%;
						height: 48%;
					}
					img:nth-child(3) {
						border-radius: 50px;
						margin: 0;
						left: calc((100% - 1400px)/2 + 20% + 40px);
						bottom: 40px;
						object-fit: cover;
						display: none;
						width: 20%;
						position: absolute;
						height: 380px;
					}
				}
				.system_content {
					padding: 0 0 30px;
					margin: 0px 0 0;
					z-index: 99;
					overflow: hidden;
					color: rgb(255, 255, 255);
					background: none;
					width: 100%;
					font-size: 16px;
					line-height: 30px;
					height: auto;
				}
				.system_idea1 {
					padding: 0;
					margin: 0;
					z-index: 0;
					overflow: hidden;
					color: #666;
					background: #fff;
					display: none;
					width: 400px;
					font-size: 16px;
					line-height: 30px;
					height: 480px;
				}
				.system_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_more {
					border: 1px solid #000;
					margin: 0;
					z-index: 999;
					display: none;
					line-height: 50px;
					right: calc(50% - 600px);
					float: right;
					border-radius: 25px;
					background: rgb(247, 222, 235);
					width: 180px;
					position: absolute;
					text-align: center;
					order: 4;
					span:nth-child(1) {
						color: inherit;
						font-size: 16px;
					}
					span:nth-child(2) {
						color: inherit;
						display: none;
						font-size: 16px;
					}
				}
				.system_more:hover {
					cursor: pointer;
					opacity: 1;
				}
			}
		}
		.news {
			padding: 30px 0 0;
			margin: 0;
			background: rgb(241, 241, 241);
			width: 100%;
			position: relative;
			text-align: center;
			order: 4;
			.news_title_box {
				padding: 0 0 28px 60px;
				margin: 0 auto;
				background: url(http://codegen.caihongy.cn/20250218/698c52a55fc042a28aacea71589d4e23.png) no-repeat left center / 700px 100%;
				width: 1200px;
				position: relative;
				.news_title {
					margin: 0 auto;
					color: rgb(25, 190, 212);
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 1px;
					width: auto;
					font-size: 28px;
					line-height: 40px;
					text-align: left;
				}
				.news_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list13 {
				padding: 0;
				margin: 30px auto;
				color: #888;
				background: none;
				width: 1200px;
				font-size: 14px;
				height: auto;
				.top {
					margin: 0 0 10px;
					background: none;
					display: flex;
					width: 100%;
					justify-content: space-between;
					height: auto;
					.left {
						padding: 0 20px 0 0;
						flex-direction: column;
						display: flex;
						gap: 18px;
						width: 50%;
						height: auto;
						.list-item {
							cursor: pointer;
							border-radius: 10px;
							padding: 10px;
							margin: 0;
							background: #fff;
							display: flex;
							width: 100%;
							flex-wrap: wrap;
							text-align: left;
							height: auto;
							.name {
								overflow: hidden;
								color: #333;
								white-space: nowrap;
								font-weight: 600;
								width: 100%;
								font-size: 15px;
								line-height: 1.5;
								text-overflow: ellipsis;
							}
							.desc {
								margin: 5px 0;
								overflow: hidden;
								color: #666;
								white-space: nowrap;
								width: 100%;
								font-size: 14px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.time_item {
								padding: 0 10px 0 0;
								color: rgb(132, 143, 180);
								display: inline-block;
								order: 10;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									display: none;
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								color: rgb(144, 188, 195);
								display: inline-block;
								order: 9;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									display: none;
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								color: rgb(197, 201, 255);
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									display: none;
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								color: rgb(254, 216, 39);
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									display: none;
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								color: rgb(160, 187, 220);
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									display: none;
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.news-swiper13 {
						width: 50%;
						height: auto;
						.swiper-slide {
							.list-item {
								width: 100%;
								position: relative;
								height: auto;
								img {
									cursor: pointer;
									object-fit: cover;
									display: block;
									width: 100%;
									height: 340px;
								}
								.infoBox {
									left: 0;
									bottom: 0;
									background: rgba(0,0,0,.3);
									width: 100%;
									position: absolute;
									.name {
										padding: 0 10px;
										overflow: hidden;
										color: #fff;
										white-space: nowrap;
										width: 100%;
										font-size: 16px;
										line-height: 44px;
										text-overflow: ellipsis;
									}
								}
							}
						}
						/deep/.swiper-pagination {
							left: 0;
							bottom: 10px;
							width: 100%;
							text-align: right;
							/deep/ span.swiper-pagination-bullet {
								border-radius: 100%;
								margin: 0 4px;
								background: #fff;
								display: inline-block;
								width: 10px;
								opacity: .2;
								height: 10px;
							}
							
							/deep/ span.swiper-pagination-bullet:hover {
								background: red;
								opacity: 1;
							}
							
							/deep/ span.swiper-pagination-bullet.swiper-pagination-bullet-active {
								background: red;
								opacity: 1;
							}
						}
					}
				}
				.bottom {
					margin: 20px 0 0 -10px;
					display: flex;
					width: calc(100% + 20px);
					height: auto;
					.list-item {
						cursor: pointer;
						margin: 0 10px;
						color: #fff;
						background: url(http://codegen.caihongy.cn/20250218/fadb01632c3e42ec86510dfaff6c8666.png) center/100% 100%;
						display: flex;
						width: calc(25% - 20px);
						position: relative;
						flex-wrap: wrap;
						height: auto;
						img {
							border-radius: 10px;
							object-fit: cover;
							display: block;
							width: 100%;
							height: 250px;
						}
						.name {
							padding: 0 10px;
							overflow: hidden;
							color: #fff;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 15px;
							line-height: 30px;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 0 10px;
							overflow: hidden;
							white-space: nowrap;
							width: 100%;
							line-height: 24px;
							text-overflow: ellipsis;
							height: 24px;
						}
						.time_item {
							padding: 10px 0 10px 10px;
							display: inline-block;
							order: 10;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 0 0 0px;
							display: inline-block;
							width: 25%;
							order: 9;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 0 0 0px;
							display: inline-block;
							width: 25%;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 0 0 0px;
							display: inline-block;
							width: 25%;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 0 0 0px;
							display: inline-block;
							width: 25%;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #000;
				cursor: pointer;
				padding: 0 20px;
				margin: 20px auto 40px;
				color: #fff;
				display: inline-block;
				line-height: 60px;
				right: calc(50% - 600px);
				border-radius: 25px;
				top: 0;
				background: url("http://codegen.caihongy.cn/20250218/eb9fc96db122406ebbd41cc9ddb60a9e.png") center center / 100% 100%;
				width: 130px;
				position: absolute;
				text-align: center;
				.text {
					font-size: 16px;
				}
				.icon {
					color: #333;
					display: none;
					font-size: 15px;
				}
			}
		}
		.recommend {
			padding: 30px 0 10px;
			margin: 0px auto;
			background: rgb(239, 239, 239);
			width: 100%;
			position: relative;
			text-align: center;
			order: 6;
			.recommend_title_box {
				padding: 0 0 28px 60px;
				margin: 0 auto;
				background: url(http://codegen.caihongy.cn/20250218/698c52a55fc042a28aacea71589d4e23.png) no-repeat left center / 700px 100%;
				width: 1200px;
				position: relative;
				text-align: center;
				.recommend_title {
					margin: 0 auto;
					color: rgb(25, 190, 212);
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 1px;
					width: auto;
					font-size: 28px;
					line-height: 40px;
					text-align: left;
				}
				.recommend_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
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
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list12 {
				padding: 0;
				margin: 0 auto;
				background: none;
				width: 1200px;
				height: auto;
				.tab_view {
					margin: 0 0 40px;
					display: flex;
					width: 100%;
					justify-content: center;
					height: auto;
					.tab {
						cursor: pointer;
						border: 0px solid rgb(0, 0, 0);
						padding: 0 20px;
						margin: 0 10px;
						color: rgb(25, 190, 212);
						display: flex;
						width: 140px;
						font-size: 16px;
						line-height: 70px;
						align-items: center;
						img {
							margin: 0 5px 0 0;
							object-fit: cover;
							display: block;
							width: 34px;
							height: 34px;
						}
						.text {
							color: inherit;
							font-size: 16px;
						}
					}
					.tab:hover {
						border: 0px solid #ddd;
						color: #fff;
						background: url(http://codegen.caihongy.cn/20250218/eb9fc96db122406ebbd41cc9ddb60a9e.png) center/100% 100%;
					}
					.tab.active {
						color: #fff;
						background: url(http://codegen.caihongy.cn/20250218/eb9fc96db122406ebbd41cc9ddb60a9e.png) center/100% 100%;
						border-color: rgb(0, 0, 0);
						border-width: 0px;
						border-style: solid;
					}
					.more_btn {
						cursor: pointer;
						padding: 5px 10px;
						margin: 0 10px;
						color: #666;
						background: #fff;
						display: none;
						line-height: 44px;
						align-items: center;
						.text {
							color: inherit;
							font-size: 16px;
						}
						.icon {
							margin: 0 0 0 2px;
							color: inherit;
							font-size: 16px;
						}
					}
					.more_btn:hover {
						color: red;
					}
					.tab.active {
						animation-name: mymove;
					
						&:nth-of-type(1) {
							animation-duration: 1s;
						}
						&:nth-of-type(2) {
							animation-duration: 1.2s;
						}
						&:nth-of-type(3) {
							animation-duration: 1.4s;
						}
						&:nth-of-type(4) {
							animation-duration: 1.6s;
						}
						&:nth-of-type(5) {
							animation-duration: 1.8s;
						}
						&:nth-of-type(6) {
							animation-duration: 2s;
						}
					}
					
					@keyframes mymove {
						from {top: 320px;}
						to {top: 0;}
					}
				}
				.list-body {
					overflow: hidden;
					flex: 1;
					background: none;
					display: flex;
					gap: 12px;
					flex-wrap: wrap;
					height: auto;
					.list-item {
						cursor: pointer;
						border-radius: 10px;
						padding: 0 0 10px 0;
						margin: 0;
						background: #fff;
						width: 230px;
						border-width: 0 0px 0 0;
						position: relative;
						border-style: dashed ;
						height: auto;
						img {
							border-radius: 10px;
							object-fit: cover;
							display: block;
							width: 100%;
							height: 260px;
						}
						.name {
							padding: 0 5px;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							width: 100%;
							font-size: 15px;
							line-height: 30px;
							text-overflow: ellipsis;
							text-align: center;
						}
						.price {
							padding: 0px;
							color: #f00;
							font-size: 16px;
							line-height: 1.5;
						}
					}
					.list-item.active {
						animation-name: mymove;
					
						&:nth-of-type(1) {
							animation-duration: 1s;
						}
						&:nth-of-type(2) {
							animation-duration: 1.2s;
						}
						&:nth-of-type(3) {
							animation-duration: 1.4s;
						}
						&:nth-of-type(4) {
							animation-duration: 1.6s;
						}
						&:nth-of-type(5) {
							animation-duration: 1.8s;
						}
						&:nth-of-type(6) {
							animation-duration: 2s;
						}
					}
					
					@keyframes mymove {
						from {top: 320px;}
						to {top: 0;}
					}
				}
			}
			.moreBtn {
				border: 0px solid #000;
				cursor: pointer;
				padding: 0 20px;
				margin: 30px auto;
				color: #fff;
				display: inline-block;
				line-height: 60px;
				right: calc(50% - 600px);
				border-radius: 25px;
				top: 0;
				background: url("http://codegen.caihongy.cn/20250218/eb9fc96db122406ebbd41cc9ddb60a9e.png") center center / 100% 100%;
				width: 130px;
				position: absolute;
				text-align: center;
				.text {
					font-size: 16px;
				}
				.icon {
					color: #fff;
					display: none;
					font-size: 15px;
				}
			}
		}
	}
</style>
