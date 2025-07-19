<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/users?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
						</div>
					</div>
					<div class="item">
						<div class="lable">用户名</div>
						<div class="text "  >{{detail.username}}</div>
					</div>
					<div class="item">
						<div class="lable">角色</div>
						<div class="text "  >{{detail.role}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('users','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('users','删除')" @click="delClick">删除</el-button>
					</div>
				</div>
			</div>
		
			<div class="swiper3" v-if="detailBanner.length">
				<div class="big">
					<img id="big" :src="swiperBigUrl" class="image">
				</div>
				<div class="samll">
					<div class="swiper3-small-item" v-for="item in detailBanner" :key="item.id">
						<img v-if="item.substr(0,4)=='http'" :src="item" @click="swiperClick3(item)" class="image">
						<img v-else :src="baseUrl + item" @click="swiperClick3(baseUrl + item)" class="image">
					</div>
				</div>
			</div>


		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
			</el-tabs>

			<div class="idea1"></div>
			<div class="idea2"></div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'users',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '管理员'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 0,
				activeName: 'first',
				total: 1,
				pageSize: 10,
				totalPage: 1,
				buynumber: 1,
				centerType: false,
				storeupType: false,
				swiperBigUrl: null,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		//方法集合
		methods: {
			swiperClick3(src) {
				this.swiperBigUrl = src
			},
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
						}

					}
					if (this.detailBanner.length) {
						if (this.detailBanner[0].substr(0,4)=='http') {
							this.swiperBigUrl = this.detailBanner[0]
						} else {
							this.swiperBigUrl = this.baseUrl + this.detailBanner[0]
						}
					}
				});
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/users', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + '/file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + '/file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/usersAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此管理员？') .then(_ => {
					this.$http.post('users/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									history.back()
								}
							});
						}
					});
				}).catch(_ => {});
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 20px calc((100% - 1200px)/2);
		margin: 0px auto;
		color: #666;
		align-content: flex-start;
		background: rgb(237, 237, 237);
		display: flex;
		width: 100%;
		font-size: 16px;
		justify-content: space-between;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 30px;
			margin: 30px 0;
			background: #fff;
			display: block;
			width: 100%;
			position: relative;
			order: 2;
			.info {
				padding: 0;
				margin: 0;
				align-content: flex-start;
				background: none;
				display: flex;
				gap: 20px;
				width: 100%;
				justify-content: space-between;
				align-items: flex-start;
				flex-wrap: wrap;
				.title-item {
					border-radius: 5px;
					padding: 10px 6px;
					margin: 0;
					background: #fff;
					display: flex;
					width: 46%;
					border-color: rgb(25, 190, 212);
					border-width: 1px;
					line-height: 1.5;
					justify-content: space-between;
					align-items: center;
					border-style: solid;
					.detail-title {
						color: #000;
						font-weight: 600;
						font-size: 18px;
					}
				}
				.item {
					border-radius: 5px;
					padding: 10px 6px !important;
					margin: 0;
					background: #fff;
					display: inline-flex;
					width: 46%;
					border-color: rgb(25, 190, 212);
					border-width: 1px;
					border-style: solid;
					.lable {
						padding: 0 10px 0 0;
						color: #333;
						white-space: nowrap;
						font-weight: 500;
						width: auto;
						font-size: inherit;
						line-height: 40px;
						text-align: right;
						height: auto;
					}
					.text {
						padding: 8px 10px 0;
						color: inherit;
						word-break: break-all;
						flex: 1;
						font-size: inherit;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					width: 100%;
					font-size: 14px;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0px solid rgba(64, 158, 255, .3);
					cursor: pointer;
					border-radius: 0px;
					padding: 0 10px;
					margin: 0 5px 0 0;
					color: #fff;
					background: rgb(93, 195, 190);
					width: auto;
					font-size: inherit;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
				}
				.delBtn {
					border: 0px solid rgba(209, 6, 2, .3);
					cursor: pointer;
					border-radius: 0px;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: rgb(33, 139, 208);
					width: auto;
					font-size: inherit;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
				}
			}
		}
		.swiper3 {
			background: none;
			display: flex;
			width: 100%;
			height: auto;
			.big {
				border: 0px solid red;
				margin: 0 0 0px;
				background: #fff;
				width: calc(100% - 175px);
				position: relative;
				height: 488px;
				img {
					box-shadow: none;
					z-index: 1;
					top: 0px;
					left: 0px;
					object-fit: cover;
					display: block;
					width: 100%;
					position: absolute;
					height: 100%;
				}
			}
			.samll {
				padding: 128px 0px 0 10px;
				flex-direction: column;
				background: none;
				display: flex;
				gap: 10px;
				width: 165px;
				height: auto;
				.swiper3-small-item {
					border: 0px solid red;
					margin: 0 0px;
					flex: 1;
					background: #fff;
					position: relative;
					height: 100%;
					img {
						box-shadow: none;
						z-index: 1;
						top: 0px;
						left: 0px;
						object-fit: cover;
						display: block;
						width: 100%;
						position: absolute;
						height: 100%;
					}
				}
			}
		}
		.detail-tabs {
			border: 0px solid #2a3b5e50;
			border-radius: 8px;
			box-shadow: none;
			padding: 20px 20px;
			margin: 20px auto;
			background: #fff;
			display: flex;
			width: 100%;
			flex-wrap: wrap;
			order: 10;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				border-radius: 20px 20px 0 0;
				padding: 10px 20px;
				margin: 0;
				flex-direction: column;
				background: rgb(25, 190, 212);
				display: flex;
				width: 100%;
				border-color: #24355950;
				border-width: 0px;
				border-style: solid;
				flex-wrap: wrap;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0px solid #ccc;
				padding: 0 0px;
				margin: 0 30px 0 0;
				color: #fff;
				font-weight: 500;
				display: inline-block;
				font-size: 16px;
				line-height: 30px;
				transition: all 0s;
				border-radius: 20px;
				background: none;
				width: 80px;
				position: relative;
				list-style: none;
				text-align: center;
				height: 30px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0px solid #000;
				margin: 0 30px 0 0;
				color: #000;
				background: none;
				width: 80px;
				font-size: 16px;
				line-height: 30px;
				text-align: center;
				height: 30px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0px solid #000;
				border-radius: 20px;
				margin: 0 30px 0 0;
				color: rgb(25, 190, 212);
				background: rgb(255, 255, 255);
				width: 80px;
				font-size: 16px;
				line-height: 30px;
				text-align: center;
				height: 30px;
			}
			
			/deep/ .el-tabs__content {
				border: 0px solid #24355950;
				padding: 30px 0;
				width: 100%;
			}
		}
	}
	.idea1 {
		background: none;
		display: none;
		width: 100%;
		height: 1px;
		order: 4;
	}
	.idea2 {
		background: none;
		display: none;
		width: 100%;
		height: 1px;
		order: 6;
	}
</style>
