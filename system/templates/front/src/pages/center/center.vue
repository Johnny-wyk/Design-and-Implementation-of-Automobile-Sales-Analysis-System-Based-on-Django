<template>
	<div class="center-preview">
		<div class="center-title">{{ title }}</div>
		<div class="center-info">
			<div class="center-info-title">个人信息</div>
			<div class="img-box" v-if="userTableName=='yonghu'">
				<img :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')">
			</div>
			<div class="info-item1" v-if="userTableName=='yonghu'">
				<span class="icon iconfont "></span>
				<div class="label">用户账号：</div>
				<div class="text">{{sessionForm.yonghuzhanghao}}</div>
			</div>
			<div class="info-item2" v-if="userTableName=='yonghu'">
				<span class="icon iconfont "></span>
				<div class="label">用户姓名：</div>
				<div class="text">{{sessionForm.yonghuxingming}}</div>
			</div>
			<div class="info-item3" v-if="userTableName=='yonghu'">
				<span class="icon iconfont "></span>
				<div class="label">性别：</div>
				<div class="text">{{sessionForm.xingbie}}</div>
			</div>
			<div class="info-item4" v-if="userTableName=='yonghu'">
				<span class="icon iconfont "></span>
				<div class="label">联系电话：</div>
				<div class="text">{{sessionForm.lianxidianhua}}</div>
			</div>
			<div class="info-item5" v-if="userTableName=='yonghu'">
				<span class="icon iconfont "></span>
				<div class="label">邮箱：</div>
				<div class="text">{{sessionForm.email}}</div>
			</div>
		
		</div>
	
		<el-tabs class="center-tabs" tab-position="left" @tab-click="handleClick">
			<el-tab-pane label="个人中心">
				<el-form class="center-preview-pv" ref="sessionForm" :model="sessionForm" :rules="rules" label-width="180px">
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户账号" prop="yonghuzhanghao">
						<el-input v-model="sessionForm.yonghuzhanghao" placeholder="用户账号" readonly></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户姓名" prop="yonghuxingming">
						<el-input v-model="sessionForm.yonghuxingming" placeholder="用户姓名" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="性别" prop="xingbie">
						<el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
							<el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="头像" prop="touxiang">
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
							@change="yonghutouxiangHandleAvatarSuccess"
							></file-upload>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="联系电话" prop="lianxidianhua">
						<el-input v-model="sessionForm.lianxidianhua" placeholder="联系电话" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="邮箱" prop="email">
						<el-input v-model="sessionForm.email" placeholder="邮箱" ></el-input>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="onSubmit('sessionForm')">
							<span class="icon iconfont "></span>
							<span class="text">更新信息</span>
						</div>
						<div class="closeBtn" type="danger" @click="logout">
							<span class="icon iconfont "></span>
							<span class="text">退出登录</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane label="修改密码">
				<el-form class="center-preview-pv" ref="passwordForm" :model="passwordForm" :rules="passwordRules" label-width="180px">
					<el-form-item class="center-item" label="原密码" prop="password">
						<el-input type="password" v-model="passwordForm.password" placeholder="原密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="新密码" prop="newpassword">
						<el-input type="password" v-model="passwordForm.newpassword" placeholder="新密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="确认密码" prop="repassword">
						<el-input type="password" v-model="passwordForm.repassword" placeholder="确认密码"></el-input>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="updatePassword">
							<span class="icon iconfont "></span>
							<span class="text">修改密码</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane v-for="(item,index) in menuList" :key="index" v-if="hasBack(item.menu)" :label="item.child[0].menu" :name="item.child[0].tableName"></el-tab-pane>
			<el-tab-pane label="我的发布"></el-tab-pane>
			<el-tab-pane label="我的收藏"></el-tab-pane>
		</el-tabs>

	</div>
</template>

