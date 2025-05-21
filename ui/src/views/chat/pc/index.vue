<template>
  <div
    class="chat-pc layout-bg"
    :class="classObj"
    v-loading="loading"
    :style="{
      '--el-color-primary': applicationDetail?.custom_theme?.theme_color,
      '--el-color-primary-light-9': hexToRgba(applicationDetail?.custom_theme?.theme_color, 0.1)
    }"
  >
    <div class="chat-pc__header" :style="customStyle">
      <div class="flex align-center">
        <div class="mr-12 ml-24 flex">
          <AppAvatar
            v-if="isAppIcon(applicationDetail?.icon)"
            shape="square"
            :size="32"
            style="background: none"
          >
            <img :src="applicationDetail?.icon" alt="" />
          </AppAvatar>
          <AppAvatar
            v-else-if="applicationDetail?.name"
            :name="applicationDetail?.name"
            pinyinColor
            shape="square"
            :size="32"
          />
        </div>
        <h4>{{ applicationDetail?.name }}</h4>
      </div>
    </div>
    <div class="chat-pc__main">
      <div class="chat-pc__container">
        <div class="chat-pc__left">
          <div class="left-content">
            <div class="p-24 pb-0">
              <el-button class="add-button w-full primary" @click="newChat">
                <el-icon><Plus /></el-icon>
                <span class="ml-4">{{ $t('chat.createChat') }}</span>
              </el-button>
              <p class="mt-20 mb-8">{{ $t('chat.history') }}</p>
            </div>
            <div class="left-list">
              <el-scrollbar>
                <div class="p-8 pt-0">
                  <common-list
                    :style="{
                      '--el-color-primary': applicationDetail?.custom_theme?.theme_color,
                      '--el-color-primary-light-9': hexToRgba(
                        applicationDetail?.custom_theme?.theme_color,
                        0.1
                      )
                    }"
                    :data="chatLogData"
                    class="mt-8"
                    v-loading="left_loading"
                    :defaultActive="currentChatId"
                    @click="clickListHandle"
                    @mouseenter="mouseenter"
                    @mouseleave="mouseId = ''"
                  >
                    <template #default="{ row }">
                      <div class="flex-between">
                        <auto-tooltip :content="row.abstract">
                          {{ row.abstract }}
                        </auto-tooltip>
                        <div @click.stop v-show="mouseId === row.id && row.id !== 'new'">
                          <el-dropdown trigger="click" :teleported="false">
                            <el-icon class="rotate-90 mt-4"><MoreFilled /></el-icon>
                            <template #dropdown>
                              <el-dropdown-menu>
                                <el-dropdown-item @click.stop="editLogTitle(row)">
                                  <el-icon><EditPen /></el-icon>
                                  {{ $t('common.edit') }}
                                </el-dropdown-item>
                                <el-dropdown-item @click.stop="deleteLog(row)">
                                  <el-icon><Delete /></el-icon>
                                  {{ $t('common.delete') }}
                                </el-dropdown-item>
                              </el-dropdown-menu>
                            </template>
                          </el-dropdown>
                        </div>
                      </div>
                    </template>

                    <template #empty>
                      <div class="text-center">
                        <el-text type="info">{{ $t('chat.noHistory') }}</el-text>
                      </div>
                    </template>
                  </common-list>
                </div>
                <div v-if="chatLogData?.length" class="gradient-divider lighter mt-8">
                  <span>{{ $t('chat.only20history') }}</span>
                </div>
              </el-scrollbar>
            </div>
          </div>
        </div>
        <div class="chat-pc__code-editor">
          <div class="code-editor-header">
            <div class="flex align-center justify-between">
              <div class="flex align-center">
                <el-select v-model="selectedLanguage" class="mr-16" style="width: 120px">
                  <el-option
                    v-for="lang in supportedLanguages"
                    :key="lang.value"
                    :label="lang.label"
                    :value="lang.value"
                  />
                </el-select>
              </div>
              <el-button type="primary" @click="runCode" :loading="running">
                <el-icon><VideoPlay /></el-icon>
                <span class="ml-4">运行代码</span>
              </el-button>
            </div>
          </div>
          <div class="code-editor-content">
            <monaco-editor
              v-model="code"
              :language="selectedLanguage"
              :options="editorOptions"
              @change="onCodeChange"
            />
          </div>
          <div class="code-output" v-if="output">
            <div class="output-header">
              <h4>运行结果</h4>
              <el-button type="text" @click="clearOutput">
                <el-icon><Delete /></el-icon>
                <span class="ml-4">清除</span>
              </el-button>
            </div>
            <div class="output-content">
              <pre>{{ output }}</pre>
            </div>
          </div>
        </div>
        <div class="chat-pc__right">
          <div class="right-header">
            <h4 class="ellipsis-1" style="width: 66%">
              {{ currentChatName }}
            </h4>
            <span class="flex align-center" v-if="currentRecordList.length">
              <AppIcon
                v-if="paginationConfig.total"
                iconName="app-chat-record"
                class="info mr-8"
                style="font-size: 16px"
              ></AppIcon>
              <span v-if="paginationConfig.total" class="lighter">
                {{ paginationConfig.total }} {{ $t('chat.question_count') }}
              </span>
              <el-dropdown class="ml-8">
                <AppIcon
                  iconName="app-export"
                  class="cursor"
                  :title="$t('chat.exportRecords')"
                ></AppIcon>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item @click="exportMarkdown"
                      >{{ $t('common.export') }} Markdown</el-dropdown-item
                    >
                    <el-dropdown-item @click="exportHTML"
                      >{{ $t('common.export') }} HTML</el-dropdown-item
                    >
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </span>
          </div>
          <div class="right-content">
            <AiChat
              ref="AiChatRef"
              v-model:applicationDetails="applicationDetail"
              :available="applicationAvailable"
              type="ai-chat"
              :appId="applicationDetail?.id"
              :record="currentRecordList"
              :chatId="currentChatId"
              @refresh="refresh"
              @scroll="handleScroll"
            >
            </AiChat>
          </div>
        </div>
      </div>
    </div>
    <EditTitleDialog ref="EditTitleDialogRef" @refresh="refreshFieldTitle" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick, computed } from 'vue'
