import { defineUserConfig } from "vuepress";
import theme from "./theme";

export default defineUserConfig({
  base: "/",

  locales: {
    "/en": {
      lang: "en-US",
      title: "E.D.I.T.H Assistants",
      description: "A demo for vuepress-theme-hope",
    },
    "/th": {
      lang: "zh-CN",
      title: "E.D.I.T.H Assistants",
      description: "vuepress-theme-hope 的演示",
    },
  },

  theme,
});
