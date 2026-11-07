#!/usr/bin/env python3
"""Brouillon de ca-04 (PAS LIVRABLE). Écrit uniquement dans un site temporaire.

Exécuter preparer_media.cjs avant le builder ; évalue les vrais contrats moteurs.
Le recueil est affiché avec son corrigé imprimé et ses ambiguïtés, non comme
corrigé officiel indépendant. Toutes les données ci-dessous doivent être relues.
"""
import sys, json, html, re, random
from pathlib import Path
from contenu_ca04 import SECTIONS
from render_qcm_recueil import render_recueil
from qcm_ar import QUESTIONS, OPTIONS

if len(sys.argv) != 2 or not sys.argv[1].startswith('/tmp/'):
    raise SystemExit('usage: build_ca04.py /tmp/.../medstudy (site temporaire uniquement)')
site=Path(sys.argv[1]); template=Path('/tmp/ca04-original-skeleton.html')
if not template.exists():
    template.write_text((site/'lecons/ca-04-pression-arterielle.html').read_text(encoding='utf-8'),encoding='utf-8')
source=template.read_text(encoding='utf-8')
head=source[:source.index('    <!-- ============ HERO DE LEÇON ============ -->')]
# Le bandeau du dictionnaire et son bouton Fermer doivent passer devant la
# navbar fixe. Correction locale à cette leçon, sans modifier les autres pages.
head=head.replace('</head>', '<style>body[data-lesson-id="ca-04"] .kw-panel{z-index:1102}body[data-lesson-id="ca-04"] .kw-backdrop{z-index:1101}@media(max-width:640px){body[data-lesson-id="ca-04"] .flashsheet.ff-2x2{grid-template-columns:1fr}}</style>\n</head>', 1)
footer=source[source.index('    <footer class="footer">'):source.index('<script type="application/json" id="cineData">')]
footer=re.sub(r'<img\b[^>]*>','',footer)
H=html.escape
imgbase='../assets/img/ca-04-delta36/'
audiobase='../assets/audio/ca-04-delta36/'
AR={}

def tr(k,fr,ar,tag='div',cls=''):
    if k in AR: raise ValueError('clé arabe dupliquée: '+k)
    AR[k]=ar
    return f'<{tag}{(" class="+chr(34)+cls+chr(34)) if cls else ""} data-tr="{k}">{fr}</{tag}>'

def visual(src,alt,cls='section-visual'):
    w,h=(1440,1080) if src.startswith('reel/') else (1376,768)
    return f'<figure class="{cls} reveal"><img src="{imgbase+H(src,quote=True)}" alt="{H(alt,quote=True)}" loading="lazy" width="{w}" height="{h}"></figure>'

def sec_start(sid,title,sub='',attr=''):
    return f'<section class="lsection" id="{sid}"{attr}><div class="lsection-head"><div class="lsection-num icon-only"><i class="fa-solid fa-heart-pulse"></i></div><div><h2>{title}</h2><div class="lsub">{sub}</div></div></div>'