import { marked } from 'marked'
import { saveAs } from 'file-saver'
import { isAppIcon } from '@/utils/application'
import useStore from '@/stores'
import useResize from '@/layout/hooks/useResize'
import { hexToRgba } from '@/utils/theme'
import EditTitleDialog from './EditTitleDialog.vue'
import { t } from '@/locales'
import MonacoEditor from '@/components/MonacoEditor.vue'
import { VideoPlay, Delete } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

useResize()

const { user, log, common } = useStore()

const EditTitleDialogRef = ref()

const isCollapse = ref(false)

const customStyle = computed(() => {
  return {
    background: applicationDetail.value?.custom_theme?.theme_color,
    color: applicationDetail.value?.custom_theme?.header_font_color
  }
})

const classObj = computed(() => {
  return {
    mobile: common.isMobile(),
    hideLeft: !isCollapse.value,
    openLeft: isCollapse.value
  }
})

const newObj = {
  id: 'new',
  abstract: t('chat.createChat')
}
const props = defineProps<{
  application_profile: any
  applicationAvailable: boolean
}>()
const AiChatRef = ref()
const loading = ref(false)
const left_loading = ref(false)

const applicationDetail = computed({
  get: () => {
    return props.application_profile
  },
  set: (v) => {}
})

const chatLogData = ref<any[]>([])

const paginationConfig = ref({
  current_page: 1,
  page_size: 20,
  total: 0
})

const currentRecordList = ref<any>([])
const currentChatId = ref('new') // 当前历史记录Id 默认为'new'
const currentChatName = ref(t('chat.createChat'))
const mouseId = ref('')

// 代码编辑器相关
const code = ref('')
const output = ref('')
const running = ref(false)
const selectedLanguage = ref('python')

const supportedLanguages = [
  { label: 'Python', value: 'python' },
  { label: 'Java', value: 'java' },
  { label: 'C++', value: 'cpp' },
  { label: 'JavaScript', value: 'javascript' },
  { label: 'TypeScript', value: 'typescript' }
]

const editorOptions = {
  theme: 'vs-dark',
  fontSize: 14,
  minimap: { enabled: false },
  scrollBeyondLastLine: false,
  automaticLayout: true
}

const onCodeChange = (value: string) => {
  code.value = value
}

const clearOutput = () => {
  output.value = ''
}

const runCode = async () => {
  if (!code.value.trim()) {
    ElMessage.warning('请输入代码')
    return
  }
  
  running.value = true
  try {
    // 根据选择的语言设置 Piston 的语言
    const languageMap: { [key: string]: string } = {
      'python': 'python',
      'java': 'java',
      'cpp': 'cpp',
      'javascript': 'javascript',
      'typescript': 'typescript'
    }

    const language = languageMap[selectedLanguage.value]
    if (!language) {
      throw new Error('不支持该编程语言')
    }

    // 使用 Piston API
    const response = await fetch('https://emkc.org/api/v2/piston/execute', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        language: language,
        version: '*',
        files: [
          {
            name: `main.${language === 'python' ? 'py' : language === 'javascript' ? 'js' : language === 'typescript' ? 'ts' : language === 'java' ? 'java' : 'cpp'}`,
            content: code.value
          }
        ],
        stdin: '',
        args: []
      })
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const result = await response.json()
    console.log('API 返回结果:', result)

    if (result.run) {
      if (result.run.stderr) {
        output.value = `错误: ${result.run.stderr}`
        ElMessage.error('代码执行出错')
      } else if (result.run.stdout) {
        output.value = result.run.stdout
        ElMessage.success('代码执行成功')
      } else {
        output.value = '代码执行成功，但没有输出'
        ElMessage.warning('代码执行成功，但没有输出')
      }
    } else {
      throw new Error('执行结果格式错误')
    }
  } catch (error: any) {
    console.error('运行代码出错:', error)
    output.value = `运行出错: ${error.message || '未知错误'}`
    ElMessage.error('运行代码时发生错误')
  } finally {
    running.value = false
  }
}

