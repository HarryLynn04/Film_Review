document.addEventListener( 'DOMContentLoaded', function () {
    new Splide('.splide', {
            type: 'fade',  
            rewind: true,
            autoplay: true,
            interval: 3000, // time in milliseconds
        }).mount();
  } );