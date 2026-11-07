/* ════════════════════════════════════════════════════════════════════
   SEENmed — js/data-merge.js  (delta 30, AGENT-1, 01/11/2026)
   PROTECTION DU TABLEAU DE BORD contre les data.js périmés.

   Problème (constat utilisateur 01/11) : chaque ZIP de leçon livre un
   js/data.js COMPLET. Si ce fichier descend d'une lignée ancienne, il
   écrase le data.js courant et les leçons déjà livrées perdent leur
   `url` → dashboard.js n'affiche plus leur bouton « Ouvrir ».

   Solution (deux couches, aucune ne dépend d'un chargement réseau) :
   1) SECOURS SYNCHRONE : la carte FALLBACK ci-dessous (leçons connues
      livrées au 01/11) est appliquée IMMÉDIATEMENT, dès l'exécution de
      ce fichier — donc avant dashboard.js, quoi qu'il arrive.
   2) PATCHS PAR LEÇON : js/data-patches/<id>.js, UN fichier livré AVEC
      chaque leçon (nom unique = jamais écrasé par une autre leçon),
      chargés par document.write (ordre d'exécution garanti pendant le
      parsing) puis appliqués par le finaliseur. Couche d'avenir : les
      leçons livrées après le delta 30 s'y déclarent sans toucher de
      fichier partagé.
   Application MONOTONE dans les deux couches : une url présente n'est
   jamais effacée par le secours, recu ne repasse jamais à false.
   Règle associée : REGLE-FORMAT-LIVRAISON-ZIP (section DATA).
   ════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  if (window.__seenmedDataMerge) return;
  window.__seenmedDataMerge = true;

  var FALLBACK = {
 "psy-01": {
  "url": "lecons/sg-00-semantique-medicale.html",
  "qcm": 7
 },
 "psy-02": {
  "url": "lecons/psy-02-aspects-communicationnels-et-examen-mental.html",
  "qcm": 6
 },
 "psy-03": {
  "url": "lecons/psy-03-l-entrevue-medicale.html",
  "qcm": 4
 },
 "psy-04": {
  "url": "lecons/psy-04-annonce-d-une-maladie-grave.html",
  "qcm": 6
 },
 "psy-05": {
  "url": "lecons/psy-05-psychologie-de-la-douleur.html",
  "qcm": 4
 },
 "psy-07": {
  "url": "lecons/psy-07-stress-et-maladies-psychosomatiques.html",
  "qcm": 6
 },
 "sg-00": {
  "url": "lecons/sg-00-semantique-medicale.html",
  "qcm": 7
 },
 "sg-01": {
  "url": "lecons/sg-01-observation-medicale.html",
  "qcm": 8
 },
 "sg-02": {
  "url": "lecons/sg-02-raisonnement-clinique.html",
  "qcm": 4
 },
 "sg-03": {
  "url": "lecons/sg-03-abord-examen-clinique.html",
  "qcm": 5
 },
 "sg-04": {
  "url": "lecons/sg-04-troubles-hydratation.html",
  "qcm": 6,
  "entr": 6
 },
 "ca-01": {
  "url": "lecons/ca-01-pericardites.html",
  "qcm": 5,
  "entr": 29
 },
 "ca-02": {
  "url": "lecons/ca-02-douleurs-thoraciques.html",
  "qcm": 9,
  "entr": 24
 },
 "ca-03": {
  "url": "lecons/ca-03-bruits-cardiaques.html",
  "qcm": 7,
  "entr": 16
 },
 "ca-04": {
  "url": "lecons/ca-04-pression-arterielle.html",
  "qcm": 9,
  "entr": 16
 },
 "ca-05": {
  "url": "lecons/ca-05-bases-trace-ecg.html",
  "qcm": 7,
  "entr": 16
 },
 "ca-06": {
  "url": "lecons/ca-06-examen-cardiaque.html",
  "qcm": 10,
  "entr": 16
 },
 "ca-07": {
  "url": "lecons/ca-07-souffles-cardiaques.html",
  "qcm": 7
 },
 "ca-08": {
  "url": "lecons/ca-08-insuffisance-cardiaque.html",
  "qcm": 10
 },
 "ca-09": {
  "url": "lecons/ca-09-syncopes.html",
  "qcm": 3,
  "entr": 32
 },
 "ca-10": {
  "url": "lecons/ca-10-semiologie-veineuse.html",
  "qcm": 4,
  "entr": 24
 },
 "ca-11": {
  "url": "lecons/ca-11-semiologie-arterielle.html",
  "qcm": 6,
  "entr": 16
 },
 "pn-01": {
  "url": "lecons/pn-01-dyspnee.html",
  "qcm": 6,
  "entr": 20
 },
 "pn-02": {
  "url": "lecons/pn-02-douleurs-thoraciques.html",
  "qcm": 3,
  "entr": 12
 },
 "pn-03": {
  "url": "lecons/pn-03-semiologie-de-la-toux.html",
  "qcm": 4,
  "entr": 16
 },
 "pn-04": {
  "url": "lecons/pn-04-expectoration.html",
  "qcm": 8,
  "entr": 20
 },
 "pn-05": {
  "url": "lecons/pn-05-hemoptysie.html",
  "qcm": 5,
  "entr": 20
 },
 "pn-06": {
  "url": "lecons/pn-06-dysphonie.html",
  "qcm": 3,
  "entr": 12
 },
 "pn-07": {
  "url": "lecons/pn-07-signes-physiques.html",
  "qcm": 5,
  "entr": 20
 },
 "pn-08": {
  "url": "lecons/pn-08-syndromes-mediastinaux.html",
  "qcm": 7,
  "entr": 12
 },
 "pn-09": {
  "url": "lecons/pn-09-syndromes-pulmonaires.html",
  "qcm": 3,
  "entr": 12
 },
 "pn-10": {
  "url": "lecons/pn-10-syndromes-bronchiques.html",
  "qcm": 1,
  "entr": 19
 },
 "pn-11": {
  "url": "lecons/pn-11-syndromes-pleuraux.html",
  "qcm": 4,
  "entr": 8
 },
 "pn-12": {
  "url": "lecons/pn-12-ponction-pleurale.html",
  "qcm": 3,
  "entr": 12
 },
 "ph-01": {
  "url": "lecons/ph-01-thermoregulation.html",
  "qcm": 3
 },
 "ph-02": {
  "url": "lecons/ph-02-denutrition.html",
  "qcm": 1,
  "entr": 16
 },
 "ph-03": {
  "url": "lecons/ph-03-troubles-hydrosodes.html",
  "qcm": 8
 },
 "ph-04": {
  "url": "lecons/ph-04-insuffisance-cardiaque.html",
  "qcm": 0,
  "entr": 22
 },
 "ph-05": {
  "url": "lecons/ph-05-choc-hypovolemique.html",
  "qcm": 5,
  "entr": 16
 },
 "ph-06": {
  "url": "lecons/ph-06-choc-septique.html",
  "qcm": 6,
  "entr": 16
 },
 "ph-07": {
  "url": "lecons/ph-07-choc-cardiogenique.html",
  "qcm": 2,
  "entr": 16
 },
 "ph-08": {
  "url": "lecons/ph-08-choc-anaphylactique.html",
  "qcm": 2,
  "entr": 16
 },
 "ph-10": {
  "url": "lecons/ph-10-oap.html",
  "qcm": 3
 },
 "ph-11": {
  "url": "lecons/ph-11-troubles-hematose.html",
  "qcm": 2,
  "entr": 16
 },
 "ph-12": {
  "url": "lecons/ph-12-insuffisance-respiratoire.html",
  "qcm": 2,
  "entr": 16
 },
 "ph-13": {
  "url": "lecons/ph-13-maladie-thromboembolique.html",
  "qcm": 1,
  "entr": 17
 },
 "bi-01": {
  "url": "lecons/bi-01-biochimie-homme-sain.html",
  "qcm": 0,
  "entr": 24
 },
 "bi-02": {
  "url": "lecons/bi-02-etapes-analyse-biochimique.html",
  "qcm": 4
 },
 "bi-03": {
  "url": "lecons/bi-03-marqueurs-stress-oxydatif.html",
  "qcm": 9
 },
 "bi-05": {
  "url": "lecons/bi-05-lipides-lipoproteines.html",
  "qcm": 15,
  "entr": 20
 },
 "bi-06": {
  "url": "lecons/bi-06-biomarqueurs-cardiaques.html",
  "qcm": 10,
  "entr": 20
 },
 "bi-07": {
  "url": "lecons/bi-07-gazometrie.html",
  "qcm": 0,
  "entr": 36
 },
 "ra-01": {
  "url": "lecons/ra-01-principes-physiques-radiographie.html",
  "qcm": 9
 },
 "ra-02": {
  "url": "lecons/ra-02-ultrasons-echographie-thoracique.html",
  "qcm": 0,
  "entr": 24
 },
 "ra-03": {
  "url": "lecons/ra-03-tdm-thoracique.html",
  "qcm": 0,
  "entr": 22
 },
 "ra-04": {
  "url": "lecons/ra-04-irm-thoracique.html",
  "qcm": 5,
  "entr": 16
 },
 "ra-06": {
  "url": "lecons/ra-06-thorax-pathologique.html",
  "qcm": 15
 },
 "ra-07": {
  "url": "lecons/ra-07-dangers-irradiation-radioprotection.html",
  "qcm": 3
 },
 "an-01": {
  "url": "lecons/an-01-place-pathologie-medecine.html",
  "qcm": 4
 },
 "an-02": {
  "url": "lecons/an-02-lesions-cellulaires-tissulaires.html",
  "qcm": 23
 },
 "an-03": {
  "url": "lecons/an-03-pathologies-mec.html",
  "qcm": 11,
  "entr": 15
 },
 "an-04": {
  "url": "lecons/an-04-atherosclerose.html",
  "qcm": 16,
  "entr": 29
 },
 "an-05": {
  "url": "lecons/an-05-processus-inflammatoire.html",
  "qcm": 6,
  "entr": 12
 },
 "an-06": {
  "url": "lecons/an-06-troubles-metabolisme.html",
  "qcm": 2,
  "entr": 20
 },
 "an-07": {
  "url": "lecons/an-07-immunopathologie.html",
  "qcm": 6,
  "entr": 20
 },
 "an-08": {
  "url": "lecons/an-08-reparation-cicatrisation.html",
  "qcm": 15,
  "entr": 20
 },
 "an-09": {
  "url": "lecons/an-09-formes-inflammation.html",
  "qcm": 13,
  "entr": 20
 },
 "an-10": {
  "url": "lecons/an-10-etiologies-cancer.html",
  "qcm": 6,
  "entr": 20
 },
 "im-01": {
  "url": "lecons/im-01-introduction-immunopathologie.html",
  "qcm": 2
 },
 "im-02": {
  "url": "lecons/im-02-immunite-antibacterienne.html",
  "qcm": 4
 },
 "im-03": {
  "url": "lecons/im-03-immunite-antiparasitaire.html",
  "qcm": 5
 },
 "im-04": {
  "url": "lecons/im-04-hypersensibilite-type-1.html",
  "qcm": 12
 },
 "im-05": {
  "url": "lecons/im-05-immunite-antivirale.html",
  "qcm": 15,
  "entr": 24
 },
 "im-07": {
  "url": "lecons/im-07-hypersensibilite-type-3.html",
  "qcm": 13,
  "entr": 26
 },
 "im-08": {
  "url": "lecons/im-08-maladies-auto-immunes.html",
  "qcm": 7,
  "entr": 11
 },
 "im-11": {
  "url": "lecons/im-11-deficits-immunitaires-primitifs.html",
  "qcm": 21,
  "entr": 15
 }
};

  function applyPatch(p, fillOnly) {
    if (!p || !p.id || !window.MED_DATA || !window.MED_DATA.modules) return;
    for (var i = 0; i < window.MED_DATA.modules.length; i++) {
      var lecons = window.MED_DATA.modules[i].lecons || [];
      for (var j = 0; j < lecons.length; j++) {
        var l = lecons[j];
        if (l.id !== p.id) continue;
        if (p.url && (!fillOnly || !l.url)) l.url = p.url;   // patch de la leçon : fait foi ; secours : comble
        if (p.recu === true && !l.recu) l.recu = true;       // monotone : jamais true → false
        if (typeof p.qcm === 'number' && (!fillOnly || typeof l.qcm !== 'number')) l.qcm = p.qcm;
        if (typeof p.entr === 'number' && (!fillOnly || typeof l.entr !== 'number')) l.entr = p.entr;
        return;
      }
    }
  }

  function applyFallback() {
    for (var id in FALLBACK) {
      var f = FALLBACK[id];
      applyPatch({ id: id, url: f.url, recu: true, qcm: f.qcm, entr: f.entr }, true);
    }
  }

  window.__applySeenmedPatches = function () {
    var P = window.MED_DATA_PATCHES || [];
    for (var i = 0; i < P.length; i++) applyPatch(P[i], false);
  };
  window.__applySeenmedData = function () { applyFallback(); window.__applySeenmedPatches(); };

  /* 1) Secours synchrone — ne dépend d'aucun chargement. */
  try { applyFallback(); } catch (e) { /* MED_DATA seul fera foi */ }

  /* 2) Patchs par leçon — document.write : exécution ordonnée pendant
        le parsing (le finaliseur tourne après les patchs et avant la
        suite du document, donc avant dashboard.js). Fichier absent =
        ignoré en silence. */
  try {
    var ids = [];
    if (window.MED_DATA && window.MED_DATA.modules) {
      window.MED_DATA.modules.forEach(function (m) {
        (m.lecons || []).forEach(function (l) { ids.push(l.id); });
      });
    }
    if (ids.length && document.write) {
      var html = '';
      for (var k = 0; k < ids.length; k++)
        html += '<script src="js/data-patches/' + ids[k] + '.js?v=1"><\/script>';
      html += '<script>window.__applySeenmedPatches && window.__applySeenmedPatches();<\/script>';
      document.write(html);
    }
  } catch (e) { /* le secours synchrone a déjà protégé le tableau de bord */ }
})();
