$(window).scroll(function() {
    var scrollPosition = $(this).scrollTop();
    var element = $('header');
  
    if (scrollPosition > 100){ // Change 100 to the scroll position you want
      element.addClass('bg-info'); // Change 'newClass' to the class you want to add
    } else {
      element.removeClass('bg-info'); // It will remove the class when scroll up
    }
  });