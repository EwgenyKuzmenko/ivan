$(document).ready(function(){

$('.slider').slick({
	infinite: true,
	dots: true,
	slidesToShow: 1,
	slidesToScroll: 1,
	autoplay:true,
	autoplaySpeed: 5000,
	fade: true,
	easing: 'easeInCubic',
	lazyLoad: 'ondemand',
	speed: 1500,
	pauseOnHover: false
});

$('.slider4').slick({
	infinite: true,
	dots: true,
	arrows: false,
	slidesToShow: 4,
	slidesToScroll: 4,
	responsive: [
	    {
	      breakpoint: 1024,
	      settings: {
	        slidesToShow: 3,
	        slidesToScroll: 3,
	        infinite: true,
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 2,
	        slidesToScroll: 2
	      }
	    },
	    {
	      breakpoint: 568,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	]
});

});


function initGallery()
{

 $('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  centerMode: true,
  focusOnSelect: true,
  responsive: [
	    {
	      breakpoint: 1024,
	      settings: {
	        slidesToShow: 3,
	        slidesToScroll: 3,
	        infinite: true,
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    },
	    {
	      breakpoint: 568,
	      settings: {
  			centerMode: false,
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	]
});


}