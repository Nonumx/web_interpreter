<template>
  <n-layout>
    <n-layout-content>
      <div class="mx-auto px-6 py-8 my-4 shadow-lg rounded-lg" style="width: 640px">
        <n-h2>{{ title }}</n-h2>
        <n-text tag="div">{{ filename }}</n-text>
        <n-text tag="div">{{ description }}</n-text>
        <n-code :code="codeContent" language="python" show-line-numbers />
        <n-data-table :columns="columns" :data="data" />
        <n-divider />
        <n-flex class="pt-4">
          <n-upload class="w-auto">
            <n-button>上传算法</n-button>
          </n-upload>
          <n-button>浏览代码</n-button>
          <n-button>开始计算</n-button>
          <n-button>查看队列</n-button>
        </n-flex>
      </div>
    </n-layout-content>
  </n-layout>
</template>

<script setup lang="ts">
import {
  NLayout,
  NLayoutContent,
  NText,
  NH2,
  NCode,
  NUpload,
  NButton,
  NInput,
  NDataTable,
  NDivider,
  NFlex
} from 'naive-ui'
import type { DataTableColumns } from 'naive-ui'
import { h, reactive, ref } from 'vue'

interface RowData {
  key: number
  name: string
  type: string
  value: string
}

const data: RowData[] = reactive([])
const columns: DataTableColumns<RowData> = [
  {
    key: 'name',
    title: '参数名称'
  },
  {
    key: 'type',
    title: '类型'
  },
  {
    key: 'value',
    title: '值',
    render(row, index) {
      return h(NInput, {
        value: row.value,
        onUpdateValue(v) {
          data[index].value = v
        }
      })
    }
  }
]

const title = ref('')
const filename = ref('')
const description = ref('')
const codeContent = ref('')

const baseURL = 'http://127.0.0.1:8000'

const init = () => {
  fetch(`${baseURL}/api/v1/algorithm-info`)
    .then((response) => response.json())
    .then((data1) => {
      title.value = data1['title']
      filename.value = data1['filename']
      description.value = data1['description']
      for (let i = 0; i < data1['arguments'].length; i++) {
        const argx = data1['arguments'][i]
        data.push({
          key: i,
          name: argx['name'],
          type: argx['type'],
          value: argx['value']
        })
      }
    })
    .catch((error) => console.log(error))
}
init()
</script>
