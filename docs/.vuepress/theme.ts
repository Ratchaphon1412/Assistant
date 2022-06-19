import { hopeTheme } from "vuepress-theme-hope";
import navbar from "./navbar";
import sidebar from "./sidebar";


export default hopeTheme({
  iconAssets: "fontawesome",
  

  logo: "/logo.svg",
  // navbar
  navbar: navbar,
  repo: "Ratchaphon1412/Assistant",
 
  //interface
  darkmode:"switch",
  backToTop: true,

  // sidebar
  sidebar: sidebar,
  //footer
  footer: "Default footer",
  displayFooter: true,
  
  plugins:{
    mdEnhance:{
        enableAll: true,
        mark: true,
        
    },
   
  }



});