parts=[head, f'''<header class="lesson-hero"><div class="container"><div class="lesson-hero-grid"><div><div class="crumbs"><a href="../index.html">Accueil</a> › Cardio-respiratoire › ca-04</div><h1>La <span class="highlight">pression artérielle</span></h1><div class="lesson-meta"><span class="chip chip-mod">Cardio-respiratoire · 3e année</span><span class="chip">Cours Dr Seddini A. · EHU Oran</span><span class="chip">Recueil ELITE CARDIO · 9 questions</span></div><div class="lesson-actions"><a href="#vue" class="btn btn-primary">Commencer</a><a href="#annales" class="btn btn-outline">QCM du recueil</a><button class="btn btn-outline" id="markDoneBtn">Marquer comme maîtrisée</button></div></div><div class="lesson-hero-visual"><img src="{imgbase}hero.webp" alt="Médecin et patient examinant un tensiomètre et un carnet de mesures." width="1376" height="768"></div></div></div></header>''']
nav=[('vue','Vue d’ensemble'),('mindmap','Plan'),('cine','Ciné')]+[(s['id'],f"{i}. {s['nav']}") for i,s in enumerate(SECTIONS,1)]+[('methode','Méthode'),('connexions','Connexions'),('annales','Recueil'),('entrainement','Entraînement'),('fiche','Fiche flash'),('flashcards','Flashcards'),('resume-total','Résumé')]
parts.append('<div class="lesson-nav" id="lessonNav"><div class="lesson-nav-inner"><div class="lesson-tabs">'+''.join(f'<button class="ltab{" active" if i==0 else ""}" data-target="{sid}">{H(t)}</button>' for i,(sid,t) in enumerate(nav))+'</div><div class="lesson-progress-wrap"><span id="lessonProgressPct">0%</span><div class="lesson-progress-bar"><div class="lesson-progress-fill" id="lessonProgressFill"></div></div></div></div></div><main class="lesson-body"><div class="container">')
parts.append(sec_start('vue','Vue d’ensemble','Du geste correct à l’interprétation des chiffres.'))
parts.append(tr('vue-1', '<b>Comprendre :</b> la pression artérielle a deux chiffres, varie au cours du temps et se mesure pour diagnostiquer ou surveiller. <b>Mesurer :</b> repos, brassard adapté, bras soutenu, méthode rigoureuse. <b>Confirmer :</b> compléter la consultation par automesure ou MAPA. <b>Interpréter :</b> les seuils dépendent du lieu et le support diverge pour la nuit.', '<b>نفهم:</b> للضغط الشرياني رقمان وهو متغير ويقاس للتشخيص والمراقبة. <b>نقيس:</b> راحة وكفة مناسبة وذراع مسندة وطريقة دقيقة. <b>نؤكد:</b> يستكمل قياس العيادة بالقياس الذاتي أو المراقبة المتنقلة. <b>نفسر:</b> تختلف الحدود حسب المكان ويختلف الدرس في حد الليل.',cls='lbox'))
parts.append('</section>')
parts.append(sec_start('mindmap','Plan du cours','La chaîne logique : comprendre → mesurer → confirmer → interpréter.'))
parts.append(tr('plan-1','<ol><li>Définition et variabilité.</li><li>Brassard, auscultation et palpation.</li><li>Consultation, appareils et erreurs.</li><li>Automesure et MAPA.</li><li>Seuils et profils.</li></ol>','<ol><li>التعريف والتغير.</li><li>الكفة والتسمع والجس.</li><li>العيادة والأجهزة والأخطاء.</li><li>القياس الذاتي والمراقبة المتنقلة.</li><li>الحدود والأنماط.</li></ol>',cls='lbox'))
parts.append('</section>')
parts.append(sec_start('cine','Ciné-révision','Chapitres français ; résumé final en français et arabe.'))
parts.append('<div id="cinePlayer"></div></section>')
chapters=[]
for i,s in enumerate(SECTIONS):
    parts.append(sec_start(s['id'],f'{i+1}. {H(s["titre"])}',H(s['source'])))
    parts.append(visual(s['img'],s['alt']))
    parts.append(f'<div class="cine-spot reveal" data-ch="{i}"></div>')
    for j,(fr,ar) in enumerate(zip(s['fr'],s['ar']),1):
        parts.append(tr(f's{i+1}-{j}',f'<p>{H(fr)}</p>',f'<p>{ar}</p>',cls='lbox reveal'))
    if i==9:
        parts.append(visual('reel/diapo-44.png','Diapositive originale indiquant que la pression nocturne normale est inférieure à 120 sur 70 mmHg.'))
        parts.append('<div class="lbox"><b>Références externes :</b> <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8109470/">AHA — mesure et brassard</a> · <a href="https://journals.lww.com/jhypertension/fulltext/2023/12000/2023_esh_guidelines_for_the_management_of_arterial.2.aspx">ESH 2023</a> · <a href="https://academic.oup.com/eurheartj/article/45/38/3912/7741010">ESC 2024</a>. Le support pédagogique reste identifié séparément.</div>')
    parts.append('</section>')
    chapters.append(dict(t=s['titre'],imgs=[imgbase+s['img']],fr=audiobase+f'{i+1:02}-fr.mp3'))
