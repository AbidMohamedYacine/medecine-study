/* ============================================================
   SEENmed — data.js
   Base de données des modules & leçons (3ème année — UI 1)
   • qcm  : nombre de QCM d'annales recensés (ELITE CARDIO 3EME,
            annales PROMO 2018 → 2022 + rattrapages)
   • recu : cours déjà reçu en amphi (état au 06/10/2026)
   • url  : page du résumé si déjà construite
   L'importance EMD = nb de QCM d'annales (leçons les plus
   tombées d'abord).
   ============================================================ */

window.MED_DATA = {
    modules: [
        {
            id: 'psycho',
            nom: 'Psychologie Médicale',
            desc: 'Sémiologie psychologique : communication, entretien, annonce, douleur, stress.',
            icon: 'fa-brain',
            color: 'purple',
            unite: 'Cardio-Respiratoire',
            lecons: [
                /* Meme cours que sg-00 (il figure aux deux programmes) : on le
                   garde visible ici, mais sa progression est celle de sg-00 et
                   il ne compte qu'UNE fois dans les totaux. */
                { id: 'psy-01', nom: 'Sémantique médicale', qcm: 7, recu: true,
                  alias: 'sg-00',
                  url: 'lecons/sg-00-semantique-medicale.html' },
                { id: 'psy-02', nom: 'Aspects communicationnels et examen mental', qcm: 6, recu: true,
                  url: 'lecons/psy-02-aspects-communicationnels-et-examen-mental.html' },
                { id: 'psy-03', nom: "L'entrevue médicale", qcm: 4, recu: true,
                  url: 'lecons/psy-03-l-entrevue-medicale.html' },
                { id: 'psy-04', nom: "L'annonce d'une maladie grave", qcm: 6, recu: true,
                  url: 'lecons/psy-04-annonce-d-une-maladie-grave.html' },
                { id: 'psy-05', nom: 'Psychologie de la douleur', qcm: 4, recu: true,
                  url: 'lecons/psy-05-psychologie-de-la-douleur.html' },
                { id: 'psy-06', nom: 'Cours inaugural de sémiologie', qcm: 0, recu: false },
                { id: 'psy-07', nom: 'Stress et maladies psychosomatiques', qcm: 6, recu: true,
                  url: 'lecons/psy-07-stress-et-maladies-psychosomatiques.html' },
                { id: 'psy-08', nom: 'Psychologie de la prescription', qcm: 2, recu: false },
                { id: 'psy-09', nom: 'Fonctionnement de la personnalité', qcm: 4, recu: false }
            ]
        },
        {
            id: 'semio-gen',
            nom: 'Sémiologie Générale',
            desc: 'Les fondations : sémantique, observation, raisonnement clinique, signes.',
            icon: 'fa-stethoscope',
            color: 'blue',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'sg-00', nom: 'Notions de sémantique médicale', qcm: 7, recu: true,
                  url: 'lecons/sg-00-semantique-medicale.html' },
                { id: 'sg-01', nom: 'Observation médicale', qcm: 8, recu: true,
                  url: 'lecons/sg-01-observation-medicale.html' },
                { id: 'sg-02', nom: 'Bases du raisonnement clinique', qcm: 4, recu: true,
                  url: 'lecons/sg-02-raisonnement-clinique.html' },
                { id: 'sg-03', nom: 'Abord et examen clinique du patient', qcm: 5, recu: true,
                  url: 'lecons/sg-03-abord-examen-clinique.html' },
                { id: 'sg-04', nom: "Troubles d'hydratation", qcm: 6, recu: false },
                { id: 'sg-05', nom: 'Sémiologie pondérale', qcm: 8, recu: false }
            ]
        },
        {
            id: 'cardio',
            nom: 'Sémiologie Cardiaque',
            desc: "Cœur : bruits, douleurs, pression, ECG, souffles, insuffisance…",
            icon: 'fa-heartbeat',
            color: 'red',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'ca-01', nom: 'Les péricardites', qcm: 5, entr: 29, recu: true, url: 'lecons/ca-01-pericardites.html' },
                { id: 'ca-02', nom: 'Les douleurs thoraciques et palpitations', qcm: 9, entr: 24, recu: true, url: 'lecons/ca-02-douleurs-thoraciques.html' },
                { id: 'ca-03', nom: 'Les bruits cardiaques', qcm: 7, entr: 16, recu: true,
                  url: 'lecons/ca-03-bruits-cardiaques.html' },
                { id: 'ca-04', nom: 'La pression artérielle', qcm: 9, entr: 16, recu: true,
                  url: 'lecons/ca-04-pression-arterielle.html' },
                { id: 'ca-05', nom: 'Les bases du tracé ECG', qcm: 7, entr: 16, recu: true,
                  url: 'lecons/ca-05-bases-trace-ecg.html' },
                { id: 'ca-06', nom: "L'examen cardiaque", qcm: 10, entr: 16, recu: true,
                  url: 'lecons/ca-06-examen-cardiaque.html' },
                { id: 'ca-07', nom: 'Les souffles cardiaques', qcm: 7, recu: true, url: 'lecons/ca-07-souffles-cardiaques.html' },
                { id: 'ca-08', nom: "L'insuffisance cardiaque", qcm: 10, recu: true,
                  url: 'lecons/ca-08-insuffisance-cardiaque.html' },
                { id: 'ca-09', nom: 'Syncopes et lipothymies', qcm: 3, entr: 32, recu: true, url: 'lecons/ca-09-syncopes.html' },
                { id: 'ca-10', nom: 'Sémiologie veineuse', qcm: 4, entr: 24, recu: true, url: 'lecons/ca-10-semiologie-veineuse.html' },
                { id: 'ca-11', nom: 'Sémiologie artérielle', qcm: 6, entr: 16, recu: true, url: 'lecons/ca-11-semiologie-arterielle.html' }
            ]
        },
        {
            id: 'pneumo',
            nom: 'Sémiologie Respiratoire',
            desc: 'Poumon : dyspnée, toux, expectoration, hémoptysie, syndromes…',
            icon: 'fa-lungs',
            color: 'teal',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'pn-01', nom: 'Sémiologie de la dyspnée', qcm: 6, recu: false },
                { id: 'pn-02', nom: 'Douleurs thoraciques en pneumologie', qcm: 3, recu: false },
                { id: 'pn-03', nom: 'Sémiologie de la toux', qcm: 4, recu: false },
                { id: 'pn-04', nom: 'Expectoration / vomique', qcm: 8, recu: false },
                { id: 'pn-05', nom: "L'hémoptysie", qcm: 5, recu: false },
                { id: 'pn-06', nom: 'La dysphonie', qcm: 3, recu: false },
                { id: 'pn-07', nom: 'Signes physiques en pneumologie', qcm: 5, recu: false },
                { id: 'pn-08', nom: 'Les syndromes médiastinaux', qcm: 4, recu: false },
                { id: 'pn-09', nom: 'Les syndromes pulmonaires', qcm: 3, recu: false },
                { id: 'pn-10', nom: 'Les syndromes bronchiques', qcm: 1, recu: false },
                { id: 'pn-11', nom: 'Les syndromes pleuraux', qcm: 4, recu: false },
                { id: 'pn-12', nom: 'La ponction pleurale', qcm: 3, recu: false }
            ]
        },
        {
            id: 'physiopath',
            nom: 'Physiopathologie',
            desc: 'Mécanismes : thermorégulation, hydrosodé, chocs, HTA, OAP…',
            icon: 'fa-wave-square',
            color: 'orange',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'ph-01', nom: 'Troubles de la thermorégulation', qcm: 3, recu: true,
                  url: 'lecons/ph-01-thermoregulation.html' },
                { id: 'ph-02', nom: 'Physiopathologie de la dénutrition', qcm: 1, entr: 16, recu: true, url: 'lecons/ph-02-denutrition.html' },
                { id: 'ph-03', nom: "Les troubles de l'eau et du sodium", qcm: 8, recu: true,
                  url: 'lecons/ph-03-troubles-hydrosodes.html' },
                { id: 'ph-04', nom: "Physiopathologie de l'insuffisance cardiaque", qcm: 0, entr: 22, recu: true,
                  url: 'lecons/ph-04-insuffisance-cardiaque.html' },
                { id: 'ph-05', nom: "États de choc hypovolémique", qcm: 5, entr: 16, recu: true,
                  url: 'lecons/ph-05-choc-hypovolemique.html' },
                { id: 'ph-06', nom: 'États de choc septique', qcm: 6, entr: 16, recu: true, url: 'lecons/ph-06-choc-septique.html' },
                { id: 'ph-07', nom: 'États de choc cardiogénique', qcm: 2, entr: 16, recu: true, url: 'lecons/ph-07-choc-cardiogenique.html' },
                { id: 'ph-08', nom: 'États de choc anaphylactique', qcm: 2, entr: 16, recu: true, url: 'lecons/ph-08-choc-anaphylactique.html' },
                { id: 'ph-09', nom: "L'hypertension artérielle", qcm: 4, recu: false },
                { id: 'ph-10', nom: "L'ŒAP (œdème aigu du poumon)", qcm: 3, recu: true,
                  url: 'lecons/ph-10-oap.html' },
                { id: 'ph-11', nom: "Les troubles de l'hématose", qcm: 2, recu: true, entr: 16, url: 'lecons/ph-11-troubles-hematose.html' },
                { id: 'ph-12', nom: "L'insuffisance respiratoire", qcm: 2, recu: true, entr: 16, url: 'lecons/ph-12-insuffisance-respiratoire.html' },
                { id: 'ph-13', nom: 'La maladie thromboembolique', qcm: 1, entr: 17, recu: true, url: 'lecons/ph-13-maladie-thromboembolique.html' }
            ]
        },
        {
            id: 'biochimie',
            nom: 'Biochimie',
            desc: 'Homme sain, stress oxydatif, lipides, biomarqueurs, gaz du sang…',
            icon: 'fa-flask',
            color: 'green',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'bi-01', nom: "Biochimie de l'homme sain", qcm: 0, entr: 24, recu: true,
                  url: 'lecons/bi-01-biochimie-homme-sain.html' },
                { id: 'bi-02', nom: "Les différentes étapes de l'analyse biochimique", qcm: 4, recu: true,
                  url: 'lecons/bi-02-etapes-analyse-biochimique.html' },
                { id: 'bi-03', nom: 'Les marqueurs biologiques du stress oxydatif', qcm: 9, recu: true,
                  url: 'lecons/bi-03-marqueurs-stress-oxydatif.html' },
                { id: 'bi-04', nom: "Les liquides d'épanchement (de ponction)", qcm: 6, recu: false },
                { id: 'bi-05', nom: 'Exploration du métabolisme des lipides et lipoprotéines', qcm: 15, recu: false },
                { id: 'bi-06', nom: 'Les biomarqueurs cardiaques', qcm: 10, recu: false },
                { id: 'bi-07', nom: "La gazométrie", qcm: 0, entr: 36, recu: true,
                  url: 'lecons/bi-07-gazometrie.html' }
            ]
        },
        {
            id: 'radio',
            nom: 'Radiologie',
            desc: 'Rayons X, écho, TDM, IRM, thorax pathologique, radioprotection…',
            icon: 'fa-x-ray',
            color: 'yellow',
            unite: 'Cardio-Respiratoire',
            lecons: [
                { id: 'ra-01', nom: 'Principes physiques de la radiographie standard', qcm: 9, recu: true,
                  url: 'lecons/ra-01-principes-physiques-radiographie.html' },
                { id: 'ra-02', nom: 'Les ultrasons — échographie thoracique', qcm: 0, entr: 24, recu: true,
                  url: 'lecons/ra-02-ultrasons-echographie-thoracique.html' },
                { id: 'ra-03', nom: 'La TDM thoracique', qcm: 0, entr: 22, recu: true, url: 'lecons/ra-03-tdm-thoracique.html' },
                { id: 'ra-04', nom: "L'IRM thoracique", qcm: 5, entr: 16, recu: true,
                  url: 'lecons/ra-04-irm-thoracique.html' },
                { id: 'ra-05', nom: 'Imagerie et radioanatomie du cœur', qcm: 17, recu: false },
                { id: 'ra-06', nom: 'Le thorax pathologique (syndromes radiologiques)', qcm: 15, recu: true,
                  url: 'lecons/ra-06-thorax-pathologique.html' },
                { id: 'ra-07', nom: "Dangers de l'irradiation et radioprotection", qcm: 3, recu: true,
                  url: 'lecons/ra-07-dangers-irradiation-radioprotection.html' }
            ]
        },
        {
            id: 'anapath',
            nom: 'Anatomopathologie',
            desc: 'Module séparé — AN-01 à AN-10 construites : lésions, inflammation, tumeurs…',
            icon: 'fa-microscope',
            color: 'pink',
            unite: 'Module séparé',
            lecons: [
                { id: 'an-01', nom: 'Place de la pathologie en médecine', qcm: 4, recu: true,
                  url: 'lecons/an-01-place-pathologie-medecine.html' },
                { id: 'an-02', nom: 'Lésions cellulaires et tissulaires', qcm: 23, recu: true,
                  url: 'lecons/an-02-lesions-cellulaires-tissulaires.html' },
                { id: 'an-03', nom: 'Pathologies de la MEC', qcm: 11, entr: 15, recu: true,
                  url: 'lecons/an-03-pathologies-mec.html' },
                { id: 'an-04', nom: "L'athérosclérose", qcm: 16, entr: 29, recu: true,
                  url: 'lecons/an-04-atherosclerose.html' },
                { id: 'an-05', nom: 'Le processus inflammatoire', url: 'lecons/an-05-processus-inflammatoire.html', qcm: 6, recu: true, entr: 12 },
                { id: 'an-06', nom: 'Les troubles du métabolisme', qcm: 2, entr: 20, recu: true,
                  url: 'lecons/an-06-troubles-metabolisme.html' },
                { id: 'an-07', nom: 'Immunopathologie', qcm: 6, entr: 20, recu: true,
                  url: 'lecons/an-07-immunopathologie.html' },
                { id: 'an-08', nom: 'Réparation — cicatrisation', qcm: 15, entr: 20, recu: true,
                  url: 'lecons/an-08-reparation-cicatrisation.html' },
                { id: 'an-09', nom: "Les formes de l'inflammation", qcm: 13, entr: 20, recu: true,
                  url: 'lecons/an-09-formes-inflammation.html' },
                { id: 'an-10', nom: "Étiologie du cancer", qcm: 6, entr: 20, recu: true,
                  url: 'lecons/an-10-etiologies-cancer.html' }
            ]
        },
        {
            id: 'immuno',
            nom: 'Immunologie',
            desc: 'Module séparé — 20+ cours : immunités, hypersensibilités, déficits…',
            icon: 'fa-shield-virus',
            color: 'teal',
            unite: 'Module séparé',
            lecons: [
                { id: 'im-01', nom: "Introduction à l'immunopathologie", qcm: 2, recu: true,
                  url: 'lecons/im-01-introduction-immunopathologie.html' },
                { id: 'im-02', nom: "L'immunité antibactérienne", qcm: 4, recu: true,
                  url: 'lecons/im-02-immunite-antibacterienne.html' },
                { id: 'im-03', nom: "L'immunité antiparasitaire", qcm: 5, recu: true,
                  url: 'lecons/im-03-immunite-antiparasitaire.html' },
                { id: 'im-04', nom: "Hypersensibilité immédiate (type I)", qcm: 12, recu: true, url: 'lecons/im-04-hypersensibilite-type-1.html' },
                { id: 'im-05', nom: "L'immunité antivirale", qcm: 15, entr: 24, recu: true, url: 'lecons/im-05-immunite-antivirale.html' },
                { id: 'im-06', nom: 'Hypersensibilité type II', qcm: 0, recu: false },
                { id: 'im-07', nom: 'Hypersensibilité type III', qcm: 13, entr: 26, recu: true, url: 'lecons/im-07-hypersensibilite-type-3.html' },
                { id: 'im-08', nom: 'Auto-immunité et maladies auto-immunes (1)', url: 'lecons/im-08-maladies-auto-immunes.html', qcm: 7, recu: true, entr: 11 },
                { id: 'im-09', nom: 'Auto-immunité et maladies auto-immunes (2)', qcm: 0, recu: false },
                { id: 'im-10', nom: 'Hypersensibilité retardée (type IV)', qcm: 0, recu: false },
                { id: 'im-11', nom: 'Les déficits immunitaires primitifs (1)', qcm: 0, recu: false },
                { id: 'im-12', nom: 'Les déficits immunitaires primitifs (2)', qcm: 0, recu: false },
                { id: 'im-13', nom: 'Immunologie de la transplantation', qcm: 0, recu: false },
                { id: 'im-14', nom: 'Les syndromes lymphoprolifératifs (1)', qcm: 0, recu: false },
                { id: 'im-15', nom: 'Les syndromes lymphoprolifératifs (2)', qcm: 0, recu: false },
                { id: 'im-16', nom: "L'immunothérapie — immunosuppression (1)", qcm: 0, recu: false },
                { id: 'im-17', nom: "L'immunothérapie — immunosuppression (2)", qcm: 0, recu: false }
            ]
        }
    ]
};

