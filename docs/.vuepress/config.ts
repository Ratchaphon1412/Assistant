import { defineUserConfig } from "vuepress";
const { docsearchPlugin } = require('@vuepress/plugin-docsearch')
import theme from "./theme";

export default defineUserConfig({
  lang: "en-US",
  title: "Assistants",
  description: "A demo for vuepress-theme-hope",

  base: "/",
 
  theme,
  plugins:[
    docsearchPlugin({
      // options
      //TODO 
    }),
    

  ]

});