parts.append(sec_start('methode','Méthode de révision','Raisonner plutôt que mémoriser un chiffre isolé.'))
parts.append(tr('methode1','<ol><li>Identifier la méthode, le lieu et les conditions de prise.</li><li>Contrôler le repos, la taille du brassard et le niveau du bras.</li><li>Comparer les deux bras, puis confirmer hors cabinet.</li><li>Lire le seuil applicable et tenir compte du contexte.</li><li>Signaler les divergences du support plutôt que les effacer.</li></ol>','<ol><li>حدد الطريقة والمكان وشروط القياس.</li><li>تحقق من الراحة وحجم الكفة ومستوى الذراع.</li><li>قارن الذراعين ثم أكد القياس خارج العيادة.</li><li>اقرأ الحد المناسب وراع السياق.</li><li>اذكر اختلافات الدرس بدلا من إخفائها.</li></ol>',cls='lbox'))
parts.append('</section>')
parts.append(sec_start('connexions','Connexions','Situer le geste dans l’examen clinique.'))
parts.append(tr('connexions1','La mesure de pression complète l’examen cardiovasculaire : la comparaison des deux bras et l’évaluation en position debout apportent des informations complémentaires. Une valeur s’interprète toujours avec les symptômes, antécédents et traitements.', 'يكمل قياس الضغط الفحص القلبي الوعائي: تعطي مقارنة الذراعين والتقييم وقوفا معلومات إضافية. وتفسر القيمة دائما مع الأعراض والسوابق والعلاج.',cls='lbox'))
parts.append('</section>')
ann_html, ann_ar=render_recueil(); AR.update(ann_ar)
parts.append(sec_start('annales','QCM du recueil','Neuf questions transcrites du recueil ELITE CARDIO, pages PDF 13–14. Les réponses sont imprimées dans le recueil, pas un corrigé officiel indépendant.',' data-qcm-set="annales"'))
parts.append('<div class="qcm-section-head"><span class="chip chip-qcm">Score : <span class="qs-val">0 / 0</span></span></div>')
parts.append(ann_html+'</section>')
# Exercices recomposés à partir des propositions du recueil, clairement signalés.
qs=json.loads(Path(__file__).with_name('QCM-RECUEIL-REVUS.json').read_text())
pool=[(q['numero'], l) for q in qs for l in 'ABCDE' if q['numero'] in (1,2,3,5,6,8) and (q['numero'],l) not in {(1,'B'),(8,'C'),(8,'E')}]
rng=random.Random(36); sets=set(); exercises=[]
while len(exercises)<16:
    chosen=rng.sample(pool,5)
    yes=[l in qs[n-1]['reponse_recueil'] for n,l in chosen]
    canonical=tuple(sorted(chosen))
    if canonical in sets or sum(yes) not in (2,3): continue
    sets.add(canonical); exercises.append(chosen)
