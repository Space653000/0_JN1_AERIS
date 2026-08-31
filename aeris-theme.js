(() => {
  const STORAGE_KEY = 'aeris-theme-preference';
  const media = window.matchMedia('(prefers-color-scheme: dark)');

  function getPreference() {
    const saved = localStorage.getItem(STORAGE_KEY);
    return ['light', 'dark', 'system'].includes(saved) ? saved : 'system';
  }

  function resolveTheme(preference) {
    if (preference === 'system') return media.matches ? 'dark' : 'light';
    return preference;
  }

  function applyTheme(preference, persist = false) {
    const resolved = resolveTheme(preference);
    document.documentElement.dataset.theme = resolved;
    document.documentElement.dataset.themePreference = preference;
    document.documentElement.style.colorScheme = resolved;
    if (persist) localStorage.setItem(STORAGE_KEY, preference);

    document.querySelectorAll('[data-theme-choice]').forEach((button) => {
      const active = button.dataset.themeChoice === preference;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });

    document.querySelectorAll('[data-theme-current]').forEach((node) => {
      const label = preference === 'system'
        ? `系統 · ${resolved === 'dark' ? '深色' : '淺色'}`
        : (resolved === 'dark' ? '深色' : '淺色');
      node.textContent = label;
    });
  }

  function makeButton(value, icon, label) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'theme-choice';
    button.dataset.themeChoice = value;
    button.setAttribute('aria-label', `切換為${label}模式`);
    button.innerHTML = `<span aria-hidden="true">${icon}</span><span>${label}</span>`;
    button.addEventListener('click', () => applyTheme(value, true));
    return button;
  }

  function injectThemeControls() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar || sidebar.querySelector('.theme-dock')) return;

    const dock = document.createElement('div');
    dock.className = 'theme-dock';
    dock.innerHTML = '<div class="theme-label"><span>APPEARANCE</span><small data-theme-current></small></div>';

    const choices = document.createElement('div');
    choices.className = 'theme-choices';
    choices.append(
      makeButton('system', '◐', '系統'),
      makeButton('light', '☀', '淺色'),
      makeButton('dark', '☾', '深色')
    );
    dock.appendChild(choices);

    const spacer = sidebar.querySelector('.spacer');
    if (spacer) spacer.insertAdjacentElement('afterend', dock);
    else sidebar.appendChild(dock);

    applyTheme(getPreference(), false);
  }

  applyTheme(getPreference(), false);

  media.addEventListener?.('change', () => {
    if (getPreference() === 'system') applyTheme('system', false);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectThemeControls, { once: true });
  } else {
    injectThemeControls();
  }
})();
