<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/discussxiaoshouinfo?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
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
						<div class="lable">关联表id</div>
						<div class="text "  >{{detail.refid}}</div>
					</div>
					<div class="item">
						<div class="lable">用户名</div>
						<div class="text "  >{{detail.nickname}}</div>
					</div>
					<div class="item">
						<div class="lable">评论内容</div>
						<div class="text "  >{{detail.content}}</div>
					</div>
					<div class="item">
						<div class="lable">评分</div>
						<div class="text "  >{{detail.score}}</div>
					</div>
					<div class="item">
						<div class="lable">回复内容</div>
						<div class="text "  >{{detail.reply}}</div>
					</div>
					<div class="item">
						<div class="lable">置顶(1:置顶,0:非置顶)</div>
						<div class="text "  >{{detail.istop}}</div>
					</div>
					<div class="item">
						<div class="lable">赞用户ids</div>
						<div class="text "  >{{detail.tuserids}}</div>
					</div>
					<div class="item">
						<div class="lable">踩用户ids</div>
						<div class="text "  >{{detail.cuserids}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('discussxiaoshouinfo','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('discussxiaoshouinfo','删除')" @click="delClick">删除</el-button>
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
				<el-tab-pane label="评论" name="second">
					<el-form class="add commentForm" :model="form" :rules="rules" ref="form">
						<el-form-item class="item" label="评论" prop="content">
							<editor
								myQuillEditor="content"
								v-model="form.content" 
								class="editor" 
								action="file/upload">
							</editor>
						</el-form-item>
						<el-form-item class="commentBtn">
							<el-button class="submitBtn" type="primary" @click="submitForm('form')">立即提交</el-button>
							<el-button class="resetBtn" @click="resetForm('form')">重置</el-button>
						</el-form-item>
					</el-form>
				
					<div v-if="infoList.length" class="comment-list">
						<div class="comment-item" v-for="item in infoList" :key="item.id" @mouseenter="discussEnter(item.id)"
							@mouseleave="discussLeave">
							<div class="istop" v-if="item.istop">
								<span class="icon iconfont icon-jiantou24"></span>
							</div>
							<div class="user">
								<el-image v-if="item.avatarurl" :size="50" :src="baseUrl + item.avatarurl"></el-image>
								<el-image v-if="!item.avatarurl" :size="50" :src="require('@/assets/touxiang.png')"></el-image>
								<div class="name">{{item.nickname}}</div>
							</div>
							<div class="comment-content-box">
								<div class="ql-snow ql-editor" v-html="item.content"></div>
								<div class="comment-time">{{item.addtime}}</div>
								<div class="zancai-box">
									<div v-if="!comcaiChange(item)" class="zan-item" :class="comzanChange(item)?'active':''" @click="comzanClick(item)">
										<span class="icon iconfont" :class="comzanChange(item)?'icon-zan11':'icon-zan07'"></span>
										<span class="label">{{comzanChange(item)?'已赞':'赞'}}</span>
										<span class="num">({{item.thumbsupnum}})</span>
									</div>
									<div v-if="!comzanChange(item)" class="cai-item" :class="comcaiChange(item)?'active':''" @click="comcaiClick(item)">
										<span class="icon iconfont" :class="comcaiChange(item)?'icon-cai16':'icon-cai01'"></span>
										<span class="label">{{comcaiChange(item)?'已踩':'踩'}}</span>
										<span class="num">({{item.crazilynum}})</span>
									</div>
								</div>
								<div class="comment-btn">
									<!-- <el-button :style='{"border":"0","cursor":"pointer","padding":"0 20px","margin":"0 10px","color":"#fff","borderRadius":"0px","background":"rgb(213, 103, 147)","width":"auto","lineHeight":"32px","fontSize":"14px","minWidth":"90px","height":"32px"}'>回复</el-button> -->
									<el-button class="delBtn" v-if="showIndex==item.id&&userid==item.userid" @click="discussDel(item.id)">删除</el-button>
								</div>
							</div>
							<div class="comment-content-box" v-if="item.reply">
								回复：<span class="ql-snow ql-editor" v-html="item.reply"></span>
							</div>
						</div>
					</div>
				
					<el-pagination
						background
						id="pagination" class="pagination"
						:page-size="pageSize"
						prev-text="上一页"
						next-text="下一页"
						:hide-on-single-page="false"
						:layout='["total","prev","pager","next","sizes","jumper"].join()'
						:total="total"
						@current-change="curChange"
						@prev-click="prevClick"
						@next-click="nextClick"
						@size-change="sizeChange"
						></el-pagination>
				</el-tab-pane>
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
				tablename: 'discussxiaoshouinfo',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: 'xiaoshouinfo评论表'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 1,
				activeName: 'second',
				form: {
					content: '',
					userid: Number(localStorage.getItem('frontUserid')),
					nickname: localStorage.getItem('username'),
					avatarurl: '',
				},
				showIndex: -1,
				infoList: [],
				rules: {
					content: [
						{ required: true, message: '请输入内容', trigger: 'blur' }
					],
				},
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
						this.getDiscussList(1);
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
					this.$router.push({path: '/index/discussxiaoshouinfo', query: params});
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
			getDiscussList(page) {
				this.$http.get('discussdiscussxiaoshouinfo/list', {params: {page, limit: this.pageSize, refid: this.detail.id,sort: 'istop',order: 'desc'}}).then(res => {
					if (res.data.code == 0) {
						this.infoList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
					}
				});
			},
			comzanChange(row){
				if(row.tuserids){
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comzanClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comzanChange(row)){
					row.thumbsupnum++
					if(row.tuserids){
						row.tuserids = row.tuserids + ',' + this.userid
					}else {
						row.tuserids = String(this.userid)
					}
					this.$http.post('discussdiscussxiaoshouinfo/update',row).then(rs=>{
						this.$message.success('点赞成功')
					})
				}else {
					row.thumbsupnum--
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.tuserids = arr.join(',')
					this.$http.post('discussdiscussxiaoshouinfo/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			comcaiChange(row){
				if(row.cuserids){
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comcaiClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comcaiChange(row)){
					row.crazilynum++
					if(row.cuserids){
						row.cuserids = row.cuserids + ',' + this.userid
					}else {
						row.cuserids = String(this.userid)
					}
					this.$http.post('discussdiscussxiaoshouinfo/update',row).then(rs=>{
						this.$message.success('点踩成功')
					})
				}else {
					row.crazilynum--
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.cuserids = arr.join(',')
					this.$http.post('discussdiscussxiaoshouinfo/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			discussEnter(index){
				this.showIndex = index
			},
			discussLeave(){
				this.showIndex = -1
			},
			discussDel(id){
				this.$confirm('是否删除此评论？').then(_ => {
					this.$http.post('discussdiscussxiaoshouinfo/delete',[id]).then(res=>{
						if(res.data&&res.data.code==0){
							this.addDiscussNum(1)
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									this.getDiscussList(1);
								}
							});
						}
					})
				}).catch(_ => {});
			},
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.form.refid = this.detail.id;
						this.form.avatarurl = localStorage.getItem('frontHeadportrait')?localStorage.getItem('frontHeadportrait'):'';
						this.$http.post('discussdiscussxiaoshouinfo/add', this.form).then(rs2 => {
							if (rs2.data.code == 0) {
								this.form.content = '';
								this.addDiscussNum(2)
								this.getDiscussList(1);
								this.$message({
									type: 'success',
									message: '评论成功!',
									duration: 1500,
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			resetForm(formName) {
				this.$refs[formName].resetFields();
			},
			addDiscussNum(type){
				if(type==2){
					this.detail.discussnum++
				}else if(type==1){
					if(this.detail.discussnum!=0){
						this.detail.discussnum--
					}else{
						this.detail.discussnum = 0
					}
				}
				this.$http.post('discussxiaoshouinfo/update',this.detail).then(res=>{})
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
				this.$router.push(`/index/discussxiaoshouinfoAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此xiaoshouinfo评论表？') .then(_ => {
					this.$http.post('discussxiaoshouinfo/delete', [this.detail.id]).then(async res => {
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
			.commentForm {
				box-shadow: none;
				padding: 0;
				margin: 20px 0;
				width: 100%;
				.item {
					padding: 0;
					display: flex;
					width: 100%;
					height: auto;
					/deep/ .el-form-item__label {
						padding: 0 10px 0 0;
						color: #666;
						white-space: nowrap;
						font-weight: 500;
						width: auto;
						font-size: inherit;
						line-height: 40px;
						text-align: right;
					}
					.editor {
						border: 1px solid #ccc;
						border-radius: 4px;
						box-shadow: 0 0 0px rgba(80, 80, 80, .2);
						color: #333;
						background: #fff;
						width: 75%;
						font-size: 14px;
						min-height: 150px;
						line-height: 32px;
						/deep/ .avatar-uploader {
							height: 0;
							line-height: 0;
						}
					}
				}
				.commentBtn {
					padding: 0;
					margin: 10px 0 0;
					width: 100%;
					text-align: right;
					height: auto;
					.submitBtn {
						border: 0;
						cursor: pointer;
						border-radius: 0px;
						padding: 0 20px 0 25px;
						margin: 0 20px 0 0;
						color: #fff;
						background: rgb(213, 103, 147);
						width: 170px;
						font-size: 15px;
						line-height: 40px;
						min-width: 110px;
						height: 40px;
					}
					.submitBtn:hover {
						opacity: 0.8;
					}
					.resetBtn {
						border: 0;
						cursor: pointer;
						border-radius: 0px;
						padding: 0 20px 0 25px;
						margin: 0 20px 0 0;
						color: #333;
						background: #c5c5c5;
						width: auto;
						font-size: 15px;
						line-height: 40px;
						min-width: 110px;
						height: 40px;
					}
					.resetBtn:hover {
						opacity: 0.8;
					}
				}
			}
			.comment-list {
				box-shadow: none;
				padding: 0;
				margin: 40px 0 0;
				display: flex;
				width: 100%;
				justify-content: space-between;
				flex-wrap: wrap;
				.comment-item {
					padding: 10px;
					margin: 0 0 20px;
					width: 100%;
					border-color: rgb(213, 103, 147);
					border-width: 1px;
					align-items: center;
					border-style: solid;
					height: auto;
					.istop {
						box-shadow: 0 4px 8px rgba(0,0,0,.1);
						top: 0;
						background: #fff;
						position: absolute;
						right: 10px;
						.icon {
							color: #000;
						}
					}
					.user {
						padding: 5px;
						background: #fff;
						display: flex;
						width: 100%;
						align-items: center;
						height: auto;
						.el-image {
							border-radius: 10px;
							margin: 0 10px 0 0;
							object-fit: cover;
							width: 60px;
							height: 60px;
						}
						.name {
							color: #333;
							font-weight: 600;
							font-size: 16px;
						}
					}
					.comment-time {
						color: #666;
					}
					.comment-content-box {
						border-radius: 4px;
						padding: 8px;
						margin: 10px 0px 0px;
						word-wrap: break-word;
						color: #888;
						background: none;
						font-size: 14px;
						line-height: 1.5;
						.zancai-box {
							margin: 8px 0 0 0;
							display: flex;
							width: 100%;
							justify-content: flex-end;
							align-items: center;
							height: 30px;
							.zan-item {
								display: flex;
								align-items: center;
								.icon {
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								font-size: 14px;
								}
							}
							.zan-item.active {
								background: none;
								.icon {
								color: #ff0000;
								font-size: 14px;
								}
								.label {
								color: #ff0000;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #ff0000;
								font-size: 14px;
								}
							}
							.zan-item:hover {
								opacity: 0.8;
								.icon {
								color: #ff000030;
								}
								.label {
								color: #ff000030;
								}
								.num {
								color: #ff000030;
								}
							}
							.cai-item {
								display: flex;
								align-items: center;
								.icon {
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								font-size: 14px;
								}
							}
							.cai-item.active {
								background: none;
								.icon {
								color: #ff0000;
								font-size: 14px;
								}
								.label {
								color: #ff0000;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #ff0000;
								font-size: 14px;
								}
							}
							.cai-item:hover {
								opacity: 0.8;
								.icon {
								color: #ff000030;
								}
								.label {
								color: #ff000030;
								}
								.num {
								color: #ff000030;
								}
							}
						}
						.comment-btn {
							margin: 8px 0 0 0;
							display: flex;
							width: 100%;
							justify-content: flex-end;
							align-items: center;
							height: 40px;
							.delBtn {
								border: 0;
								cursor: pointer;
								padding: 0 20px;
								margin: 0 0px 0 10px;
								color: #000;
								font-size: 14px;
								line-height: 32px;
								border-radius: 0px;
								outline: none;
								background: rgb(211, 211, 210);
								width: auto;
								min-width: 90px;
								height: 32px;
							}
						}
					}
				}
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
