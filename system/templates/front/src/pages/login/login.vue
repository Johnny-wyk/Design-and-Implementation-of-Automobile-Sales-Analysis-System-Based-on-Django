<template>
	<div>
		<div class="login-container">
			<el-form ref="loginForm" :model="loginForm" :rules="rules" class="login_form animate__animated animate__slideInRight">
				<div class="login_form2">
					<div class="login-title">汽车销量分析系统</div>
					<div v-if="loginType==1" class="list-item" prop="username">
						<div class="lable">
							账号
						</div>
						<input v-model="loginForm.username" placeholder="请输入账号">
					</div>
					<div v-if="loginType==1" class="list-item" prop="password">
						<div class="lable">
							密码
						</div>
						<div class="password-box">
							<input v-model="loginForm.password" placeholder="请输入密码" :type="showPassword?'text':'password'">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item select" v-if="roles.length>1">
						<div class="lable">
							角色
						</div>
						<el-select v-model="loginForm.tableName" placeholder="请选择角色" @change="selectChange">
							<el-option v-for="item,index in roles" :key="index" :label="item.roleName" :value="item.tableName" />
						</el-select>
					</div>

			
					<div class="list-btn">
						<el-button class="login_btn" v-if="loginType==1" @click="submitForm('loginForm')">登录</el-button>

						<div class="list-btn2">
							<router-link class="register_btn" :to="{path: '/register', query: {role: item.tableName,pageFlag:'register'}}" v-if="item.hasFrontRegister=='是'" v-for="(item, index) in roles" :key="index">注册{{item.roleName.replace('注册','')}}</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css';
