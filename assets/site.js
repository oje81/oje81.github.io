(function(){
  var root=document.documentElement, KEY='site-lang', lang='ko';
  try{ lang=localStorage.getItem(KEY)||((navigator.language||'ko').slice(0,2)==='ko'?'ko':'en'); }catch(e){}
  function set(l){ root.setAttribute('data-lang',l); root.lang=l;
    document.querySelectorAll('.langbtn button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.l===l)});
    try{localStorage.setItem(KEY,l)}catch(e){} }
  set(lang);
  document.addEventListener('click',function(e){var b=e.target.closest('.langbtn button'); if(b) set(b.dataset.l);});
})();
