export const typeMap = {"article":{"/":{"path":"/article/","keys":["v-0e0ab8a0"]},"/en":{"path":"/enarticle/","keys":[]},"/th":{"path":"/tharticle/","keys":["v-b2163d80","v-0f7d2360","v-d2006416"]}},"encrypted":{"/":{"path":"/encrypted/","keys":[]},"/en":{"path":"/enencrypted/","keys":[]},"/th":{"path":"/thencrypted/","keys":[]}},"slide":{"/":{"path":"/slide/","keys":[]},"/en":{"path":"/enslide/","keys":[]},"/th":{"path":"/thslide/","keys":[]}},"star":{"/":{"path":"/star/","keys":[]},"/en":{"path":"/enstar/","keys":[]},"/th":{"path":"/thstar/","keys":[]}},"timeline":{"/":{"path":"/timeline/","keys":[]},"/en":{"path":"/entimeline/","keys":[]},"/th":{"path":"/thtimeline/","keys":[]}}}

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
