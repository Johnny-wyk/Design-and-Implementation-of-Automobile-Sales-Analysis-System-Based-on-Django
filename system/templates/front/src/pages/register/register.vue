<template>
	<div>

		<div class="container">
			<el-form class='rgs-form animate__animated animate__' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">汽车销量分析系统</p></div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuzhanghao">
						<div class="label" :class="changeRules('yonghuzhanghao')?'required':''">用户账号：</div>
						<el-input v-model="registerForm.yonghuzhanghao"  placeholder="请输入用户账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuxingming">
						<div class="label" :class="changeRules('yonghuxingming')?'required':''">用户姓名：</div>
						<el-input v-model="registerForm.yonghuxingming"  placeholder="请输入用户姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="lianxidianhua">
						<div class="label" :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
						<el-input v-model="registerForm.lianxidianhua"  placeholder="请输入联系电话" />
					</el-form-item>
					<el-form-item v-if="tableName=='yonghu'" class="el-email list-item">
						<div class="label required">邮箱：</div>
						<div style="display: flex;flex: 1;">
							<input v-model="registerForm.email" type="text" id="email" name="email" placeholder="请输入邮箱" autocomplete="off" class="emailInput">
							<button v-if="isEndFlag" @click="sendemailcode" id="sendemailcode" type="button" class="el-btn">发送验证码</button>
							<button v-if="!isEndFlag" disabled="disabled" type="button" class="el-btn">{{count}}秒后重发</button>
						</div>
					</el-form-item>
					<el-form-item v-if="tableName=='yonghu'" class="el-email list-item">
						<div class="label required">验证码：</div>
						<el-input v-model="emailcode" type="text" id="emailcode" name="emailcode" placeholder="请输入验证码" autocomplete="off" class="el-input" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
            emailcode:'',
			//倒计时60s
			count: 60,
			//倒计时定时器
			inter: null,
			//倒计结束标识
			isEndFlag: true,
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='yonghu'){
				this.registerForm = {
					yonghuzhanghao: '',
					mima: '',
					mima2: '',
					yonghuxingming: '',
					xingbie: '',
					touxiang: '',
					lianxidianhua: '',
					email: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }];
				this.requiredRules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }];
				this.requiredRules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',');
			if ('yonghu' == this.tableName) {
				this.rules.lianxidianhua = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('yonghu' == this.tableName) {
				this.rules.email = [{ required: true, validator: this.$validate.isEmail, trigger: 'blur' }];
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随
		yonghutouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},

		// 多级联动参数

		sendemailcode() {
			if(!this.registerForm.email){
				this.$message.error(`邮箱不能为空`);
				return
			}
			let emailF = this.$validate.isEmail2(this.registerForm.email);
			if(this.registerForm.email&&(!this.$validate.isEmail2(this.registerForm.email))){
				this.$message.error(`请输入正确的邮箱格式`);
				return
			}
			this.isEndFlag = false;
			var _this = this;
			this.inter = window.setInterval(function() {
				_this.count = _this.count - 1;
				if (_this.count <= 0) {
					window.clearInterval(_this.inter);
					_this.isEndFlag = true;
					_this.count=60;
				}
			}, 1000);
			this.$http({
				url: `${this.tableName}/sendemail?email=`+this.registerForm.email,
				method: "get",
				params: {}
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message.success(`发送成功`);
				} else {
					this.$message.error(`服务器异常，请稍后重试`)
				}
			});
		},

		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`yonghu` == this.tableName ){
						url=this.tableName+"/register?emailcode="+this.emailcode;
						if(this.registerForm.email&&(!this.$validate.isEmail2(this.registerForm.email))){
							this.$message.error(`请输入正确的邮箱格式`);
							return
						}
					}
					if((!this.emailcode) && `yonghu` == this.tableName){
						this.$message.error(`验证码不能为空`);
						return
					}
					if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
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
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		background-repeat: no-repeat;
		background-size: 100% 100% !important;
		background: url(http://codegen.caihongy.cn/20250215/ae8441db2b1d499ab4230a9b924ed954.webp);
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-end;
		align-items: center;
		background-position: center center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250215/ae8441db2b1d499ab4230a9b924ed954.webp);
		.rgs-form {
			border: 0px solid rgb(0, 0, 0);
			border-radius: 10px;
			padding: 0px 0 0 0;
			margin: 20px 10% 20px 0%;
			background: #fff;
			width: 600px;
			.rgs-form2 {
				width: 100%;
				.title {
					margin: 0 0 30px 0;
					color: rgb(25, 190, 212);
					background: none;
					font-weight: 600;
					width: 100%;
					font-size: 30px;
					line-height: 100px;
					text-align: center;
				}
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					border-radius: 0px;
					padding: 5px;
					box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
					margin: 0 auto 20px;
					background: #fff;
					border-image: linear-gradient(90deg, rgba(25, 190, 212, 0.06) 10%, rgb(165, 241, 224), rgba(25, 190, 212, 0.06) 90%) 1;
					width: 80%;
					border-width: 0 0 2px 0;
					border-style: solid;
					/deep/.el-form-item__content {
						padding: 0 0 0 130px;
						display: block;
						width: calc(100% - 0px);
						.label {
							padding: 0 5px 0 0;
							z-index: 9;
							color: #000;
							left: 0;
							background: #fff;
							width: 120px;
							font-size: 16px;
							line-height: 40px;
							position: absolute !important;
							text-align: center;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							margin: 0 10px 0 0;
							color: red;
							left: 110px;
							position: inherit;
							content: "*";
						}
						.el-input {
							flex: 1;
							width: 100%;
						}
						.el-input .el-input__inner {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px;
							color: #666;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input .el-input__inner:focus {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px;
							outline: none;
							color: #666;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input-number {
							flex: 1;
							width: 100%;
						}
						.el-input-number .el-input__inner {
							text-align: left;
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px;
							color: #666;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input-number .el-input-number__decrease {
							display: none;
						}
						.el-input-number .el-input-number__increase {
							display: none;
						}
						.el-select {
							flex: 1;
							width: calc(100% - 0px);
						}
						.el-select .el-input__inner {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-select .el-input__inner:focus {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px;
							outline: none;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-date-editor {
							flex: 1;
							width: calc(100% - 0px);
						}
						.el-date-editor .el-input__inner {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px 0 30px;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-date-editor .el-input__inner:focus {
							border: 0px solid #b0b0b0;
							border-radius: 8px;
							padding: 0 10px 0 30px;
							outline: none;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0px;
							margin: 5px 0 0;
							color: #b0b0b0;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 50px;
							text-align: center;
							height: 50px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0px;
							margin: 5px 0 0;
							color: #b0b0b0;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 50px;
							text-align: center;
							height: 50px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0px;
							margin: 5px 0 0;
							color: #b0b0b0;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 50px;
							text-align: center;
							height: 50px;
						}
						.el-upload__tip {
							color: #666;
							font-size: 15px;
						}
						.emailInput {
							border: 0px solid #b0b0b0;
							border-radius: 0px 0 0 0px;
							padding: 0 10px;
							margin: 0;
							color: #606266;
							background: #fff;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.emailInput:focus {
							border: 0px solid #b0b0b0;
							border-radius: 0px 0 0 0px;
							padding: 0 10px;
							outline: none;
							color: #606266;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-btn {
							border: 0px solid #b0b0b0;
							cursor: pointer;
							border-radius: 0;
							padding: 0 10px;
							margin: 0;
							color: #fff;
							background: rgb(25, 190, 212);
							width: 110px;
							font-size: 15px;
							border-width: 0px 0px 0px 0;
							float: right;
							height: 40px;
						}
						.el-btn:hover {
						}
						
						.el-input__inner::placeholder {
							color: #999;
							font-size: 15px;
						}
						input::placeholder {
							color: #999;
							font-size: 15px;
						}
						.editor {
							border-radius: 8px;
							margin: 0 0 0 0px;
							background: #fff;
							width: calc(100% - 0px);
							height: auto;
						}
					}
				}
				.register-btn {
					margin: 20px auto;
					display: flex;
					width: 80%;
					flex-wrap: wrap;
				}
				.register-btn1 {
					padding: 0 0 0 0px;
					width: 100%;
				}
				.register-btn2 {
					padding: 0 0 0 0px;
					margin: 0 auto 10px;
					width: 100%;
					text-align: center;
					order: -1;
				}
				.register_btn {
					border: 0;
					cursor: pointer;
					border-radius: 0px;
					padding: 0 30px;
					margin: 0 0 20px;
					color: #fff;
					background: rgb(25, 190, 212);
					letter-spacing: 4px;
					width: 100%;
					font-size: 20px;
					height: 48px;
				}
				.register_btn:hover {
				}
				.has_btn {
					cursor: pointer;
					padding: 0;
					color: #333;
					display: inline-block;
					text-decoration: none;
					font-size: 15px;
					line-height: 40px;
				}
				.has_btn:hover {
					opacity: 0.8;
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
	
	::-webkit-scrollbar {
		display: none;
	}
</style>
