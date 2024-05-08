<template>
    <div id="cesiumContainer"></div>

  <el-card class="box-card">
    <div>
      城市选择：
      <el-radio-group v-model="radio">
        <el-radio :value="0">成都</el-radio>
        <el-radio :value="1">西安</el-radio>
        <el-radio :value="2">Porto</el-radio>
      </el-radio-group>
    </div>
    <div style="margin-top: 10px">
      算法选择：
      <el-radio-group v-model="radio1">
        <el-radio :value="0">DTW</el-radio>
        <el-radio :value="1">EDR</el-radio>
        <el-radio :value="2">ERP</el-radio>
      </el-radio-group>
    </div>
    <div style="margin-top: 10px" class="slider-demo-block">
      <span class="demonstration">设置返回TOPK条数</span>
      <el-slider max="1000" v-model="value1" />
    </div>
    <div style="margin-top: 10px">
      <el-select-v2 v-model="value" :options="options" placeholder="请选择查询轨迹" size="large" style="width: 240px" />
    </div>

    <div style="text-align: center; margin-top: 10px"><el-button type="primary" style="text-align: center" @click="fetchResults">查询</el-button></div>
  </el-card>
</template>

<script setup>
import 'cesium/Build/Cesium/Widgets/widgets.css'
import { onMounted, ref, watch } from 'vue'
import * as Cesium from 'cesium'
import axios from 'axios'
const value1 = ref(10)
const radio = ref(0)
const radio1 = ref(0)
const value = ref()
const city = ['chengdu', 'xian', 'porto']
const alg = ['dtw', 'edr', 'erp']
let viewer = null
const options = Array.from({ length: 2000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `轨迹编号 ${idx + 1}`
}))
Cesium.Ion.defaultAccessToken =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3YmU2ODc2Zi1lNDNkLTQ4ZTItYjU2OC03NDZkMDU4ZmQyY2QiLCJpZCI6OTI3OTYsImlhdCI6MTY1MTkzNzEyNX0.MPjw3IclN7R29pv1bE9vsBjxxA7pMbqMBEZSGrm-jVo'
const fetchResults = async () => {
  viewer.entities.removeAll()
  let response = null
  let responseData = null
  const url = 'http://localhost:8000/api/results/'
  const params = {
    city: city[radio.value],
    alg: alg[radio1.value],
    query_id: value.value,
    limit: value1.value
  }

  try {
    response = await axios.get(url, { params })
    console.log(response.data) // 处理响应数据
  } catch (error) {
    console.error('Error fetching data:', error)
  }
  responseData = response.data

  // 解析查询轨迹
  const queryTrajectory = JSON.parse(responseData.querytrajectory.trajectory)
  console.log(queryTrajectory)
  const queryPositions = queryTrajectory.map((coord) => Cesium.Cartesian3.fromDegrees(coord.lng, coord.lat))
  console.log(queryPositions)
  // 添加查询轨迹到 Cesium
  viewer.entities.add({
    polyline: {
      positions: queryPositions,
      width: 5,
      material: Cesium.Color.BLUE // 查询轨迹使用蓝色
    }
  })

  // 处理结果轨迹
  responseData.final_results.forEach((result, index) => {
    const positions = result.map((coord) => Cesium.Cartesian3.fromDegrees(coord.lng, coord.lat))
    const color = Cesium.Color.fromRandom({ alpha: 1.0 }) // 随机颜色，全透明度
    if (positions.length < 2) {
      viewer.entities.add({
        position: positions,
        point: {
          pixelSize: 10, // 点的大小
          color: Cesium.Color.RED, // 点的颜色
          outlineColor: Cesium.Color.WHITE, // 点的轮廓颜色
          outlineWidth: 2 // 点的轮廓宽度
        }
      })
    } else {
      viewer.entities.add({
        polyline: {
          positions: positions,
          width: 5,
          material: color
        }
      })
    }
  })
  // 视角定位到第一个点
  viewer.camera.flyTo({
    destination: Cesium.Cartesian3.fromDegrees(queryTrajectory[0].lng, queryTrajectory[0].lat, 3000)
  })
}
onMounted(() => {
  viewer = new Cesium.Viewer('cesiumContainer', {
    baseLayerPicker: false, // 移除底图选择器
    geocoder: false, // 移除地理编码器
    homeButton: false, // 移除Home按钮
    sceneModePicker: false, // 移除场景模式选择器
    navigationHelpButton: false, // 移除导航帮助按钮
    fullscreenButton: false, // 移除全屏按钮
    animation: false, // 移除动画控件
    timeline: false, // 移除时间线
    vrButton: false, // 移除VR按钮
    creditContainer: undefined, // 移除版权信息
    imageryProvider: new Cesium.UrlTemplateImageryProvider({
      url: 'https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}',
      credit: 'Google Maps'
    })
    // 定位到四川省的中心
  })
  viewer.cesiumWidget.creditContainer.style.display = 'none'
  // 设置相机初始视图到成都
  viewer.camera.setView({
    destination: Cesium.Cartesian3.fromDegrees(104.066, 30.657, 10000), // 经度、纬度、高度(单位: 米)
    orientation: {
      heading: Cesium.Math.toRadians(0), // 方向
      pitch: Cesium.Math.toRadians(-90), // 俯仰角，-90度表示向下看
      roll: 0 // 翻滚
    }
  })
})
watch(radio, (newVal) => {
  if (viewer) {
    switch (newVal) {
      case 0: // 成都
        flyToCity(104.066, 30.657)
        break
      case 1: // 西安
        flyToCity(108.94, 34.341)
        break
      case 2: // Porto
        flyToCity(-8.61099, 41.14961)
        break
      default:
        break
    }
  }
})
function flyToCity(longitude, latitude) {
  viewer.camera.flyTo({
    destination: Cesium.Cartesian3.fromDegrees(longitude, latitude, 5000),
    duration: 2
  })
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-card {
  position: absolute;
  top: 20px; /* 可调整为需要的位置 */
  right: 20px; /* 可调整为需要的位置 */
  width: 400px;
  background: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 5px;
  z-index: 1000; /* 确保它位于 Cesium 容器之上 */
}
#cesiumContainer {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>
