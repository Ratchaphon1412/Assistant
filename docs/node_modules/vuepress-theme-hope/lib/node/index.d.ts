import { covertFrontmatter, covertNavbarConfig, convertSidebarConfig, covertThemeConfig, config, navbarConfig, sidebarConfig, themeConfig, defineHopeConfig, defineThemeConfig, defineNavbarConfig, defineSidebarArrayConfig, defineSidebarConfig, defineSidebarObjectConfig } from "./compact";
export { config, navbarConfig, sidebarConfig, themeConfig, covertFrontmatter, covertNavbarConfig, convertSidebarConfig, covertThemeConfig, defineHopeConfig, defineThemeConfig, defineNavbarConfig, defineSidebarArrayConfig, defineSidebarConfig, defineSidebarObjectConfig, };
export * from "./themeConfig";
export * from "./helpers";
export * from "./locales";
export * from "./theme";
export * from "../shared";
declare const _default: {
    config: (userConfig: Record<string, unknown>) => import("@vuepress/cli").UserConfig;
    navbarConfig: (config: import("../shared").HopeThemeNavbarConfig) => import("../shared").HopeThemeNavbarConfig;
    sidebarConfig: (config: import("../shared").HopeThemeSidebarConfig) => import("../shared").HopeThemeSidebarConfig;
    themeConfig: (themeConfig: import("../shared").HopeThemeOptions) => import("../shared").HopeThemeOptions;
};
export default _default;
