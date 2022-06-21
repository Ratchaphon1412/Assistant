import { useScriptTag } from "/Users/ratchaphonhinsui/Desktop/Assistant/docs/node_modules/vuepress-plugin-components/lib/client/composables";
import { h } from "vue";
import { defineClientConfig } from "@vuepress/client";
import Badge from "/Users/ratchaphonhinsui/Desktop/Assistant/docs/node_modules/vuepress-plugin-components/lib/client/components/Badge";
import FontIcon from "/Users/ratchaphonhinsui/Desktop/Assistant/docs/node_modules/vuepress-plugin-components/lib/client/components/FontIcon";
import BackToTop from "/Users/ratchaphonhinsui/Desktop/Assistant/docs/node_modules/vuepress-plugin-components/lib/client/components/BackToTop";


export default defineClientConfig({
  enhance: ({ app }) => {
    app.component("Badge", Badge);
    app.component("FontIcon", FontIcon);
    
  },
  setup: () => {
    useScriptTag(`https://kit.fontawesome.com/ca37c296c5.js`);
    
  },
  rootComponents: [
    () => h(BackToTop, { threshold: 300 }),
    
  ],
});