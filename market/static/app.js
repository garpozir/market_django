var see5=angular.module("see5",["ngAnimate","ui.bootstrap"]);angular.module("see5").controller("DemoCtrl",["$scope",function(e){e.open=!0,e.toggleOpen=function(){e.open=!e.open}}]),angular.module("see5").controller("sectionTabCtrl",["$scope",function(e){e.tab=0,e.navigations=[{icon:"ion-android-star",text:"ویژگی های سی فایو"},{icon:"ion-ios-videocam",text:"فیلم های آموزشی"},{icon:"ion-android-phone-portrait",text:"سایت های واکنش گرا"},{icon:"ion-android-call",text:"پشتیبانی ۲۴*۷"},{icon:"ion-stats-bars",text:"۳۰۰ مگابایت هاست"}],e.changeTab=function(t){e.tab=t}}]),angular.module("see5").controller("See5templateCtrl",["$scope","$http",function(e,t){e.templateList=[],e.loading=!1,e.page=1,e.showBtn=!0,e.search="",e.searchTemp="",e.searching=!1,e.error="",e.loadMore=function(n){e.loading=!0,t({method:"post",url:"",data:"from="+e.page+"&category="+n+"&text="+e.search,timeout:15e3,headers:{"Content-Type":"application/x-www-form-urlencoded"}}).success(function(t){0!=t.length&&(e.templateList=t,$("body, html").animate({scrollTop:$("#list-template").offset().top-100},1e3)),e.loading=!1}).error(function(){alert("ارتباط برقرار نشد"),e.loading=!1})},e.doSearch=function(){0==e.search.length?e.error="متن جستجو خالیست":(e.showBtn=!0,e.error="",e.page=1,e.templateList=[],e.searching=!0,e.searchTemp=e.search,e.loadMore(""))}}]),angular.module("see5").directive("countUp",["$interval",function($interval){var directive={link:function(scope,element,attr){var options={maxnumber:14591,whenclass:!1,time:7};try{var config=eval("("+attr.countUp+")");angular.extend(options,config)}catch(e){}var interval=$interval(function(){0!=options.whenclass?$(element).hasClass(options.whenclass)&&(new countUp(attr.id,0,options.maxnumber,0,options.time).start(),$interval.cancel(interval)):(new countUp(attr.id,0,options.maxnumber,0,options.time).start(),$interval.cancel(interval))},50)}};return directive}]),angular.module("see5").directive("ngReach",function(){return{link:function(scope,element,attr){function onScroll(){window.pageYOffset>=$(element).position().top-options.range&&(window.removeEventListener("scroll",onScroll,!1),$(element).addClass(options.addclass))}var options={range:600,addclass:"reached"};try{var config=eval("("+attr.ngReach+")");angular.extend(options,config)}catch(e){}window.addEventListener("scroll",onScroll,!1),onScroll()}}}),angular.module("see5").directive("ngSlider",["$timeout",function($timeout){return{link:function(scope,element,attr){var options={auto:1e4,pagination:!1,itemcount:3,delay:0,stopOnHover:!0,navigation:!1,lazyLoad:!1,itemsDesktop:"",itemsDesktopSmall:"",buttons:!1};try{var config=eval("("+attr.ngSlider+")");angular.extend(options,config)}catch(e){}var owl=$(element).owlCarousel({autoPlay:options.auto,stopOnHover:options.stopOnHover,navigation:options.navigation,items:options.itemcount,itemsDesktop:options.itemsDesktop,itemsDesktopSmall:options.itemsDesktopSmall,singleItem:options.single,pagination:options.pagination,lazyLoad:options.lazyLoad,afterMove:function(e){var t=this.currentItem,n=e.find(".owl-item").eq(t);e.find(".owl-item.active").removeClass("active"),$(n).addClass("active")}});if($(element).find(".owl-item:first-child").addClass("active"),$timeout(function(){$(element).css("opacity","")},1),1==options.buttons){var next=$("<div class='gnext'><div class='bg'><i class='ion ion-chevron-right'></i></div></div>"),prev=$("<div class='gprev'><div class='bg'><i class='ion ion-chevron-left'></i></div></div>");$(next).click(function(){owl.trigger("owl.next")}),$(prev).click(function(){owl.trigger("owl.prev")}),$(element).append(next),$(element).append(prev)}}}}]);

$('.crp_related .owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    rtl:true,
    autoplay:true,
    autoplayTimeout:100,
    autoplayHoverPause:true,

    lazyLoad: true,


    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
});

$('.owl-testmonial').owlCarousel({
    loop:true,
     nav:true,
      autoplay:true,
         autoWidth:true,
           navigation: true,

          navigationText:['<div class="nav-ol">  </div>','<div class="nav-ol">  </div>'],  
 
    items:2,


    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:2
        }
    }
});

 $(document).ready (
    function ()
    {
$('.owl-pages').owlCarousel({
    loop:true,
     nav:true,
      autoplay:true,
         autoWidth:true,
           navigation: true,

          navigationText:['<div class="nav-ol">  </div>','<div class="nav-ol">  </div>'],  
 
    items:5,


    responsive:{
        0:{
            items:2
        },
        600:{
            items:2
        },
        1000:{
            items:2
        }
    }
});

});

$("#side-cat-btn").click( function ()
{
  if ($(".side-cat").hasClass("active"))
  {
  $(".side-cat").removeClass("active");

  }
  else
  {
  $(".side-cat").addClass("active");

  }

});
 
$("#side-cat-btn-exit").click( function ()
{
  $(".side-cat").removeClass("active");

});

 
 $(document).ready(function(){  $("#mega-menu-wrap-header").show();
});
$(window).scroll(function(){
        if ($("body").hasClass("single-post"))
{
  var sticky = $('.sticky'),
      scroll = $(window).scrollTop();
      scroll_crp = $(".post-tags").position().top -200;
     console.log(scroll_crp);

  if (scroll >= 500 && scroll <=scroll_crp-100) sticky.addClass('fixed-Psite');
  else
    {
     sticky.removeClass('fixed-Psite');
    }

  }
    
    /*
       var sticky = $('.navigation'),
      scroll = $(window).scrollTop();

  if (scroll > 100) sticky.addClass('fixed');
  else sticky.removeClass('fixed');
  */
});