<script>
	import config from '@/config/config';
	import menu from '@/config/menu';
	import Vue from 'vue';
	export default {
		//数据集合
		data() {
			return {
				title: '个人中心',
				baseUrl: config.baseUrl,
				sessionForm: {},
				passwordForm: {},
				passwordRules: {
					password: [
						{
							required: true,
							message: "密码不能为空",
							trigger: "blur"
						}
					],
					newpassword: [
						{
							required: true,
							message: "新密码不能为空",
							trigger: "blur"
						}
					],
					repassword: [
						{
							required: true,
							message: "确认密码不能为空",
							trigger: "blur"
						}
					]
				},
				rules: {},
				menuList: [],
				disabled: false,
				uploadUrl: config.baseUrl + 'file/upload',
				imageUrl: '',
				headers: {Token: localStorage.getItem('frontToken')},
				userTableName: localStorage.getItem('UserTableName'),
				dynamicProp: {},
			}
		},
		created() {
			let menus = menu.list()
			for(let x in menus){
				if(menus[x].tableName == this.userTableName){
					for(let i in menus[x].backMenu){
						if(menus[x].backMenu[i].menu=='考试管理'){
							menus[x].backMenu.splice(i,1)
						}
					}
					this.menuList = menus[x].backMenu
				}
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuzhanghao', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'mima', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuxingming', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'xingbie', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'touxiang', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'lianxidianhua', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'email', null);
			}

			if ('yonghu' == this.userTableName&&this.rules['yonghuzhanghao']){
				this.rules['yonghuzhanghao'].push({ required: true, message: '请输入用户账号', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuzhanghao']) {
				this.$set(this.rules, 'yonghuzhanghao', [{ required: true, message: '请输入用户账号', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['mima']){
				this.rules['mima'].push({ required: true, message: '请输入密码', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['mima']) {
				this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['yonghuxingming']){
				this.rules['yonghuxingming'].push({ required: true, message: '请输入用户姓名', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuxingming']) {
				this.$set(this.rules, 'yonghuxingming', [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'lianxidianhua', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'email', [{ required: false, validator: this.$validate.isEmail, trigger: 'blur' }]);
			}

			this.init();
			this.sessionForm = JSON.parse(localStorage.getItem('sessionForm'))
		},
		//方法集合
		methods: {
			init() {
				if ('yonghu' == this.userTableName) {
					this.dynamicProp.xingbie = '男,女'.split(',');
				}
			},
			setSession(){
				localStorage.setItem('sessionForm',JSON.stringify(this.sessionForm))
			},
			onSubmit(formName) {
				if(`yonghu` == this.userTableName && this.sessionForm.touxiang!=null){
					this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
				}
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
							if (res.data.code == 0) {
								this.setSession()
								this.$message({
									message: '更新成功',
									type: 'success',
									duration: 1500
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			yonghutouxiangHandleAvatarSuccess(fileUrls) {
				this.sessionForm.touxiang = fileUrls;
			},
			handleClick(tab, event) {
				switch(event.target.outerText) {
					case '个人中心':
						tab.$router.push('/index/center');
						break;
					case '修改密码':
						this.passwordForm = {
							password: '',
							newpassword: '',
							repassword: '',
						}
						this.$forceUpdate()
						break;
					case '我的发布':
						tab.$router.push('/index/myForumList');
						break;
					case '我的收藏':
						localStorage.setItem('storeupType', 1);
						tab.$router.push('/index/storeup');
						break;
					default:
						tab.$router.push(`/index/${tab.name}?centerType=1`);
				}

				this.title = event.target.outerText;
			},
			async updatePassword(){
				this.$refs["passwordForm"].validate(async valid => {
					if (valid) {
						var password = "";
						if (this.sessionForm.mima) {
							password = this.sessionForm.mima;
						} else if (this.sessionForm.password) {
							password = this.sessionForm.password;
						}
						if (this.userTableName == 'yonghu') {
						}
						if (this.passwordForm.password != password) {
							this.$message.error("原密码错误");
							return;
						}
						if (this.passwordForm.newpassword != this.passwordForm.repassword) {
							this.$message.error("两次密码输入不一致");
							return;
						}
						if (this.passwordForm.newpassword == this.passwordForm.password) {
							this.$message.error("新密码与原密码相同！");
							return;
						}
						this.sessionForm.password = this.passwordForm.newpassword;
						this.sessionForm.mima = this.passwordForm.newpassword;
						this.$http.post(`${this.userTableName}/update`,this.sessionForm).then(({data})=>{
							if (data && data.code === 0) {
								this.$message({
									message: "修改密码成功,下次登录系统生效",
									type: "success",
									duration: 1500,
									onClose: () => {
									}
								});
								this.setSession()
							} else {
								this.$message.error(data.msg);
							}
						});
					}
				})
			},
			logout() {
				localStorage.clear();
				Vue.http.headers.common['Token'] = "";
				this.$router.push('/index/home');
				this.activeIndex = '0'
				localStorage.setItem('keyPath', this.activeIndex)
				this.$forceUpdate()
				this.$message({
					message: '登出成功',
					type: 'success',
					duration: 1500,
				});
			},
			hasBack(name){
				switch(name){
					case '我的收藏管理':
						return false
						break;
					case '看板管理':
						return false
						break;
					default:
						return true
				}
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.center-preview {
		padding: 30px 0;
		margin: 0px auto;
		color: #666;
		display: flex;
		gap: 20px;
		width: 1200px;
		font-size: 16px;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.center-title {
			padding: 0 0 0 50px;
			margin: 0px auto 0;
			color: rgb(25, 190, 212);
			background: url(http://codegen.caihongy.cn/20250220/e85584abac2c4b3ebee6d1c211618e75.png) no-repeat center bottom;
			width: 100%;
			font-size: 26px;
			line-height: 100px;
			position: relative;
			text-align: left;
		}
		.center-info {
			border: 0px solid #fcc285;
			padding: 20px;
			margin: 0 auto;
			color: rgb(110, 110, 110);
			display: flex;
			font-size: 14px;
			min-height: auto;
			line-height: 2;
			flex-wrap: wrap;
			border-radius: 0;
			box-shadow: none;
			flex-direction: column;
			overflow: hidden;
			background: url(http://codegen.caihongy.cn/20250220/ddbdd4cd89a24532b76245092d5461c5.png) no-repeat center /100% 100%;
			gap: 20px 30px;
			width: 100%;
			align-items: center;
			position: relative;
			height: 150px;
			order: 2;
			.center-info-title {
				color: #333;
				display: none;
				width: 100%;
				font-size: 18px;
				line-height: 40px;
				text-align: center;
				height: 40px;
			}
			.img-box {
				display: inline-block;
				width: auto;
				font-size: 0;
				border-color: #efefef;
				border-width: 0 0 0px 0;
				border-style: solid;
				height: auto;
				img {
					border-radius: 100%;
					margin: 0;
					object-fit: cover;
					display: block;
					width: 90px;
					height: 90px;
				}
			}
			.info-item1 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
			.info-item2 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
			.info-item3 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
			.info-item4 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
			.info-item5 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
			.info-item6 {
				border-radius: 30px;
				padding: 5px 0;
				background: rgb(255, 255, 255);
				display: flex;
				width: auto;
				border-color: #ddd;
				border-width: 0 0 0px 0;
				line-height: inherit;
				border-style: dashed;
				min-width: 25%;
				height: auto;
				.icon {
					padding: 0 5px;
					color: inherit;
					font-size: inherit;
				}
				.label {
					margin: 0 10px 0 0;
					color: inherit;
					font-weight: 500;
					font-size: inherit;
				}
				.text {
					color: inherit;
					flex: 1;
					font-size: inherit;
					text-align: left;
				}
			}
		}
		.center-tabs.el-tabs {
			border: 1px solid rgb(25, 190, 212);
			border-radius: 20px;
			padding: 0px;
			margin: 0px;
			background: #fff;
			display: flex;
			width: 100%;
			flex-wrap: wrap;
			order: 3;
			/deep/ .el-tabs__header {
				border-radius: 0px;
				padding: 20px;
				margin: 0 0 20px;
				background: rgb(25, 190, 212);
				display: flex;
				width: 100%;
				border-color: #39496950;
				border-width: 0px;
				position: relative;
				border-style: solid;
				text-align: center;
			}
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0px solid #000;
				padding: 0;
				margin: 0 10px;
				color: #fff;
				font-weight: 500;
				display: inline-block;
				font-size: inherit;
				line-height: 30px;
				border-radius: 0px;
				background: none;
				width: 100px;
				position: relative;
				text-align: center;
				height: 30px;
			}
			/deep/ .el-tabs__header .el-tabs__item:hover {
				background: none;
			}
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0px solid rgb(213, 103, 147);
				border-radius: 20px;
				margin: 0 10px;
				color: rgb(25, 190, 212);
				background: rgb(255, 255, 255);
				display: inline-block;
				width: 100px;
				line-height: 30px;
				height: 30px;
			}
			/deep/ .el-tabs__content {
				padding: 20px;
				background: none;
				flex: 1;
				display: flex;
				width: calc(100% - 200px);
				justify-content: space-between;
				flex-wrap: wrap;
			}
			/deep/ .el-tabs__content .el-tab-pane {
				background: none;
				width: 100%;
			}
			& /deep/ .el-tabs__header {
				.el-tabs__nav{
					overflow: auto;
				}
				::-webkit-scrollbar {
					-webkit-appearance: none;
					width: 6px;
					height: 6px;
				}
				::-webkit-scrollbar-track {
					background: rgba(0, 0, 0, 0.1);
					border-radius: 0;
				}
				::-webkit-scrollbar-thumb {
					cursor: pointer;
					border-radius: 5px;
					background: rgba(0, 0, 0, 0.15);
					transition: color 0.2s ease;
				}
				::-webkit-scrollbar-thumb:hover {
					background: rgba(0, 0, 0, 0.3);
				}
				.el-tabs__nav-wrap {
					margin: 0;
					&::after {
						content: none;
					}
				}
				.el-tabs__active-bar {
					display: none !important;
				}
			}
			.center-preview-pv {
				.center-item.el-form-item {
					border-radius: 0px;
					padding: 6px 0 0;
					margin: 0 0 20px 0;
					background: #fff;
					border-color: #475a8310;
					border-width:  0 0 0px;
					border-style: solid;
					/deep/ .el-form-item__label {
						padding: 0 10px 0 0;
						color: inherit;
						font-weight: 500;
						width: 180px;
						font-size: inherit;
						line-height: 40px;
						text-align: right;
					}
					.el-form-item__content {
						margin-left: 180px;
					}
					.el-input {
						width: 100%;
					}
					.el-input /deep/ .el-input__inner {
						border: 1px solid #ddd;
						border-radius: 4px;
						padding: 0 12px;
						box-shadow: none;
						color: inherit;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					.el-input /deep/ .el-input__inner[readonly="readonly"] {
						border: 0;
						cursor: not-allowed;
						border-radius: 0px;
						padding: 0 12px;
						box-shadow: none;
						color: inherit;
						background: none;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					.el-select {
						width: auto;
					}
					.el-select /deep/ .el-input__inner {
						border: 1px solid #ddd;
						border-radius: 4px;
						padding: 0 10px;
						box-shadow: none;
						color: inherit;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					.el-select /deep/ .is-disabled .el-input__inner {
						border: 0;
						cursor: not-allowed;
						border-radius: 0px;
						padding: 0 10px;
						box-shadow: none;
						color: inherit;
						background: none;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					.el-date-editor {
						width: 100%;
					}
					.el-date-editor /deep/ .el-input__inner {
						border: 1px solid #ddd;
						border-radius: 4px;
						padding: 0 10px 0 30px;
						box-shadow: none;
						color: inherit;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
						border: 0;
						cursor: not-allowed;
						border-radius: 0px;
						padding: 0 10px 0 30px;
						box-shadow: none;
						color: inherit;
						background: none;
						width: auto;
						font-size: 16px;
						height: 40px;
					}
					/deep/ .el-upload--picture-card {
						background: transparent;
						border: 0;
						border-radius: 0;
						width: auto;
						height: auto;
						line-height: initial;
						vertical-align: middle;
					}
					/deep/ .upload .upload-img {
						border: 1px solid #ddd;
						cursor: pointer;
						border-radius: 4px;
						color: #999;
						background: #fff;
						width: 80px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
					}
					/deep/ .el-upload-list .el-upload-list__item {
						border: 1px solid #ddd;
						cursor: pointer;
						border-radius: 4px;
						color: #999;
						background: #fff;
						width: 80px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
						font-size: 14px;
						line-height: 1.8;
					}
					/deep/ .el-upload .el-icon-plus {
						border: 1px solid #ddd;
						cursor: pointer;
						border-radius: 4px;
						color: #999;
						background: #fff;
						width: 80px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
					}
					/deep/ .el-upload__tip {
						color: #838fa1;
						font-size: 16px;
					}
					/deep/ .el-input__inner::placeholder {
						color: #999;
						font-size: inherit;
					}
				}
				.center-btn-item {
					padding: 0;
					margin: 30px 0 0;
					width: 100%;
					text-align: right;
					.updateBtn {
						border: 0;
						cursor: pointer;
						padding: 0 24px 0 30px;
						margin: 0 20px 0 0;
						display: inline-block;
						font-size: 16px;
						line-height: 44px;
						border-radius: 2px;
						background: rgb(25, 190, 212);
						width: auto;
						text-align: center;
						min-width: 120px;
						height: 44px;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
					.updateBtn:hover {
						.icon {
						}
						.text {
						}
					}
					.closeBtn {
						border: 0px solid #ddd;
						cursor: pointer;
						padding: 0 24px 0 30px;
						margin: 0 20px 0 0;
						color: rgb(110, 110, 110);
						display: inline-block;
						font-size: 16px;
						line-height: 44px;
						border-radius: 2px;
						background: rgb(232, 232, 232);
						width: auto;
						text-align: center;
						min-width: 120px;
						height: 44px;
						.icon {
							color: #fff;
						}
						.text {
							color: inherit;
						}
					}
					.closeBtn:hover {
						.icon {
						}
						.text {
						}
					}
				}
				.el-date-editor.el-input {
					width: auto;
				}
			}
		}
	}
</style>
