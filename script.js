/* =========================================================
   P3MAI — Shared Interactive Behavior
   ========================================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Page loader / transition overlay ---------- */
  var pageTransition = document.getElementById('page-transition');

  if (pageTransition) {
    // Briefly show the loader mark on first open, then fade the overlay away.
    var reveal = function () {
      setTimeout(function () { pageTransition.classList.add('hide'); }, 250);
    };
    if (document.readyState === 'complete') {
      reveal();
    } else {
      window.addEventListener('load', reveal);
    }

    // Fade the overlay back in before following a link to another page on
    // this site, so navigating between pages feels like a soft transition
    // rather than an abrupt reload.
    document.querySelectorAll('a[href$=".html"]').forEach(function (link) {
      if (link.target === '_blank') return;
      link.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button === 1) return;
        var href = link.getAttribute('href');
        if (!href) return;
        e.preventDefault();
        pageTransition.classList.remove('hide');
        setTimeout(function () { window.location.href = href; }, 280);
      });
    });
  }

  /* ---------- Mobile nav toggle ---------- */
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile menu when a link is clicked
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        navToggle.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------- Header shadow on scroll ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 10);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Smooth scroll for same-page anchor links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = anchor.getAttribute('href');
      if (targetId.length > 1) {
        var target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  /* ---------- Scroll-reveal animation ---------- */
  var revealEls = document.querySelectorAll('.reveal');

  // Cards inside the testimonials grid fade in with a slight stagger rather
  // than all at once. The delay is applied inline and cleared once the
  // reveal transition finishes, so it never lingers and slows down hover.
  function applyStaggerDelay(el) {
    var grid = el.closest ? el.closest('.testimonial-grid') : null;
    if (!grid) return;
    var siblings = Array.prototype.slice.call(grid.querySelectorAll('.testimonial-card'));
    var index = siblings.indexOf(el);
    if (index > -1) {
      el.style.transitionDelay = (index * 0.15) + 's';
      el.addEventListener('transitionend', function clearDelay() {
        el.style.transitionDelay = '';
        el.removeEventListener('transitionend', clearDelay);
      });
    }
  }

  if ('IntersectionObserver' in window && revealEls.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          applyStaggerDelay(entry.target);
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in-view'); });
  }

  /* ---------- Contact form handling ---------- */
  var contactForm = document.getElementById('contact-form');
  var formSuccess = document.getElementById('form-success');
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function setFieldError(fieldName, hasError) {
    var group = contactForm.querySelector('[data-field="' + fieldName + '"]');
    if (group) group.classList.toggle('has-error', hasError);
  }

  if (contactForm) {
    // Clear a field's error as soon as the person starts fixing it.
    ['name', 'email', 'message'].forEach(function (fieldName) {
      var input = contactForm.querySelector('#' + fieldName);
      if (input) {
        input.addEventListener('input', function () { setFieldError(fieldName, false); });
      }
    });

    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      var name = contactForm.querySelector('#name');
      var email = contactForm.querySelector('#email');
      var message = contactForm.querySelector('#message');
      var valid = true;

      var nameOk = !!name.value.trim();
      setFieldError('name', !nameOk);
      if (!nameOk) valid = false;

      var emailValue = email.value.trim();
      var emailOk = emailValue && EMAIL_RE.test(emailValue);
      setFieldError('email', !emailOk);
      if (!emailOk) valid = false;

      var messageOk = !!message.value.trim();
      setFieldError('message', !messageOk);
      if (!messageOk) valid = false;

      if (formSuccess) formSuccess.classList.add('hidden');

      if (!valid) {
        var firstError = contactForm.querySelector('.has-error');
        if (firstError) firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }

      // No backend wired up yet — simulate a successful submission.
      if (formSuccess) {
        formSuccess.classList.remove('hidden');
        formSuccess.textContent = "Thank you! I'll be in touch within 24 hours.";
        formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      contactForm.reset();
    });
  }

});