function mouseenter(row: any) {
  mouseId.value = row.id
}

function editLogTitle(row: any) {
  EditTitleDialogRef.value.open(row, applicationDetail.value.id)
}
function refreshFieldTitle(chatId: string, abstract: string) {
  const find = chatLogData.value.find((item: any) => item.id == chatId)
  if (find) {
    find.abstract = abstract
  }
}
function deleteLog(row: any) {
  log.asyncDelChatClientLog(applicationDetail.value.id, row.id, left_loading).then(() => {
    if (currentChatId.value === row.id) {
      currentChatId.value = 'new'
      currentChatName.value = t('chat.createChat')
      paginationConfig.value.current_page = 1
      paginationConfig.value.total = 0
      currentRecordList.value = []
    }
    getChatLog(applicationDetail.value.id)
  })
}

function handleScroll(event: any) {
  if (
    currentChatId.value !== 'new' &&
    event.scrollTop === 0 &&
    paginationConfig.value.total > currentRecordList.value.length
  ) {
    const history_height = event.dialogScrollbar.offsetHeight
    paginationConfig.value.current_page += 1
    getChatRecord().then(() => {
      event.scrollDiv.setScrollTop(event.dialogScrollbar.offsetHeight - history_height)
    })
  }
}

function newChat() {
  if (!chatLogData.value.some((v) => v.id === 'new')) {
    paginationConfig.value.current_page = 1
    paginationConfig.value.total = 0
    currentRecordList.value = []
    chatLogData.value.unshift(newObj)
  } else {
    paginationConfig.value.current_page = 1
    paginationConfig.value.total = 0
    currentRecordList.value = []
  }
  currentChatId.value = 'new'
  currentChatName.value = t('chat.createChat')
  if (common.isMobile()) {
    isCollapse.value = false
  }
}

function getChatLog(id: string, refresh?: boolean) {
  const page = {
    current_page: 1,
    page_size: 20
  }

  log.asyncGetChatLogClient(id, page, left_loading).then((res: any) => {
    chatLogData.value = res.data.records
    if (refresh) {
      currentChatName.value = chatLogData.value?.[0]?.abstract
    } else {
      paginationConfig.value.current_page = 1
      paginationConfig.value.total = 0
      currentRecordList.value = []
      currentChatId.value = chatLogData.value?.[0]?.id || 'new'
      currentChatName.value = chatLogData.value?.[0]?.abstract || t('chat.createChat')
      if (currentChatId.value !== 'new') {
        getChatRecord()
      }
    }
  })
}

function getChatRecord() {
  return log
    .asyncChatRecordLog(
      applicationDetail.value.id,
      currentChatId.value,
      paginationConfig.value,
      loading,
      false
    )
    .then((res: any) => {
      paginationConfig.value.total = res.data.total
      const list = res.data.records
      list.map((v: any) => {
        v['write_ed'] = true
        v['record_id'] = v.id
      })
      currentRecordList.value = [...list, ...currentRecordList.value].sort((a, b) =>
        a.create_time.localeCompare(b.create_time)
      )
      if (paginationConfig.value.current_page === 1) {
        nextTick(() => {
          // 将滚动条滚动到最下面
          AiChatRef.value.setScrollBottom()
        })
      }
    })
}

const clickListHandle = (item: any) => {
  if (item.id !== currentChatId.value) {
    paginationConfig.value.current_page = 1
    paginationConfig.value.total = 0
    currentRecordList.value = []
    currentChatId.value = item.id
    currentChatName.value = item.abstract
    if (currentChatId.value !== 'new') {
      getChatRecord()

      // 切换对话后，取消暂停的浏览器播放
      if (window.speechSynthesis.paused && window.speechSynthesis.speaking) {
        window.speechSynthesis.resume()
        nextTick(() => {
          window.speechSynthesis.cancel()
        })
      }
    }
  }
  if (common.isMobile()) {
    isCollapse.value = false
  }
}

