/**
 * Disagree Wisely — Board Onboarding Site
 * Main JavaScript: section loading, toggling, TOC scroll-spy, mobile nav
 */

(function () {
  'use strict';

  // ── Section Loading ──────────────────────────────────────────────────
  // Load section HTML files into their placeholder elements.
  // If no placeholders exist (sections are inlined), this is a no-op.

  async function loadSections() {
    const placeholders = document.querySelectorAll('[data-section-src]');
    if (!placeholders.length) return;
    const promises = Array.from(placeholders).map(async (el) => {
      const src = el.getAttribute('data-section-src');
      try {
        const resp = await fetch(src);
        if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
        el.innerHTML = await resp.text();
      } catch (err) {
        el.innerHTML = `<p class="note warning">Could not load section: ${src}</p>`;
        console.error(`Failed to load section "${src}":`, err);
      }
    });
    await Promise.all(promises);
  }

  // ── Collapsible Sections ─────────────────────────────────────────────

  function initToggle(container) {
    // Top-level sections
    container.querySelectorAll('.section-header').forEach((header) => {
      header.addEventListener('click', () => {
        const section = header.closest('.section');
        section.classList.toggle('open');
      });
    });

    // Nested subsections
    container.querySelectorAll('.subsection-header').forEach((header) => {
      header.addEventListener('click', (e) => {
        e.stopPropagation();
        const subsection = header.closest('.subsection');
        subsection.classList.toggle('open');
      });
    });
  }

  // ── TOC Scroll-Spy ───────────────────────────────────────────────────

  function initScrollSpy() {
    var tocLinks = document.querySelectorAll('.toc-nav a');
    var sections = [];

    tocLinks.forEach(function (link) {
      var href = link.getAttribute('href');
      var id = href ? href.replace('#', '') : '';
      if (id) {
        var target = document.getElementById(id);
        if (target) sections.push({ id: id, el: target, link: link, visible: false });
      }
    });

    if (!sections.length) return;

    var observed = [];
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          sections.forEach(function (s) {
            if (s.el === entry.target) s.visible = entry.isIntersecting;
          });
        });

        // Highlight the LAST visible section in TOC order.
        // Sub-tabs appear after their parent in the list, so a visible
        // subsection (e.g. #bylaws) wins over its parent (#governance).
        tocLinks.forEach(function (l) { l.classList.remove('active'); });
        for (var i = sections.length - 1; i >= 0; i--) {
          if (sections[i].visible) {
            sections[i].link.classList.add('active');
            break;
          }
        }
      },
      { rootMargin: '-10% 0px -70% 0px' }
    );

    sections.forEach(function (s) {
      if (observed.indexOf(s.el) === -1) {
        observer.observe(s.el);
        observed.push(s.el);
      }
    });
  }

  // ── Anchor Click-to-Open ────────────────────────────────────────────
  // When any in-page anchor link targets a collapsed section or subsection, open it.

  function openSectionForId(id) {
    var target = document.getElementById(id);
    if (!target) return;

    // Open the parent .section if collapsed
    var section = target.closest('.section');
    if (section) section.classList.add('open');

    // Open the .subsection itself (or its containing subsection)
    if (target.classList.contains('subsection')) {
      target.classList.add('open');
    } else {
      var sub = target.closest('.subsection');
      if (sub) sub.classList.add('open');
    }
  }

  function initTocNavigation() {
    // Handle all in-page anchor links, not just TOC links
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;
      var id = link.getAttribute('href').replace('#', '');
      if (id) openSectionForId(id);
    });
  }

  // ── Mobile Nav ───────────────────────────────────────────────────────

  function initMobileNav() {
    const toggle = document.querySelector('.mobile-nav-toggle');
    const sidebar = document.querySelector('.toc-sidebar');
    const overlay = document.querySelector('.toc-overlay');

    if (!toggle || !sidebar) return;

    function closeSidebar() {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('open');
    }

    toggle.addEventListener('click', () => {
      const isOpen = sidebar.classList.toggle('open');
      if (overlay) overlay.classList.toggle('open', isOpen);
    });

    if (overlay) overlay.addEventListener('click', closeSidebar);

    // Close sidebar when a TOC link is clicked on mobile
    sidebar.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeSidebar);
    });
  }

  // ── Expand All / Collapse All (keyboard shortcut) ────────────────────

  function initKeyboard() {
    document.addEventListener('keydown', (e) => {
      // Ctrl/Cmd + E = expand all, Ctrl/Cmd + Shift + E = collapse all
      if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
        e.preventDefault();
        const open = !e.shiftKey;
        document.querySelectorAll('.section').forEach((s) => {
          s.classList.toggle('open', open);
        });
        document.querySelectorAll('.subsection').forEach((s) => {
          s.classList.toggle('open', open);
        });
      }
    });
  }

  // ── Theme Toggle ────────────────────────────────────────────────────

  function initThemeToggle() {
    var saved = localStorage.getItem('theme');
    var theme;
    if (saved === 'light' || saved === 'dark') {
      theme = saved;
    } else {
      theme = 'dark';
    }
    document.documentElement.dataset.theme = theme;

    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;

    var icon = btn.querySelector('.theme-toggle-icon');
    updateIcon(icon, theme);

    btn.addEventListener('click', function () {
      var current = document.documentElement.dataset.theme;
      var next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      localStorage.setItem('theme', next);
      updateIcon(icon, next);
    });
  }

  function updateIcon(icon, theme) {
    // Show sun when dark (click to go light), moon when light (click to go dark)
    icon.textContent = theme === 'dark' ? '\u2600' : '\u263E';
  }

  // ── Init ─────────────────────────────────────────────────────────────

  async function init() {
    initThemeToggle();
    await loadSections();
    initToggle(document);
    initScrollSpy();
    initTocNavigation();
    initMobileNav();
    initKeyboard();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