parts.append(sec_start('entrainement','Entraînement','16 exercices recomposés à partir de propositions du recueil ; ce ne sont pas 16 nouvelles annales.',' data-qcm-set="entrainement"'))
parts.append('<div class="qcm-section-head"><span class="chip chip-qcm">Score : <span class="qs-val">0 / 0</span></span></div>')
for i,chosen in enumerate(exercises,1):
    ans=[l for l,(n,original) in zip('ABCDE',chosen) if original in qs[n-1]['reponse_recueil']]
    qid=f'ent-{i}'
    opts=[]; expfr=[]; expar=[]
    for letter,(n,old) in zip('ABCDE',chosen):
        q=qs[n-1]; fact=q['propositions'][old]; x=q['explications'][old]; good=old in q['reponse_recueil']; c='t' if good else 'f'
        # Une proposition reprise sans son sujet peut changer de sens : préserver
        # le contexte de la question originale dans les deux langues.
        context_fr=q['enonce']; context_ar=QUESTIONS[n-1]
        k=f'{qid}-{letter}'; AR[k]=H(context_ar)+' '+H(OPTIONS[n-1][ord(old)-65])
        opts.append(f'<li data-l="{letter}"><span class="ql">{letter}</span><span class="qtxt" data-tr="{k}">{H(context_fr)} {H(fact)}</span><span class="xe"></span></li>')
        expfr.append(f'<div class="qexp-item {c}"><b>{letter} — {"À COCHER" if good else "À NE PAS COCHER"}.</b> Contexte initial : {H(context_fr)} {H(x["fr"])} (recueil Q{n}{old})</div>')
        expar.append(f'<div class="qexp-item {c}"><b><bdi class="fr-plain">{letter}</bdi> — {"يختار" if good else "لا يختار"}.</b> السياق الأصلي: {H(context_ar)} {H(x["ar"])}</div>')
    AR[qid+'-q']='اختر العبارات الصحيحة عن قياس الضغط الشرياني.'
    AR[qid+'-exp']='<div class="qexp-title">التفسير اقتراحا باقتراح</div>'+''.join(expar)+f'<div class="qexp-memo">الجواب: <bdi class="fr-plain">{"".join(ans)}</bdi>.</div>'
    encoded=H(json.dumps(ans),quote=True)
    parts.append(f'<div class="qblock reveal" data-answer="{encoded}"><div class="qhead"><div class="qtext">{i}. <span data-tr="{qid}-q">Quelles propositions sur la mesure de la pression artérielle sont exactes ?</span></div><span class="qsrc src-new">Révision recomposée</span></div><ul class="qch">{"".join(opts)}</ul><div class="qverdict"></div><div class="qexp" data-tr="{qid}-exp"><div class="qexp-title">Correction détaillée</div>{"".join(expfr)}<div class="qexp-memo">Réponse : {"".join(ans)}. Propositions recomposées du recueil.</div></div><button class="btn btn-primary btn-sm qcheck">Corriger</button></div>')
parts.append('</section>')
# Quatre cellules illustrées, avec contenu bilingue.
fiche=[(0,1,'Comprendre','الفهم'),(2,3,'Mesurer','القياس'),(5,6,'Cabinet','العيادة'),(7,9,'Confirmer et interpréter','التأكيد والتفسير')]
parts.append(sec_start('fiche','Fiche flash','Quatre cases illustrées pour réviser les étapes essentielles.'))
parts.append('<div class="flashsheet ff-2x2">')
for i,(a,b,title,ar_title) in enumerate(fiche):
    s,t=SECTIONS[a],SECTIONS[b]
    # Ne jamais séparer les faits du cours de leurs réserves importantes :
    # dimensions du brassard (case 2) et profils tensionnels (case 4).
    selection=[[(a,0),(a,1),(b,0),(b,1)],[(a,0),(a,1),(a,2),(b,0),(b,1)],[(a,0),(a,1),(b,0),(b,1),(b,2)],[(a,0),(a,1),(b,0),(b,1),(b,2)]][i]
    fr='<h4>'+title+'</h4><ul>'+''.join('<li>'+H(SECTIONS[j]['fr'][k])+'</li>' for j,k in selection)+'</ul>'
    ar='<h4>'+ar_title+'</h4><ul>'+''.join('<li>'+SECTIONS[j]['ar'][k]+'</li>' for j,k in selection)+'</ul>'
    # Quatre illustrations distinctes adaptées au sujet de chaque case.
    fiche_img=[('fiche-comprendre.webp','Coupe d’une artère et courbe de pression, avec maximum systolique et minimum diastolique.'),('choix-brassard.webp','Choix du brassard selon la circonférence du bras et sens des erreurs de taille.'),('fiche-cabinet.webp','Patiente au cabinet avec bras nu soutenu, brassard et appareil de mesure.'),('profils.webp','Comparaison entre consultation et domicile : profils blouse blanche et masqué.')]
    src, alt=fiche_img[i]
    # Image stays outside translated text so ar-mode never removes it.
    parts.append('<div class="flash-cell">'+visual(src,alt,cls='fiche-figure').replace('<img ','<img class="flash-img" ')+tr(f'fiche-{i}',fr,ar)+'</div>')
