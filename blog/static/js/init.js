

document.addEventListener('DOMContentLoaded', () => {

  //Navegation Menu
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
        duration: 500,
        indicators: true,
        numVisible: 3,
        dist: -30,
      
    });
  });
