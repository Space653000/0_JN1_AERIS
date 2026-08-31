(() => {
  const THEME_KEY='aeris-theme-preference';
  const SIDEBAR_KEY='aeris-sidebar-state';
  const media=window.matchMedia('(prefers-color-scheme: dark)');
  const savedTheme=localStorage.getItem(THEME_KEY);
  const initial=savedTheme==='light'||savedTheme==='dark'?savedTheme:(media.matches?'dark':'light');
  document.documentElement.dataset.theme=initial;
  document.documentElement.style.colorScheme=initial;
  if(localStorage.getItem(SIDEBAR_KEY)==='collapsed') document.documentElement.dataset.sidebar='collapsed';

  function syncTheme(){const b=document.querySelector('[data-theme-toggle]');if(!b)return;const dark=document.documentElement.dataset.theme==='dark';b.querySelector('.nav-icon').textContent=dark?'☀':'☾';b.querySelector('[data-theme-label]').textContent=dark?'Light Mode':'Dark Mode';b.title=dark?'切換淺色模式':'切換深色模式'}
  function syncSidebar(){const b=document.querySelector('[data-sidebar-toggle]');if(!b)return;const c=document.documentElement.dataset.sidebar==='collapsed';b.querySelector('.nav-icon').textContent=c?'→':'←';b.querySelector('[data-sidebar-label]').textContent=c?'Expand':'Collapse';b.title=c?'展開側欄':'收合側欄'}
  function inject(){const s=document.querySelector('.sidebar');if(!s||s.querySelector('.sidebar-utilities'))return;const u=document.createElement('div');u.className='sidebar-utilities';u.innerHTML='<button class="utility-btn" type="button" data-theme-toggle><span class="nav-icon">☾</span><span data-theme-label>Dark Mode</span></button><button class="utility-btn" type="button" data-sidebar-toggle><span class="nav-icon">←</span><span data-sidebar-label>Collapse</span></button>';s.appendChild(u);u.querySelector('[data-theme-toggle]').onclick=()=>{const next=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=next;document.documentElement.style.colorScheme=next;localStorage.setItem(THEME_KEY,next);syncTheme()};u.querySelector('[data-sidebar-toggle]').onclick=()=>{const c=document.documentElement.dataset.sidebar==='collapsed';if(c){delete document.documentElement.dataset.sidebar;localStorage.setItem(SIDEBAR_KEY,'expanded')}else{document.documentElement.dataset.sidebar='collapsed';localStorage.setItem(SIDEBAR_KEY,'collapsed')}syncSidebar()};syncTheme();syncSidebar()}
  media.addEventListener?.('change',e=>{if(!localStorage.getItem(THEME_KEY)){document.documentElement.dataset.theme=e.matches?'dark':'light';document.documentElement.style.colorScheme=e.matches?'dark':'light';syncTheme()}});
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',inject,{once:true}); else inject();
})();