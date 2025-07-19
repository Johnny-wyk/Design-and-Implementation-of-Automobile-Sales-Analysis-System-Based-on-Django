<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="input" v-if="type!='info'"  label="厂商" prop="changshang" >
					<el-input v-model="ruleForm.changshang" placeholder="厂商" clearable  :readonly="ro.changshang"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="厂商" prop="changshang" >
					<el-input v-model="ruleForm.changshang" placeholder="厂商" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="车型" prop="chexing" >
					<el-input v-model="ruleForm.chexing" placeholder="车型" clearable  :readonly="ro.chexing"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="车型" prop="chexing" >
					<el-input v-model="ruleForm.chexing" placeholder="车型" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="最低售价（万元）" prop="minprice" >
					<el-input-number v-model="ruleForm.minprice" placeholder="最低售价（万元）" :disabled="ro.minprice"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="最低售价（万元）" prop="minprice" >
					<el-input v-model="ruleForm.minprice" placeholder="最低售价（万元）" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="最高售价（万元）" prop="maxprice" >
					<el-input-number v-model="ruleForm.maxprice" placeholder="最高售价（万元）" :disabled="ro.maxprice"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="最高售价（万元）" prop="maxprice" >
					<el-input v-model="ruleForm.maxprice" placeholder="最高售价（万元）" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="时间" prop="tjtime" >
					<el-input v-model="ruleForm.tjtime" placeholder="时间" clearable  :readonly="ro.tjtime"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="时间" prop="tjtime" >
					<el-input v-model="ruleForm.tjtime" placeholder="时间" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="月销量(辆)" prop="mxiaoliang" >
					<el-input v-model.number="ruleForm.mxiaoliang" placeholder="月销量(辆)" clearable  :readonly="ro.mxiaoliang"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="月销量(辆)" prop="mxiaoliang" >
					<el-input v-model="ruleForm.mxiaoliang" placeholder="月销量(辆)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="当月销量排名" prop="dyxlpm" >
					<el-input v-model.number="ruleForm.dyxlpm" placeholder="当月销量排名" clearable  :readonly="ro.dyxlpm"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="当月销量排名" prop="dyxlpm" >
					<el-input v-model="ruleForm.dyxlpm" placeholder="当月销量排名" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="占厂商份额（%）" prop="zcsfe" >
					<el-input-number v-model="ruleForm.zcsfe" placeholder="占厂商份额（%）" :disabled="ro.zcsfe"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="占厂商份额（%）" prop="zcsfe" >
					<el-input v-model="ruleForm.zcsfe" placeholder="占厂商份额（%）" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="在厂商排名" prop="zcspm" >
					<el-input v-model.number="ruleForm.zcspm" placeholder="在厂商排名" clearable  :readonly="ro.zcspm"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="在厂商排名" prop="zcspm" >
					<el-input v-model="ruleForm.zcspm" placeholder="在厂商排名" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="在微型车排名" prop="zwxcpm" >
					<el-input v-model.number="ruleForm.zwxcpm" placeholder="在微型车排名" clearable  :readonly="ro.zwxcpm"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="在微型车排名" prop="zwxcpm" >
					<el-input v-model="ruleForm.zwxcpm" placeholder="在微型车排名" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isNumber,
		isIntNumer,
	} from "@/utils/validate";
	export default {
		data() {
			var validateNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isNumber(value)) {
					callback(new Error("请输入数字"));
				} else {
					callback();
				}
			};
			var validateIntNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isIntNumer(value)) {
					callback(new Error("请输入整数"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
				ro:{
					changshang : false,
					chexing : false,
					minprice : false,
					maxprice : false,
					tjtime : false,
					mxiaoliang : false,
					dyxlpm : false,
					zcsfe : false,
					zcspm : false,
					zwxcpm : false,
					clicktime : false,
					clicknum : false,
					discussnum : false,
					totalscore : false,
					storeupnum : false,
				},
			
				ruleForm: {
					changshang: '',
					chexing: '',
					minprice: '',
					maxprice: '',
					tjtime: '',
					mxiaoliang: '',
					dyxlpm: '',
					zcsfe: '',
					zcspm: '',
					zwxcpm: '',
					clicktime: '',
				},

				rules: {
					changshang: [
					],
					chexing: [
					],
					minprice: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					maxprice: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					tjtime: [
					],
					mxiaoliang: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					dyxlpm: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					zcsfe: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					zcspm: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					zwxcpm: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					clicktime: [
					],
					clicknum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					discussnum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					totalscore: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					storeupnum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
					for (var o in obj){
						if(o=='changshang'){
							this.ruleForm.changshang = obj[o];
							this.ro.changshang = true;
							continue;
						}
						if(o=='chexing'){
							this.ruleForm.chexing = obj[o];
							this.ro.chexing = true;
							continue;
						}
						if(o=='minprice'){
							this.ruleForm.minprice = obj[o];
							this.ro.minprice = true;
							continue;
						}
						if(o=='maxprice'){
							this.ruleForm.maxprice = obj[o];
							this.ro.maxprice = true;
							continue;
						}
						if(o=='tjtime'){
							this.ruleForm.tjtime = obj[o];
							this.ro.tjtime = true;
							continue;
						}
						if(o=='mxiaoliang'){
							this.ruleForm.mxiaoliang = obj[o];
							this.ro.mxiaoliang = true;
							continue;
						}
						if(o=='dyxlpm'){
							this.ruleForm.dyxlpm = obj[o];
							this.ro.dyxlpm = true;
							continue;
						}
						if(o=='zcsfe'){
							this.ruleForm.zcsfe = obj[o];
							this.ro.zcsfe = true;
							continue;
						}
						if(o=='zcspm'){
							this.ruleForm.zcspm = obj[o];
							this.ro.zcspm = true;
							continue;
						}
						if(o=='zwxcpm'){
							this.ruleForm.zwxcpm = obj[o];
							this.ro.zwxcpm = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='clicknum'){
							this.ruleForm.clicknum = obj[o];
							this.ro.clicknum = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='totalscore'){
							this.ruleForm.totalscore = obj[o];
							this.ro.totalscore = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
					}
				}
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `xiaoshouinfo/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					var objcross = this.$storage.getObj('crossObj');
					if(!this.ruleForm.id) {
						delete this.ruleForm.userid
					}
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `xiaoshouinfo/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.xiaoshouinfoCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});
						}
					});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.xiaoshouinfoCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 30px 20px 20px 20px;
	}
	.add-update-preview {
		border: 1px solid #BFBFBF;
		padding: 40px 30% 20px 10%;
		background: #FFFFFF;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 26px 0;
		display: inline-block;
		width: 100%;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #666;
		font-weight: 600;
		width: 180px;
		font-size: 16px;
		line-height: 40px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	.add-update-preview .el-form-item span.text {
		border: 0px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: 360px;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 16px;
		min-width: 360px;
		height: 40px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 16px;
		min-width: 360px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 30px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px dashed #bfbfbf;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 30px;
		color: #666;
		background: none;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .viewBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 30px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 1px dashed #bfbfbf;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 1px dashed #bfbfbf;
		border-radius: 0px;
		padding: 12px;
		color: #666;
		background: #fff;
		width: 100%;
		font-size: 14px;
		min-width: 400px;
		height: 120px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 1px dashed #bfbfbf;
				border-radius: 0px;
				padding: 12px;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 14px;
				min-width: 400px;
				height: 120px;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 20px 0 0;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: linear-gradient( 135deg, #097499 0%, #A5DDFD 100%);
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
