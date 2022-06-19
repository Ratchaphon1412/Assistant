export const categoryMap = {"category":{"/":{"path":"/category/","map":{"Guide":{"path":"/category/guide/","keys":["v-4eaf9f84","v-fffb8e28","v-4c863446","v-bf720700","v-0978b044"]}}}},"tag":{"/":{"path":"/tag/","map":{"disable":{"path":"/tag/disable/","keys":["v-4c863446"]},"encryption":{"path":"/tag/encryption/","keys":["v-bf720700"]},"Markdown":{"path":"/tag/markdown/","keys":["v-0978b044"]},"Page config":{"path":"/tag/page-config/","keys":["v-4eaf9f84"]},"Guide":{"path":"/tag/guide/","keys":["v-4eaf9f84"]}}}}}

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateBlogCategory) {
    __VUE_HMR_RUNTIME__.updateBlogCategory(categoryMap)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ categoryMap }) => {
    __VUE_HMR_RUNTIME__.updateBlogCategory(categoryMap)
  })
}
