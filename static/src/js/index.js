// import $ from "jquery";
import StickySidebar from "sticky-sidebar";
// import plugin from "./plugin";
import "../sass/style.sass";

// plugin("stickysidebar", StickySidebar);
//
// $(document).ready(function(){
// 	$("#sidebar").stickysidebar({
// 		topSpacing: 50,
// 		bottomSpacing: 20,
// 		resizeSensor: false,
// 		minWidth: 300,
// 	});
// });
//
// window.$ = $;
// window.jQuery = jQuery;






new StickySidebar('#sidebar', {
    topSpacing: 50,
    bottomSpacing: 50,
    additionalMarginTop: 30,
    resizeSensor: false,
    // minWidth: 300,
    containerSelector: '#main-content',
    innerWrapperSelector: '.sidebar__inner',
    stickyClass: 'is-affixed',
});