function refresh(id: string) {
  getChatLog(applicationDetail.value.id, true)
  currentChatId.value = id
}

async function exportMarkdown(): Promise<void> {
  const suggestedName: string = `${currentChatId.value}.md`
  const markdownContent: string = currentRecordList.value
    .map((record: any) => `# ${record.problem_text}\n\n${record.answer_text}\n\n`)
    .join('\n')

  const blob: Blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8' })
  saveAs(blob, suggestedName)
}

async function exportHTML(): Promise<void> {
  const suggestedName: string = `${currentChatId.value}.html`
  const markdownContent: string = currentRecordList.value
    .map((record: any) => `# ${record.problem_text}\n\n${record.answer_text}\n\n`)
    .join('\n')
  const htmlContent: any = marked(markdownContent)

  const blob: Blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' })
  saveAs(blob, suggestedName)
}

/**
 *初始化历史对话记录
 */
const init = () => {
  if (
    (applicationDetail.value.show_history || !user.isEnterprise()) &&
    props.applicationAvailable
  ) {
    getChatLog(applicationDetail.value.id)
  }
}
onMounted(() => {
  init()
})
</script>
<style lang="scss">
.chat-pc {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--app-bg-color);

  &__header {
    height: var(--app-header-height);
    background: var(--app-header-bg-color);
    border-bottom: 1px solid var(--el-border-color);
    flex-shrink: 0;
  }

  &__main {
    flex: 1;
    overflow: hidden;
    position: relative;
  }

  &__container {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
  }

  &__left {
    width: 280px;
    background: #fff;
    border-right: 1px solid var(--el-border-color);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;

    .left-content {
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    .left-list {
      flex: 1;
      overflow: hidden;
    }
  }

  &__code-editor {
    width: 400px;
    background: #fff;
    border-right: 1px solid var(--el-border-color);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;

    .code-editor-header {
      padding: 16px;
      border-bottom: 1px solid var(--el-border-color);
      flex-shrink: 0;
    }

    .code-editor-content {
      flex: 1;
      overflow: hidden;
      position: relative;
    }

    .code-output {
      height: 200px;
      border-top: 1px solid var(--el-border-color);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;

      .output-header {
        padding: 12px 16px;
        border-bottom: 1px solid var(--el-border-color);
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #f5f7fa;

        h4 {
          margin: 0;
          font-size: 14px;
        }
      }

      .output-content {
        flex: 1;
        overflow: auto;
        padding: 16px;

        pre {
          margin: 0;
          white-space: pre-wrap;
          word-wrap: break-word;
        }
      }
    }
  }

  &__right {
    flex: 1;
    background: #fff;
    display: flex;
    flex-direction: column;
    min-width: 0;

    .right-header {
      padding: 16px;
      border-bottom: 1px solid var(--el-border-color);
      flex-shrink: 0;
    }

    .right-content {
      flex: 1;
      overflow: hidden;
      position: relative;
    }
  }

  .gradient-divider {
    position: relative;
    text-align: center;
    color: var(--el-color-info);

    ::before {
      content: '';
      width: 17%;
      height: 1px;
      background: linear-gradient(90deg, rgba(222, 224, 227, 0) 0%, #dee0e3 100%);
      position: absolute;
      left: 16px;
      top: 50%;
    }

    ::after {
      content: '';
      width: 17%;
      height: 1px;
      background: linear-gradient(90deg, #dee0e3 0%, rgba(222, 224, 227, 0) 100%);
      position: absolute;
      right: 16px;
      top: 50%;
    }
  }

  .collapse {
    display: none;
  }
}

// 移动端适配
.mobile {
  .chat-pc {
    &__container {
      flex-direction: column;
    }

    &__left {
      width: 100%;
      height: 100%;
      display: none;

      &.show {
        display: flex;
      }
    }

    &__code-editor {
      width: 100%;
      height: 100%;
      display: none;

      &.show {
        display: flex;
      }
    }

    &__right {
      width: 100%;
      height: 100%;
    }
  }
  .collapse {
    display: block;
    position: fixed;
    bottom: 90px;
    z-index: 99;
  }
  &.openLeft {
    .chat-pc {
      &__left {
        display: block;
        position: fixed;
        width: 100%;
        z-index: 99;
        height: calc(100vh - var(--app-header-height));
      }
    }
    .collapse {
      display: block;
      position: absolute;
      bottom: 90px;
      right: 0;
      z-index: 99;
    }
  }
}

.chat-width {
  max-width: 80%;
  margin: 0 auto;
}
@media only screen and (max-width: 1000px) {
  .chat-width {
    max-width: 100% !important;
    margin: 0 auto;
  }
}
</style>