import menu from '@/config/menu'
export default {
	//数据集合
	data() {
		return {
            baseUrl: this.$config.baseUrl,
            loginType: 1,
			roleMenus: [],
			loginForm: {
				username: '',
				password: '',
				tableName: '',
			},
			role: '',
            roles: [],
			rules: {
				username: [
					{ required: true, message: '请输入账号', trigger: 'blur' }
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' }
				]
			},
			codes: [{
				num: 1,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 2,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 3,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 4,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}],
			flag: false,
			verifyCheck2: false,
			showPassword: false,
		}
	},
	components: {
	},
	created() {
		this.roleMenus = menu.list()
		for(let item in this.roleMenus) {
			if(this.roleMenus[item].hasFrontLogin=='是') {
				this.roles.push(this.roleMenus[item]);
			}
		}
		
	},
	mounted() {
	},
	//方法集合
	methods: {
		randomString() {
			var len = 4;
			var chars = [
				'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
				'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
				'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
				'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
				'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
				'3', '4', '5', '6', '7', '8', '9'
			]
			var colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			var sizes = ['14', '15', '16', '17', '18']
			
			var output = []
			for (var i = 0; i < len; i++) {
				// 随机验证码
				var key = Math.floor(Math.random() * chars.length)
				this.codes[i].num = chars[key]
				// 随机验证码颜色
				var code = '#'
				for (var j = 0; j < 6; j++) {
					var key = Math.floor(Math.random() * colors.length)
					code += colors[key]
				}
				this.codes[i].color = code
				// 随机验证码方向
				var rotate = Math.floor(Math.random() * 45)
				var plus = Math.floor(Math.random() * 2)
				if (plus == 1) rotate = '-' + rotate
				this.codes[i].rotate = 'rotate(' + rotate + 'deg)'
				// 随机验证码字体大小
				var size = Math.floor(Math.random() * sizes.length)
				this.codes[i].size = sizes[size] + 'px'
			}
		},
		selectChange(e){
			for(let x in this.roles){
				if(this.roles[x].tableName == e){
					this.role = this.roles[x].roleName
				}
			}
		},
		submitForm(formName) {
			if (this.roles.length!=1) {
				if (!this.role) {
					this.$message.error("请选择登录用户类型");
					return false;
				}
			} else {
				this.role = this.roles[0].roleName;
				this.loginForm.tableName = this.roles[0].tableName;
			}
			if (!this.loginForm.username) {
				this.$message.error("请输入用户名");
				return;
			}
			if (!this.loginForm.password) {
				this.$message.error("请输入密码");
				return;
			}

			this.loginPost(formName)
		},
		loginPost(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.$http.get(`${this.loginForm.tableName}/login`, {params: this.loginForm}).then(res => {
						if (res.data.code === 0) {
							localStorage.setItem('frontToken', res.data.token);
							localStorage.setItem('UserTableName', this.loginForm.tableName);
							localStorage.setItem('username', this.loginForm.username);
							localStorage.setItem('frontSessionTable', this.loginForm.tableName);
							localStorage.setItem('frontRole', this.role);
							localStorage.setItem('keyPath', 0);
							this.$router.push('/');
							this.$message({
								message: '登录成功',
								type: 'success',
								duration: 1500,
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.login-container {
		background-repeat: no-repeat;
		background-size: 100% 100% !important;
		background: url(http://codegen.caihongy.cn/20250213/5474aa6529114740b081a365b2d7e200.webp);
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-end;
		align-items: center;
		background-position: center center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250213/5474aa6529114740b081a365b2d7e200.webp);
		.login_form {
			border: 0px solid rgb(0, 0, 0);
			border-radius: 10px;
			padding: 0px 0 50px;
			margin: 0 10% 0 0%;
			background: #fff;
			width: 570px;
			min-height: 700px;
			.login_form2 {
				display: flex;
				width: 100%;
				flex-wrap: wrap;
				.login-title {
					margin: 0 0 30px 0;
					color: rgb(25, 190, 212);
					background: none;
					font-weight: 600;
					width: 100%;
					font-size: 30px;
					line-height: 100px;
					text-align: center;
				}
				.list-item {
					border: 0px solid rgb(0, 0, 0);
					border-radius: 0px;
					padding: 5px 5px 5px;
					box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
					margin: 0 auto 30px;
					background: #fff;
					border-image: linear-gradient(90deg, rgba(25, 190, 212, 0.06) 10%, rgb(165, 241, 224), rgba(25, 190, 212, 0.06) 90%) 1;
					display: flex;
					width: 80%;
					border-width: 0 0 2px 0;
					align-items: center;
					.lable {
						border-radius: 0;
						padding: 0 10px;
						color: #000;
						background: none;
						width: auto;
						font-size: 16px;
						line-height: 40px;
						text-align: center;
						min-width: 90px;
					}
					input {
						border: 0px solid #ebd8ba;
						border-radius: 8px;
						padding: 0 10px;
						color: #666;
						flex: 1;
						background: #fff;
						width: calc(100% - 0px);
						font-size: 15px;
						height: 40px;
					}
					input:focus {
						border: 0px solid #96a7c9;
						border-radius: 8px;
						padding: 0 10px;
						outline: none;
						color: #666;
						flex: 1;
						background: #f5f5f5;
						width: calc(100% - 0px);
						font-size: 15px;
						height: 40px;
					}
					.password-box {
						flex: 1;
						display: flex;
						width: calc(100% - 0px);
						position: relative;
						align-items: center;
						input {
							border: 0px solid #ebd8ba;
							border-radius: 8px;
							padding: 0 10px;
							color: #666;
							background: #fff;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						input:focus {
							border: 0px solid #96a7c9;
							border-radius: 8px;
							padding: 0 10px;
							color: #666;
							background: #f5f5f5;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						.iconfont {
							cursor: pointer;
							z-index: 1;
							color: #000;
							top: 0;
							font-size: 16px;
							line-height: 44px;
							position: absolute;
							right: 16px;
						}
					}
					input::placeholder {
						color: #666;
						font-size: 15px;
					}
				}
				.select {
					border: 0px solid rgb(0, 0, 0);
					border-radius: 0px;
					padding: 5px 5px 5px;
					box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
					margin: 0 auto 30px;
					background: #fff;
					border-image: linear-gradient(90deg, rgba(25, 190, 212, 0.06) 10%, rgb(165, 241, 224), rgba(25, 190, 212, 0.06) 90%) 1;
					display: flex;
					width: 80%;
					border-width: 0 0 2px 0;
					align-items: center;
					// select
					/deep/ .el-select {
						border: none;
						box-shadow: none;
						width: 100%;
					}
					/deep/ .el-select .el-input__inner {
						border: 0px solid rgba(64, 158, 255, 1);
						padding: 0 10px;
						box-shadow: none;
						color: #000;
						width: 288px;
						font-size: 14px;
						height: 44px;
					}
					/deep/ .el-select .is-focus .el-input__inner {
						border: 0px solid rgba(85, 170, 0, 1.0);
						padding: 0 10px;
						box-shadow: none;
						outline: 0px solid #efefef;
						color: #000;
						width: 288px;
						font-size: 14px;
						outline-offset: 4px;
						height: 44px;
					}
					/deep/ .el-select .el-input__inner::placeholder{
						color: #666;
						font-size: 15px;
					}
				}
				.list-btn {
					padding: 0;
					margin: 0 auto 40px;
					display: flex;
					width: 80%;
					flex-wrap: wrap;
					.login_btn {
						border: 0;
						cursor: pointer;
						border-radius: 0px;
						padding: 0 30px;
						margin: 0 0px;
						color: #fff;
						background: rgb(25, 190, 212);
						letter-spacing: 4px;
						width: 100%;
						font-size: 20px;
						height: 48px;
						order: 3;
					}
					.login_btn:hover {
					}
					.list-btn2 {
						margin: 0px auto 0;
						flex-direction: column;
						display: flex;
						width: 100%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						order: 2;
						.register_btn {
							cursor: pointer;
							padding: 5px;
							margin: 0 0 10px 0px;
							color: rgb(175, 175, 175);
							background: none;
							text-decoration: none;
							font-size: 16px;
							float: right;
						}
						.register_btn:hover {
							opacity: 0.8;
						}
						.resetpwd_btn {
							cursor: pointer;
							padding: 5px;
							margin: 0 0px 10px 0;
							color: rgb(175, 175, 175);
							background: none;
							text-decoration: none;
							font-size: 16px;
							float: left;
						}
						.resetpwd_btn:hover {
							opacity: 0.8;
						}
					}
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
</style>
