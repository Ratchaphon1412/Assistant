import { sidebar } from "vuepress-theme-hope";

export default sidebar([
 "/Guide",
  {
    text:"Get Started",
    icon:"fa-solid fa-lightbulb",
    
    prefix:"/Guide/Get-Started",
    collapsable: true,
    children:[
      "Introduction.md",
      "Installation.md",

    ],
  }

  

]);