parts.append('</div></section>')
# Le deck de référence contient uniquement le châssis et aucun contenu médical.
fcsec=source[source.index('            <section class="lsection" id="flashcards">'):source.index('            <!-- ═══════════════ RÉSUMÉ TOTAL')]
fcsec=re.sub(r'<div class="lsub">.*?</div>','<div class="lsub">Cartes de révision à retourner puis à évaluer.</div>',fcsec,count=1,flags=re.S)
parts.append(fcsec)
parts.append(sec_start('resume-total','Résumé total','La leçon de bout en bout.'))
parts.append(tr('resume1','<p>La pression varie. Mesure fiable : repos, brassard adapté, bras au cœur, méthode et deux bras. Le premier bruit correspond à la systolique ; la disparition correspond habituellement à la diastolique. La palpation donne uniquement la systolique.</p><p>Confirmer hors cabinet par automesure ou MAPA ; comparer aux seuils adaptés au contexte. Blouse blanche : élevé au cabinet seul. Masquée : élevé hors cabinet seul. Le cours diverge sur le seuil nocturne ; voir les deux diapositives et les recommandations distinctes.</p>', '<p>يتغير الضغط. القياس الموثوق يتطلب الراحة وكفة مناسبة وذراعا بمستوى القلب وطريقة صحيحة ومقارنة الذراعين. أول صوت يمثل الانقباضي والاختفاء يمثل عادة الانبساطي؛ أما الجس فيعطي الانقباضي فقط.</p><p>يؤكد التقييم خارج العيادة بالقياس الذاتي أو المراقبة، مع حدود مناسبة للسياق. المعطف الأبيض: مرتفع في العيادة وحدها؛ المقنع: مرتفع خارجها وحدها. يختلف الدرس في حد الليل؛ راجع الشريحتين والتوصيات المستقلة.</p>',cls='lbox'))
parts.append(f'<div class="cine-spot reveal" data-ch="{len(chapters)}"></div></section>')
chapters.append(dict(t='Résumé intégral français et arabe',imgs=[imgbase+'pression.webp',imgbase+'posture.webp',imgbase+'mapa.webp'],fr=audiobase+'resume-fr.mp3',ar=audiobase+'resume-ar.mp3'))
parts.append('</div></main>'); parts.append(footer)
# Cartes : chaque réponse est explicitement reliée à un paragraphe source.
card_questions=[
('Définir la pression artérielle.',0,0),('PAS et PAD : que représentent les deux chiffres ?',0,1),('Convertir 13/8 cmHg en mmHg.',0,2),('Comment la pression varie-t-elle avec effort et sommeil ?',1,0),('Pourquoi interpréter les chiffres dans leur contexte ?',1,1),('Où placer le brassard et quel effet a une taille inadaptée ?',2,0),('Quelles différences entre le cours et l’AHA pour le brassard ?',2,2),('Où placer le stéthoscope ?',3,0),('Quels bruits repèrent PAS et PAD ?',3,1),('Quel est le désaccord de nomenclature des phases ?',3,2),('Que mesure la méthode palpatoire ?',4,0),('Quelle valeur ne donne pas la palpation ?',4,1),('Quelles conditions et combien de mesures au cabinet ?',5,0),('Comment installer le patient assis ?',5,1),('Quelles erreurs de mesure faut-il éviter ?',6,1),('Que faire en cas de différence interbras confirmée ?',6,2),('Quelle est la règle des trois du cours ?',7,0),('Quelles sont les limites de l’automesure ?',7,1),('Quel est le principe de la MAPA ?',8,0),('Quelles sont les limites de la MAPA ?',8,1),('Quels sont les seuils cabinet et domicile ?',9,0),('Quelle divergence nocturne faut-il signaler ?',9,1),('Blouse blanche et hypertension masquée : comment les distinguer ?',9,2)]
fc=[dict(id=f'ca04-{i+1:02}',q=q,a=H(SECTIONS[s]['fr'][p])) for i,(q,s,p) in enumerate(card_questions)]
terms=[('Pression artérielle',0),('Systolique',0),('Diastolique',0),('Millimètre de mercure',0),('Centimètre de mercure',0),('Variabilité',1),('Effort',1),('Émotion',1),('Sommeil',1),('Hypotension',1),('Brassard',2),('Circonférence du bras',2),('Poche gonflable',2),('Artère humérale',2),('Taille adaptée',2),('Auscultation',3),('Stéthoscope',3),('Bruits de Korotkoff',3),('Phase IV',3),('Phase V',3),('Trou auscultatoire',3),('Palpation',4),('Pouls radial',4),('Dégonflage',4),('Systolique palpatoire',4),('Repos',5),('Position assise',5),('Deux bras',5),('Hypotension orthostatique',5),('Consultation',5),('Oscillométrie',6),('Anéroïde',6),('Anisotension',6),('Différence interbras',6),('Appareil validé',6),('Automesure',7),('Règle des trois',7),('Arythmie',7),('MAPA',8),('Enregistreur',8),('Pression nocturne',8),('Hypertension blouse blanche',9),('Hypertension masquée',9),('Seuil cabinet',9),('Seuil domicile',9),('Moyenne 24 heures',9),('Seuil nocturne',9)]
from lexique_ca04 import DEFINITIONS
assert len(terms) == len(DEFINITIONS)
kw=[dict(t=t,s=SECTIONS[i]['id'],n=str(i+1),d=H(fr),a=ar) for (t,i),(fr,ar) in zip(terms,DEFINITIONS)]
def jsblock(id,obj): return f'<script type="application/json" id="{id}">'+json.dumps(obj,ensure_ascii=False).replace('</','<\\/')+'</script>'
parts.extend([jsblock('cineData',{'chapitres':chapters}),jsblock('arData',AR),jsblock('kwData',kw),jsblock('fcData',fc)])
parts.append('''<script src="../js/bg-mode.js?v=14"></script><script src="../js/progress.js?v=6"></script><script src="../js/main.js?v=6"></script><script src="../js/cardio-field.js?v=4"></script><script src="../js/lesson.js?v=12"></script><script src="../js/ar-mode.js?v=1"></script><script src="../js/keywords.js?v=2"></script><script src="../js/cine.js?v=3"></script></body></html>''')
result='\n'.join(parts)
keys=re.findall(r'data-tr="([^"]+)"',result)
if len(keys)!=len(set(keys)) or set(keys)!=set(AR): raise ValueError(f'Data AR incohérentes {set(keys)-set(AR)} / {set(AR)-set(keys)}')
out=site/'lecons/ca-04-pression-arterielle.html';out.write_text(result,encoding='utf-8')
print('BROUILLON',out,len(result),'caractères',len(nav),'sections',len(chapters),'chapitres',len(qs),'QCM recueil',len(exercises),'entraînement',len(fc),'cartes',len(kw),'mots-clés',len(keys),'blocs AR')
