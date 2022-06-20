export const categoryMap = {"category":{"/":{"path":"/category/","map":{"Guide":{"path":"/category/guide/","keys":["v-0e0ab8a0"]}}},"/en":{"path":"/encategory/","map":{}},"/th":{"path":"/thcategory/","map":{}}},"tag":{"/":{"path":"/tag/","map":{"encryption":{"path":"/tag/encryption/","keys":["v-0e0ab8a0"]}}},"/en":{"path":"/entag/","map":{}},"/th":{"path":"/thtag/","map":{}}}}

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