/* ---------- helpers ---------- */
window.MED_DATA.importantce = function (lecon) { return lecon.qcm; };

window.MED_DATA.totalLecons = function () {
    return this.modules.reduce(function (n, m) { return n + m.lecons.length; }, 0);
};
/* Nombre de resumes REELLEMENT construits (ceux qui ont une page).
   C'est le seul denominateur honnete pour un pourcentage de maitrise :
   compter sur les 105 lecons du programme afficherait 2 % a quelqu'un qui a
   termine tout ce qui existe. L'accueil, les cartes de module et la page
   Progression doivent tous passer par ici. */
/* Total du site : chaque PAGE compte une fois, meme si deux modules
   l'affichent tous les deux (sinon 17 pages donneraient 18 resumes). */
window.MED_DATA.totalDispo = function () {
    var self = this, vus = {};
    this.modules.forEach(function (m) {
        m.lecons.forEach(function (l) { if (l.url) vus[self.refId(l)] = 1; });
    });
    return Object.keys(vus).length;
};
/* Vue d'un module : l'alias compte ici, car la lecon est bien au programme
   de ce module et sa ligne s'affiche « Maitrisee ». La barre doit le dire. */
window.MED_DATA.disposDe = function (m) {
    return m.lecons.filter(function (l) { return !!l.url; }).length;
};
window.MED_DATA.faitesDe = function (m, P) {
    var self = this;
    return m.lecons.filter(function (l) {
        return l.url && P && P.getLecon(self.refId(l)).done;
    }).length;
};
/* Identifiant sous lequel la progression d'une lecon est reellement stockee.
   Deux entrees peuvent partager une meme page (meme cours a deux programmes) :
   elles doivent alors partager un seul et meme etat. */
window.MED_DATA.refId = function (lecon) { return lecon.alias || lecon.id; };
window.MED_DATA.totalQcm = function () {
    return this.modules.reduce(function (n, m) {
        return n + m.lecons.reduce(function (s, l) { return s + (l.qcm || 0); }, 0);
    }, 0);
};
window.MED_DATA.getLecon = function (id) {
    for (var i = 0; i < this.modules.length; i++) {
        var m = this.modules[i];
        for (var j = 0; j < m.lecons.length; j++) {
            if (m.lecons[j].id === id) return { module: m, lecon: m.lecons[j] };
        }
    }
    return null;
};
