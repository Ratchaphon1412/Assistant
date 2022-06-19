export const typeMap = {"article":{"/":{"path":"/article/","keys":["v-4eaf9f84","v-184f4da6","v-0e503981","v-fffb8e28","v-4c863446","v-bf720700","v-0978b044"]}},"encrypted":{"/":{"path":"/encrypted/","keys":["v-bf720700"]}},"slide":{"/":{"path":"/slide/","keys":["v-0e503981"]}},"star":{"/":{"path":"/star/","keys":["v-4eaf9f84"]}},"timeline":{"/":{"path":"/timeline/","keys":["v-4eaf9f84"]}}}

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateBlogType) {
    __VUE_HMR_RUNTIME__.updateBlogType(typeMap)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ typeMap }) => {
    __VUE_HMR_RUNTIME__.updateBlogType(typeMap)
  })
}
