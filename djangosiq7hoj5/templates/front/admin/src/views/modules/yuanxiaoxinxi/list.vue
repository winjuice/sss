<template>
	<div class="main-content" :style='{"minHeight":"calc(100vh - 200px)","padding":"20px 0 30px","margin":"0 auto","color":"#666","background":"none","width":"calc(100% - 60px)","fontSize":"16px","height":"100%"}'>
		<!-- 列表页 -->
		<template v-if="showFlag">
			<el-form class="center-form-pv" :style='{"border":"0px solid #ceddee","minHeight":"100px","padding":"10px 0px","boxShadow":"0 0px 0px 0px rgba(100,100,100,.05)","margin":"0px","overflow":"hidden","borderRadius":"20px 20px","flexWrap":"wrap","background":"none","display":"flex","fontSize":"inherit","justifyContent":"center"}' :inline="true" :model="searchForm">
				<el-row :style='{"padding":"0px","boxShadow":"0 0px 0px 0px rgba(115,108,203,.23)","margin":"0 0px 0px 0","borderRadius":"0px","alignItems":"center","flexWrap":"wrap","background":"none","display":"flex","width":"auto","fontSize":"inherit","justifyContent":"flex-end","order":"2"}' >
					<div :style='{"margin":"0 5px 10px 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 5px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">学校名称</label>
						<el-input v-model="searchForm.schoolname" placeholder="学校名称" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 5px 10px 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 5px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">专业名称</label>
						<el-input v-model="searchForm.specialname" placeholder="专业名称" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 5px 10px 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 5px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">学校类型</label>
						<el-input v-model="searchForm.typeschool" placeholder="学校类型" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 5px 10px 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 5px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">硕士类型</label>
						<el-input v-model="searchForm.degreename" placeholder="硕士类型" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<el-button class="search" type="success" @click="search()">
						<span class="icon iconfont icon-chakan18" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none","height":"auto"}'></span>
						搜索
					</el-button>
				</el-row>

				<el-row class="actions" :style='{"boxShadow":"0 0px 0px 0px rgba(115,108,203,.23)","padding":"0 20px 0 0","margin":"0px 0 0px","color":"#333","alignItems":"center","textAlign":"left","display":"flex","justifyContent":"flex-start","borderRadius":"0px","flexWrap":"wrap","background":"none","flex":"1","width":"auto","fontSize":"inherit","order":"1"}'>
					<el-button class="add" v-if="isAuth('yuanxiaoxinxi','新增')" type="success" @click="addOrUpdateHandler()">
						<span class="icon iconfont icon-tianjia13" :style='{"margin":"0px 2px","fontSize":"24px","position":"absolute","color":"#327e33","left":"10px","display":"inline-block"}'></span>
						新增
					</el-button>
					<el-button class="del" v-if="isAuth('yuanxiaoxinxi','删除')" :disabled="dataListSelections.length?false:true" type="danger" @click="deleteHandler()">
						<span class="icon iconfont icon-shanchu8" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						删除
					</el-button>


					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','爬取数据')" type="success" @click="spider()">
						<span class="icon iconfont icon-shuju17" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						爬取数据
					</el-button>

					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','学校总分统计')" type="success" @click="chartDialog1()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						学校总分统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','学校名称')" type="success" @click="chartDialog2()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						学校名称
					</el-button>
					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','分类')" type="success" @click="chartDialog3()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						分类
					</el-button>
					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','专业名称')" type="success" @click="chartDialog4()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						专业名称
					</el-button>
					<el-button class="btn18" v-if="isAuth('yuanxiaoxinxi','专业类型统计')" type="success" @click="chartDialog5()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","color":"#327e33","left":"10px","display":"inline-block","fontSize":"24px","position":"absolute","fontWeight":"500"}'></span>
						专业类型统计
					</el-button>
				</el-row>
			</el-form>
			<div :style='{"padding":"0px","boxShadow":"inset 0px 0px 0px 0px #E8EFF6","borderColor":"#d2d0d0","margin":"0 0 0px","borderRadius":"0px","background":"rgba(255,255,255,.8)","borderWidth":"1px","width":"100%","borderStyle":"solid"}'>
				<el-table class="tables"
					:stripe='true'
					:style='{"padding":"0","borderColor":"#eee","color":"inherit","borderRadius":"0px","borderWidth":"0px 0px 0 0px","background":"none","width":"100%","fontSize":"inherit","borderStyle":"solid"}' 
					:border='true'
					v-if="isAuth('yuanxiaoxinxi','查看')"
					:data="dataList"
					v-loading="dataListLoading"
				@selection-change="selectionChangeHandler">
					<el-table-column :resizable='true' type="selection" align="center" width="50"></el-table-column>
					<el-table-column :resizable='true' :sortable='true' label="序号" type="index" width="50" />
					<el-table-column :resizable='true' :sortable='true'  
						prop="year"
						label="年份">
						<template slot-scope="scope">
							{{scope.row.year}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="schoolname"
						label="学校名称">
						<template slot-scope="scope">
							{{scope.row.schoolname}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="specialname"
						label="专业名称">
						<template slot-scope="scope">
							{{scope.row.specialname}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="specialcode"
						label="专业编码">
						<template slot-scope="scope">
							{{scope.row.specialcode}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="typename"
						label="分类">
						<template slot-scope="scope">
							{{scope.row.typename}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="typeschool"
						label="学校类型">
						<template slot-scope="scope">
							{{scope.row.typeschool}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="degreename"
						label="硕士类型">
						<template slot-scope="scope">
							{{scope.row.degreename}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="ranking"
						label="排名">
						<template slot-scope="scope">
							{{scope.row.ranking}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="total"
						label="总分">
						<template slot-scope="scope">
							{{scope.row.total}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="politics"
						label="政治">
						<template slot-scope="scope">
							{{scope.row.politics}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="english"
						label="英语">
						<template slot-scope="scope">
							{{scope.row.english}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="specialone"
						label="专业课一">
						<template slot-scope="scope">
							{{scope.row.specialone}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="specialtwo"
						label="专业课二">
						<template slot-scope="scope">
							{{scope.row.specialtwo}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="clicknum"
						label="点击次数">
						<template slot-scope="scope">
							{{scope.row.clicknum}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="discussnum"
						label="评论数">
						<template slot-scope="scope">
							{{scope.row.discussnum}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="storeupnum"
						label="收藏数">
						<template slot-scope="scope">
							{{scope.row.storeupnum}}
						</template>
					</el-table-column>
					<el-table-column width="300" label="操作">
						<template slot-scope="scope">
							<el-button class="view" v-if=" isAuth('yuanxiaoxinxi','查看')" type="success" @click="addOrUpdateHandler(scope.row.id,'info')">
								<span class="icon iconfont icon-chakan5" :style='{"margin":"0 0 0 4px","fontSize":"24px","position":"absolute","color":"#327e33","left":"0","height":"auto"}'></span>
								详情
							</el-button>
							<el-button class="edit" v-if=" isAuth('yuanxiaoxinxi','修改') " type="success" @click="addOrUpdateHandler(scope.row.id)">
								<span class="icon iconfont icon-xiugai19" :style='{"margin":"0 0 0 4px","fontSize":"24px","position":"absolute","color":"#45B6B0","left":"0","height":"auto"}'></span>
								修改
							</el-button>

							<el-button class="view" v-if="isAuth('yuanxiaoxinxi','查看评论')" type="success" @click="disscussListHandler(scope.row.id)">
								<span class="icon iconfont icon-chakan5" :style='{"margin":"0 0 0 4px","fontSize":"24px","position":"absolute","color":"#327e33","left":"0","height":"auto"}'></span>
								查看评论
							</el-button>



							<el-button class="del" v-if="isAuth('yuanxiaoxinxi','删除') " type="primary" @click="deleteHandler(scope.row.id )">
								<span class="icon iconfont icon-shanchu6" :style='{"margin":"0 0 0 4px","fontSize":"24px","position":"absolute","color":"#d9534f","left":"0","height":"auto"}'></span>
								删除
							</el-button>
						</template>
					</el-table-column>
				</el-table>
			</div>
			<el-pagination
				@size-change="sizeChangeHandle"
				@current-change="currentChangeHandle"
				:current-page="pageIndex"
				background
				:page-sizes="[10, 50, 100, 200]"
				:page-size="pageSize"
				:layout="layouts.join()"
				:total="totalPage"
				prev-text="上一页 "
				next-text="下一页 "
				:hide-on-single-page="false"
				:style='{"border":"1px solid #e1e1e1","padding":"10px 0","margin":"20px 0 0","whiteSpace":"nowrap","color":"inherit","textAlign":"center","background":"#eff3f9","width":"100%","fontSize":"inherit","fontWeight":"500"}'
			></el-pagination>
		</template>
		
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-if="addOrUpdateFlag" :parent="this" ref="addOrUpdate"></add-or-update>





		<el-dialog
		  :visible.sync="chartVisiable1"
		  width="800">
			<div id="totalChart1" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog1">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable2"
		  width="800">
			<div id="schoolnameChart2" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog2">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable3"
		  width="800">
			<div id="typenameChart3" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog3">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable4"
		  width="800">
			<div id="specialnameChart4" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog4">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable5"
		  width="800">
			<div id="specialnameChart5" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog5">返回</el-button>
		  </span>
		</el-dialog>
	</div>
</template>

<script>
import * as echarts from 'echarts'
import chinaJson from "@/components/echarts/china.json";
import axios from 'axios'
import AddOrUpdate from "./add-or-update";
	export default {
		data() {
			return {
				searchForm: {
					key: ""
				},
				form:{},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				dataListSelections: [],
				showFlag: true,
				sfshVisiable: false,
				shForm: {},
				chartVisiable: false,
				chartVisiable1: false,
				chartVisiable2: false,
				chartVisiable3: false,
				chartVisiable4: false,
				chartVisiable5: false,
				addOrUpdateFlag:false,
				layouts: ["total","prev","pager","next","sizes","jumper"],
			};
		},
		created() {
			this.init();
			this.getDataList();
			this.contentStyleChange()
		},
		mounted() {
		},
		filters: {
			htmlfilter: function (val) {
				return val.replace(/<[^>]*>/g).replace(/undefined/g,'');
			}
		},
		computed: {
			tablename(){
				return this.$storage.get('sessionTable')
			},
		},
		components: {
			AddOrUpdate,
		},
		methods: {
			contentStyleChange() {
				this.contentPageStyleChange()
			},
			// 分页
			contentPageStyleChange(){
				let arr = []

				// if(this.contents.pageTotal) arr.push('total')
				// if(this.contents.pageSizes) arr.push('sizes')
				// if(this.contents.pagePrevNext){
				//   arr.push('prev')
				//   if(this.contents.pagePager) arr.push('pager')
				//   arr.push('next')
				// }
				// if(this.contents.pageJumper) arr.push('jumper')
				// this.layouts = arr.join()
				// this.contents.pageEachNum = 10
			},


//统计接口
    chartDialog1() {
      this.chartVisiable1 = !this.chartVisiable1;
      this.$nextTick(()=>{
        var totalChart1 = echarts.init(document.getElementById("totalChart1"),'carp');
        this.$http({
            url: `yuanxiaoxinxi/value/schoolname/total`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].schoolname);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].schoolname
                    })
                }
                var option = {};
				option = {
					title: {
						text: '学校总分统计',
						left: 'center'
					},
					tooltip: {
						trigger: 'item',
						formatter: "{b} : {c}"
					},
					
					legend: {
						data: xAxis,
						bottom: 0
					},
					series: [{
						data: pArray,
						name: '学校总分统计',
						type:'funnel',
						left: '10%',
						top: 60,
						//x2: 80,
						bottom: 60,
						width: '80%',
						minSize: '0%',
						maxSize: '100%',
						// sort: 'descending',
						gap: 2,
						label: {
							show: true,
							position: 'inside'
						},
						labelLine: {
							length: 10,
							lineStyle: {
								width: 1,
								type: 'solid'
							}
						},
						itemStyle: {
							borderColor: '#fff',
							borderWidth: 1
						},
						emphasis: {
							label: {
								fontSize: 20
							}
						},
					}]
					
				}
                // 使用刚指定的配置项和数据显示图表。
                totalChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    totalChart1.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog2() {
      this.chartVisiable2 = !this.chartVisiable2;
      this.$nextTick(()=>{

        var schoolnameChart2 = echarts.init(document.getElementById("schoolnameChart2"),'carp');
        this.$http({
            url: "yuanxiaoxinxi/group/schoolname",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].schoolname);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].schoolname
                    })
                }
                var option = {};
                // 使用刚指定的配置项和数据显示图表。
                schoolnameChart2.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    schoolnameChart2.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog3() {
      this.chartVisiable3 = !this.chartVisiable3;
      this.$nextTick(()=>{

        var typenameChart3 = echarts.init(document.getElementById("typenameChart3"),'carp');
        this.$http({
            url: "yuanxiaoxinxi/group/typename",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].typename);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].typename
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '分类',
                            left: 'center'
                        },
                        legend: {
                          orient: 'vertical',
                          left: 'left'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: ['25%', '55%'],
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
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                typenameChart3.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    typenameChart3.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog4() {
      this.chartVisiable4 = !this.chartVisiable4;
      this.$nextTick(()=>{
        // specialname specialname

        var specialnameChart4 = echarts.init(document.getElementById("specialnameChart4"),'carp');
        this.$http({
            url: `yuanxiaoxinxi/valueMul/specialname?yColumnNameMul=politics,english,specialone,specialtwo`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis1 = [];
                let yAxis1 = [];
                let pArray1 = []
                for(let i=0;i<res[0].length;i++){
                    xAxis1.push(res[0][i].specialname);
                    yAxis1.push(parseFloat((res[0][i].total)));
                    pArray1.push({
                        value: parseFloat((res[0][i].total)),
                        name: res[0][i].specialname
                    })
                }
                let xAxis2 = [];
                let yAxis2 = [];
                let pArray2 = []
                for(let i=0;i<res[1].length;i++){
                    xAxis2.push(res[1][i].specialname);
                    yAxis2.push(parseFloat((res[1][i].total)));
                    pArray2.push({
                        value: parseFloat((res[1][i].total)),
                        name: res[1][i].specialname
                    })
                }
                let xAxis3 = [];
                let yAxis3 = [];
                let pArray3 = []
                for(let i=0;i<res[2].length;i++){
                    xAxis3.push(res[2][i].specialname);
                    yAxis3.push(parseFloat((res[2][i].total)));
                    pArray3.push({
                        value: parseFloat((res[2][i].total)),
                        name: res[2][i].specialname
                    })
                }
                let xAxis4 = [];
                let yAxis4 = [];
                let pArray4 = []
                for(let i=0;i<res[3].length;i++){
                    xAxis4.push(res[3][i].specialname);
                    yAxis4.push(parseFloat((res[3][i].total)));
                    pArray4.push({
                        value: parseFloat((res[3][i].total)),
                        name: res[3][i].specialname
                    })
                }
                var option = {};
                option = {
                    title: {
                        left: 'left'
                    },
                    legend: {
                        data: [
                                '政治',
                                '英语',
                                '专业一',
                                '专业二',
                              ]
                    },
                    tooltip: {
                      trigger: 'axis',
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: xAxis1
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                    {
                        data: yAxis1,
                        type: 'line',
                        name: '政治',
                    },
                    {
                        data: yAxis2,
                        type: 'line',
                        name: '英语',
                    },
                    {
                        data: yAxis3,
                        type: 'line',
                        name: '专业一',
                    },
                    {
                        data: yAxis4,
                        type: 'line',
                        name: '专业二',
                    },
                    ]
                };
                // 使用刚指定的配置项和数据显示图表。
                specialnameChart4.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    specialnameChart4.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog5() {
      this.chartVisiable5 = !this.chartVisiable5;
      this.$nextTick(()=>{

        var specialnameChart5 = echarts.init(document.getElementById("specialnameChart5"),'carp');
        this.$http({
            url: "yuanxiaoxinxi/group/specialname",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].specialname);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].specialname
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '专业类型统计',
                            left: 'center'
                        },
                        legend: {
                          orient: 'vertical',
                          left: 'left'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: ['25%', '55%'],
                                roseType: 'area',
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
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                specialnameChart5.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    specialnameChart5.resize();
                };
            }
        });
      })
    },
    init () {
    },
    search() {
      this.pageIndex = 1;
      this.getDataList();
    },

    // 获取数据列表
    getDataList() {
      this.dataListLoading = true;
      let params = {
        page: this.pageIndex,
        limit: this.pageSize,
        sort: 'id',
        order: 'desc',
      }
           if(this.searchForm.schoolname!='' && this.searchForm.schoolname!=undefined){
            params['schoolname'] = '%' + this.searchForm.schoolname + '%'
          }
           if(this.searchForm.specialname!='' && this.searchForm.specialname!=undefined){
            params['specialname'] = '%' + this.searchForm.specialname + '%'
          }
           if(this.searchForm.typeschool!='' && this.searchForm.typeschool!=undefined){
            params['typeschool'] = '%' + this.searchForm.typeschool + '%'
          }
           if(this.searchForm.degreename!='' && this.searchForm.degreename!=undefined){
            params['degreename'] = '%' + this.searchForm.degreename + '%'
          }
    params['sort'] = 'total';
    params['order'] = 'desc';
			let user = JSON.parse(this.$storage.getObj('userForm'))
			console.log(user)
			this.$http({
				url: "yuanxiaoxinxi/page",
				method: "get",
				params: params
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.dataList = data.data.list;
					this.totalPage = data.data.total;
				} else {
					this.dataList = [];
					this.totalPage = 0;
				}
				this.dataListLoading = false;
			});
    },
    // 每页数
    sizeChangeHandle(val) {
      this.pageSize = val;
      this.pageIndex = 1;
      this.getDataList();
    },
    // 当前页
    currentChangeHandle(val) {
      this.pageIndex = val;
      this.getDataList();
    },
    // 多选
    selectionChangeHandler(val) {
      this.dataListSelections = val;
    },
    // 添加/修改
    addOrUpdateHandler(id,type) {
      this.showFlag = false;
      this.addOrUpdateFlag = true;
      this.crossAddOrUpdateFlag = false;
      if(type!='info'){
        type = 'else';
      }
      this.$nextTick(() => {
        this.$refs.addOrUpdate.init(id,type);
      });
    },
    // 查看评论
    disscussListHandler(id,type) {
	this.$router.push({path:'/discussyuanxiaoxinxi',query:{refid:id}});
    },
    // 下载
    download(file){
      let arr = file.replace(new RegExp('upload/', "g"), "")
      axios.get(this.$base.url + 'file/download?fileName=' + arr, {
      	headers: {
      		token: this.$storage.get('Token')
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
		  axios.get((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] :'') + this.$base.name + '/file/download?fileName=' + arr, {
		  	headers: {
		  		token: this.$storage.get('Token')
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
	// 预览
	preClick(file){
		if(!file){
			return false
		}
		window.open((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] + this.$base.name + '/' + file :this.$base.url + file))
	},
	yuanxiaoxinxistatusChange(e,row){
		if(row.status==0){
			row.passwordwrongnum = 0
		}
		this.$http({
			url:'yuanxiaoxinxi/update',
			method:'post',
			data:row
		}).then(res=>{
			if(row.status==1){
				this.$message.error('该用户已锁定')
			}else{
				this.$message.success('该用户已解除锁定')
			}
		})
	},
    // 删除
    deleteHandler(id ) {
      var ids = id
        ? [Number(id)]
        : this.dataListSelections.map(item => {
            return Number(item.id);
          });
      this.$confirm(`确定进行[${id ? "删除" : "批量删除"}]操作?`, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http({
          url: "yuanxiaoxinxi/delete",
          method: "post",
          data: ids
        }).then(({ data }) => {
          if (data && data.code === 0) {
			this.$message({
			  message: "操作成功",
			  type: "success",
			  duration: 1500,
			  onClose: () => {
			    this.search();
			  }
			});
            
          } else {
            this.$message.error(data.msg);
          }
        });
      });
    },

    spider() {
        this.$message({
              message: "数据爬取中...",
              type: "success",
              duration: 3000,
              onClose: () => {
                this.search();
              }
            });
        this.$http({
          url: "spider/yuanxiaoxinxi",
          method: "get",
        }).then(({ data }) => {
          if (data && data.code === 0) {
            this.$message({
                message: "爬取完成",
                type: "success",
                duration: 1500,
                onClose: () => {
                    this.getDataList(this.roleName);
                }
            });
          } else {
            this.$alert(data.msg)
          }
        });
    },

  }

};
</script>
<style lang="scss" scoped>
	
	.center-form-pv {
	  .el-date-editor.el-input {
	    width: auto;
	  }
	}
	
	.el-input {
	  width: auto;
	}
	
	// form
	.center-form-pv .el-input /deep/ .el-input__inner {
				border: 1px solid #b4b4b4;
				border-radius: 6px;
				padding: 0 12px;
				color: inherit;
				max-width: 180px;
				background: #fff;
				width: auto;
				font-size: 16px;
				height: 40px;
			}
	
	.center-form-pv .el-select /deep/ .el-input__inner {
				border: 1px solid #b4b4b4;
				border-radius: 6px;
				padding: 0 10px;
				box-shadow: 0 0 0px rgba(64, 158, 255, .5);
				outline: none;
				color: inherit;
				background: #fff;
				width: 160px;
				font-size: 16px;
				height: 40px;
			}
	
	.center-form-pv .el-date-editor /deep/ .el-input__inner {
				border: 1px solid #b4b4b4;
				border-radius: 6px;
				padding: 0 10px 0 30px;
				box-shadow: 0 0 0px rgba(64, 158, 255, .5);
				outline: none;
				color: inherit;
				background: #fff;
				width: 170px;
				font-size: 16px;
				height: 40px;
			}
	
	.center-form-pv .search {
				border: 0;
				cursor: pointer;
				border-radius: 6px;
				padding: 0 24px ;
				margin: 0 0 10px;
				color: #fff;
				background: #327e33;
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .search:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .add {
				border: 1px solid #b9c8d2;
				cursor: pointer;
				padding: 4px 10px 0 45px;
				margin: 0px 2px 10px;
				color: #000;
				font-weight: 600;
				display: flex;
				font-size: inherit;
				line-height: 30px;
				border-radius: 4px;
				outline: none;
				background: rgba(255,255,255,.6);
				width: auto;
				align-items: center;
				position: relative;
				min-width: 66px;
				height: auto;
			}
	
	.center-form-pv .actions .add:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .del {
				border: 1px solid #b9c8d2;
				cursor: pointer;
				padding: 4px 10px 0 45px;
				margin: 0px 2px 10px;
				color: #000;
				font-weight: 600;
				font-size: inherit;
				line-height: 30px;
				border-radius: 3px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: rgba(255,255,255,.6);
				width: auto;
				position: relative;
				min-width: 66px;
				height: auto;
			}
	
	.center-form-pv .actions .del:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .statis {
				border: 1px solid #b9c8d2;
				cursor: pointer;
				padding: 4px 10px 0 40px;
				margin: 0px 2px 10px;
				color: #000;
				font-weight: 600;
				font-size: inherit;
				line-height: 30px;
				border-radius: 3px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: rgba(255,255,255,.6);
				width: auto;
				position: relative;
				min-width: 66px;
				height: auto;
			}
	
	.center-form-pv .actions .statis:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .btn18 {
				border: 1px solid #b9c8d2;
				cursor: pointer;
				padding: 4px 10px 0 45px;
				margin: 0px 2px 10px;
				color: #333;
				font-weight: 600;
				font-size: inherit;
				line-height: 30px;
				border-radius: 4px;
				outline: none;
				background: rgba(255,255,255,.6);
				width: auto;
				position: relative;
				min-width: 66px;
				height: 1px solid #b9c8d2;
			}
	
	.center-form-pv .actions .btn18:hover {
				opacity: 0.8;
			}
	
	// table
	.el-table /deep/ .el-table__header-wrapper thead {
				color: inherit;
				background: #dff0d8;
				width: 100%;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th {
				padding: 6px 0;
				background: none;
				border-color: #d2d0d0;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}

	.el-table /deep/ .el-table__header-wrapper thead tr th .cell {
				padding: 0 10px;
				word-wrap: normal;
				white-space: normal;
				font-weight: 600;
				display: flex;
				vertical-align: middle;
				font-size: 13px;
				line-height: 24px;
				text-overflow: ellipsis;
				word-break: break-all;
				width: 100%;
				align-items: center;
				position: relative;
			}

	
	.el-table /deep/ .el-table__body-wrapper tbody {
				padding: 0;
				width: 100%;
			}

	.el-table /deep/ .el-table__body-wrapper tbody tr {
				background: none;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 4px 0 0;
				color: inherit;
				background: none;
				font-size: inherit;
				border-color: #d2d0d0;
				border-width: 0 1px 1px 0px;
				border-style: solid;
				text-align: left;
			}
	
		.el-table /deep/ .el-table__body-wrapper tbody tr.el-table__row--striped td {
		background: rgba(238,238,238,.5);
	}
		
	.el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
				padding: 4px 0 0;
				color: #666;
				background: none;
				border-color: #d2d0d0;
				border-width: 0 1px 1px 0px;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 4px 0 0;
				color: inherit;
				background: none;
				font-size: inherit;
				border-color: #d2d0d0;
				border-width: 0 1px 1px 0px;
				border-style: solid;
				text-align: left;
			}

	.el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
				padding: 0 10px;
				overflow: hidden;
				color: inherit;
				word-break: break-all;
				white-space: normal;
				line-height: 24px;
				text-overflow: ellipsis;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0 2px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view:hover {
				border-color: #23b7e5;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add {
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add:hover {
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0 2px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit:hover {
				border-color: #45B6B0;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0 2px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del:hover {
				border-color: #d9534f;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8 {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0 2px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8:hover {
				border-color: #666;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	// pagination
	.main-content .el-pagination /deep/ .el-pagination__total {
				margin: 0 10px 0 0;
				color: inherit;
				font-weight: 400;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-prev {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: 18px;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-next {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: 18px;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-prev:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #999;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: 18px;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-next:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #999;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: 18px;
				line-height: 28px;
				height: 28px;
			}

	.main-content .el-pagination /deep/ .el-pager {
				padding: 0;
				margin: 0;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
			}

	.main-content .el-pagination /deep/ .el-pager .number {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: auto;
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination /deep/ .el-pager .number:hover {
				cursor: pointer;
				border: 1px solid #ddd;
				padding: 0 4px;
				margin: 0 5px;
				color: #333;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: auto;
				border-radius: 4px;
				background: rgba(255,255,255,.5);
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination /deep/ .el-pager .number.active {
				cursor: default;
				border: 1px solid #ddd;
				padding: 0 4px;
				margin: 0 5px;
				color: #333;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: auto;
				border-radius: 4px;
				background: rgba(255,255,255,.5);
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes {
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input {
				margin: 0 5px;
				color: inherit;
				width: 100px;
				font-size: inherit;
				position: relative;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
				border: 0px solid #ddd;
				cursor: pointer;
				padding: 0 25px 0 8px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: none;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
				top: 0;
				position: absolute;
				right: 0;
				height: 100%;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
				cursor: pointer;
				color: #C0C4CC;
				width: 25px;
				font-size: 14px;
				line-height: 28px;
				text-align: center;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump {
				margin: 0 0 0 24px;
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input {
				border-radius: 3px;
				padding: 0 2px;
				margin: 0 2px;
				color: inherit;
				display: inline-block;
				width: 50px;
				font-size: inherit;
				line-height: 18px;
				position: relative;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
				border: 1px solid #eee;
				cursor: pointer;
				padding: 0 0px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 24px;
				border-radius: 3px;
				outline: 0;
				background: #fff;
				width: auto;
				text-align: center;
				height: 24px;
			}
	
	// list one
	.one .list1-view {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0px 5px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: double;
				min-width: 40px;
				height: 24px;
			}
	
	.one .list1-view:hover {
				border-color: #23b7e5;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.one .list1-edit {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0px 5px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: double;
				min-width: 40px;
				height: 24px;
			}
	
	.one .list1-edit:hover {
				border-color: #45B6B0;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.one .list1-del {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0px 5px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.one .list1-del:hover {
				border-color: #d9534f;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.one .list1-btn8 {
				cursor: pointer;
				padding: 0 8px 0 30px;
				margin: 0px 5px 5px 0;
				color: #333;
				font-size: inherit;
				border-color: #fff;
				line-height: 24px;
				border-radius: 20px;
				box-shadow: inset 0px 0px 0px 0px rgba(244,100,130,.3);
				outline: none;
				background: none;
				width: auto;
				border-width: 0px;
				position: relative;
				border-style: solid;
				min-width: 40px;
				height: 24px;
			}
	
	.one .list1-btn8:hover {
				border-color: #333;
				border-width: 0px;
				opacity: 0.8;
				border-style: solid;
			}
	
	.main-content .el-table .el-switch {
				display: inline-flex;
				vertical-align: middle;
				line-height: 30px;
				position: relative;
				align-items: center;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__label--left {
				cursor: pointer;
				margin: 0 10px 0 0;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__label--right {
				cursor: pointer;
				margin: 0 0 0 10px;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__core {
				border: 1px solid #dff0d8;
				cursor: pointer;
				border-radius: 15px;
				margin: 0;
				outline: 0;
				background: #dff0d8;
				display: inline-block;
				width: 55px;
				box-sizing: border-box;
				transition: border-color .3s,background-color .3s;
				height: 26px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__core::after {
				border-radius: 100%;
				top: 1px;
				left: 1px;
				background: #fff;
				width: 22px;
				position: absolute;
				transition: all .3s;
				height: 22px;
			}
	.main-content .el-table .el-switch.is-checked /deep/ .el-switch__core::after {
				margin: 0 0 0 -27px;
				left: 100%;
			}
	
	.main-content .el-table .el-rate /deep/ .el-rate__item {
				cursor: pointer;
				display: inline-block;
				vertical-align: middle;
				font-size: 0;
				position: relative;
			}
	.main-content .el-table .el-rate /deep/ .el-rate__item .el-rate__icon {
				margin: 0 3px;
				color: #666;
				display: inline-block;
				font-size: 18px;
				position: relative;
				transition: .3s;
			}
</style>
