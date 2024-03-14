$(document).ready(function() {
  var animated = false; // Flag to ensure animation happens once

  function isElementInView(element) {
      var elementTop = $(element).offset().top;
      var elementBottom = elementTop + $(element).outerHeight();

      var viewportTop = $(window).scrollTop();
      var viewportBottom = viewportTop + $(window).height();

      return elementBottom > viewportTop && elementTop < viewportBottom;
  }

  $(window).scroll(function() {
      if (isElementInView($('#start-counting')) && !animated) {
          $('.counter').each(function() {
              $(this).prop('Counter', 0).animate({
                  Counter: $(this).text()
              }, {
                  duration: 2000,
                  easing: 'swing',
                  step: function(now) {
                      $(this).text(Math.ceil(now));
                  }
              });
          });

          animated = true; // Change flag after animation
      }
  });
});




