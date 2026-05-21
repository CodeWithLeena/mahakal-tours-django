// ── LOADER ──
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hide');
  }, 2200);
});

// ── PARTICLES ──
const pc = document.getElementById('particles');
for (let i = 0; i < 30; i++) {
  const p = document.createElement('div');
  p.className = 'particle';
  p.style.cssText = `left:${Math.random()*100}%;width:${1+Math.random()*3}px;height:${1+Math.random()*3}px;animation-duration:${6+Math.random()*10}s;animation-delay:${Math.random()*8}s`;
  pc.appendChild(p);
}

// ── NAV SCROLL ──
const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 50);
});

// ── MOBILE MENU ──
function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('open');
}

// ── SCROLL REVEAL ──
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

// ── COUNT-UP ANIMATION ──
const countObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      const el = e.target;
      const target = parseInt(el.dataset.target);
      let current = 0;
      const step = target / 50;
      const t = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = Math.floor(current);
        if (current >= target) clearInterval(t);
      }, 30);
      countObs.unobserve(el);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('.count-up').forEach(el => countObs.observe(el));

// ── CONTACT FORM ──
document.getElementById('contactForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = e.target.querySelector('.form-submit');
  btn.textContent = '⏳ Bhejna...';
  btn.disabled = true;
  const msgEl = document.getElementById('form-msg');

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  try {
    const res = await fetch('/contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({
        name: document.getElementById('f-name').value,
        phone: document.getElementById('f-phone').value,
        message: document.getElementById('f-msg').value,
      })
    });
    const data = await res.json();
    msgEl.className = data.success ? 'success' : 'error';
    msgEl.textContent = data.message;
    msgEl.style.display = 'block';
    if (data.success) e.target.reset();
  } catch {
    msgEl.className = 'error';
    msgEl.textContent = 'Network error. Please try again.';
    msgEl.style.display = 'block';
  }
  btn.textContent = '🙏 Message Bhejein';
  btn.disabled = false;
});
