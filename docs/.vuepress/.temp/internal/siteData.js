export const siteData = JSON.parse("{\"base\":\"/\",\"lang\":\"en-US\",\"title\":\"\",\"description\":\"\",\"head\":[],\"locales\":{\"/en\":{\"lang\":\"en-US\",\"title\":\"E.D.I.T.H Assistants\",\"description\":\"A demo for vuepress-theme-hope\"},\"/th\":{\"lang\":\"zh-CN\",\"title\":\"E.D.I.T.H Assistants\",\"description\":\"vuepress-theme-hope 的演示\"}}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateSiteData) {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ siteData }) => {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  })
}
