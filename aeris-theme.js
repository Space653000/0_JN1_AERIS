(() => {
  const THEME_KEY = 'aeris-theme-preference';
  const SIDEBAR_KEY = 'aeris-sidebar-state';
  const media = window.matchMedia('(prefers-color-scheme: dark)');

  const savedTheme = localStorage.getItem(THEME_KEY);
  const initialTheme = savedTheme === 'light' || savedTheme === 'dark'
    ? savedTheme
    : (media.matches ? 'dark' : 'light');
  document.documentElement.dataset.theme = initialTheme;
  document.documentElement.style.colorScheme = initialTheme;

  const savedSidebar = localStorage.getItem(SIDEBAR_KEY);
  if (savedSidebar === 'collapsed') document.documentElement.dataset.sidebar = 'collapsed';

  function applyTheme(theme, persist = true) {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
    if (persist) localStorage.setItem(THEME_KEY, theme);
    syncThemeButton();
  }

  function syncThemeButton() {
    const btn = document.querySelector('[data-theme-toggle]');
    if (!btn) return;
    const dark = document.documentElement.dataset.theme === 'dark';
    const icon = btn.querySelector('.ico');
    const label = btn.querySelector('[data-theme-label]');
    if (icon) icon.textContent = dark ? '☀' : '☾';
    if (label) label.textContent = dark ? 'Light Mode' : 'Dark Mode';
    btn.setAttribute('aria-label', dark ? '切換淺色模式' : '切換深色模式');
    btn.title = dark ? '切換 Light Mode' : '切換 Dark Mode';
  }

  function syncSidebarButton() {
    const btn = document.querySelector('[data-sidebar-toggle]');
    if (!btn) return;
    const collapsed = document.documentElement.dataset.sidebar === 'collapsed';
    const icon = btn.querySelector('.ico');
    const label = btn.querySelector('[data-sidebar-label]');
    if (icon) icon.textContent = collapsed ? '→' : '←';
    if (label) label.textContent = collapsed ? 'Expand' : 'Collapse';
    btn.setAttribute('aria-label', collapsed ? '展開側欄' : '收合側欄');
    btn.title = collapsed ? 'Expand sidebar' : 'Collapse sidebar';
  }

  function injectUtilities() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar || sidebar.querySelector('.sidebar-utilities')) return;

    const utilities = document.createElement('div');
    utilities.className = 'sidebar-utilities';
    utilities.innerHTML = `
      <button class="utility-btn" type="button" data-theme-toggle>
        <span class="ico" aria-hidden="true">☾</span>
        <span data-theme-label>Dark Mode</span>
      </button>
      <button class="utility-btn" type="button" data-sidebar-toggle>
        <span class="ico" aria-hidden="true">←</span>
        <span data-sidebar-label>Collapse</span>
      </button>`;

    const spacer = sidebar.querySelector('.spacer');
    if (spacer) spacer.insertAdjacentElement('afterend', utilities);
    else sidebar.appendChild(utilities);

    utilities.querySelector('[data-theme-toggle]').addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      applyTheme(next, true);
    });
    utilities.querySelector('[data-sidebar-toggle]').addEventListener('click', () => {
      const collapsed = document.documentElement.dataset.sidebar === 'collapsed';
      if (collapsed) {
        delete document.documentElement.dataset.sidebar;
        localStorage.setItem(SIDEBAR_KEY, 'expanded');
      } else {
        document.documentElement.dataset.sidebar = 'collapsed';
        localStorage.setItem(SIDEBAR_KEY, 'collapsed');
      }
      syncSidebarButton();
    });

    syncThemeButton();
    syncSidebarButton();
  }

  media.addEventListener?.('change', (event) => {
    if (!localStorage.getItem(THEME_KEY)) applyTheme(event.matches ? 'dark' : 'light', false);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectUtilities, { once: true });
  } else {
    injectUtilities();
  }
})();
