const swiper = new Swiper('.swiper', {

  direction: 'horizontal',
  loop: true,


  pagination: {
    el: '.swiper-pagination',
  },

autoplay: {
    delay: 2000,
  },

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  scrollbar: {
    el: '.swiper-scrollbar',
  },
});
