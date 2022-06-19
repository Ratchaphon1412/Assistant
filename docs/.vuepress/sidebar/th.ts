import { sidebar } from "vuepress-theme-hope";

export const th = sidebar({
  "/th": [
   {
    text: "Guide",
    
    icon: "fa-solid fa-lightbulb",
    prefix:"/th/Guide",
    link:"/th/Guide",
    collapsable:true,
    children:[
      "Introduction.md",
      "Installation.md"
    ]
   }
  ]
});
