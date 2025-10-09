// ======================
// Scrollspy
// ======================
var spy = new Gumshoe('#nav a');

// ======================
// Burger menu
// ======================
$('.burger').on('click', function () {
  $(this).toggleClass('open');
  $('.navigation-bar').toggleClass('show');
});

// ======================
// Dark mode toggle
// ======================
const THEME_KEY = 'theme';
const DIR_KEY = 'direction';

document.addEventListener("DOMContentLoaded", function () {
  const savedTheme = localStorage.getItem(THEME_KEY);
  const savedDir = localStorage.getItem(DIR_KEY);

  if (!savedTheme || savedTheme === "dark") {
    document.body.classList.add("darkmode");
  } else {
    document.body.classList.remove("darkmode");
  }

  if (!savedDir || savedDir === "rtl") {
    document.body.classList.add("rtl");
  } else {
    document.body.classList.remove("rtl");
  }
});

$('.darkmode-btn').on('click', function () {
  $('body').toggleClass('darkmode');
  localStorage.setItem('theme', $('body').hasClass('darkmode') ? 'dark' : 'light');
});

$('.dir-btn').on('click', function () {
  $('body').toggleClass('ltr');
  localStorage.setItem('direction', $('body').hasClass('ltr') ? 'ltr' : 'rtl');
});

// ======================
// Modal
// ======================
$('.btn-view').on('click', function () {
  $('.modal-container').addClass('active');
});
$('.close-modal').on('click', function () {
  $('.modal-container').removeClass('active');
});

// ======================
// Sticky navbar
// ======================
$(document).ready(function(){
    const header = $('header');
    $(window).scroll(function() {
        if($(window).scrollTop() > 50){
            header.addClass('fixed');
        } else {
            header.removeClass('fixed');
        }
    });
});

// ======================
// Scrollspy با offset ساده
// ======================
$('#nav a').on('click', function(e){
    e.preventDefault();
    var target = $(this).attr('href');
    var headerHeight = $('header').outerHeight();
    var scrollTo;

    if(target === '#home') {
        // برای Home offset نذاریم
        scrollTo = 0;
    } else {
        scrollTo = $(target).offset().top - headerHeight - 5;
    }

    $('html, body').animate({ scrollTop: scrollTo }, 400);
});

// Scrollspy با offset برای header fixed
var spy = new Gumshoe('#nav a', {
    offset: function() {
        return $('header').outerHeight() + 5; // ارتفاع header + کمی فاصله
    },
    reflow: true,
    events: true
});

// ======================
// Scroll to TOP
// ======================
var btn = $('.scrollup');
$(window).scroll(function() {
  if ($(window).scrollTop() > 500) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});
btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, 500);
});

// ======================
// Testimonial slider (Owl Carousel)
// ======================
$('.testmonial-slider').owlCarousel({
    autoplay:true,
    autoplayTimeout:1500,
    autoplayHoverPause:true,
    loop: true,
    responsiveClass: true,
    nav: false,
    dots: true,
    smartSpeed: 700,
    margin:30,
    responsive: {
        0: { items: 1 },
        600: { items: 2 },
        1000: { items: 2 }
    }
});

// ======================
// Reveal animation (ScrollReveal)
// ======================
const sr = ScrollReveal({
    origin: 'top',
    distance: '90px',
    duration: 2000,
    reset: true
});
ScrollReveal().reveal('.social-icon, .feature-item, .progressbar-item, .services-block, .project-item, .form-item', { interval: 100 });
ScrollReveal().reveal('.sub-heading');
ScrollReveal().reveal('.col-right');
ScrollReveal().reveal('.heading', { delay: 100 });
ScrollReveal().reveal('.heading2', { delay: 200 });
ScrollReveal().reveal('.paragraph', { delay: 300 });
ScrollReveal().reveal('.btn-blk', { delay: 400 });
// About
ScrollReveal().reveal('.about-col-left');
ScrollReveal().reveal('.about-heading');
ScrollReveal().reveal('.about2', { delay: 100 });
ScrollReveal().reveal('.about3', { delay: 200 });
ScrollReveal().reveal('.about-btn-blk', { delay: 300 });
// CTA
ScrollReveal().reveal('.cta-inner', { delay: 100 });
ScrollReveal().reveal('.btn-outline', { delay: 200 });
// Testimonial
ScrollReveal().reveal('.testmonial-slider');
// Contact form
ScrollReveal().reveal('.contact-inner');
