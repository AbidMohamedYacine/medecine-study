/* SEENMED_CARDIO_THEMES_DELTA34 — réglages limités aux leçons ca-*. */
;(function(){
  var b=document.body;
  if(!b || !/^ca-\d\d$/.test(b.getAttribute('data-lesson-id')||'')) return;
  if(document.getElementById('seenmed-cardio-themes-delta34')) return;
  var style=document.createElement('style');
  style.id='seenmed-cardio-themes-delta34';
  style.textContent="/* DELTA34 \u2014 fond des le\u00e7ons cardiaques seulement ; pas les composants,\n   le texte, les images, les audios ou les couleurs s\u00e9mantiques des QCM. */\n@media screen {\n  body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#1b0710;\n  }\n  html[data-theme=\"light\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#e8f3ff;\n  }\n  html[data-theme=\"aurora\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#03110b;\n  }\n  html[data-theme=\"ocean\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#211208;\n  }\n  body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(255,80,105,.11),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(255,164,125,.08),transparent 60%);\n  }\n  html[data-theme=\"aurora\"] body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(70,207,151,.12),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(165,231,174,.07),transparent 60%);\n  }\n  html[data-theme=\"ocean\"] body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(255,187,89,.12),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(235,113,61,.08),transparent 60%);\n  }\n}\n";
  document.head.appendChild(style);
})();
