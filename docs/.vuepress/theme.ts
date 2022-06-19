import { hopeTheme } from "vuepress-theme-hope";
import * as navbar from "./navbar";
import * as sidebar from "./sidebar";

export default hopeTheme({
  hostname: "https://vuepress-theme-hope-v2-demo.mrhope.site",



  iconAssets: "fontawesome",

  logo: "/logo.svg",

  repo: "vuepress-theme-hope/vuepress-theme-hope",


  locales: {
    "/en": {
      // navbar
      navbar: navbar.en,

      // sidebar
      sidebar: sidebar.en,

      footer: "Default footer",

      displayFooter: true,

      
    },

    /**
     * Chinese locale config
     */
    "/th": {
      // navbar
      navbar: navbar.th,

      // sidebar
      sidebar: sidebar.th,

      footer: "Default footer",

      displayFooter: true,

    },
  },



  plugins: {
    blog: {
      autoExcerpt: true,
    },

    mdEnhance: {
      enableAll: true,
      presentation: {
        plugins: ["highlight", "math", "search", "notes", "zoom"],
      },
    },
  },
});
