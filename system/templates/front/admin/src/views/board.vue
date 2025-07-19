<template>
	<div class="content" :style='{"alignContent":"flex-start","padding":"0","overflow":"hidden","background":"url(http://codegen.caihongy.cn/20250108/e3a25122fa624c92bc45d9974166879d.png) no-repeat bottom center / 50% 300px,rgb(17,17,17)","flexDirection":"column","display":"flex","width":"100%","position":"relative","height":"100%"}'>
		<div id="particles"></div>
		<div :style='{"padding":"24px 0 0","margin":"0 0 20px 0","background":"url(http://codegen.caihongy.cn/20250108/556520e2bc654d7881d32fcb136f82dc.png) top center","display":"flex","width":"100%","position":"relative","justifyContent":"center","height":"130px","zIndex":"9"}'>
			<!-- 标题 -->
			<div :style='{"margin":"0","color":"transparent","textAlign":"center","background":"linear-gradient(to bottom, rgba(253, 254, 255, 1), rgba(255, 211, 129, 1)) padding-box text","fontSize":"24px","-webkit-text-fill-color":"transparent","fontWeight":"700"}'>欢迎使用 {{this.$project.projectName}}</div>
			<!-- 时间 -->
			<div :style='{"top":"70px","color":"rgb(255, 227, 168)","display":"inline-block","lineHeight":"44px","fontSize":"16px","position":"absolute","right":"10%","height":"44px"}'>{{ dates }} <span @click="backClick" style="cursor:pointer;padding: 0 0 0 8px;">管理界面</span></div>
		</div>
		<div :style='{"padding":"0 10px","flex":"auto","background":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"0","zIndex":"9"}'>
			<div :style='{"width":"25%","padding":"5% 5% 5% 20px","flexDirection":"column","background":"url(http://codegen.caihongy.cn/20250108/8f4c3d62a57542989e456cc9919afbf0.png) no-repeat center / 100% 100%","display":"flex","gap":"10px"}'>
				<div class="echarts1">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							车型统计
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","height":"0"}'>
						<div id="xiaoshouinfoChart1" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts2">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							最低售价统计
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","height":"0"}'>
						<div id="xiaoshouinfoChart2" style="width:100%;height:100%;"></div>
					</div>
				</div>
			</div>
			<div :style='{"padding":"0 10px","margin":"0","flexWrap":"wrap","flexDirection":"row","flex":"auto","background":"none","display":"flex","width":"0"}'>
				<!-- 统计 -->
				<div :style='{"padding":"0 0 10px 0","margin":"0","color":"#fff","alignItems":"center","background":"none","display":"flex","gap":"10px","width":"100%","fontSize":"14px","justifyContent":"space-evenly","height":"84px"}'>

					<div :style='{"margin":"0","alignItems":"flex-end","background":"url(http://codegen.caihongy.cn/20250107/13d8ebc9ea4b45d9b66b2632facbaa6e.png) no-repeat center / 100% 100%","flexDirection":"column","flex":"0 1 auto","display":"flex","width":"175px","position":"relative","justifyContent":"flex-end","height":"100%","maxWidth":"175px"}'>
						<div :style='{"width":"12px","margin":"0","background":"#2097db","display":"none","height":"12px"}'></div>
						<div :style='{"padding":"0 10px 0 0","alignItems":"flex-end","flexDirection":"column","display":"flex","width":"100%","justifyContent":"center","height":"100%"}'>
							<div :style='{"lineHeight":"24px","fontSize":"12px","position":"relative","color":"inherit","height":"24px"}'>销售信息总数</div>
							<div :style='{"lineHeight":"24px","fontSize":"16px","color":"rgba(255, 120, 0, 1)","fontWeight":"bold","height":"24px","order":"20"}'>{{xiaoshouinfoCount}}</div>
						</div>
					</div>
				</div>
				<div class="echarts5">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							当月销量排名
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","height":"0"}'>
						<div id="xiaoshouinfoChart5" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts6">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							销售信息
							(月销量(辆)TOP10)
						</div>
					</div>
					<el-table id="xiaoshouinfoTable" :data="xiaoshouinfoList" border :stripe="true" :style='{"padding":"0","borderColor":"rgba(92,135,230,.3)","borderWidth":"0","background":"none","width":"100%","overflow-y":"scroll","borderStyle":"solid","height":"calc(100% - 36px)"}'>
						<el-table-column :resizable="true" :sortable="false" prop="changshang" label="厂商">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="chexing" label="车型">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="minprice" label="最低售价（万元）">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="maxprice" label="最高售价（万元）">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="tjtime" label="时间">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="mxiaoliang" label="月销量(辆)">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="dyxlpm" label="当月销量排名">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="zcsfe" label="占厂商份额（%）">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="zcspm" label="在厂商排名">
						</el-table-column>
						<el-table-column :resizable="true" :sortable="false" prop="zwxcpm" label="在微型车排名">
						</el-table-column>
					</el-table>
				</div>
				<div class="forecast-box" :style='{"border":"0px solid #4198ce50","padding":"0 15px","margin":"0","alignItems":"flex-start","display":"flex","transition":"0.3s","alignContent":"flex-start","flexWrap":"wrap","background":"none","flex":"0 0 auto","gap":"12px","width":"30%","height":"calc(50% - 42px)","order":"10","zIndex":"9"}'>
					<div :style='{"border":"1px solid #675e3d","padding":"0 10px","margin":"0 0 10px 0","alignItems":"center","display":"flex","width":"100%","order":"2"}'>
						<div :style='{"width":"auto","color":"#999","textAlign":"left","order":"1"}'>
							厂商
						</div>
						<input :style='{"border":"none","padding":"0 10px","margin":"0","color":"#FF7800","background":"none","flex":"auto","width":"0","lineHeight":"30px","height":"30px"}' v-model="forecastForm.changshang" placeholder="请输入厂商"></input>
					</div>
					<div :style='{"border":"1px solid #675e3d","padding":"0 10px","margin":"0 0 10px 0","alignItems":"center","display":"flex","width":"100%","order":"2"}'>
						<div :style='{"width":"auto","color":"#999","textAlign":"left","order":"1"}'>
							车型
						</div>
						<input :style='{"border":"none","padding":"0 10px","margin":"0","color":"#FF7800","background":"none","flex":"auto","width":"0","lineHeight":"30px","height":"30px"}' v-model="forecastForm.chexing" placeholder="请输入车型"></input>
					</div>
					<div :style='{"border":"1px solid #675e3d","padding":"0 10px","margin":"0 0 10px 0","alignItems":"center","display":"flex","width":"100%","order":"2"}'>
						<div :style='{"width":"auto","color":"#999","textAlign":"left","order":"1"}'>
							最低售价（万元
						</div>
						<input :style='{"border":"none","padding":"0 10px","margin":"0","color":"#FF7800","background":"none","flex":"auto","width":"0","lineHeight":"30px","height":"30px"}' v-model="forecastForm.minprice" placeholder="请输入最低售价（万元"></input>
					</div>
					<div :style='{"border":"1px solid #675e3d","padding":"0 10px","margin":"0 0 10px 0","alignItems":"center","display":"flex","width":"100%","order":"2"}'>
						<div :style='{"width":"auto","color":"#999","textAlign":"left","order":"1"}'>
							最高售价（万元
						</div>
						<input :style='{"border":"none","padding":"0 10px","margin":"0","color":"#FF7800","background":"none","flex":"auto","width":"0","lineHeight":"30px","height":"30px"}' v-model="forecastForm.maxprice" placeholder="请输入最高售价（万元"></input>
					</div>
					<div :style='{"width":"100%","fontSize":"16px","lineHeight":"24px","color":"#FF7800","textAlign":"left"}'>
						预测月销量(辆)：{{form.mxiaoliang}}
					</div>
					<div @click="forecastClick" :style='{"border":"1px solid #FF7800","cursor":"pointer","margin":"0 auto","color":"#FF7800","borderRadius":"5px","textAlign":"center","background":"none","width":"100%","lineHeight":"34px","height":"34px","order":"2"}'>
						立即预测
					</div>
				</div>
			</div>
			<div :style='{"padding":"5% 20px 5% 5%","flexWrap":"wrap","flexDirection":"column","background":"url(http://codegen.caihongy.cn/20250108/6420b64185d6417790344ce66606fcd4.png) no-repeat right center / 100% 100%","display":"flex","gap":"10px","width":"25%"}'>
				<div class="echarts3">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							最高售价统计
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","height":"0"}'>
						<div id="xiaoshouinfoChart3" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts4">
					<div :style='{"padding":"0 0 0 30px","margin":"0","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250108/3d20617b738d4f528ffe9924e6e63ad0.png) no-repeat bottom center / 100% auto","flex":"none","width":"100%","height":"auto"}'>
						<div :style='{"padding":"0","fontSize":"18px","lineHeight":"40px","color":"#FF7800","background":"none","fontWeight":"600"}'>
							月销量统计
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","height":"0"}'>
						<div id="xiaoshouinfoChart4" style="width:100%;height:100%;"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import * as echarts from 'echarts'
	import chinaJson from "@/components/echarts/china.json";
	require('@/utils/particles.js')
	import {
		Loading
	} from 'element-ui';
	import router from '@/router/router-static'
	export default {
		data() {
			return {
				line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"symbol":"circle","animationEasing":"circularInOut","showSymbol":true,"symbolSize":5,"itemStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgb(219,109,4)"},{"offset":1,"color":"rgb(217,193,111)"}],"type":"linear"},"borderColor":"rgba(219,109,4,0.3)","borderWidth":8},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line2: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"symbol":"circle","animationEasing":"circularInOut","showSymbol":true,"symbolSize":5,"itemStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgb(219,109,4)"},{"offset":1,"color":"rgb(217,193,111)"}],"type":"linear"},"borderColor":"rgba(219,109,4,0.3)","borderWidth":8},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line3: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"symbol":"circle","animationEasing":"circularInOut","areaStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(219,109,4,0.3)"},{"offset":1,"color":"rgba(217,193,111,0.3)"}],"type":"linear"}},"showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(219,109,4,0.3)","borderWidth":8},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line4: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"symbol":"circle","animationEasing":"circularInOut","areaStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(219,109,4,0.3)"},{"offset":1,"color":"rgba(217,193,111,0.3)"}],"type":"linear"}},"showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(219,109,4,0.3)","borderWidth":8},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line5: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":14,"show":true,"icon":"roundRect","type":"scroll","top":"top","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":20,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":10,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"grid":{"right":"20","top":"30","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"symbol":"circle","animationEasing":"circularInOut","showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(219,109,4,0.3)","borderWidth":8},"animation":true},"series2":{"barWidth":"auto","animationDuration":5000,"colorBy":"series","animationEasing":"circularInOut","barMaxWidth":"10px","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","borderRadius":[20,20,0,0],"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"barCategoryGap":"20%","animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"bottom","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"center","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"itemStyle":{"borderType":"solid","shadowOffsetX":5,"borderColor":"inherit","shadowOffsetY":5,"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(219,109,4,1)"},{"offset":1,"color":"rgba(217,193,111,1)"}],"type":"linear"},"borderRadius":[20,20,0,0],"shadowBlur":10,"borderWidth":0,"opacity":1,"shadowColor":"rgba(0, 0, 0, 0.4)"},"colorBy":"series","animationEasing":"circularInOut","barMaxWidth":"10px","animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false},"base":{"animate":true,"interval":6000}},
				bar2: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"bottom","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"center","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":5000,"itemStyle":{"borderType":"solid","shadowOffsetX":5,"borderColor":"inherit","shadowOffsetY":5,"color":{"x":0,"y":0,"y2":0,"x2":1,"colorStops":[{"offset":0,"color":"rgba(219,109,4,1)"},{"offset":1,"color":"rgba(217,193,111,1)"}],"type":"linear"},"borderRadius":[0,20,20,0],"shadowBlur":10,"borderWidth":0,"opacity":1,"shadowColor":"rgba(0, 0, 0, 0.4)"},"colorBy":"series","animationEasing":"circularInOut","barMaxWidth":"10px","animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false},"base":{"animate":true,"interval":6000}},
				bar3: {"polar":{"radius":[20,"80%"]},"backgroundColor":"transparent","radiusAxis":{"axisLabel":{"show":false},"axisTick":{"show":false},"type":"category"},"color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"show":false},"series":{"animationDuration":5000,"barWidth":"auto","animationEasing":"circularInOut","color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(219,109,4,1)"},{"offset":1,"color":"rgba(217,193,111,1)"}],"type":"linear"},"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#fff","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"coordinateSystem":"polar","label":{"formatter":"{b}: {c}","show":true,"fontSize":10,"position":"middle","color":"#000"},"animation":true,"barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"},"trigger":"axis"},"title":{"show":false},"base":{"animate":true,"interval":6000},"angleAxis":{"startAngle":90}},
				pie: {"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"legend":{"padding":[0,0,0,20],"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"animationDuration":5000,"animationEasing":"circularInOut","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"#fff","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","formatter":"{d}%","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"inside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"radius":[0,"75%"],"animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				pie2: {"tooltip":{"backgroundColor":"#123","trigger":"item","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"show":false},"legend":{"padding":[0,0,0,10],"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":12,"textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"animationDuration":5000,"animationEasing":"circularInOut","avoidLabelOverlap":false,"emphasis":{"label":{"show":true,"fontSize":16,"fontWeight":"bold"}},"itemStyle":{"borderRadius":20},"label":{"show":false,"position":"center"},"labelLine":{"show":false},"padAngle":5,"animation":true}},
				pie3: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"show":false},"legend":{"padding":[0,0,0,10],"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"animationDuration":5000,"animationEasing":"circularInOut","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"rgb(3, 12, 59)","shadowOffsetY":0,"color":"","borderRadius":5,"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"#fff","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":true},"radius":["30%","75%"],"animation":true}},
				funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"show":false},"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":8,"show":true,"icon":"roundRect","type":"scroll","top":"bottom","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":14,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":10,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2}},
				funnel2: {"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"legend":{"itemGap":4,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				funnel3: {"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"legend":{"itemGap":4,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				funnel4: {"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"legend":{"itemGap":4,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				funnel5: {"backgroundColor":"transparent","color":["rgb(219,109,4)","rgb(217,193,111)","#95a4ca","#b34c54","#73D13D","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"legend":{"itemGap":4,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"center","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				map: {"tooltip":{"formatter":"{b} : {c}","trigger":"item"},"backgroundColor":"transparent","title":{"borderType":"solid","padding":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"auto","itemWidth":25,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"aspectScale":0.75,"itemStyle":{"areaColor":"#a8d5fc"},"zoom":1.8,"label":{"emphasis":{"show":true,"textStyle":{"color":"#3ba372"}},"normal":{"color":"#3ba372","show":true}},"roam":true,"showLegendSymbol":false,"animation":false},"visualMap":{"min":0,"text":["High","Low"],"inRange":{"color":["#27b3ff","#fe9900","#57bd57","#f92f00","#01cbcf","#3ba272","#fc8452","#9a60b4","#ea7ccc"]},"max":500,"calculable":true,"seriesIndex":[0]}},
				boardBase: {"funnelNum":6,"lineNum":8,"gaugeNum":4,"barNum":10,"pieNum":6},
				gauge: {"tooltip":{"formatter":"{b} : {c}","trigger":"item"},"backgroundColor":"transparent","color":["rgb(251, 140, 61)","rgb(59, 220, 31)","rgb(83, 207, 252)","#fac858","#3ba272","#5470c6","#ee6666","#ea7ccc"],"title":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"diamond","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"axisTick":{"lineStyle":{"color":"#999","width":2},"length":10,"splitNumber":1},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":4,"show":true,"width":6,"fontSize":12,"height":4},"title":{"color":"","show":true,"fontSize":12},"animation":true}},
				myChart0: null,
				xiaoshouinfoList: [],
				xiaoshouinfoTimer: null,
				systemIntroductionDetail: null,
				dates: '',
				xiaoshouinfoCount: 0,
				forecastForm: {},
				form: {},
				particlesJson: {"retina_detect":true,"particles":{"number":{"density":{"value_area":800,"enable":true},"value":40},"move":{"straight":false,"random":true,"bounce":false,"enable":true,"attract":{"rotateX":600,"enable":false,"rotateY":600},"speed":1,"direction":"none","out_mode":"out"},"color":{"value":"#FF7800"},"shape":{"image":{"width":100,"src":"img/github.svg","height":100},"polygon":{"nb_sides":5},"type":"circle","stroke":{"color":"#FF7800","width":0}},"size":{"anim":{"size_min":0.3,"sync":false,"enable":false,"speed":4},"random":true,"value":3},"line_linked":{"width":1,"distance":150,"color":"#ffffff","opacity":0.4,"enable":false},"opacity":{"anim":{"opacity_min":0,"sync":true,"enable":true,"speed":1},"random":true,"value":1}},"interactivity":{"detect_on":"canvas","events":{"resize":true,"onclick":{"mode":"repulse","enable":false},"onhover":{"mode":"bubble","enable":true}},"modes":{"grab":{"distance":100,"line_linked":{"opacity":0.8}},"bubble":{"duration":2,"distance":250,"size":4,"opacity":1,"speed":3},"repulse":{"duration":0.4,"distance":400},"push":{"particles_nb":4},"remove":{"particles_nb":2}}}}
			};
		},
		mounted(){
			this.init();
			this.getxiaoshouinfoList()
			particlesJS('particles',this.particlesJson)
		},
		created() {
			this.$nextTick(()=>{
				this.times()
				setTimeout(()=>{
					this.getxiaoshouinfoCount();
					this.xiaoshouinfoChat1();
					this.xiaoshouinfoChat2();
					this.xiaoshouinfoChat3();
					this.xiaoshouinfoChat4();
					this.xiaoshouinfoChat5();
				},500)
			})
		},
		methods:{
			forecastClick(row) {
				this.$confirm(`是否进行数据预测?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(()=>{
					let loading = null
					loading = Loading.service({
						target: this.$refs['roleMenuBox'],
						fullscreen: false,
						text: '数据预测中...'
					})
					this.$http({
						url: 'xiaoshouinfoforecast/save',
						method: 'post',
						data: this.forecastForm
					}).then(res=>{
						if(res.data&&res.data.code==0){
							this.forecastForm.id = res.data.data
							this.$http({
								url: 'xiaoshouinfoforecast/forecast',
								method: 'post',
								data: this.forecastForm
							}).then(obj=>{
								if(obj.data&&obj.data.code==0){
									this.$http({
										url: 'xiaoshouinfoforecast/info/' + res.data.data,
										method: 'get'
									}).then(rs2=>{
										if(rs2.data&&rs2.data.code==0){
											if (loading) loading.close()
											this.$message({
												message: "数据预测完成！",
												type: "success",
												duration: 1500,
												onClose: () => {
													this.form = rs2.data.data
												}
											});
										}
									})
									
								}
							})
						}
					})
					
				})
			},
			getxiaoshouinfoList() {
				let params = {
					page: 1,
					limit: 20,
				}
				params.order = 'desc'
				params.sort = 'mxiaoliang'
				this.$http({
					url: "xiaoshouinfo/page",
					method: "get",
					params: params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.xiaoshouinfoList = data.data.list;
						let div = document.getElementById('xiaoshouinfoTable')
						var scrollTop = -1
						function move() {
							if (div){
								if(div.scrollTop==scrollTop){
									div.scrollTo({
										top: 0, 
										behavior: "smooth"
									});
									return false
								}
								scrollTop = div.scrollTop
								div.scrollTo({ 
									top: div.scrollTop + 40, 
									behavior: "smooth"
								});
							}
								
						}
						this.xiaoshouinfoTimer = setInterval(move, 2000);
						div.addEventListener('mouseenter', e => {
							e.stopPropagation()
							clearInterval(this.xiaoshouinfoTimer);
						})
						div.addEventListener('mouseleave', e => {
							e.stopPropagation()
							this.xiaoshouinfoTimer = setInterval(move, 2000);
						})
					}
				});
			},
			backClick(){
				this.$router.replace({ path: "/" });
			},
			myChartInterval(type, xAxisData, seriesData, myChart) {
				this.$nextTick(() => {
					setInterval(() => {
						let xAxis = xAxisData.shift()
						xAxisData.push(xAxis)
						let series = seriesData.shift()
						seriesData.push(series)
			
						if (type == 1) {
							myChart.setOption({
								xAxis: [{
									data: xAxisData
								}],
								series: [{
									data: seriesData
								}]
							});
						}
						if (type == 2) {
							myChart.setOption({
								yAxis: [{
									data: xAxisData
								}],
								series: [{
									data: seriesData
								}]
							});
						}
					}, 6000);
				})
			},
			wordclouds(wordcloudData,echartsId) {
				let wordcloud = {"maskImage":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACW0lEQVRYR72XT0iUQRjGW5X8A1ZeVOgPSoKFonjw5qFblw5BkfQHDx51UehUFFYkghcLdG9JEERFEB26dBA8dAs8SFlRHkRUdBGKIKVa8PfI98Hu1ze7M7uzvfAw3zfzvs88M8y8M5M4UJzVEHYPnAdV4GXwv+NKl3ANCPyfUl6JxKrumitfMQLa6eQTiIs9Rf0XFxHFCJilg0FDJ4/ztMWGuApohGUVHDQI+Ev9UbBlOwuuAiYgvlmAfJL2G+UQUAvpJqgvQP6T9iZgtSNcZmAU0oeWI7uO3wMbXxsBdRBp5b8GJ2xI8VkH58DnQjORLaAX59PgZIBWyjaghVeKScxX8C0oJUrfH0UqAVq1c8EoS+nINfYJAUkJeA76XaM9+ack4Ac45InQlSYtARug2TXSk/+yBIyDW54IXWmGJEDQSXbZNbpE/2fEXw23YSU/2ufau//D3tCJ7hKZ7DygA+YtOFNmBfPwnwW/1U80EyrryUFJqRz2Phjgr5A8LhUfofEd6PCsQJmvD3zP5jWdBUq/C0BZ0oetQdID0lGyfIfRB4+zoNF3xo3EJKAC5z9ApQ/LQFINVOaYSYBOxSUfPWdxiFMnoZWAi3jpru/TLkD2ylbAGI56ePg0cd63FfACx0s+e4dLx/4/6d60BnzugHAci3x0286AbrR6/+UzXbN0+ZTvFOgq4L9Lu27WOWaaAT0+jhkIlcm0PqI35AHqdLQfN8StUN9iK+AOjndjiB5Rp0fHtqETzVoS3AaHIz6qT9kKkN8MGA4Cwuf3/k3WwhqCzsJFN83/SFzcHuflWvJycLzsAAAAAElFTkSuQmCC","option":{"tooltip":{"show":false},"backgroundColor":"transparent","series":[{"sizeRange":[8,20],"layoutAnimation":true,"shape":"circle","data":[{"name":"花鸟市场","value":1446},{"name":"汽车","value":928},{"name":"视频","value":906},{"name":"电视","value":825},{"name":"Lover Boy 88","value":514},{"name":"动漫","value":486},{"name":"音乐","value":53},{"name":"直播","value":163},{"name":"广播电台","value":86},{"name":"戏曲曲艺","value":17},{"name":"演出票务","value":6},{"name":"给陌生的你听","value":1},{"name":"资讯","value":1437},{"name":"商业财经","value":422},{"name":"娱乐八卦","value":353},{"name":"军事","value":331},{"name":"科技资讯","value":313},{"name":"社会时政","value":307},{"name":"时尚","value":43},{"name":"网络奇闻","value":15},{"name":"旅游出行","value":438},{"name":"景点类型","value":957},{"name":"国内游","value":927},{"name":"远途出行方式","value":908},{"name":"酒店","value":693},{"name":"关注景点","value":611},{"name":"旅游网站偏好","value":512},{"name":"出国游","value":382},{"name":"交通票务","value":312},{"name":"旅游方式","value":187},{"name":"旅游主题","value":163},{"name":"港澳台","value":104},{"name":"本地周边游","value":3},{"name":"小卖家","value":1331},{"name":"全日制学校","value":941},{"name":"基础教育科目","value":585},{"name":"考试培训","value":473},{"name":"语言学习","value":358},{"name":"留学","value":246},{"name":"K12课程培训","value":207},{"name":"艺术培训","value":194},{"name":"技能培训","value":104},{"name":"IT培训","value":87},{"name":"高等教育专业","value":63},{"name":"家教","value":48},{"name":"体育培训","value":23},{"name":"职场培训","value":5},{"name":"金融财经","value":1328},{"name":"银行","value":765},{"name":"股票","value":452},{"name":"保险","value":415},{"name":"贷款","value":253},{"name":"基金","value":211},{"name":"信用卡","value":180},{"name":"外汇","value":138},{"name":"P2P","value":116},{"name":"贵金属","value":98},{"name":"债券","value":93},{"name":"网络理财","value":92},{"name":"信托","value":90},{"name":"征信","value":76},{"name":"期货","value":76},{"name":"公积金","value":40},{"name":"银行理财","value":36},{"name":"银行业务","value":30},{"name":"典当","value":7},{"name":"海外置业","value":1},{"name":"汽车","value":1309},{"name":"汽车档次","value":965},{"name":"汽车品牌","value":900},{"name":"汽车车型","value":727},{"name":"购车阶段","value":461},{"name":"二手车","value":309},{"name":"汽车美容","value":260},{"name":"新能源汽车","value":173},{"name":"汽车维修","value":155},{"name":"租车服务","value":136},{"name":"车展","value":121},{"name":"违章查询","value":76},{"name":"汽车改装","value":62},{"name":"汽车用品","value":37},{"name":"路况查询","value":32},{"name":"汽车保险","value":28},{"name":"陪驾代驾","value":4},{"name":"网络购物","value":1275},{"name":"做我的猫","value":1088},{"name":"只想要你知道","value":907},{"name":"团购","value":837},{"name":"比价","value":201},{"name":"海淘","value":195},{"name":"移动APP购物","value":179},{"name":"支付方式","value":119},{"name":"代购","value":43},{"name":"体育健身","value":1234},{"name":"体育赛事项目","value":802},{"name":"运动项目","value":405},{"name":"体育类赛事","value":337},{"name":"健身项目","value":199},{"name":"健身房健身","value":78},{"name":"运动健身","value":77},{"name":"家庭健身","value":36},{"name":"健身器械","value":29},{"name":"办公室健身","value":3},{"name":"商务服务","value":1201},{"name":"法律咨询","value":508},{"name":"化工材料","value":147},{"name":"广告服务","value":125},{"name":"会计审计","value":115},{"name":"人员招聘","value":101},{"name":"印刷打印","value":66},{"name":"知识产权","value":32},{"name":"翻译","value":22},{"name":"安全安保","value":9},{"name":"公关服务","value":8},{"name":"商旅服务","value":2},{"name":"展会服务","value":2},{"name":"特许经营","value":1},{"name":"休闲爱好","value":1169},{"name":"收藏","value":412},{"name":"摄影","value":393},{"name":"温泉","value":230},{"name":"博彩彩票","value":211},{"name":"美术","value":207},{"name":"书法","value":139},{"name":"DIY手工","value":75},{"name":"舞蹈","value":23},{"name":"钓鱼","value":21},{"name":"棋牌桌游","value":17},{"name":"KTV","value":6},{"name":"密室","value":5},{"name":"采摘","value":4},{"name":"电玩","value":1},{"name":"真人CS","value":1},{"name":"轰趴","value":1},{"name":"家电数码","value":1111},{"name":"手机","value":885},{"name":"电脑","value":543},{"name":"大家电","value":321},{"name":"家电关注品牌","value":253},{"name":"网络设备","value":162},{"name":"摄影器材","value":149},{"name":"影音设备","value":133},{"name":"办公数码设备","value":113},{"name":"生活电器","value":67},{"name":"厨房电器","value":54},{"name":"智能设备","value":45},{"name":"个人护理电器","value":22},{"name":"服饰鞋包","value":1047},{"name":"服装","value":566},{"name":"饰品","value":289},{"name":"鞋","value":184},{"name":"箱包","value":168},{"name":"奢侈品","value":137},{"name":"母婴亲子","value":1041},{"name":"孕婴保健","value":505},{"name":"母婴社区","value":299},{"name":"早教","value":103},{"name":"奶粉辅食","value":66},{"name":"童车童床","value":41},{"name":"关注品牌","value":271},{"name":"宝宝玩乐","value":30},{"name":"母婴护理服务","value":25},{"name":"纸尿裤湿巾","value":16},{"name":"妈妈用品","value":15},{"name":"宝宝起名","value":12},{"name":"童装童鞋","value":9},{"name":"胎教","value":8},{"name":"宝宝安全","value":1},{"name":"宝宝洗护用品","value":1},{"name":"软件应用","value":1018},{"name":"系统工具","value":896},{"name":"理财购物","value":440},{"name":"生活实用","value":365},{"name":"影音图像","value":256},{"name":"社交通讯","value":214},{"name":"手机美化","value":39},{"name":"办公学习","value":28},{"name":"应用市场","value":23},{"name":"母婴育儿","value":14},{"name":"游戏","value":946},{"name":"手机游戏","value":565},{"name":"PC游戏","value":353},{"name":"网页游戏","value":254},{"name":"游戏机","value":188},{"name":"模拟辅助","value":166},{"name":"个护美容","value":942},{"name":"护肤品","value":177},{"name":"彩妆","value":133},{"name":"美发","value":80},{"name":"香水","value":50},{"name":"个人护理","value":46},{"name":"美甲","value":26},{"name":"SPA美体","value":21},{"name":"花鸟萌宠","value":914},{"name":"绿植花卉","value":311},{"name":"狗","value":257},{"name":"其他宠物","value":131},{"name":"水族","value":125},{"name":"猫","value":122},{"name":"动物","value":81},{"name":"鸟","value":67},{"name":"宠物用品","value":41},{"name":"宠物服务","value":26},{"name":"书籍阅读","value":913},{"name":"网络小说","value":483},{"name":"关注书籍","value":128},{"name":"文学","value":105},{"name":"报刊杂志","value":77},{"name":"人文社科","value":22},{"name":"建材家居","value":907},{"name":"装修建材","value":644},{"name":"家具","value":273},{"name":"家居风格","value":187},{"name":"家居家装关注品牌","value":140},{"name":"家纺","value":107},{"name":"厨具","value":47},{"name":"灯具","value":43},{"name":"家居饰品","value":29},{"name":"家居日常用品","value":10},{"name":"生活服务","value":883},{"name":"物流配送","value":536},{"name":"家政服务","value":108},{"name":"摄影服务","value":49},{"name":"搬家服务","value":38},{"name":"物业维修","value":37},{"name":"婚庆服务","value":24},{"name":"二手回收","value":24},{"name":"鲜花配送","value":3},{"name":"维修服务","value":3},{"name":"殡葬服务","value":1},{"name":"求职创业","value":874},{"name":"创业","value":363},{"name":"目标职位","value":162},{"name":"目标行业","value":50},{"name":"兼职","value":21},{"name":"期望年薪","value":20},{"name":"实习","value":16},{"name":"雇主类型","value":10},{"name":"星座运势","value":789},{"name":"星座","value":316},{"name":"算命","value":303},{"name":"解梦","value":196},{"name":"风水","value":93},{"name":"面相分析","value":47},{"name":"手相","value":32},{"name":"公益","value":90}],"keepAspect":false,"type":"wordCloud","rotationRange":[-90,90],"gridSize":4,"shrinkToFit":true,"top":"center","left":"center","width":"80%","emphasis":{"focus":"self","textStyle":{"textShadowColor":"#333","textShadowBlur":4}},"drawOutOfBound":false,"rotationStep":45,"textStyle":{"color":"function(){return\"rgb(\"+[Math.round(Math.floor(Math.random() * (100 - 255)) + 255),Math.round(Math.floor(Math.random() * (100 - 255)) + 255),Math.round(Math.floor(Math.random() * (100 - 255)) + 255)].join(\",\")+\")\"}","fontWeight":500,"fontFamily":"sans-serif"},"height":"80%","maskImage":{}}]}}
				wordcloud = JSON.parse(JSON.stringify(wordcloud), (k, v) => {
					if(typeof v == 'string' && v.indexOf('function') > -1){
						return eval("(function(){return "+v+" })()")
					}
					return v;
				})
				wordcloud.option.series[0].data=wordcloudData;
				
				this.myChart0 = echarts.init(document.getElementById(echartsId));
				let myChart = this.myChart0
				let img = wordcloud.maskImage
			
				if (img) {
					var maskImage = new Image();
					maskImage.src = img
					maskImage.onload = function() {
						wordcloud.option.series[0].maskImage = maskImage
						myChart.clear()
						myChart.setOption(wordcloud.option)
					}
				} else {
					delete wordcloud.option.series[0].maskImage
					myChart.clear()
					myChart.setOption(wordcloud.option)
				}
			},
			getTimeStrToDay(game_over_timestamp) {
				if (game_over_timestamp == 0)
					return "";
				var date = new Date(parseInt(game_over_timestamp));
				var now = new Date();
				var hours = date.getHours() >= 10 ? date.getHours().toString() : "0" + date.getHours();
				var minutes = date.getMinutes() >= 10 ? date.getMinutes().toString() : "0" + date.getMinutes();
				var seconds = date.getSeconds() >= 10 ? date.getSeconds().toString() : "0" + date.getSeconds();
				let arr = ["日", "一", "二", "三", "四", "五", "六"];
				let d = arr[date.getDay()]
				return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + '日' + ' ' + ' ' + '星期' + d  + ' ' + "  " + hours + ":" + minutes + ":" + seconds
			},
			times() {
				setInterval(()=>{
					let date = new Date().getTime()
					this.dates = this.getTimeStrToDay(date)
				}, 1000)
			},
			filterTime(time) {
				const date = new Date(time)
				const Y = date.getFullYear()
				const M = date.getMonth() + 1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1 
				const D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
			  
				const H = date.getHours() < 10 ? '0' + date.getHours() : date.getHours() // 小时
				const I = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes() // 分钟
				const S = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds() // 秒
			  
				return `${Y}-${M}-${D} ${H}:${I}:${S}`
			},
			getSystemIntroduction() {
				this.$http({
					url: `systemintro/detail/1`,
					method: "get"
				}).then(({
					data
				}) => {
					if (data && data.code == 0) {
						this.systemIntroductionDetail = data.data
					}
				})
			},
			init(){
				if(this.$storage.get('Token')){
					this.$http({
						url: `${this.$storage.get('sessionTable')}/session`,
						method: "get"
					}).then(({ data }) => {
						if (data && data.code != 0) {
						router.push({ name: 'login' })
						}
					});
				}else{
					router.push({ name: 'login' })
				}
				this.getSystemIntroduction();
			},
			getxiaoshouinfoCount() {
				this.$http({
					url: `xiaoshouinfo/count`,
					method: "get"
				}).then(({
					data
				}) => {
					if (data && data.code == 0) {
						this.xiaoshouinfoCount = data.data
					}
				})
			},
			//统计接口1 词云图
			xiaoshouinfoChat1() {
				this.$nextTick(()=>{

					this.$http({
						url: "group/xiaoshouinfo/chexing",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								xAxis.push(res[i].chexing);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].chexing
								})
							}
							var option = {};
							this.wordclouds(pArray,'xiaoshouinfoChart1');
				

						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			//统计接口2 价格柱状图
			xiaoshouinfoChat2() {
				this.$nextTick(()=>{

					var xiaoshouinfoChart2 = echarts.init(document.getElementById("xiaoshouinfoChart2"),'macarons');
					this.$http({
						url: `xiaoshouinfo/value/chexing/minprice`,
						method: "get",
						params: {
							order: 'desc'
						}
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.barNum){
									break;
								}
								xAxis.push(res[i].chexing);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].chexing
								})
							}
							var option = {};
							let titleObj = this.bar.title
							titleObj.text = '最低售价统计'
							
							const legendObj = this.bar.legend
							
							let xAxisObj = this.bar.xAxis
							xAxisObj.type = 'category'
							xAxisObj.data = xAxis
							
							
							let yAxisObj = this.bar.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = {
									data: yAxis,
									type: 'bar'
								}
							seriesObj = Object.assign(seriesObj , this.bar.series)
							const gridObj = this.bar.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c}'
							}
							tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
							option = {
								backgroundColor: this.bar.backgroundColor,
								color: this.bar.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xiaoshouinfoChart2.setOption(option);
				
							this.myChartInterval(1, option.xAxis.data, option.series[0].data, xiaoshouinfoChart2)

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xiaoshouinfoChart2.resize();
							},false);
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			//统计接口3
			xiaoshouinfoChat3() {
				this.$nextTick(()=>{

					var xiaoshouinfoChart3 = echarts.init(document.getElementById("xiaoshouinfoChart3"),'macarons');
					this.$http({
						url: `xiaoshouinfo/value/chexing/maxprice`,
						method: "get",
						params: {
							order: 'desc'
						}
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.barNum){
									break;
								}
								xAxis.push(res[i].chexing);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].chexing
								})
							}
							var option = {};
							let titleObj = this.bar2.title
							titleObj.text = '最高售价统计'
							
							const legendObj = this.bar2.legend
							
							let xAxisObj = this.bar2.xAxis
							xAxisObj.type = 'value'
							
							
							let yAxisObj = this.bar2.yAxis
							yAxisObj.type = 'category'
							yAxisObj.data = xAxis
							let seriesObj = {
								data: yAxis,
								type: 'bar'
							}
							seriesObj = Object.assign(seriesObj , this.bar2.series)
							const gridObj = this.bar2.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c}'
							}
							tooltipObj = Object.assign(tooltipObj , this.bar2.tooltip?this.bar2.tooltip:{})
							option = {
								backgroundColor: this.bar2.backgroundColor,
								color: this.bar2.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xiaoshouinfoChart3.setOption(option);
				
							this.myChartInterval(2, option.yAxis.data, option.series[0].data, xiaoshouinfoChart3)

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xiaoshouinfoChart3.resize();
							},false);
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			//统计接口4
			xiaoshouinfoChat4() {
				this.$nextTick(()=>{

					var xiaoshouinfoChart4 = echarts.init(document.getElementById("xiaoshouinfoChart4"),'macarons');
					this.$http({
						url: `xiaoshouinfo/value/chexing/mxiaoliang`,
						method: "get",
						params: {
							order: 'desc'
						}
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.pieNum){
									break;
								}
								xAxis.push(res[i].chexing);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].chexing
								})
							}
							var option = {};
							let titleObj = this.pie.title
							titleObj.text = '月销量统计'
							
							const legendObj = this.pie.legend
							
							let seriesObj = {
								type: 'pie',
								radius: '55%',
								center: ['50%', '60%'],
								data: pArray,
								emphasis: {
									itemStyle: {
										shadowBlur: 10,
										shadowOffsetX: 0,
										shadowColor: 'rgba(0, 0, 0, 0.5)'
									}
								}
							}
							seriesObj = Object.assign(seriesObj , this.pie.series)
							const gridObj = this.pie.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c} ({d}%)'
							}
							tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
							option = {
								backgroundColor: this.pie.backgroundColor,
								color: this.pie.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xiaoshouinfoChart4.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xiaoshouinfoChart4.resize();
							},false);
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			//统计接口5
			xiaoshouinfoChat5() {
				this.$nextTick(()=>{

					var xiaoshouinfoChart5 = echarts.init(document.getElementById("xiaoshouinfoChart5"),'macarons');
					this.$http({
						url: `xiaoshouinfo/value/chexing/dyxlpm`,
						method: "get",
						params: {
							order: 'desc'
						}
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis.push(res[i].chexing);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].chexing
								})
							}
							var option = {};
							let titleObj = this.line.title
							titleObj.text = '当月销量排名'
							
							const legendObj = this.line.legend
							
							let xAxisObj = this.line.xAxis
							xAxisObj.type = 'category'
							xAxisObj.boundaryGap = false
							xAxisObj.data = xAxis
							
							
							let yAxisObj = this.line.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = {
								data: yAxis,
								type: 'line',
							}
							seriesObj = Object.assign(seriesObj , this.line.series)
							const gridObj = this.line.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c}'
							}
							tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
							option = {
								backgroundColor: this.line.backgroundColor,
								color: this.line.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xiaoshouinfoChart5.setOption(option);


							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xiaoshouinfoChart5.resize();
							},false);
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
		}
	};
</script>
<style lang="scss" scoped>
	// table
	.el-table:before{
		display: none;
	}
	.el-table:after{
		display: none;
	}
	.el-table /deep/ .el-table__header-wrapper thead {
				color: #fff;
				font-weight: 500;
				width: 100%;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th {
				padding: 6px 0;
				background: none;
				border-color: rgba(92,135,230,.3);
				border-width: 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th .cell {
				padding: 0 10px;
				word-wrap: normal;
				color: rgb(255, 227, 168);
				word-break: break-all;
				white-space: normal;
				font-weight: bold;
				display: inline-block;
				vertical-align: middle;
				width: 100%;
				line-height: 24px;
				position: relative;
				text-overflow: ellipsis;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody {
				width: 100%;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr {
				background: none;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #fff;
				background: none;
				border-color: rgba(92,135,230,.3);
				border-width: 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr.el-table__row--striped td {
		background: rgba(255, 227, 168,0.1);
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
				padding: 6px 0;
				color: #fff;
				background: rgba(255, 227, 168,0.2);
				border-color: rgba(92,135,230,.3);
				border-width: 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #fff;
				background: none;
				border-color: rgba(92,135,230,.3);
				border-width: 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
				padding: 0 10px;
				overflow: hidden;
				word-break: break-all;
				white-space: normal;
				line-height: 24px;
				text-overflow: ellipsis;
			}
	.echarts1 {
				padding: 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: 1 1 auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
			}
	.echarts1:hover {
			}
	.echarts2 {
				padding: 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
			}
	.echarts2:hover {
			}
	.echarts3 {
				padding: 0;
				max-height: 500px;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
			}
	.echarts3:hover {
			}
	.echarts4 {
				padding: 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				order: 1;
			}
	.echarts4:hover {
			}
	.echarts5 {
				padding: 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 70%;
				transition: 0.3s;
				height: calc(50% - 42px);
				order: 2;
			}
	.echarts5:hover {
			}
	.echarts6 {
				padding: 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: calc(50% - 42px);
				order: 1;
			}
	.echarts6:hover {
			}
	#particles{
		background-repeat: no-repeat;
		z-index: 1;
		background-size: cover;
		width: 100%;
		position: absolute;
		background-position: 50% 50%;
		height: 100%;
	}
	::-webkit-scrollbar {
		display: none; /* 针对Webkit浏览器 */
	}
</style>

