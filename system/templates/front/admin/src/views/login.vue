<template>
	<div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__backInDown">
				<div class="login_form2">
					<div class="title-container">汽车销量分析系统</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
				<div class="idea-box1"></div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						this.$nextTick(()=>{
							this.$http({
								url: this.tableName + '/session',
								method: "get"
							}).then(({
								data
							}) => {
								if (data && data.code === 0) {
									if(this.tableName == 'yonghu') {
										this.$storage.set('headportrait',data.data.touxiang)
									}
									if(this.tableName == 'users') {
										this.$storage.set('headportrait',data.data.image)
									}
									this.$storage.set('userForm',JSON.stringify(data.data))
									this.$storage.set('userid',data.data.id);
								} else {
									let message = this.$message
									message.error(data.msg);
								}
								if(this.boardAuth('hasBoard','查看',this.rulesForm.role)) {
									this.$router.replace({ path: "/board" });
								}else {
									this.$router.replace({ path: "/" });
								}
							});
						})
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240926/85224f2f6e894e38b53ef41b2f35df09.png);
	background-repeat: no-repeat;
	background-size: cover !important;
	background: url(http://codegen.caihongy.cn/20240926/85224f2f6e894e38b53ef41b2f35df09.png);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center center;

	.login_form {
		border-radius: 0;
		padding: 0px 600px  0px 0;
		box-shadow: inset 0px 0px 0px 0px #000;
		margin: 0;
		z-index: 1000;
		background: rgba(2, 124, 159,0.6);
		display: flex;
		width: 1200px;
		min-height: 704px;
		position: relative;
		height: auto;
		.login_form2 {
			padding: 56px 10px 20px 0;
			flex-direction: column;
			background: #fff;
			display: flex;
			width: 100%;
		}
		.title-container {
			padding: 0 40px;
			margin: 0 0 10px 0;
			color: #333333;
			top: 60px;
			left: 0;
			background: none;
			font-weight: 500;
			width: 100%;
			font-size: 24px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			margin: 15px 53px 15px 69px;
			background: none;
			display: flex;
			position: relative;
			align-items: center;
			height: 60px;
			.lable {
				color: #000;
				top: 33%;
				left: 15px;
				width: 120px;
				font-size: 16px;
				position: absolute!important;
				text-align: left;
				height: 60px;
			}
			input {
				border: 1px solid #333333;
				border-radius: 30px;
				padding: 0 72px;
				color: #333333;
				background: #F5F6F6;
				flex: 1;
				width: 100%;
				font-size: 16px;
				height: 60px;
			}
			input:focus {
				border: 1px solid #333333;
				border-radius: 30px;
				padding: 0 72px;
				color: #333333;
				background: #F5F6F6;
				flex: 1;
				width: 500px;
				font-size: 16px;
				height: 60px;
			}
			.password-box {
				margin: 0;
				display: flex;
				width: 100%;
				line-height: 60px;
				align-items: center;
				height: 60px;
				input {
					border: 1px solid #333333;
					border-radius: 30px;
					padding: 0 72px;
					color: #333333;
					background: #F5F6F6;
					flex: 1;
					width: 500px;
					font-size: 16px;
					height: 60px;
				}
				input:focus {
					border: 1px solid #333333;
					border-radius: 30px;
					padding: 0 72px;
					color: #333333;
					background: #F5F6F6;
					flex: 1;
					width: 500px;
					font-size: 16px;
					height: 60px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					position: absolute;
					right: 20px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
		}
		.list-type {
			border: 1px solid #333333;
			padding: 0 72px;
			margin: 15px 0;
			color: #333333;
			display: flex;
			font-size: 16px;
			min-height: 60px;
			line-height: 50px;
			flex-wrap: wrap;
			border-radius: 30px;
			background: #F5F6F6;
			flex: 1;
			width: 500px;
			align-items: center;
			/deep/ .el-radio__input .el-radio__inner {
				background: rgba(53, 53, 53, 0);
				border-color: #666;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: #017095;
				border-color: #017095;
			}
			/deep/ .el-radio__label {
				color: #666;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #017095;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 30px auto;
			display: flex;
			width: 468px;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				width: 100%;
				order: 2;
			}
			.login-btn2 {
				padding: 0;
				bottom: 28%;
				display: flex;
				width: 50%;
				justify-content: center;
				align-items: center;
				position: absolute;
				right: 0;
				flex-wrap: wrap;
			}
			.login-btn3 {
				margin: 0 0 20px 0;
				width: 100%;
				order: 1;
			}
			.loginInBt {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 30px;
				padding: 0 10px;
				margin: 0 0 10px;
				color: #fff;
				background: linear-gradient( 117deg, #017095 0%, #B2DEFF 100%);
				font-weight: 600;
				width: 100%;
				font-size: 28px;
				height: 60px;
			}
			.loginInBt:hover {
				opacity: 0.8;
			}
			.register {
				border: 2px solid #FFFFFF;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 10px;
				color:  #FFFFFF;
				background: none;
				width: auto;
				font-size: 16px;
				height: 34px;
			}
			.register:hover {
				opacity: 0.8;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 10px 10px 0;
				color: #000000;
				background: none;
				font-weight: 400;
				width: 100%;
				font-size: 16px;
				text-align: center;
				height: 34px;
			}
			.forget:hover {
				color: #017095;
				opacity: 1;
			}
		}
	}
	.idea-box1 {
		background-size: 150px 150px;
		bottom: 40%;
		font-weight: 600;
		font-size: 20px;
		right: 0;
		background-position: center center;
		border-radius: 10px;
		background-repeat: no-repeat;
		width: 50%;
		background-image: url(http://codegen.caihongy.cn/20241015/bb7a6681ff2b4606a7ada75b1ca06f3c.png);
		position: absolute;
		height: 150px;
		order: -2;
	}
}

</style>
