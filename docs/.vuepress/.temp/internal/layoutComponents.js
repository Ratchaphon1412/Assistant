import { defineAsyncComponent } from 'vue'

export const layoutComponents = {
  "404": defineAsyncComponent(() => import("/Users/ratchaphonhinsui/Desktop/Assistant /docs/node_modules/vuepress-theme-hope/lib/client/layouts/404.js")),
  "Layout": defineAsyncComponent(() => import("/Users/ratchaphonhinsui/Desktop/Assistant /docs/node_modules/vuepress-theme-hope/lib/client/layouts/Layout.js")),
  "Slide": defineAsyncComponent(() => import("/Users/ratchaphonhinsui/Desktop/Assistant /docs/node_modules/vuepress-theme-hope/lib/client/layouts/Slide.js")),
}
