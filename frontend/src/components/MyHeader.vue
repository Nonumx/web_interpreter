<template>
  <n-layout-header bordered class="h-16 px-8 flex items-center">
    <n-icon :component="Flow20Regular" size="40" class="mr-3" />
    <n-text class="text-lg">←图标</n-text>
    <n-button text>
      <router-link to="/"> 首页 </router-link>
    </n-button>
    <n-button text> 随便取 </n-button>
    <n-button text> 个菜单 </n-button>
    <n-badge
      @click="
        () => {
          notificationDrawerActive = true
        }
      "
      :value="notificationSize"
    >
      <n-avatar>用户</n-avatar>
    </n-badge>
  </n-layout-header>
  <n-drawer v-model:show="notificationDrawerActive" :width="502" placement="right">
    <n-drawer-content title="通知管理">
      <n-text class="py-16 block text-center text-lg text-slate-600" v-if="notificationSize == 0"
        >没有新通知</n-text
      >
    </n-drawer-content>
  </n-drawer>
</template>

<script setup lang="ts">
import { Flow20Regular } from '@vicons/fluent'
import {
  NLayoutHeader,
  NText,
  NButton,
  NIcon,
  NBadge,
  NAvatar,
  NDrawer,
  NDrawerContent
} from 'naive-ui'
import { ref } from 'vue'

const notificationDrawerActive = ref(false)
const notificationSize = ref(0)
</script>
