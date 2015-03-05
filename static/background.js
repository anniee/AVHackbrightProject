//$(document).ready(function() {
 //  $('#gear').mouseenter(function() {
   //    $('#gear').animate({
   //        height: '+=100px'
   //    });
  // });
 //  $('#gear').mouseleave(function() {
 //      $('#gear').animate({
  //         height: '-=100px'
 //      }); 
 //  });
//});



$(document).ready(function() {  
      
        //when hover over the selected item animate it, changing the left padding from its initial value to 20px  
  $('#menu li').hover(function() {  
    $(this).stop().animate({ paddingLeft: '100px' }, 500, 'swing');  
      }, function() {  
    $(this).stop().animate({ paddingLeft: '0' }, 1000, 'swing');  
      });  
          
}); 
 