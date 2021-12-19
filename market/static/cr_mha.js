

(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5248H59');

        var arr_crisp_data=[];


window.$crisp=[];
CRISP_RUNTIME_CONFIG={
locale:'fa'
};
CRISP_WEBSITE_ID='c55c0d24-98fe-419a-862f-0b31e955fd59';(function(){
d=document;s=d.createElement('script');
s.src='https://client.crisp.chat/l.js';
s.async=1;d.getElementsByTagName('head')[0].appendChild(s);
})();

console.log($crisp);

    
        function isset(a)
        {
         if (typeof(a) != "undefined" )
         {
         return true;
         }
         return false;
    
        }
     
       var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-62787234-1']);


if (typeof($crisp) != "undefined")
{

 (function(){
 
 setTimeout(function()
 {
document.querySelector(".mha .btn").addEventListener("click", mha_open_pop );
function mha_open_pop (){
if(typeof($crisp)!="undefined"){

      _gaq.push(['_trackPageview', '/startchat/']);

var show_a_message = function(){
$crisp.push(["do", "message:send", ["text",jQuery("._input_kar").val()]]);
};
setTimeout(show_a_message, 2000);

$crisp.push(["do", "chat:open"]);
navigator.vibrate(200); // vibrate for 200ms
navigator.vibrate([100,30,100,30,100,30,200,30,200,30,200,30,100,30,100,30,100]); // Vibrate 'SOS' in Morse.

}
document.querySelector(".mha").style.visibility = "hidden";
 
} 
},3000);

})();
 

$crisp.push(["on", "message:sent", getads]) ; 
// $crisp.push(["on", "session:loaded", start_notif])
 
        $crisp.push(["set", "session:data", ["ip", "5.123.205.215"] ]);
        
        
       var parts = window.location.search.substr(1).split("&");
    var $_GET = {};
    for (var i = 0; i < parts.length; i++) {
        var temp = parts[i].split("=");
         $_GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
       arr_crisp_data.push([decodeURIComponent(temp[0])  , decodeURIComponent(temp[1]) ]);
    }
    
        $crisp.push(["set", "session:data",  [arr_crisp_data] ]);

    $crisp.push(["set", "session:data", ["page_"+new Date().getTime()+"_"+Math.floor(Math.random() * 100),window.location.href] ]);

    console.log("$$$", $_GET["utm_source"]);

    if( $_GET["utm_source"]=="demo")
    {
     console.log("demo");
      $crisp.push(["do", "message:send", ["text"," درخواست مشاوره برای سایت  " + $_GET["utm_content"] ]]);
$crisp.push(["do", "chat:open"]);

navigator.vibrate(200); // vibrate for 200ms
navigator.vibrate([100,30,100,30,100,30,200,30,200,30,200,30,100,30,100,30,100]); // Vibrate 'SOS' in Morse.

    }
    }
 

 function getads(message=0)
 {
                       localStorage.setItem("time_visit",99999999999999);       

      _gaq.push(['_trackPageview', '/getchat/']);
      console.log("crisp ok");
  } 
  
      var a = document.getElementById("myAudio"); 

 function start_notif(message=0)
 {
     if (localStorage.getItem("ft")!="1")
    
    {
    // var audio = new Audio('https://see5.ir/noti.mp3');

a.play();



setTimeout(function ()
{
  a.pause();
},2000);

localStorage.setItem("ft", "1");

}

   } 
   
   
   if(document.getElementById("mha_btn_install")!=null)
   {
   document.getElementById("mha_btn_install").addEventListener("click",function ()
                                                            {
    if(localStorage.getItem("time_visit")!=99999999999999)
    {
var d=new Date();
var n=d.getTime();
localStorage.setItem("time_visit",n+120000);

    }
     
});
}

  
   (function() {
   var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
   ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();


