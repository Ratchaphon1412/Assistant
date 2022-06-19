export const categoryMap = {"category":{"/":{"path":"/category/","map":{}},"/en":{"path":"/encategory/","map":{}},"/th":{"path":"/thcategory/","map":{}}},"tag":{"/":{"path":"/tag/","map":{}},"/en":{"path":"/entag/","map":{}},"/th":{"path":"/thtag/","map":{}}}}

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
