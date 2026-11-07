#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder bi-06 — squelette gold + peau Biochimie (has-bio-field) dès la construction."""
import re, json, os

MS = '/tmp/seenmed-clean/medstudy'
SRC = open(os.path.join(MS, 'lecons/ra-02-ultrasons-echographie-thoracique.html'), encoding='utf-8').read()
AR = {}
OUT = []
IMG = '../assets/img/bi-06'
D1 = 'width="1536" height="1024"'
D2 = D1

def sub(key, fr, ar):
    AR[key] = ar
    return f'<div class="lsub" data-tr="{key}">{fr}</div>'

def lbox(key, icon, title, items, ar_inner):
    AR[key] = ar_inner
    lis = '\n'.join(f'                        <li>{i}</li>' for i in items)
    return f'''                <div class="lbox reveal" data-tr="{key}">
                    <div class="lbox-title"><i class="fa-solid {icon}"></i> {title}</div>
                    <ul>
{lis}
                    </ul>
                </div>'''

def mini(key, acc, icon, title, items, ar_inner, delay=''):
    AR[key] = ar_inner
    dl = f' data-delay="{delay}"' if delay else ''
    lis = '\n'.join(f'                            <li>{i}</li>' for i in items)
    return f'''                    <div class="mini-card acc-{acc} reveal"{dl} data-tr="{key}">
                        <h4><i class="fa-solid {icon}"></i> {title}</h4>
                        <ul>
{lis}
                        </ul>
                    </div>'''

def grid2(a, b):
    return f'                <div class="lgrid2">\n{a}\n{b}\n                </div>'

def fig(img, alt, caption, dims=D1, cls='section-visual reveal'):
    return f'''                <figure class="{cls}">
                    <img src="{IMG}/{img}" alt="{alt}" loading="lazy" {dims}>
                    <figcaption>{caption}</figcaption>
                </figure>'''

def spot(ch):
    return f'                <div class="cine-spot reveal" data-ch="{ch}"></div>'

def focus(items):
    lis = '\n'.join(f'                        <li>{i}</li>' for i in items)
    return f'''                <div class="qcm-focus reveal">
                    <span class="qf-sub">Ce que l'examinateur peut fabriquer avec cette seule section</span>
                    <ul>
{lis}
                    </ul>
                </div>'''

def reels(srcnote, figs):
    fs = ''
    for img, w, h, alt, cap in figs:
        fs += f'''                        <figure>
                            <img src="{IMG}/reel/{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}">
                            <figcaption>{cap}</figcaption>
                        </figure>
'''
    return f'''                <div class="reel-strip reveal">
                    <p class="reel-head">Document original du cours<span class="reel-src">{srcnote}</span></p>
                    <div class="reel-grid">
{fs}                    </div>
                </div>'''

def table(key, head, rows, ar_inner):
    AR[key] = ar_inner
    th = ''.join(f'<th>{h}</th>' for h in head)
    trs = ''
    for r in rows:
        trs += '                            <tr>\n' + ''.join(f'                                <td>{c}</td>\n' for c in r) + '                            </tr>\n'
    return f'''                <div class="ltable-wrap reveal">
                    <table class="ltable" data-tr="{key}">
                        <thead>
                            <tr>{th}</tr>
                        </thead>
                        <tbody>
{trs}                        </tbody>
                    </table>
                </div>'''

def section(sid, num, title, sub_html, blocks, comment):
    body = '\n\n'.join(blocks)
    return f'''            <!-- ═══════════════ {comment} ═══════════════ -->
            <section class="lsection" id="{sid}">
                <div class="lsection-head">
                    <div class="lsection-num n{num}">{num}</div>
                    <div>
                        <h2>{title}</h2>
                        {sub_html}
                    </div>
                </div>

{body}
            </section>'''

def arbox(icon, title_ar, items_ar):
    lis = ''.join(f'<li>{i}</li>' for i in items_ar)
    return f'<div class="lbox-title"><i class="fa-solid {icon}"></i> {title_ar}</div><ul>{lis}</ul>'

def armini(icon, title_ar, items_ar):
    lis = ''.join(f'<li>{i}</li>' for i in items_ar)
    return f'<h4><i class="fa-solid {icon}"></i> {title_ar}</h4><ul>{lis}</ul>'

FT = '<bdi class="fr-term">%s</bdi>'
FP = '<bdi class="fr-plain">%s</bdi>'

# ═══════════════ SQUELETTE (peau Biochimie appliquée immédiatement) ═══════════════
top = SRC.split('<!-- ============ NAVIGATION DE LEÇON')[0]
top = top.replace('<title>Les ultrasons — échographie thoracique — SEENmed</title>',
                  '<title>Les biomarqueurs cardiaques — SEENmed</title>')
top = top.replace('data-lesson-id="ra-02"', 'data-lesson-id="bi-06"')
top = top.replace('has-orbital-sphere', 'has-bio-field')  # peau du module Biochimie
top = top.replace('>Radiologie</a>', '>Biochimie</a>').replace('<span>Leçon 2</span>', '<span>Leçon 6</span>')
top = re.sub(r'<h1>.*?</h1>', '<h1>Les <span class="highlight">biomarqueurs cardiaques</span></h1>', top, flags=re.S)
top = re.sub(r'(<div class="lesson-meta">).*?(</div>\s*<div class="lesson-actions">)',
             r'''\1
                <span class="chip chip-mod"><i class="fa-solid fa-flask"></i> Biochimie</span>
                <span class="chip chip-qcm"><i class="fa-solid fa-bullseye"></i> 10 QCM d'annales + 20 d'entraînement</span>
                <span class="chip chip-star"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i> Importance EMD</span>
                <span class="chip"><i class="fa-solid fa-user-doctor"></i> Dr Besbes, A — Biochimie, 2025/2026</span>
                <span class="chip chip-done"><i class="fa-solid fa-check"></i> Cours reçu</span>
            \2''', top, flags=re.S)
top = re.sub(r'(<div class="lesson-actions">).*?(</div>\s*</div>\s*<div class="lesson-hero-visual">)',
             r'''\1
                <a href="#vue" class="btn btn-primary btn-glow"><i class="fa-solid fa-play"></i> Commencer le résumé</a>
                <a href="#annales" class="btn btn-outline"><i class="fa-solid fa-award"></i> Les 10 annales</a>
                <a href="#entrainement" class="btn btn-outline"><i class="fa-solid fa-bullseye"></i> Les 20 QCM</a>
                <button class="btn btn-outline" id="markDoneBtn"><i class="fa-solid fa-graduation-cap"></i> Marquer comme maîtrisée</button>
            \2''', top, flags=re.S)
top = re.sub(r'(<div class="lesson-hero-visual">)\s*<img[^>]*>',
             r'\1\n                <img src="../assets/img/bi-06/hero.webp" alt="Illustration : aux urgences, un patient allongé se tenant la poitrine sous un moniteur ECG affichant un tracé avec sus-décalage du segment ST, et au premier plan un tube de sang étiqueté Troponine tenu par une main gantée" loading="eager" width="1536" height="1024">', top)

TABS = [
    ('vue', 'fa-compass', "Vue d'ensemble", True),
    ('mindmap', 'fa-sitemap', 'Mind Map', False),
    ('cine', 'fa-clapperboard', 'Ciné', False),
    ('enjeux', 'fa-heart-pulse', '1. Définition &amp; familles', False),
    ('necrose', 'fa-heart-crack', '2. Marqueurs de nécrose', False),
    ('troponine', 'fa-dna', '3. Le complexe troponine', False),
    ('hs', 'fa-magnifying-glass', '4. Classique vs hypersensible', False),
    ('interpretation', 'fa-scale-balanced', '5. Interpréter une troponine', False),
    ('sca', 'fa-truck-medical', '6. SCA &amp; algorithmes', False),
    ('myoglobine', 'fa-bolt', '7. Myoglobine', False),
    ('ckmb', 'fa-rotate', '8. CK-MB', False),
    ('cinetique', 'fa-chart-line', '9. La courbe des cinétiques', False),
    ('peptides', 'fa-droplet', '10. BNP &amp; NT-proBNP', False),
    ('np-clinique', 'fa-stethoscope', '11. Peptides en clinique', False),
    ('inflammation', 'fa-fire', '12. Inflammation &amp; risque', False),
    ('methode', 'fa-user-secret', 'Méthode EMD', False),
    ('connexions', 'fa-link', 'Connexions', False),
    ('annales', 'fa-award', 'QCM annales', False),
    ('entrainement', 'fa-bullseye', 'Entraînement', False),
    ('fiche', 'fa-bolt', 'Fiche flash', False),
    ('flashcards', 'fa-clone', 'Flashcards', False),
    ('resume-total', 'fa-image', 'Résumé total', False),
]
tabs_html = '\n'.join(
    f'                <button class="ltab{" active" if a else ""}" data-target="{t}"><i class="fa-solid {i}"></i> {l}</button>'
    for t, i, l, a in TABS)
navblock = SRC.split('<!-- ============ NAVIGATION DE LEÇON')[1].split('<!-- ============ CORPS DE LEÇON')[0]
navblock = re.sub(r'(<div class="lesson-tabs">).*?(</div>\s*<div class="lesson-progress-wrap">)',
                  r'\1\n' + tabs_html + r'\n            \2', navblock, flags=re.S)
nav = '<!-- ============ NAVIGATION DE LEÇON' + navblock
main_open = '''    <!-- ============ CORPS DE LEÇON ============ -->
    <main class="lesson-body">
        <div class="container">
'''

# ═══════════════ VUE D'ENSEMBLE ═══════════════
vue = '''            <!-- ═══════════════ VUE D'ENSEMBLE ═══════════════ -->
            <section class="lsection" id="vue">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-compass"></i></div>
                    <div>
                        <h2>Vue d'ensemble — l'essentiel en 60 secondes</h2>
                        ''' + sub('vue-sub',
                            'Trois familles, trois questions : le myocarde <b>meurt-il</b> (nécrose : troponine, CK-MB, myoglobine), le ventricule <b>souffre-t-il</b> (fonction : BNP, NT-proBNP), le risque <b>couve-t-il</b> (inflammation : hs-CRP, fibrinogène). Sur 10 annales, <b>la troponine et les cinétiques dominent</b>.',
                            'ثلاث عائلات وثلاثة أسئلة: هل <b>يموت</b> عضل القلب (النخر: تروبونين، ' + FP % 'CK-MB' + '، ميوغلوبين)، هل <b>يعاني</b> البطين (الوظيفة: ' + FP % 'BNP' + '، ' + FP % 'NT-proBNP' + '، هل <b>يختمر</b> الخطر (الالتهاب: ' + FP % 'hs-CRP' + '، فيبرينوجين). من بين 10 أسئلة، <b>تهيمن التروبونين والحركيات</b>.') + '''
                    </div>
                </div>

                <div class="overview-grid">
                    <div class="essence reveal">
                        <h3><i class="fa-solid fa-bolt"></i> L'essentiel</h3>
                        <ul>
                            <li><b>Biomarqueur cardiaque</b> = substance <b>mesurable dans le sang</b>, produite/libérée par le cœur atteint, pour le <b>diagnostic, le pronostic, le suivi</b>. Idéal : <b>sensible, spécifique, précoce</b>.</li>
                            <li><b>Troponine</b> = marqueur de <b>référence</b> du SCA. Complexe <b>TnC</b> (calcium) · <b>TnI</b> (inhibitrice) · <b>TnT</b> (tropomyosine) ; <b>I et T cardiospécifiques, C non</b>.</li>
                            <li><b>Hypersensible</b> : détectable en <b>1–2 h</b> (classique 3–6 h) ; <b>TnI 3–6 j, TnT jusqu'à 10 j</b> — d'où le diagnostic <b>rétrospectif</b>.</li>
                            <li><b>Troponine ↑ ≠ infarctus</b> : myocardite, IC, EP, sepsis, insuffisance rénale, effort prolongé… Interprétation = <b>anamnèse + clinique + ECG</b>, toujours.</li>
                            <li><b>STEMI</b> : reperfusion <b>sans attendre</b> la troponine. <b>NSTEMI</b> : la <b>cinétique</b> décide (H0 → H1–H3 en hs, H6–H9 en classique) ; <b>2 normales = IDM exclu</b>.</li>
                            <li><b>Myoglobine</b> : la plus précoce (<b>2 h</b>, pic 4–12 h, normale à 24 h) mais <b>non spécifique</b> (muscle strié) → supplantée.</li>
                            <li><b>CK-MB</b> : 4–6 h, normale en <b>2–3 j</b> → voyait les <b>réinfarctus précoces</b> ; supplantée aussi.</li>
                            <li><b>BNP / NT-proBNP</b> : sécrétés par les <b>ventricules</b> distendus ; BNP actif (vasodilatation, diurèse, natriurèse), NT-proBNP inactif et stable → <b>dyspnée cardiaque vs pulmonaire</b>, diagnostic/pronostic/suivi de l'IC.</li>
                            <li><b>hs-CRP</b> : &lt; 1 risque faible · 1–3 intermédiaire · <b>&gt; 3 mg/L élevé</b> ; fibrinogène = inflammation vasculaire + thrombose.</li>
                            <li>Le mot de la fin du cours : les marqueurs <b>complètent, ne remplacent ni la clinique ni l'imagerie</b>.</li>
                        </ul>
                    </div>
                    <div class="roadmap reveal" data-delay="1">
                        <h3><i class="fa-solid fa-route"></i> Où on va — la feuille de route</h3>
                        <ol>
                            <li><b>Définition &amp; familles</b> — ce qu'on demande à un marqueur</li>
                            <li><b>Marqueurs de nécrose</b> — le principe « la cellule meurt »</li>
                            <li><b>Le complexe troponine</b> — C, I, T et la spécificité ★★</li>
                            <li><b>Classique vs hypersensible</b> — voir en 1–2 h ★★</li>
                            <li><b>Interpréter une troponine</b> — élevée sans infarctus ★★</li>
                            <li><b>SCA &amp; algorithmes</b> — STEMI, NSTEMI, H0 → H1 ★★</li>
                            <li><b>Myoglobine</b> — la sprinteuse déclassée</li>
                            <li><b>CK-MB</b> — l'œil du réinfarctus</li>
                            <li><b>La courbe des cinétiques</b> — trois signatures, un graphique</li>
                            <li><b>BNP &amp; NT-proBNP</b> — la voix du ventricule distendu ★★</li>
                            <li><b>Peptides en clinique</b> — dyspnée, pronostic, variations ★★</li>
                            <li><b>Inflammation &amp; risque</b> — hs-CRP, fibrinogène</li>
                            <li><b>La méthode de l'examinateur</b> — puis <b>10 annales</b> et <b>20 QCM</b></li>
                        </ol>
                    </div>
                </div>

''' + lbox('vue-box1', 'fa-circle-info', 'Transparence : la source de cette leçon et ses QCM',
    [
        'Leçon construite sur le cours du <b>Dr Besbes, A (2025/2026, 32 diapositives)</b> — le même enseignant que les lipides (bi-05) — lu en entier, tableaux et courbe de cinétique compris. <b>Versionnée N-1</b> : à l\'arrivée du cours de cette année, seuls les écarts seront patchés.',
        'Les <b>10 QCM d\'annales</b> sont <b>authentiques</b> : recueil ELITE CARDIO 3ᵉ, Biochimie §5 (PROMO 2018 → 2022), texte et <b>corrigés officiels</b> repris sans retouche.',
        'Trois notions sont <b>testées mais absentes des diapositives</b> — déclassement d\'<b>ASAT/ALAT/LDH</b>, non-recommandation de <b>copeptine/h-FABP</b>, vocabulaire <b>VPN/VPP</b> : enseignées <b>au niveau exact des annales</b> et signalées « à confirmer sur le cours ».',
    ],
    arbox('fa-circle-info', 'شفافية: مصدر هذا الدرس وأسئلته', [
        'الدرس مبنيّ على محاضرة <b>الدكتورة بسبس (2025/2026، 32 شريحة)</b> — نفس أستاذة درس الدهون — قُرئت كاملة بما فيها الجداول ومنحنى الحركية. <b>إصدار N-1</b>: عند وصول محاضرة هذه السنة لن تُصحَّح إلا الفروقات.',
        '<b>الأسئلة العشرة</b> في قسم الامتحانات <b>أصلية</b>: مجموعة ' + FP % 'ELITE CARDIO' + '، كيمياء حيوية §5 (دفعات 2018 ← 2022)، <b>بالنص والتصحيح الرسمي</b>.',
        'ثلاثة مفاهيم <b>مختبَرة لكنها غائبة عن الشرائح</b> — إسقاط <b>' + FP % 'ASAT/ALAT/LDH' + '</b>، وعدم التوصية بـ<b>' + FT % 'copeptine/h-FABP' + '، ومصطلحا <b>القيمة التكهنية</b>: تُدرَّس <b>بمستوى الامتحانات بالضبط</b> مع تنبيه «للتثبت من المحاضرة».',
    ])) + '''
            </section>'''
OUT.append(vue)

OUT.append('''            <!-- ═══════════════ MIND MAP ═══════════════ -->
            <section class="lsection" id="mindmap">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-sitemap"></i></div>
                    <div>
                        <h2>Mind Map — la leçon vue du ciel</h2>
                        <div class="lsub">Un cœur, <b>trois questions</b> : <b>meurt-il</b> (nécrose), <b>souffre-t-il</b> (fonction), le risque <b>couve-t-il</b> (inflammation). Chaque famille de marqueurs répond à une seule de ces questions — clique pour agrandir.</div>
                    </div>
                </div>

''' + fig('mindmap.webp',
    "Mind map des biomarqueurs cardiaques en trois familles autour d'un cœur en coupe : branche nécrose vers une cellule myocardique détruite libérant troponine CK-MB et myoglobine, branche fonction vers un ventricule distendu émettant BNP et NT-proBNP, branche inflammation vers une paroi artérielle enflammée avec hs-CRP et fibrinogène",
    '🗺️ <b>La carte mentale :</b> nécrose → troponine · fonction → peptides · inflammation → hs-CRP') + '''
            </section>

            <!-- ═══════════════ CINÉ-RÉVISION ═══════════════ -->
            <section class="lsection" id="cine">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-clapperboard"></i></div>
                    <div>
                        <h2>Ciné-révision — la leçon racontée</h2>
                        <div class="lsub">Les planches défilent, la voix explique en reliant les idées : <b>huit chapitres en français</b>, plus le <b>résumé total en français et en arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.</div>
                    </div>
                </div>
                <div id="cinePlayer" class="reveal"></div>
            </section>''')

# ═══════════════ 1. ENJEUX ═══════════════
OUT.append(section('enjeux', 1, 'Définition & les trois familles — ce qu\'on demande à un marqueur',
    sub('enj-sub',
        'Les maladies cardiovasculaires sont la <b>première cause de mortalité au monde</b> : chaque minute de diagnostic compte. Un biomarqueur cardiaque est une substance <b>mesurable dans le sang</b>, produite ou libérée par le cœur atteint, au service du <b>diagnostic, du pronostic et du suivi</b>.',
        'أمراض القلب والأوعية هي <b>السبب الأول للوفاة في العالم</b>: كل دقيقة تشخيص مهمّة. الواسم القلبي مادة <b>قابلة للقياس في الدم</b>، ينتجها أو يحرّرها القلب المصاب، في خدمة <b>التشخيص والتكهن والمتابعة</b>.'),
    [
        fig('enjeux.webp',
            "Planche des enjeux des biomarqueurs cardiaques dans un laboratoire d'analyses : un cœur relié à trois cartouches mesurable dans le sang produit ou libéré par le cœur atteint et utile au diagnostic pronostic et suivi, avec le marqueur idéal sensible spécifique et précoce",
            '💡 <b>La définition en trois verbes :</b> mesurer (dans le sang) · venir du cœur · servir la décision'),
        spot(0),
        lbox('enj-box1', 'fa-quote-left', 'La définition du cours, et le portrait du marqueur idéal',
            [
                '<b>Mesurable dans le sang</b> — sans dosage fiable, pas de biomarqueur, juste une idée.',
                '<b>Produite par le cœur</b> (ou libérée en réponse à une atteinte cardiaque) — c\'est ce lien au myocarde qui fait sa valeur.',
                '<b>Utilisée en pratique</b> pour le <b>diagnostic</b>, le <b>pronostic</b> ou le <b>suivi thérapeutique</b> des maladies cardiovasculaires.',
                'Le marqueur <b>idéal</b> (formule d\'annale) : <b>sensible</b> (ne rien rater), <b>spécifique</b> (ne signaler que le cœur) et <b>précoce</b> (monter vite). Toute la leçon note les candidats sur ces trois critères.',
            ],
            arbox('fa-quote-left', 'تعريف الدرس وصورة الواسم المثالي', [
                '<b>قابل للقياس في الدم</b> — دون قياس موثوق لا واسم، مجرد فكرة.',
                '<b>من إنتاج القلب</b> (أو محرَّر استجابة لإصابة قلبية) — هذا الارتباط بعضل القلب هو قيمته.',
                '<b>مستعمَل عملياً</b> في <b>التشخيص</b> أو <b>التكهن</b> أو <b>المتابعة العلاجية</b>.',
                'الواسم <b>المثالي</b> (صيغة الامتحانات): <b>حسّاس</b> (لا يفوّت شيئاً)، <b>نوعي</b> (لا يشير إلا إلى القلب)، <b>مبكر</b> (يصعد بسرعة). الدرس كله يقيّم المرشحين على هذه المعايير الثلاثة.',
            ])),
        grid2(
            mini('enj-mini1', 'red', 'fa-heart-crack', 'LES 3 FAMILLES DU COURS',
                [
                    '<b>Nécrose myocardique</b> : la cellule meurt et vide son contenu (troponine, CK-MB, myoglobine)',
                    '<b>Fonction myocardique</b> : la paroi souffre et sécrète (BNP, NT-proBNP)',
                    '<b>Inflammation & risque</b> : le terrain se prépare (hs-CRP, fibrinogène)',
                ],
                armini('fa-heart-crack', 'عائلات الدرس الثلاث', [
                    '<b>نخر عضل القلب</b>: الخلية تموت وتفرّغ محتواها (تروبونين، ' + FP % 'CK-MB' + '، ميوغلوبين)',
                    '<b>وظيفة عضل القلب</b>: الجدار يعاني ويفرز (' + FP % 'BNP' + '، ' + FP % 'NT-proBNP' + ')',
                    '<b>الالتهاب والخطر</b>: الأرضية تتهيأ (' + FP % 'hs-CRP' + '، فيبرينوجين)',
                ])),
            mini('enj-mini2', 'blue', 'fa-star', 'POURQUOI « PRÉCOCE » VAUT DE L\'OR',
                [
                    'Dans l\'infarctus, <b>le temps, c\'est du myocarde</b> : plus le marqueur monte tôt, plus on traite tôt',
                    'Un marqueur tardif mais <b>durable</b> garde un autre talent : le diagnostic <b>rétrospectif</b>',
                    'Sensibilité et précocité sans spécificité = fausses alertes : c\'est le drame de la myoglobine (section 7)',
                ],
                armini('fa-star', 'لماذا تساوي «المبكرة» ذهباً', [
                    'في الاحتشاء، <b>الوقت هو عضل قلب</b>: كلما صعد الواسم أبكر عالجنا أبكر',
                    'واسم متأخر لكن <b>دائم</b> يحتفظ بموهبة أخرى: التشخيص <b>الرجعي</b>',
                    'حساسية وبكور دون نوعية = إنذارات كاذبة: إنها مأساة الميوغلوبين (القسم 7)',
                ]), delay='1')),
        focus([
            '<b>Annales réelles (×3)</b> : le marqueur idéal doit être « sensible, spécifique et précoce » / « spécificité et sensibilité élevées » — la définition tombe telle quelle.',
            '<b>Négation plaquée (⑥)</b> : « les biomarqueurs ne permettent pas un diagnostic précoce », « utilisables qu\'en milieu hospitalier » — corrigés faux en 2018.',
            '<b>Famille croisée (②)</b> : ranger le BNP parmi les marqueurs de nécrose coronaire — il appartient à la <b>fonction</b>.',
        ]),
    ], '1. DÉFINITION & FAMILLES'))

# ═══════════════ 2. NÉCROSE ═══════════════
OUT.append(section('necrose', 2, 'Marqueurs de nécrose — quand la cellule meurt, elle parle',
    sub('nec-sub',
        'Le principe est brutal et simple : une cellule myocardique qui se nécrose <b>libère ses protéines dans le sang</b>. Les doser permet de <b>diagnostiquer les syndromes coronariens aigus</b> — ischémies aiguës du myocarde, le plus souvent par athérosclérose — et d\'en <b>évaluer la sévérité</b>.',
        'المبدأ وحشي وبسيط: خلية العضل القلبي المتنخّرة <b>تحرّر بروتيناتها في الدم</b>. وقياسها يسمح بـ<b>تشخيص المتلازمات الإكليلية الحادة</b> — إقفارات حادة لعضل القلب سببها غالباً التصلّب — و<b>تقييم شدّتها</b>.'),
    [
        fig('necrose.webp',
            "Planche de la nécrose myocardique : une coronaire obstruée par thrombus sur plaque d'athérome, en aval des cellules myocardiques détruites aux membranes rompues libérant leurs protéines dans un capillaire, avec les étiquettes ischémie aiguë cellules détruites protéines libérées dans le sang et diagnostic des SCA plus sévérité",
            '💡 <b>Le mécanisme unique de toute la famille :</b> membrane rompue → protéines dans le sang → dosage'),
        spot(0),
        lbox('nec-box1', 'fa-gears', 'Le principe, et ce qu\'il permet',
            [
                '<b>Le déclencheur</b> : l\'ischémie aiguë (le plus souvent rupture de plaque d\'athérosclérose + thrombus) prive les cardiomyocytes d\'oxygène → <b>nécrose</b>.',
                '<b>La fuite</b> : les membranes cèdent, les protéines intracellulaires (troponines, CK-MB, myoglobine) <b>passent dans le sang</b> — chacune à sa vitesse, selon sa taille et sa localisation dans la cellule.',
                '<b>Deux usages</b> : <b>diagnostiquer</b> le syndrome coronarien aigu et <b>évaluer sa sévérité</b> (plus la nécrose est étendue, plus les taux montent).',
                'Définition d\'annale à retenir telle quelle : l\'infarctus est une <b>nécrose ischémique accompagnée de libération de marqueurs mesurables</b>.',
            ],
            arbox('fa-gears', 'المبدأ وما يتيحه', [
                '<b>المحرّك</b>: الإقفار الحاد (غالباً تمزّق عصيدة + خثرة) يحرم الخلايا من الأكسجين ← <b>نخر</b>.',
                '<b>التسرّب</b>: تنهار الأغشية فتمرّ البروتينات داخل الخلوية (تروبونينات، ' + FP % 'CK-MB' + '، ميوغلوبين) <b>إلى الدم</b> — كلٌّ بسرعته حسب حجمه وموقعه في الخلية.',
                '<b>استعمالان</b>: <b>تشخيص</b> المتلازمة الإكليلية الحادة و<b>تقييم شدّتها</b> (كلما اتسع النخر ارتفعت المستويات).',
                'تعريف امتحاني يُحفظ كما هو: الاحتشاء <b>نخر إقفاري مصحوب بتحرّر واسمات قابلة للقياس</b>.',
            ])),
        focus([
            '<b>Libérée, pas sécrétée (②)</b> : « la troponine est sécrétée/produite par le ventricule gauche » — corrigé faux en annale ; la sécrétion ventriculaire, c\'est le BNP.',
            '<b>Cause noyée (③)</b> : oublier que la cause la plus fréquente du SCA est l\'<b>athérosclérose</b> — le cours le dit dans la définition même.',
        ]),
    ], '2. MARQUEURS DE NÉCROSE'))

# ═══════════════ 3. TROPONINE ★★ ═══════════════
OUT.append(section('troponine', 3, 'Le complexe troponine — trois sous-unités, deux cartes d\'identité ★★',
    sub('tro-sub',
        'La troponine est la protéine de la contraction accrochée au filament d\'actine : <b>TnC</b> capte le calcium, <b>TnI</b> inhibe l\'actine-myosine, <b>TnT</b> ancre le complexe à la tropomyosine. Seules <b>I et T sont spécifiques du myocarde</b> — c\'est pour cela qu\'on les dose.',
        'التروبونين بروتين الانقباض المتعلّق بخيط الأكتين: <b>' + FP % 'TnC' + '</b> يرتبط بالكالسيوم، <b>' + FP % 'TnI' + '</b> يثبّط الأكتين-ميوسين، <b>' + FP % 'TnT' + '</b> يرسّخ المركّب على التروبوميوسين. فقط <b>I وT نوعيتان لعضل القلب</b> — ولهذا نقيسهما.'),
    [
        fig('troponine.webp',
            "Schéma du complexe troponine sur un filament d'actine avec tropomyosine et têtes de myosine : troponine C qui lie le calcium et déclenche la contraction, troponine I qui inhibe l'actine-myosine, troponine T qui fixe le complexe à la tropomyosine, avec le bandeau I et T spécifiques du myocarde, C aussi dans le muscle squelettique",
            '💡 <b>Le trio :</b> C déclenche (calcium) · I inhibe · T ancre — et seules I/T portent la carte « cœur »'),
        spot(1),
        lbox('tro-box1', 'fa-id-card', 'Le rôle de chaque sous-unité (cours, mot pour mot)',
            [
                '<b>Troponine C (TnC)</b> : se lie au <b>calcium</b> et <b>déclenche la contraction</b>. Présente aussi dans le muscle squelettique → <b>non spécifique</b>, jamais dosée pour le cœur.',
                '<b>Troponine I (TnI)</b> : <b>inhibe l\'interaction actine-myosine</b> (rôle régulateur) — <b>absente du muscle squelettique</b> : cardiospécifique.',
                '<b>Troponine T (TnT)</b> : <b>fixe le complexe à la tropomyosine</b> — cardiospécifique elle aussi.',
                'Libérées lors de la nécrose, les cTn sont les <b>marqueurs de référence</b> du SCA : très sensibles, très spécifiques, diagnostiques précoces, et elles restent <b>élevées 6 à 10 jours</b>.',
            ],
            arbox('fa-id-card', 'دور كل وحيدة (الدرس حرفياً)', [
                '<b>تروبونين ' + FP % 'C (TnC)' + '</b>: يرتبط بـ<b>الكالسيوم</b> و<b>يُطلق الانقباض</b>. موجود أيضاً في العضل الهيكلي ← <b>غير نوعي</b>، لا يُقاس للقلب أبداً.',
                '<b>تروبونين ' + FP % 'I (TnI)' + '</b>: <b>يثبّط تفاعل الأكتين-ميوسين</b> (دور منظّم) — <b>غائب عن العضل الهيكلي</b>: نوعي قلبياً.',
                '<b>تروبونين ' + FP % 'T (TnT)' + '</b>: <b>يثبّت المركّب على التروبوميوسين</b> — نوعي قلبياً أيضاً.',
                'محرَّرة عند النخر، التروبونينات هي <b>الواسمات المرجعية</b> للمتلازمة الإكليلية: حسّاسة جداً ونوعية جداً ومبكرة، وتبقى <b>مرتفعة 6 إلى 10 أيام</b>.',
            ])),
        reels('D<sup>r</sup> Besbes, A — « Structure de la troponine », page 7 du cours (étiquettes d\'origine en anglais)', [
            ('troponine-structure.webp', 678, 434,
             "Schéma original du cours du complexe troponine sur le filament d'actine et de tropomyosine, avec les trois sous-unités troponine C, troponine I et troponine T",
             '<b>Le schéma du professeur</b> — repère les trois sous-unités sur le filament : C (calcium), I (inhibitrice), T (tropomyosine)'),
        ]),
        focus([
            '<b>Annale réelle</b> : « la troponine C représente un marqueur de choix en cardiologie » → <b>faux</b> (2018) : C n\'est pas spécifique.',
            '<b>Rôles permutés (⑧)</b> : « TnT lie le calcium », « TnC fixe la tropomyosine » — chaque lettre a UN métier : <b>C</b>alcium · <b>I</b>nhibe · <b>T</b>ropomyosine.',
            '<b>Spécificité dévoyée (①)</b> : « très bonne spécificité <b>coronarienne</b> » — corrigé faux : la spécificité est <b>myocardique</b> (la troponine monte aussi sans atteinte coronaire, section 5).',
        ]),
    ], '3. LE COMPLEXE TROPONINE'))

# ═══════════════ 4. HS ★★ ═══════════════
OUT.append(section('hs', 4, 'Classique vs hypersensible — voir plus tôt, décider plus vite ★★',
    sub('hs-sub',
        'Même molécule, meilleure loupe : les dosages <b>hypersensibles (hs-cTn)</b> détectent des concentrations très faibles, donc le signal <b>1 à 2 heures</b> après le début — contre <b>3 à 6 heures</b> pour la troponine classique. Et une fois montées, <b>TnI tient 3–6 jours, TnT jusqu\'à 10 jours</b>.',
        'نفس الجزيء بعدسة أقوى: القياسات <b>فائقة الحساسية</b> تلتقط تراكيز ضئيلة جداً، فتظهر الإشارة بعد <b>ساعة إلى ساعتين</b> — مقابل <b>3 إلى 6 ساعات</b> للتقليدية. وبعد صعودها: <b>' + FP % 'TnI' + ' تبقى 3–6 أيام و' + FP % 'TnT' + ' حتى 10 أيام</b>.'),
    [
        fig('hs.webp',
            "Planche comparant un analyseur de troponine classique détectable en trois à six heures et un analyseur hypersensible détectable en une à deux heures, avec les durées TnI élevée trois à six jours et TnT élevée jusqu'à dix jours",
            '💡 <b>Deux horloges à verrouiller :</b> la montée (1–2 h vs 3–6 h) et la durée (TnI 3–6 j · TnT 10 j)'),
        spot(1),
        table('hs-tab1',
            ['Dosage', 'Détection', 'Durée d\'élévation', 'Conséquence pratique'],
            [
                ['<b>Troponine classique</b>', '<b>3–6 h</b>', 'TnI 3–6 j · TnT ≤ 10 j', 'Contrôle tardif (H6–H9)'],
                ['<b>Troponine hypersensible (hs-cTn)</b>', '<b>1–2 h</b>', 'TnI 3–6 j · TnT ≤ 10 j', 'Algorithmes rapides H0 → H1–H3, excellente <b>valeur prédictive négative</b>'],
            ],
            '<thead><tr><th>القياس</th><th>الكشف</th><th>مدة الارتفاع</th><th>العاقبة العملية</th></tr></thead><tbody>'
            '<tr><td><b>التروبونين التقليدية</b></td><td><b>3–6 ساعات</b></td><td>' + FP % 'TnI' + ' ‏3–6 أيام · ' + FP % 'TnT' + ' ≤ 10 أيام</td><td>مراقبة متأخرة (H6–H9)</td></tr>'
            '<tr><td><b>فائقة الحساسية</b></td><td><b>1–2 ساعة</b></td><td>' + FP % 'TnI' + ' ‏3–6 أيام · ' + FP % 'TnT' + ' ≤ 10 أيام</td><td>خوارزميات سريعة H0 ← H1–H3، وقيمة تكهنية سلبية ممتازة</td></tr></tbody>'),
        lbox('hs-box1', 'fa-magnifying-glass', 'Ce que l\'hypersensibilité change — et ce qu\'elle ne change pas',
            [
                '<b>Elle change l\'heure</b> : en voyant des concentrations très faibles, elle rend le diagnostic possible <b>dès 1–2 h</b> et alimente les algorithmes rapides (section 6).',
                '<b>Elle sécurise l\'exclusion</b> : les annales valident son « <b>excellente valeur prédictive négative</b> » pour l\'IDM — négative deux fois, on peut exclure avec fiabilité.',
                '<b>Elle ne change ni la molécule ni la durée</b> : TnI reste élevée <b>3–6 jours</b>, TnT <b>jusqu\'à 10 jours</b>, en classique comme en hypersensible — le socle du diagnostic rétrospectif.',
                'Contrepartie logique : voir plus tôt et plus bas, c\'est aussi voir les <b>élévations non coronariennes</b> (section 5) — l\'interprétation clinique devient encore plus indispensable.',
            ],
            arbox('fa-magnifying-glass', 'ما تغيّره الحساسية الفائقة — وما لا تغيّره', [
                '<b>تغيّر التوقيت</b>: برؤية التراكيز الضئيلة تجعل التشخيص ممكناً <b>منذ 1–2 ساعة</b> وتغذّي الخوارزميات السريعة (القسم 6).',
                '<b>تؤمّن الاستبعاد</b>: الامتحانات تصادق على «<b>قيمتها التكهنية السلبية الممتازة</b>» للاحتشاء — سلبية مرتين يعني الاستبعاد بثقة.',
                '<b>لا تغيّر لا الجزيء ولا المدة</b>: ' + FP % 'TnI' + ' تبقى <b>3–6 أيام</b> و' + FP % 'TnT' + ' <b>حتى 10 أيام</b>، تقليدية كانت أو فائقة — أساس التشخيص الرجعي.',
                'الثمن المنطقي: الرؤية الأبكر والأدنى تعني رؤية <b>الارتفاعات غير الإكليلية</b> أيضاً (القسم 5) — فيصبح التفسير السريري ألزم.',
            ])),
        focus([
            '<b>Durées permutées (⑧)</b> : « TnI jusqu\'à 10 jours, TnT 3–6 jours » — c\'est l\'inverse : <b>T dure plus longtemps que I</b>.',
            '<b>Annale réelle</b> : « mesurée à l\'admission et 2 heures après » (hs) → vrai ; « cinétique H0–H1 pour classer en <b>deux</b> catégories » → non retenu par le corrigé.',
            '<b>Précoce déniée (⑥)</b> : « l\'hypersensible ne détecte pas plus tôt que la classique » — tout son intérêt est là : 1–2 h contre 3–6 h.',
        ]),
    ], '4. CLASSIQUE VS HYPERSENSIBLE'))

# ═══════════════ 5. INTERPRÉTATION ★★ ═══════════════
OUT.append(section('interpretation', 5, 'Interpréter une troponine — élevée ne veut pas dire infarctus ★★',
    sub('int-sub',
        'La troponine signe une <b>souffrance myocardique</b>, pas un mécanisme : elle monte dans une foule de situations cardiaques et extracardiaques, et même un peu avec l\'<b>âge</b> et chez l\'<b>homme</b>. Le cours tranche : l\'interprétation associe <b>obligatoirement anamnèse, clinique et ECG</b>.',
        'التروبونين توقّع <b>معاناة عضل القلب</b> لا آليتها: تصعد في حشد من الحالات القلبية وغير القلبية، بل قليلاً مع <b>العمر</b> وعند <b>الرجل</b>. الدرس يحسم: التفسير يضمّ <b>إلزامياً السوابق والسريرية وتخطيط القلب</b>.'),
    [
        fig('interpretation.webp',
            "Planche troponine élevée différent d'infarctus : un résultat de troponine élevé entouré de scènes embolie pulmonaire sepsis insuffisance rénale myocardite et effort intense prolongé chez un marathonien, avec le bandeau toujours interpréter avec anamnèse clinique et ECG",
            '💡 <b>La phrase-clé des annales :</b> une élévation n\'est <b>jamais</b> « uniquement en cas d\'infarctus »'),
        spot(2),
        table('int-tab1',
            ['Causes cardiaques d\'↑ cTn (hors IDM)', 'Causes extracardiaques d\'↑ cTn'],
            [
                ['Myocardite', 'Embolie pulmonaire, HTAP'],
                ['Cardiomyopathies', 'Sepsis, choc septique'],
                ['Insuffisance cardiaque', 'Insuffisance rénale (chronique ou aiguë)'],
                ['Troubles du rythme sévères', 'AVC, hémorragie méningée'],
                ['Contusion cardiaque (traumatisme, chirurgie, défibrillation)', 'Exercice physique intense et prolongé'],
                ['Hypertension', 'Brûlure sévère'],
                ['Intoxication au monoxyde de carbone', 'Venin de serpent'],
            ],
            '<thead><tr><th>أسباب قلبية لارتفاع التروبونين (خارج الاحتشاء)</th><th>أسباب خارج القلب</th></tr></thead><tbody>'
            '<tr><td>التهاب عضل القلب</td><td>انصمام رئوي، فرط ضغط رئوي</td></tr>'
            '<tr><td>اعتلالات عضل القلب</td><td>إنتان، صدمة إنتانية</td></tr>'
            '<tr><td>قصور القلب</td><td>قصور كلوي (مزمن أو حاد)</td></tr>'
            '<tr><td>اضطرابات نظم شديدة</td><td>سكتة دماغية، نزف سحائي</td></tr>'
            '<tr><td>رضّ قلبي (إصابة، جراحة، رجفان مزال)</td><td>جهد بدني شديد مطوّل</td></tr>'
            '<tr><td>فرط ضغط</td><td>حرق شديد</td></tr>'
            '<tr><td>تسمّم بأحادي أكسيد الكربون</td><td>سمّ الأفعى</td></tr></tbody>'),
        grid2(
            mini('int-mini1', 'blue', 'fa-user', 'VARIATIONS PHYSIOLOGIQUES',
                [
                    '<b>Âge</b> : la cTn augmente avec l\'âge — plus élevée après <b>60 ans</b>',
                    '<b>Sexe</b> : plus élevée chez l\'<b>homme</b> que chez la femme',
                    'Deux pièges de seuil : un même chiffre ne se lit pas pareil à 25 et à 70 ans',
                ],
                armini('fa-user', 'التغيرات الفيزيولوجية', [
                    '<b>العمر</b>: التروبونين يزيد مع العمر — أعلى بعد <b>60 عاماً</b>',
                    '<b>الجنس</b>: أعلى عند <b>الرجل</b> من المرأة',
                    'فخّا عتبة: الرقم نفسه لا يُقرأ بنفس الطريقة في 25 و70 عاماً',
                ])),
            mini('int-mini2', 'red', 'fa-triangle-exclamation', 'MYOCARDIQUE ≠ CORONARIENNE',
                [
                    'La troponine est spécifique du <b>tissu myocardique</b>, pas de la <b>maladie coronaire</b>',
                    'Preuve par le tableau : EP, sepsis, rein, cerveau la font monter <b>sans coronaire bouchée</b>',
                    'L\'annale 2018 corrige « très bonne spécificité coronarienne » en <b>FAUX</b> — un seul adjectif tombe',
                ],
                armini('fa-triangle-exclamation', 'عضل-قلبية ≠ إكليلية', [
                    'التروبونين نوعية لـ<b>نسيج عضل القلب</b> لا لـ<b>الداء الإكليلي</b>',
                    'البرهان بالجدول: الانصمام والإنتان والكلى والدماغ ترفعها <b>دون أي إكليلي مسدود</b>',
                    'سؤال 2018 يصحّح «نوعية إكليلية جيدة جداً» بـ<b>خطأ</b> — صفة واحدة تسقط',
                ]), delay='1')),
        focus([
            '<b>Annale n°1 (2022)</b> : vraies réponses = IC sévère, embolie pulmonaire, choc septique ; les deux « <b>uniquement</b> » (IDM seul, IC seule) sont les pièges — « uniquement » est presque toujours faux.',
            '<b>Chiffre sans contexte (⑨)</b> : conclure IDM sur une valeur isolée — le cours impose le trio <b>anamnèse + clinique + ECG</b>.',
            '<b>Cause rangée au mauvais camp (②)</b> : l\'embolie pulmonaire est une cause <b>extracardiaque</b> d\'élévation (souffrance du VD), la myocardite une cause <b>cardiaque</b>.',
        ]),
    ], '5. INTERPRÉTER UNE TROPONINE'))

# ═══════════════ 6. SCA ★★ ═══════════════
OUT.append(section('sca', 6, 'SCA & algorithmes — quand l\'ECG parle, quand la troponine décide ★★',
    sub('sca-sub',
        'Deux mondes : le <b>STEMI</b>, où le diagnostic est clinique et ECG et où la reperfusion ne doit <b>jamais attendre</b> la troponine ; le <b>NSTEMI</b>, où sans sus-décalage, c\'est l\'<b>élévation et la cinétique</b> de la troponine qui font le diagnostic. L\'algorithme enchaîne H0 puis le contrôle — <b>H1–H3 en hypersensible, H6–H9 en classique</b>.',
        'عالمان: الـ<b>' + FP % 'STEMI' + '</b> حيث التشخيص سريري وتخطيطي ولا يجب أن تنتظر إعادة التروية <b>أبداً</b> التروبونين؛ والـ<b>' + FP % 'NSTEMI' + '</b> حيث دون ارتفاع ' + FP % 'ST' + ' يكون الحكم لـ<b>ارتفاع التروبونين وحركيته</b>. الخوارزمية: ' + FP % 'H0' + ' ثم مراقبة — <b>' + FP % 'H1–H3' + ' فائق الحساسية، ' + FP % 'H6–H9' + ' تقليدي</b>.'),
    [
        fig('sca.webp',
            "Planche des syndromes coronariens aigus en deux panneaux : à gauche élévation du segment ST avec équipe poussant le brancard, STEMI diagnostic ECG et reperfusion immédiate sans attendre la troponine ; à droite pas de sus-décalage et tubes horodatés, NSTEMI la cinétique de troponine décide H0 puis H1 à H3 en hypersensible ou H6 à H9 en classique ; bandeau deux troponines normales égale infarctus exclu avec fiabilité",
            '💡 <b>La frontière :</b> ST↑ → on fonce · pas de ST↑ → on dose deux fois et on regarde la pente'),
        spot(3),
        lbox('sca-box1', 'fa-code-branch', 'L\'algorithme du cours, pas à pas',
            [
                '<b>H0</b> : premier dosage à l\'admission, dans les deux stratégies.',
                '<b>Troponine classique</b> : deuxième dosage à <b>H6–H9</b> — le temps que le signal devienne détectable (3–6 h).',
                '<b>Troponine hypersensible</b> : contrôle à <b>H1, H2 ou H3</b> selon le protocole disponible — la sensibilité achète des heures.',
                '<b>Règle de sortie</b> (phrase du cours) : troponine <b>normale à H0 et au contrôle</b> → IDM <b>exclu avec fiabilité</b>. Une seule valeur ne suffit ni à exclure, ni (sans contexte) à conclure.',
                '<b>Exception vitale</b> : devant un STEMI, on ne dose pas pour décider — on <b>reperfuse immédiatement</b>, le résultat viendra après.',
            ],
            arbox('fa-code-branch', 'خوارزمية الدرس خطوة بخطوة', [
                '<b>' + FP % 'H0' + '</b>: القياس الأول عند القبول في الاستراتيجيتين.',
                '<b>التقليدية</b>: قياس ثانٍ عند <b>' + FP % 'H6–H9' + '</b> — وقت تصبح فيه الإشارة قابلة للكشف (3–6 ساعات).',
                '<b>فائقة الحساسية</b>: مراقبة عند <b>' + FP % 'H1' + ' أو ' + FP % 'H2' + ' أو ' + FP % 'H3' + '</b> حسب البروتوكول — الحساسية تشتري ساعات.',
                '<b>قاعدة الخروج</b> (جملة الدرس): تروبونين <b>طبيعية عند H0 وعند المراقبة</b> ← الاحتشاء <b>مستبعَد بثقة</b>. قيمة واحدة لا تكفي لا للاستبعاد ولا (دون سياق) للاستنتاج.',
                '<b>الاستثناء الحيوي</b>: أمام ' + FP % 'STEMI' + ' لا نقيس لنقرّر — <b>نعيد التروية فوراً</b>، والنتيجة تأتي بعد.',
            ])),
        reels('D<sup>r</sup> Besbes, A — « SCA avec sus-décalage de ST », page 13 du cours', [
            ('ecg-stemi.webp', 301, 228,
             "Schéma original du cours d'un tracé ECG avec sus-décalage du segment ST, légendé SCA avec sus-décalage de ST",
             '<b>Le tracé qui ne attend pas</b> — sus-décalage de ST : le diagnostic est sur l\'ECG, pas au laboratoire'),
        ]),
        focus([
            '<b>Inversion mortelle (⑤)</b> : « devant un STEMI, attendre la troponine avant la reperfusion » — jamais : <b>le temps, c\'est du myocarde</b>.',
            '<b>Heures croisées (⑧)</b> : H6–H9 appartient à la <b>classique</b>, H1–H3 à l\'<b>hypersensible</b> — les annales valident « admission et 2 heures après » pour la hs.',
            '<b>Exclusion à un dosage (⑥)</b> : « troponine H0 normale = IDM exclu » — il faut les <b>deux</b> temps normaux.',
        ]),
    ], '6. SCA & ALGORITHMES'))

# ═══════════════ 7. MYOGLOBINE ═══════════════
OUT.append(section('myoglobine', 7, 'Myoglobine — la sprinteuse déclassée',
    sub('myo-sub',
        'Petite protéine du transport d\'oxygène dans le <b>muscle strié</b>, la myoglobine est le marqueur <b>le plus précoce</b> de la leçon — et le moins spécifique. Sa carrière résume le critère « idéal » : sensible et précoce ne suffit pas, la troponine l\'a <b>supplantée</b>.',
        'بروتين صغير لنقل الأكسجين في <b>العضل المخطط</b>، الميوغلوبين هو الواسم <b>الأبكر</b> في الدرس — والأقل نوعية. مساره يختصر معيار «المثالي»: الحساسية والبكور لا يكفيان، التروبونين <b>أزاحه</b>.'),
    [
        fig('myoglobine.webp',
            "Planche de la myoglobine : une fibre musculaire striée en coupe libérant sa myoglobine en deux heures avec pic à quatre-douze heures et retour à la normale en vingt-quatre heures, et une jambe traumatisée libérant aussi de la myoglobine, supplantée par la troponine car présente dans le muscle squelettique",
            '💡 <b>Sa signature temps :</b> 2 h → pic 4–12 h → normale ~24 h · <b>son défaut :</b> tout le muscle strié'),
        spot(4),
        lbox('myo-box1', 'fa-bolt', 'Précoce, sensible… et disqualifiée par la spécificité',
            [
                '<b>Le sprinter</b> : libérée rapidement, elle <b>apparaît dès 2 h</b>, culmine à <b>4–12 h</b> et redevient <b>normale en ~24 h</b>.',
                '<b>Le réflexe annale</b> : en 2019, « la myoglobine est un marqueur <b>cardiospécifique</b> » est corrigé <b>faux</b> — c\'est un marqueur <b>précoce de lésion musculaire, non cardiospécifique</b>.',
                '<b>Elle monte partout où le muscle strié souffre</b> : traumatisme, chirurgie, rhabdomyolyse, exercice intense, convulsions prolongées…',
                '<b>Verdict du cours</b> : lésion musculaire ou infarctus, elle ne distingue pas → <b>supplantée par les troponines cardiaques</b>.',
            ],
            arbox('fa-bolt', 'مبكر وحسّاس… ومستبعَد لانعدام النوعية', [
                '<b>العدّاء</b>: يُحرَّر بسرعة فيظهر <b>منذ ساعتين</b>، يبلغ الذروة <b>4–12 ساعة</b> ويعود <b>طبيعياً في ~24 ساعة</b>.',
                '<b>منعكس الامتحان</b>: في 2019، «الميوغلوبين واسم <b>نوعي للقلب</b>» صُحّحت <b>خطأ</b> — فهو واسم <b>مبكر للأذية العضلية، غير نوعي للقلب</b>.',
                '<b>يصعد أينما يعاني العضل المخطط</b>: رضّ، جراحة، انحلال عضلي، تمرين شديد، اختلاجات مطوّلة…',
                '<b>حكم الدرس</b>: أذية عضلية أم احتشاء، لا يفرّق ← <b>أزاحته التروبونينات القلبية</b>.',
            ])),
        focus([
            '<b>Trio de temps permuté (⑧)</b> : 2 h (apparition) · 4–12 h (pic) · 24 h (normale) — ne pas confondre avec CK-MB (4–6 h → 2–3 j).',
            '<b>Spécificité prêtée (①)</b> : « la myoglobine est spécifique du myocarde » — c\'est exactement le contraire de sa disqualification.',
        ]),
    ], '7. MYOGLOBINE'))

# ═══════════════ 8. CK-MB ═══════════════
OUT.append(section('ckmb', 8, 'CK-MB — l\'isoenzyme qui voyait les réinfarctus',
    sub('ck-sub',
        'Isoenzyme de la créatine kinase surtout présente dans le myocarde, la CK-MB monte en <b>4–6 heures</b> et revient à la normale en <b>2–3 jours</b>. Cette descente rapide fut son super-pouvoir : une <b>remontée</b> signait le réinfarctus précoce. Aujourd\'hui, elle aussi est <b>supplantée par la troponine</b>.',
        'نظير إنزيم الكرياتين كيناز الموجود خاصة في عضل القلب، ' + FP % 'CK-MB' + ' يصعد في <b>4–6 ساعات</b> ويعود طبيعياً في <b>2–3 أيام</b>. هذا الهبوط السريع كان قوته الخارقة: أي <b>صعود جديد</b> كان يفضح الاحتشاء المتكرر المبكر. واليوم <b>أزاحته هو أيضاً التروبونين</b>.'),
    [
        fig('ckmb.webp',
            "Planche de la CK-MB : un cœur en coupe avec petite zone de nécrose fraîche sur territoire déjà cicatriciel et courbe de CK-MB qui monte en quatre à six heures, redevient normale en deux à trois jours puis remonte, signalant un réinfarctus précoce, aujourd'hui supplantée par la troponine",
            '💡 <b>Son talent historique :</b> redescendre vite (2–3 j), donc une remontée = événement nouveau'),
        spot(4),
        grid2(
            mini('ck-mini1', 'blue', 'fa-clock', 'SA CINÉTIQUE',
                [
                    'Apparition : <b>4–6 heures</b> (plus lente que la myoglobine)',
                    'Retour à la normale : <b>2–3 jours</b> (beaucoup plus court que la troponine)',
                    'D\'où l\'usage historique : <b>dépister le réinfarctus/récidive précoce</b>',
                ],
                armini('fa-clock', 'حركيته', [
                    'الظهور: <b>4–6 ساعات</b> (أبطأ من الميوغلوبين)',
                    'العودة للطبيعي: <b>2–3 أيام</b> (أقصر بكثير من التروبونين)',
                    'ومن هنا استعماله التاريخي: <b>كشف الاحتشاء المتكرر المبكر</b>',
                ])),
            mini('ck-mini2', 'red', 'fa-gavel', 'LE VERDICT (COURS + ANNALES)',
                [
                    'Moins sensible et moins spécifique que la troponine → <b>plus le marqueur de choix</b>',
                    '« CPK-MB, copeptine ou h-FABP <b>toujours</b> recommandé dans la démarche SCA » — corrigé <b>faux</b> (l\'absolu « toujours » est le piège)',
                    'Sa place aujourd\'hui : comprendre les courbes, historiquement la récidive',
                ],
                armini('fa-gavel', 'الحكم (الدرس + الامتحانات)', [
                    'أقل حساسية ونوعية من التروبونين ← <b>لم يعد واسم الخيار</b>',
                    '«' + FP % 'CPK-MB' + ' أو كوبيبتين أو h-FABP <b>يُوصى به دائماً</b> في مسيرة تشخيص المتلازمة» — <b>خطأ</b> في التصحيح (كلمة «دائماً» هي الفخ)',
                    'مكانه اليوم: فهم المنحنيات، وتاريخياً كشف التكرر',
                ]), delay='1')),
        focus([
            '<b>Annale réelle (2019)</b> : « la CK-MB augmente <b>plus rapidement</b> que la myoglobine » → <b>faux</b> : 4–6 h contre 2 h, et retour 2–3 j contre 24 h — plus lente des deux côtés.',
            '<b>Réinfarctus raconté à l\'envers (⑤)</b> : c\'est sa <b>descente rapide</b> qui permet de voir une remontée — pas sa persistance (ça, c\'est la troponine et le rétrospectif).',
        ]),
    ], '8. CK-MB'))

# ═══════════════ 9. CINÉTIQUE ═══════════════
OUT.append(section('cinetique', 9, 'La courbe des cinétiques — trois signatures, un graphique',
    sub('cine-sub',
        'Sur le même axe du temps, les trois marqueurs de nécrose racontent trois carrières : la <b>flèche éclair</b> de la myoglobine, le <b>pic bref</b> de la CK-MB, la <b>longue traîne</b> de la troponine. Chaque zone de la courbe répond à une question clinique différente.',
        'على محور زمني واحد تروي واسمات النخر الثلاثة ثلاث مسيرات: <b>سهم البرق</b> للميوغلوبين، <b>الذروة القصيرة</b> لـ' + FP % 'CK-MB' + '، و<b>الذيل الطويل</b> للتروبونين. وكل منطقة في المنحنى تجيب عن سؤال سريري مختلف.'),
    [
        fig('cinetique.webp',
            "Graphique de cinétique des marqueurs cardiaques après infarctus : trois courbes sur axe heures puis jours, myoglobine dès deux heures pic quatre à douze heures normale en vingt-quatre heures, CK-MB quatre à six heures normale en deux à trois jours, troponine trois à six heures en classique une à deux heures en hypersensible et élevée jusqu'à dix jours",
            '💡 <b>Lis la courbe comme un emploi du temps :</b> qui arrive, qui repart, qui reste'),
        spot(5),
        reels('D<sup>r</sup> Besbes, A — « Marqueurs de nécrose : cinétique », page 20 du cours', [
            ('cinetique.webp', 850, 481,
             "Graphique original du cours des concentrations des marqueurs cardiaques au cours du temps après infarctus : courbes de la myoglobine, de la troponine cardiaque et de la CK-MB en multiples de la limite supérieure de la normale",
            '<b>La courbe du professeur</b> — compare-la à la planche : la troponine (violet) est la seule encore debout à 8–10 jours'),
        ]),
        table('cine-tab1',
            ['Marqueur', 'Apparition', 'Retour normale', 'La question qu\'il tranchait'],
            [
                ['<b>Myoglobine</b>', '<b>2 h</b> (pic 4–12 h)', '<b>~24 h</b>', 'Signaler très tôt — sans spécificité'],
                ['<b>CK-MB</b>', '<b>4–6 h</b>', '<b>2–3 j</b>', 'Voir la <b>remontée</b> = réinfarctus'],
                ['<b>Troponine (hs / classique)</b>', '<b>1–2 h / 3–6 h</b>', '<b>TnI 3–6 j · TnT ≤ 10 j</b>', 'Diagnostiquer — et <b>rétrospectivement</b>'],
            ],
            '<thead><tr><th>الواسم</th><th>الظهور</th><th>العودة للطبيعي</th><th>السؤال الذي كان يجيب عنه</th></tr></thead><tbody>'
            '<tr><td><b>الميوغلوبين</b></td><td><b>ساعتان</b> (ذروة 4–12 سا)</td><td><b>~24 ساعة</b></td><td>الإنذار المبكر جداً — دون نوعية</td></tr>'
            '<tr><td><b>' + FP % 'CK-MB' + '</b></td><td><b>4–6 ساعات</b></td><td><b>2–3 أيام</b></td><td>رؤية <b>الصعود الجديد</b> = تكرر</td></tr>'
            '<tr><td><b>التروبونين (فائق/تقليدي)</b></td><td><b>1–2 سا / 3–6 سا</b></td><td><b>' + FP % 'TnI' + ' ‏3–6 أيام · ' + FP % 'TnT' + ' ≤ 10 أيام</b></td><td>التشخيص — و<b>الرجعي</b> أيضاً</td></tr></tbody>'),
        lbox('cine-box1', 'fa-landmark', 'Les anciens du service — testés en annale, absents des diapositives ⚠',
            [
                '<b>ASAT, ALAT, LDH, CK totale</b> : les corrigés valident qu\'ils furent utilisés (ASAT/LDH/CK = anciens marqueurs de « nécrose coronaire ») et qu\'ils sont <b>aujourd\'hui déclassés</b>.',
                '<b>Copeptine et h-FABP</b> (avec la CPK-MB) : « toujours recommandé dans la démarche diagnostique du SCA » → corrigé <b>faux</b> : ce ne sont pas des examens systématiques.',
                'Ces quatre noms reviennent dans <b>4 annales sur 10</b> mais n\'apparaissent pas dans les 32 diapositives reconstruites ici : retiens-les <b>au niveau des annales</b> (déclassés / non systématiques) et vérifie-les sur le cours de l\'année à son arrivée.',
            ],
            arbox('fa-landmark', 'قدماء المصلحة — مختبَرون في الامتحان غائبون عن الشرائح ⚠', [
                '<b>' + FP % 'ASAT, ALAT, LDH' + '، ' + FP % 'CK' + ' الكلي</b>: التصحيحات تصادق أنهم استُعملوا (واسمات «نخر إكليلي» قديمة) وأنهم <b>اليوم مسقَطون</b>.',
                '<b>' + FT % 'copeptine' + ' و' + FP % 'h-FABP' + '</b>: «يُطلبان دائماً في المتلازمات الإكليلية» ← <b>خطأ</b>: ليسا فحصين منهجيين.',
                'الأسماء الأربعة تعود في <b>4 أسئلة من 10</b> لكنها لا تظهر في الشرائح الـ32: احفظها <b>بمستوى الامتحان</b> (مسقَطة/غير منهجية) وتحقّق منها في محاضرة هذه السنة عند وصولها.',
            ])),
        focus([
            '<b>Annale réelle (2019)</b> : « diagnostic <b>rétrospectif</b> des IDM » figure parmi les indications validées du dosage des troponines — la longue traîne (6–10 j) EST la justification.',
            '<b>Ordre renversé (⑤)</b> : « la troponine apparaît avant la myoglobine » — non : 2 h bat 3–6 h (classique) ; c\'est la durée qui fait la championne, pas le sprint.',
        ]),
    ], '9. LA COURBE DES CINÉTIQUES'))

# ═══════════════ 10. PEPTIDES ★★ ═══════════════
OUT.append(section('peptides', 10, 'BNP & NT-proBNP — la voix du ventricule distendu ★★',
    sub('pep-sub',
        'Changement de famille : ici, rien ne meurt. Quand le volume ou la pression <b>distendent les ventricules</b>, le myocarde clive son précurseur <b>pro-BNP</b> en deux fragments — le <b>BNP**, hormone active, et le **NT-proBNP</b>, fragment inactif et pratique à doser.',
        'نغيّر العائلة: هنا لا يموت شيء. عندما يمدّد الحجم أو الضغط <b>البطينات</b>، يشطر عضل القلب سلفه <b>' + FP % 'pro-BNP' + '</b> إلى قطعتين: <b>' + FP % 'BNP' + '</b> الهرمون الفعال و<b>' + FP % 'NT-proBNP' + '</b> القطعة غير الفعالة والعملية للقياس.'),
    [
        fig('peptides.webp',
            "Schéma du clivage du pro-BNP en BNP et NT-proBNP : un ventricule distendu libère le pro-BNP qui se scinde en BNP actif agissant sur les vaisseaux et le rein avec vasodilatation filtration accrue et natriurèse, et NT-proBNP inactif stable éliminé par le rein",
            '💡 <b>Un précurseur, deux destins :</b> BNP agit · NT-proBNP témoigne (plus stable)'),
        spot(6),
        lbox('pep-box1', 'fa-gears', 'La physiologie, du stimulus à l\'action',
            [
                '<b>Le déclencheur</b> : augmentation du <b>volume</b> ou de la <b>pression</b> intracardiaque → distension, principalement <b>ventriculaire</b> — d\'où la sécrétion.',
                '<b>Le clivage</b> : le <b>pro-BNP</b> (précurseur) donne <b>1 BNP + 1 NT-proBNP</b>, en quantités équimolaires.',
                '<b>Le BNP agit</b> : <b>vasodilatation</b>, augmentation de la <b>filtration</b> et de l\'<b>excrétion rénale du sodium</b> (diuresa, natriurèse), <b>inhibition du SRAA et du sympathique</b>, effet <b>anti-fibrotique</b> — il décharge le ventricule qui l\'a appelé.',
                '<b>Le NT-proBNP témoigne</b> : fragment <b>inactif</b>, <b>stable</b>, <b>demi-vie plus longue</b>, élimination <b>rénale</b>, concentrations plus élevées → souvent le plus <b>pratique et précis</b> à doser.',
            ],
            arbox('fa-gears', 'الفيزيولوجيا، من المنبّه إلى الفعل', [
                '<b>المحرّك</b>: ازدياد <b>الحجم</b> أو <b>الضغط</b> داخل القلب ← تمدّد <b>بطيني</b> أساساً — ومنه الإفراز.',
                '<b>الشطر</b>: <b>' + FP % 'pro-BNP' + '</b> (السلف) يعطي <b>BNP واحد + NT-proBNP واحد</b> بكميات متكافئة مولياً.',
                '<b>' + FP % 'BNP' + ' يعمل</b>: <b>توسّع وعائي</b>، ازدياد <b>الترشيح</b> و<b>إطراح الصوديوم كلوياً</b> (إدرار)، <b>تثبيط SRAA والودّي</b>، أثر <b>مضاد للتليّف</b> — يفرّغ البطين الذي ناداه.',
                '<b>' + FP % 'NT-proBNP' + ' يشهد</b>: قطعة <b>غير فعالة</b>، <b>ثابتة</b>، <b>نصف عمر أطول</b>، إطراح <b>كلوي</b>، تراكيز أعلى ← غالباً <b>الأعملي والأدق</b> قياساً.',
            ])),
        table('pep-tab1',
            ['', 'BNP', 'NT-proBNP'],
            [
                ['Nature', 'Fragment <b>actif</b> (hormone)', 'Fragment <b>inactif</b>'],
                ['Stabilité', 'Moindre, dégradation rapide', '<b>Stable</b>, <b>demi-vie plus longue</b>'],
                ['Élimination', 'Enzymes plasmatiques (dont Néprilysine) + rein', 'Principalement <b>rénale</b>'],
                ['Effets', 'Vasodilatation, diurèse, natriurèse, anti-SRAA', 'Aucun — c\'est un témoin'],
                ['Usage', 'Diagnostic et suivi de l\'IC', 'Diagnostic et suivi de l\'IC, souvent <b>plus pratique</b>'],
            ],
            '<thead><tr><th></th><th>BNP</th><th>NT-proBNP</th></tr></thead><tbody>'
            '<tr><td>الطبيعة</td><td>قطعة <b>فعالة</b> (هرمون)</td><td>قطعة <b>غير فعالة</b></td></tr>'
            '<tr><td>الثبات</td><td>أقل، تدرّك سريع</td><td><b>ثابتة</b>، <b>نصف عمر أطول</b></td></tr>'
            '<tr><td>الإطراح</td><td>إنزيمات بلازمية (منها ' + FT % 'Néprilysine' + ') + كلية</td><td><b>كلوي</b> أساساً</td></tr>'
            '<tr><td>الآثار</td><td>توسّع وعائي، إدرار، إطراح صوديوم، ضد SRAA</td><td>لا شيء — إنه شاهد</td></tr>'
            '<tr><td>الاستعمال</td><td>تشخيص ومتابعة قصور القلب</td><td>تشخيص ومتابعة، غالباً <b>أعملي</b></td></tr></tbody>'),
        focus([
            '<b>Fragments intervertis (②)</b> : « le NT-proBNP est l\'hormone active vasodilatatrice » — non : actif = <b>BNP</b>, inactif = NT-proBNP.',
            '<b>Annale réelle (2020)</b> : « la BNP est sécrétée par le <b>ventricule</b> » → vrai ; « le pro-BNP est sécrété par l\'<b>oreillette</b> suite à une <b>diminution</b> du volume » → faux deux fois (ventricules + augmentation).',
            '<b>Stimulus inversé (⑤)</b> : c\'est la surcharge (volume/pression ↑) qui déclenche — « quand le volume diminue » est faux.',
        ]),
    ], '10. BNP & NT-proBNP'))

# ═══════════════ 11. NP CLINIQUE ★★ ═══════════════
OUT.append(section('np-clinique', 11, 'Les peptides en clinique — la dyspnée qui hésite ★★',
    sub('npc-sub',
        'Quatre métiers pour deux molécules : <b>diagnostiquer</b> l\'insuffisance cardiaque (avec l\'échographie), <b>trancher</b> l\'origine d\'une dyspnée, <b>pronostiquer</b> et <b>suivre</b> le traitement. À condition de connaître leurs humeurs : âge, sexe, rein, obésité…',
        'أربعة أدوار لجزيئتين: <b>تشخيص</b> قصور القلب (مع التخطيط فوق الصوتي)، و<b>حسم</b> أصل ضيق النفس، و<b>التكهن</b> و<b>متابعة</b> العلاج. بشرط معرفة تقلّباتهما: العمر، الجنس، الكلية، السمنة…'),
    [
        fig('np-clinique.webp',
            "Planche clinique des peptides natriurétiques : patiente âgée dyspnéique aux urgences hésitant entre cœur et poumon, à gauche insuffisance cardiaque avec NT-proBNP très élevé et cœur dilaté radio, à droite dyspnée pulmonaire avec NT-proBNP normal et poumons hyperclairs, bandeau diagnostic pronostic suivi toujours avec ETT",
            '💡 <b>Le geste qui rapporte :</b> dyspnée indécise → le peptide tranche cardiaque vs pulmonaire'),
        spot(7),
        lbox('npc-box1', 'fa-stethoscope', 'Les quatre usages du cours',
            [
                '<b>Diagnostic de l\'IC</b> : surtout quand les symptômes sont ambigus — <b>en complément de l\'ETT</b>, jamais à sa place.',
                '<b>Orientation d\'urgence</b> : dyspnée <b>cardiaque → peptides très élevés</b> ; dyspnée pulmonaire → <b>valeurs normales</b>. C\'est LA question des annales.',
                '<b>Pronostic</b> : des niveaux élevés signalent un <b>pronostic péjoratif</b> (risque de décompensation, hospitalisation, décès).',
                '<b>Suivi thérapeutique</b> : une <b>baisse</b> sous traitement suggère une <b>amélioration de la fonction cardiaque</b> ; la cinétique guide les ajustements.',
            ],
            arbox('fa-stethoscope', 'استعمالات الدرس الأربعة', [
                '<b>تشخيص قصور القلب</b>: خاصة عند غموض الأعراض — <b>مكمّلاً للتخطيط فوق الصوتي (ETT)</b>، أبداً بدلاً عنه.',
                '<b>التوجيه الطارئ</b>: ضيق نفس <b>قلبي ← الببتيدات مرتفعة جداً</b>؛ رئوي ← <b>قيم طبيعية</b>. هذا هو سؤال الامتحانات.',
                '<b>التكهن</b>: المستويات المرتفعة تشير إلى <b>تكهن سيئ</b> (خطر انهيار، استشفاء، وفاة).',
                '<b>المتابعة العلاجية</b>: <b>انخفاضها</b> تحت العلاج يوحي <b>بتحسّن الوظيفة القلبية</b>؛ والحركية توجّه التعديلات.',
            ])),
        table('npc-tab1',
            ['Le NT-proBNP augmente ↑', 'Le NT-proBNP diminue ↓ / pièges'],
            [
                ['<b>Âge</b> (plus élevé chez le sujet âgé)', '<b>Obésité</b> : valeurs plus <b>basses</b> — traîtresse'],
                ['<b>Sexe féminin</b> (femme &gt; homme)', 'Après <b>effort intense</b> : élévation <b>transitoire</b> (à ne pas surinterpréter)'],
                ['IC, dysfonction ventriculaire', '—'],
                ['Hypertrophie ventriculaire', '—'],
                ['Fibrillation atriale', '—'],
                ['Insuffisance rénale', '—'],
                ['Hypertension artérielle / pulmonaire', '—'],
                ['Anémie · hyperthyroïdie · BPCO · embolie pulmonaire · diabète · cirrhose avec ascite · syndromes coronariens', '—'],
            ],
            '<thead><tr><th>NT-proBNP يرتفع ↑</th><th>NT-proBNP ينخفض ↓ / فخاخ</th></tr></thead><tbody>'
            '<tr><td><b>العمر</b> (أعلى عند المسنّ)</td><td><b>السمنة</b>: قيم <b>أخفض</b> — مخادعة</td></tr>'
            '<tr><td><b>الأنوثة</b> (مرأة > رجل)</td><td>بعد <b>جهد شديد</b>: ارتفاع <b>عابر</b> (لا تضخّمه)</td></tr>'
            '<tr><td>قصور قلب، خلل وظيفة بطينية</td><td>—</td></tr>'
            '<tr><td>تضخّم بطيني</td><td>—</td></tr>'
            '<tr><td>رجفان أذيني</td><td>—</td></tr>'
            '<tr><td>قصور كلوي</td><td>—</td></tr>'
            '<tr><td>فرط ضغط شرياني/رئوي</td><td>—</td></tr>'
            '<tr><td>فقر دم · فرط درقية · داء انسداد رئوي · انصمام رئوي · سكري · تليّف كبد مع حبن · متلازمات إكليلية</td><td>—</td></tr></tbody>'),
        focus([
            '<b>Annales réelles (×3)</b> : « le dosage de la BNP permettrait de différencier dyspnée cardiaque ou pulmonaire » et « NT-proBNP : très bonne VPN <b>et</b> VPP pour l\'IC » → vrais ; et « dyspnées d\'étiologie difficile » proposée comme indication des <b>troponines</b> → faux : c\'est le territoire des peptides.',
            '<b>Obésité inversée (⑤)</b> : l\'obésité <b>baisse</b> le NT-proBNP — une valeur « normale » chez l\'obèse n\'exclut pas l\'IC.',
            '<b>Troponine égarée (②)</b> : « la troponine est un marqueur de suivi de l\'insuffisance cardiaque » — corrigé faux : le suivi d\'IC, c\'est <b>BNP/NT-proBNP</b>.',
        ]),
    ], '11. PEPTIDES EN CLINIQUE'))

# ═══════════════ 12. INFLAMMATION ═══════════════
OUT.append(section('inflammation', 12, 'Inflammation & risque cardiovasculaire — le terrain qui couve',
    sub('inf-sub',
        'Troisième famille : des marqueurs qui ne diagnostiquent aucun événement, mais <b>prédisent le risque</b> sur le long cours — inflammation vasculaire silencieuse et thrombus en préparation.',
        'العائلة الثالثة: واسمات لا تشخّص أي حدث، لكنها <b>تتنبأ بالخطر</b> على المدى البعيد — التهاب وعائي صامت وخثرة قيد التحضير.'),
    [
        fig('inflammation.webp',
            "Planche de l'inflammation et du risque cardiovasculaire : paroi artérielle avec plaque d'athérome enflammée, échelle de risque hs-CRP inférieure à un faible, un à trois intermédiaire, supérieure à trois milligrammes par litre élevé, et réseau de fibrinogène formant un début de caillot",
            '💡 <b>Deux seuils, une phrase :</b> hs-CRP &gt; 3 mg/L = risque élevé · fibrinogène = inflammation + thrombose'),
        spot(7),
        grid2(
            mini('inf-mini1', 'red', 'fa-fire', 'HS-CRP — PROPHÈTE DU RISQUE',
                [
                    '<b>Protéine C-réactive hypersensible</b> : l\'inflammation vasculaire silencieuse, chiffres à l\'appui',
                    '<b>&lt; 1 mg/L</b> risque faible · <b>1–3</b> intermédiaire · <b>&gt; 3 mg/L</b> risque élevé',
                    'Elle <b>prédit</b> les événements futurs — elle ne diagnostique <b>pas</b> l\'infarctus en cours',
                ],
                armini('fa-fire', 'HS-CRP — نبيّ الخطر', [
                    '<b>البروتين C التفاعلي فائق الحساسية</b>: التهاب وعائي صامت، بالأرقام',
                    '<b>&lt; 1 مغ/ل</b> خطر منخفض · <b>1–3</b> متوسط · <b>&gt; 3 مغ/ل</b> خطر مرتفع',
                    '<b>يتنبأ</b> بالأحداث المستقبلية — ولا يشخّص الاحتشاء الجاري',
                ])),
            mini('inf-mini2', 'blue', 'fa-droplet', 'FIBRINOGÈNE — DOUBLE CASQUETTE',
                [
                    'Protéine de l\'<b>inflammation</b> et facteur de <b>thrombose</b> (précurseur de la fibrine)',
                    'Élevé = paroi enflammée <b>et</b> sang plus prêt à coaguler',
                    'Même logique que la hs-CRP : marqueur de <b>risque</b>, pas d\'événement',
                ],
                armini('fa-droplet', 'الفيبرينوجين — قبعتان', [
                    'بروتين <b>الالتهاب</b> وعامل <b>خثر</b> (سلف الفيبرين)',
                    'مرتفع = جدار ملتهب <b>و</b>دم أجهز للتخثر',
                    'نفس منطق ' + FP % 'hs-CRP' + ': واسم <b>خطر</b> لا حدث',
                ]), delay='1')),
        focus([
            '<b>Seuils mélangés (⑧)</b> : « hs-CRP &lt; 1 mg/L = risque élevé » — l\'échelle monte avec le risque : &lt;1 faible, &gt;3 élevé.',
            '<b>Métier confondu (②)</b> : « la hs-CRP diagnostique l\'infarctus » — elle <b>prédit</b>, la troponine <b>diagnostique</b>.',
        ]),
    ], '12. INFLAMMATION & RISQUE'))

# ═══════════════ MÉTHODE ═══════════════
methode = '''            <!-- ═══════════════ MÉTHODE EMD ═══════════════ -->
            <section class="lsection" id="methode">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-user-secret"></i></div>
                    <div>
                        <h2>La méthode de l'examinateur — ce que les 10 annales révèlent</h2>
                        ''' + sub('met-sub',
                            'J\'ai disséqué les 10 QCM authentiques (recueil ELITE CARDIO 3ᵉ, Biochimie §5, PROMO 2018 → 2022) : la troponine occupe <b>8 questions sur 10</b>, les cinétiques reviennent sans relâche, et les pièges tournent autour de l\'absolu (« toujours », « uniquement ») et d\'un adjectif — <b>coronarienne au lieu de myocardique</b>.',
                            'شرّحت الأسئلة العشرة الحقيقية (مجموعة ' + FP % 'ELITE CARDIO' + '، §5، دفعات 2018 ← 2022): التروبونين تحتل <b>8 أسئلة من 10</b>، الحركيات تعود بلا هوادة، والفخاخ تدور حول المطلق («دائماً»، «فقط») وحول صفة واحدة — <b>إكليلية بدل عضل-قلبية</b>.') + '''
                    </div>
                </div>

''' + table('met-tab1',
    ['Thème', 'Fréquence', 'Ce qu\'il faut savoir faire'],
    [
        ['<b>Troponine : spécificité & causes</b>', '★★★★ (8/10)', 'I/T spécifiques, C non ; myocardique ≠ coronarienne ; lister les ↑ hors IDM (IC, EP, sepsis…)'],
        ['<b>Cinétiques comparées</b>', '★★★', 'Ranger myo (2 h → 24 h), CK-MB (4–6 h → 2–3 j), troponine (→ 10 j, rétrospectif)'],
        ['<b>BNP / NT-proBNP</b>', '★★★', 'Ventriculaire, diurétique/vasodilatateur ; dyspnée cardiaque vs pulmonaire ; VPN/VPP'],
        ['<b>Marqueur idéal & définitions</b>', '★★★', 'Sensible + spécifique + précoce ; IDM = nécrose ischémique + marqueurs mesurables'],
        ['<b>Algorithmes hs</b>', '★★', 'H0 + 2 h validé ; « deux catégories » non retenu ; VPN excellente'],
        ['<b>Anciens marqueurs</b>', '★★', 'ASAT/LDH/CK déclassés ; copeptine/h-FABP non systématiques (absents des diapos ⚠)'],
    ],
    '<thead><tr><th>الموضوع</th><th>التواتر</th><th>ما يجب إتقانه</th></tr></thead><tbody>'
    '<tr><td><b>التروبونين: النوعية والأسباب</b></td><td>★★★★ (8/10)</td><td>I/T نوعيتان، C لا؛ عضل-قلبية ≠ إكليلية؛ تعداد ارتفاعات خارج الاحتشاء (قصور قلب، انصمام، إنتان…)</td></tr>'
    '<tr><td><b>الحركيات المقارَنة</b></td><td>★★★</td><td>ترتيب ميوغلوبين (2س ← 24س)، ' + FP % 'CK-MB' + ' (4–6س ← 2–3 أيام)، تروبونين (← 10 أيام، رجعي)</td></tr>'
    '<tr><td><b>' + FP % 'BNP / NT-proBNP' + '</b></td><td>★★★</td><td>بطيني، مدرّ وموسّع وعائي؛ ضيق نفس قلبي مقابل رئوي؛ قيم تكهنية</td></tr>'
    '<tr><td><b>الواسم المثالي والتعاريف</b></td><td>★★★</td><td>حسّاس + نوعي + مبكر؛ الاحتشاء = نخر إقفاري + واسمات قابلة للقياس</td></tr>'
    '<tr><td><b>خوارزميات فائقة الحساسية</b></td><td>★★</td><td>H0 + ساعتان مصادَق؛ «فئتان» غير محتفظ به؛ قيمة سلبية ممتازة</td></tr>'
    '<tr><td><b>الواسمات القديمة</b></td><td>★★</td><td>' + FP % 'ASAT/LDH/CK' + ' مسقَطة؛ ' + FT % 'copeptine/h-FABP' + ' غير منهجية (غائبة عن الشرائح ⚠)</td></tr></tbody>') + '''

''' + lbox('met-box1', 'fa-bullseye', 'Les 5 réflexes qui rapportent des points dans cette leçon',
    [
        '<b>1. Chasse l\'absolu</b> — « toujours demandée », « uniquement en cas d\'infarctus », « que pour l\'IC gauche » : dans ces annales, l\'absolu est <b>systématiquement faux</b>.',
        '<b>2. Pèse chaque adjectif</b> — « spécificité <b>coronarienne</b> » (faux, 2018) contre « <b>cardiospécifique/myocardique</b> » (vrai, 2019) ; « diagnostic <b>rétrospectif</b> » validé grâce à la persistance 6–10 j. Un mot = un point.',
        '<b>3. Classe avant de juger</b> — nécrose, fonction ou inflammation ? Le BNP dans les marqueurs « coronariens », la troponine en « suivi d\'IC » : deux inversions de famille corrigées faux.',
        '<b>4. Aie la courbe en tête</b> — 2 h / 4–6 h / 1–2 h ou 3–6 h, et 24 h / 2–3 j / 10 j : la moitié des questions est une lecture d\'horaire.',
        '<b>5. Réclame le contexte</b> — toute proposition qui conclut sur un chiffre seul sans anamnèse, clinique ni ECG est suspecte par construction.',
    ],
    arbox('fa-bullseye', 'المنعكسات الخمسة التي تجلب النقاط في هذا الدرس', [
        '<b>1. اصطد المطلق</b> — «يُطلب دائماً»، «فقط في حالة الاحتشاء»، «لقصور القلب الأيسر فقط»: في هذه الأسئلة المطلق <b>خاطئ منهجياً</b>.',
        '<b>2. ازن كل صفة</b> — «نوعية <b>إكليلية</b>» (خطأ، 2018) مقابل «<b>نوعية قلبية/عضل-قلبية</b>» (صح، 2019)؛ و«تشخيص <b>رجعي</b>» المصادَق عليه بفضل البقاء 6–10 أيام. كلمة = نقطة.',
        '<b>3. صنّف قبل الحكم</b> — نخر، وظيفة أم التهاب؟ إقحام ' + FP % 'BNP' + ' في واسمات «إكليلية»، والتروبونين في «متابعة قصور القلب»: قلبا عائلة صُحّحا خطأ.',
        '<b>4. احمل المنحنى في ذهنك</b> — ساعتان / 4–6سا / 1–2سا أو 3–6سا، و24سا / 2–3 أيام / 10 أيام: نصف الأسئلة قراءة جدول مواعيد.',
        '<b>5. اطلب السياق</b> — أي اقتراح يستنتج من رقم وحده دون سوابق وسريرية وتخطيط مشبوه بتركيبه.',
    ])) + '''

''' + lbox('met-box2', 'fa-clock', 'Calibration QCM (les vrais corrigés ont parlé)',
    [
        'Les 10 corrigés officiels : <b>1 réponse × 2 · 2 réponses × 1 · 3 réponses × 6 · 4 réponses × 1</b> — une leçon où <b>trois bonnes réponses sur cinq est la norme</b> (60 %).',
        'Les 20 QCM d\'entraînement de cette leçon respectent cette signature : <b>4 × 1 réponse, 2 × 2, 12 × 3, 2 × 4</b>.',
        'Conséquence le jour J : si tu n\'as coché qu\'une seule proposition en biomarqueurs, relis — tu rates probablement deux sœurs de la même famille vraie.',
    ],
    arbox('fa-clock', 'معايرة الأسئلة (التصحيحات الحقيقية تكلّمت)', [
        'التصحيحات الرسمية العشرة: <b>إجابة واحدة ×2 · إجابتان ×1 · ثلاث إجابات ×6 · أربع إجابات ×1</b> — درسٌ فيه <b>ثلاث إجابات صحيحة من خمس هي القاعدة</b> (60٪).',
        'أسئلة التدريب العشرون هنا تحترم هذه البصمة: <b>4×1، 2×2، 12×3، 2×4</b>.',
        'النتيجة يوم الامتحان: إن اخترت اقتراحاً واحداً فقط في الواسمات، أعد القراءة — فغالباً تفوّت أختين من نفس عائلة الصحّات.',
    ])) + '''
            </section>'''
OUT.append(methode)

connexions = '''            <!-- ═══════════════ CONNEXIONS ═══════════════ -->
            <section class="lsection" id="connexions">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-link"></i></div>
                    <div>
                        <h2>Connexions — cette leçon ne vit pas seule</h2>
                        ''' + sub('cx-sub',
                            'La troponine se lit avec un ECG et un patient : cette leçon de laboratoire irrigue tout le module cardio et revient en pneumologie par la dyspnée.',
                            'التروبونين تُقرأ مع تخطيط ومريض: درس المختبر هذا يروي وحدة القلب كلها ويعود في طب الرئتين عبر ضيق النفس.') + '''
                    </div>
                </div>

                <div class="mini-grid cols-3">
''' + mini('cx-mini1', 'red', 'fa-heart-pulse', 'CLINIQUE DU SCA',
    [
        'STEMI/NSTEMI, reperfusion, douleur thoracique : le laboratoire s\'branche sur la <b>sémiologie cardio</b>',
        'L\'ECG trône en premier — la troponine ne retarde <b>jamais</b> la reperfusion',
    ],
    armini('fa-heart-pulse', 'سريرية المتلازمة الإكليلية', [
        FP % 'STEMI/NSTEMI' + '، إعادة التروية، ألم الصدر: المختبر يلتحم بـ<b>سريرية القلب</b>',
        'التخطيط يتصدّر — التروبونين لا تؤخّر إعادة التروية <b>أبداً</b>',
    ])) + '''

''' + mini('cx-mini2', 'blue', 'fa-lungs', 'LA DYSPNÉE (PNEUMO)',
    [
        'Le NT-proBNP tranche <b>cœur vs poumon</b> — directement utile en <b>BPCO/asthme</b> (pn-*)',
        'L\'embolie pulmonaire fait monter <b>les deux</b> (cTn et peptides) : le carrefour parfait',
    ],
    armini('fa-lungs', 'ضيق النفس (طب الرئتين)', [
        FP % 'NT-proBNP' + ' يحسم <b>قلب مقابل رئة</b> — مفيد مباشرة في <b>الانسداد الرئوي/الربو</b>',
        'الانصمام الرئوي يرفع <b>الإثنين</b> (تروبونين وببتيدات): ملتقى مثالي',
    ])) + '''

''' + mini('cx-mini3', 'green', 'fa-flask', 'BIOCHIMIE VOISINE',
    [
        '<b>Lipides (bi-05)</b> : l\'athérosclérose fabrique le SCA que la troponine détecte',
        '<b>Gazométrie (bi-07)</b> : acidose et souffrance d\'organe parlent au même myocarde',
        '<b>Rein</b> : insuffisance rénale = ↑ cTn ET ↑ NT-proBNP — double vigilance',
    ],
    armini('fa-flask', 'الكيمياء الحيوية المجاورة', [
        '<b>الدهون (bi-05)</b>: التصلّب يصنع المتلازمة التي تكشفها التروبونين',
        '<b>قياس الغازات (bi-07)</b>: الحماض ومعاناة العضو يخاطبان العضل نفسه',
        '<b>الكلية</b>: قصورها = تروبونين ↑ وببتيدات ↑ — يقظة مضاعفة',
    ])) + '''
                </div>
            </section>'''
OUT.append(connexions)

# ═══════════════ ANNALES — ELITE Biochimie §5, pp.30-32 (verbatim + corrigés officiels) ═══════════════
ann = '''            <!-- ═══════════════ QCM ANNALES ═══════════════ -->
            <section class="lsection" id="annales">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-award"></i></div>
                    <div>
                        <h2>QCM d'annales — les 10 questions réelles</h2>
                        <div class="lsub">Recueil <b>ELITE CARDIO 3ᵉ année, Biochimie §5 « Biomarqueurs cardiaques »</b> (pp. 30–32), PROMO 2018 → 2022. Énoncés et <b>corrigés officiels</b> reproduits à l'identique — aucun choix inventé ; quand un corrigé ancien diverge du cours actuel, la correction te le dit explicitement. Coche, valide, puis lis pourquoi.</div>
                    </div>
                </div>
'''
AQ = [
 ('PROMO 2022',
  "Une élévation de la troponine est observée :",
  ["Uniquement en cas d'infarctus du myocarde.","En cas d'insuffisance cardiaque sévère aigue ou chronique.","En cas d'embolie pulmonaire.","En cas d'un choc septique.","Uniquement en cas d'insuffisance cardiaque."],
  'B,C,D', 'Réponse : BCD',
  """
<b>Pourquoi :</b> insuffisance cardiaque sévère, embolie pulmonaire et choc septique figurent tous dans le tableau des causes d'élévation des cTn du cours (section 5).
<b>Piège :</b> A et E portent « uniquement » — l'exclusivité est fausse dans les deux sens : la troponine signe une souffrance myocardique, pas un mécanisme.""",
  """
<b>لماذا:</b> قصور القلب الشديد والانصمام الرئوي والصدمة الإنتانية كلها في جدول الدرس لأسباب ارتفاع التروبونين (القسم 5).
<b>الفخ:</b> A وE تحملان «فقط» — الحصرية خاطئة في الاتجاهين: التروبونين توقّع معاناة عضل القلب لا آلية."""),
 ('PROMO 2021 / 2018',
  "Concernant les biomarqueurs cardiaques :",
  ["Les troponines T hypersensibles (TnT Hs) ou I Ultra-Sensible (TnI Us) ont une excellente valeur prédictive négative pour l'IDM.","Le dosage des biomarqueurs type CPK-MB, copeptine ou h-FABP est toujours recommandé dans la démarche diagnostique du SCA.","En cas de suspicion d'IDM, la cinétique de la troponines TnT Hs à H0-H1 permettrait de classer les patients en deux catégories.","Le dosage de la BNP permettrait de différencier entre une dyspnée d'origine cardiaque ou pulmonaire.","Le NT-Pro BNP possède une très bonne valeur prédictive négative et positive pour le diagnostic d'insuffisance cardiaque."],
  'A,D,E', 'Réponse : ADE',
  """
<b>Pourquoi :</b> A (VPN de la hs-cTn), D (dyspnée cardiaque vs pulmonaire) et E (VPN+VPP du NT-proBNP pour l'IC) sont trois usages validés du cours.
<b>Pièges :</b> B porte « toujours recommandé » pour trois marqueurs non systématiques (CPK-MB supplantée, copeptine/h-FABP non validées en routine) ; C n'est pas retenue par le corrigé — les algorithmes réels ne se réduisent pas à deux catégories.""",
  """
<b>لماذا:</b> A (القيمة السلبية لفائق الحساسية)، D (ضيق النفس القلبي مقابل الرئوي)، E (القيمتان السلبية والإيجابية لـNT-proBNP في قصور القلب) ثلاث استخدامات مصادَق عليها في الدرس.
<b>الفخاخ:</b> B تحمل «يُوصى به دائماً» لثلاثة واسمات غير منهجية (CPK-MB مُزاحة، كوبيبتين/h-FABP غير روتينيين)؛ وC غير محتفظ بها في التصحيح — الخوارزميات الحقيقية لا تُختزل في فئتين."""),
 ('PROMO 2021',
  "Parmi les examens biologiques suivants, quel est celui prescrit dans le diagnostic biochimique d'un infarctus du myocarde ?",
  ["Alanine aminotransférase.","Myoglobine.","Troponine.","CKmb.","Gamma glutamyltransférase."],
  'C', 'Réponse : C',
  """
<b>Pourquoi :</b> la troponine est le marqueur de référence actuel (sensible, spécifique, précoce en hypersensible).
<b>Pièges :</b> myoglobine et CK-MB sont supplantées ; ALAT et GGT sont des enzymes hépatiques sans place dans le diagnostic de l'IDM.""",
  """
<b>لماذا:</b> التروبونين هي الواسم المرجعي الحالي (حسّاسة، نوعية، مبكرة بصيغتها فائقة الحساسية).
<b>الفخاخ:</b> الميوغلوبين وCK-MB مُزاحتان؛ وALAT وGGT إنزيمان كبديان لا مكان لهما في تشخيص الاحتشاء."""),
 ('PROMO 2020',
  "Concernant l'insuffisance cardiaque :",
  ["Peut-être secondaire l'athérosclérose.","La troponine est la molécule de choix pour l'évaluation de la maladie.","La BNP est secrétée par le ventricule, et a une action diurétique et vasodilatatrice.","Le pro-BNP est la molécule de choix pour le diagnostic et pronostic de la maladie","Le pro-BNP est secrété par l'oreillette suite à une diminution du volume diastolique."],
  'A,C,D', 'Réponse : ACD',
  """
<b>Pourquoi :</b> l'IC peut être secondaire à l'athérosclérose (cardiopathie ischémique) ; le BNP ventriculaire est bien diurétique et vasodilatateur. B est l'inversion de famille (IC = peptides, pas troponine) et E inverse tout (oreillette + diminution de volume).
<b>Nuance honnête sur D :</b> le corrigé officiel valide « pro-BNP, molécule de choix » ; le cours précise qu'en pratique on dose ses produits de clivage, <b>BNP ou NT-proBNP</b>. Retiens D pour cette annale, dose BNP/NT-proBNP en clinique.""",
  """
<b>لماذا:</b> قصور القلب قد يكون ثانوياً للتصلّب (قلب إقفاري)؛ وBNP البطيني مدرٌّ وموسّع وعائي فعلاً. وB قلبُ عائلة (قصور القلب = الببتيدات لا التروبونين) وE تقلب كل شيء (أذينة + نقص حجم).
<b>فارق صادق حول D:</b> التصحيح الرسمي يصادق على «pro-BNP جزيء الخيار»؛ والدرس يوضح أن ما يُقاس عملياً هو ناتجا شطره <b>BNP أو NT-proBNP</b>."""),
 ('PROMO 2020',
  "Concernant l'infarctus du myocarde :",
  ["Est défini comme une nécrose ischémique accompagnée de sécrétion de marqueurs mesurables.","Les marqueurs enzymatiques ASAT, ALAT, LDH sont des marqueurs précoces et spécifiques.","La myoglobine est un bon marqueur de suivi du risque de ré-infarctus.","La troponine reste à ce jour le marqueur de choix de diagnostic et de pronostic.","La troponine est produite par le ventricule gauche."],
  'A,C,D', 'Réponse : ACD',
  """
<b>Pourquoi :</b> A est la définition (l'annale écrit « sécrétion », le cours dit <b>libération</b> — verbatim conservé) ; D est le credo du chapitre. C est cohérente avec le cours : la myoglobine redescendant en ~24 h, une ré-ascension signale une récidive (p. 16 du cours).
<b>Pièges :</b> B réhabilite ASAT/ALAT/LDH déclassés ; E transforme la troponine (libérée par les cardiomyocytes nécrosés) en sécrétion du ventricule gauche — c'est le BNP.""",
  """
<b>لماذا:</b> A هو التعريف (السؤال يكتب «إفراز» والدرس يقول <b>تحرّر</b> — أبقينا النص)؛ وD هي عقيدة الفصل. وC منسجمة مع الدرس: الميوغلوبين ينزل في ~24 ساعة، فصعود جديد يفضح تكرراً (ص 16).
<b>الفخاخ:</b> B تؤهّل ASAT/ALAT/LDH المسقَطة؛ وE تحوّل التروبونين (المحرَّرة من الخلايا المتنخّرة) إلى إفراز بطين أيسر — ذاك هو BNP."""),
 ('PROMO 2020',
  "Concernant les marqueurs cardiaques :",
  ["Le marqueur idéal doit être sensible, spécifique et précoce.","La troponine ultrasensible doit être mesurée à l'admission et 2heures après pour le diagnostic.","La troponine ne peut être utilisée pour le suivi de l'infarctus du myocarde.","La myoglobine est un marqueur précoce mais peu sensible contrairement à la troponine.","L'intérêt d'un marqueur cardiaque est insuffisant si l'ECG est négatif"],
  'A,B,D', 'Réponse : ABD',
  """
<b>Pourquoi :</b> A est la définition canonique du marqueur idéal ; B est l'algorithme rapide hypersensible (H0 + contrôle précoce). C est fausse (la troponine sert aussi au suivi) et E aussi (ECG « négatif » = NSTEMI possible, justement tranché par la troponine).
<b>Nuance sur D :</b> le corrigé valide « peu sensible » ; le cours insiste surtout sur le défaut de <b>spécificité</b> de la myoglobine. Retiens le verdict officiel ici, et la formule « sensible et précoce mais non spécifique » pour toute question nouvelle.""",
  """
<b>لماذا:</b> A هو التعريف القانوني للواسم المثالي؛ وB هي الخوارزمية السريعة فائقة الحساسية (H0 + مراقبة مبكرة). وC خاطئة (التروبونين تخدم المتابعة أيضاً) وE كذلك (تخطيط «سالب» = NSTEMI محتمل تحسمه التروبونين بالضبط).
<b>فارق حول D:</b> التصحيح يصادق على «قليلة الحساسية»؛ والدرس يؤكد خصوصاً على غياب <b>النوعية</b> عن الميوغلوبين."""),
 ('PROMO 2019',
  "Lesquelles sont des marqueurs biochimiques des maladies coronaires :",
  ["Lactate déshydrogénase.","La Créatine Kinase et isoformes.","La Myoglobine.","Les troponines.","Le Peptide Natriurétique de type B (BNP)."],
  'A,B,C,D', 'Réponse : ABCD',
  """
<b>Pourquoi :</b> LDH, CK et isoformes, myoglobine et troponines sont des contenus libérés par le cardiomyocyte nécrosé (des plus anciens aux actuels).
<b>Piège :</b> le BNP est sécrété par un ventricule vivant qui souffre — famille fonction, exclue des marqueurs de nécrose.""",
  """
<b>لماذا:</b> LDH وCK ونظائرها والميوغلوبين والتروبونينات محتويات تُحرّرها خلية العضل المتنخّرة (من الأقدم إلى الحالي).
<b>الفخ:</b> BNP يُفرزه بطين حي يعاني — عائلة الوظيفة، مستبعَدة من واسمات النخر."""),
 ('PROMO 2019',
  "Concernant les marqueurs biochimiques de l'infarctus du myocarde :",
  ["La myoglobine est un marqueur cardiospécifique.","La CK-MB augmente plus rapidement que la myoglobine.","L'ASAT reste actuellement un marqueur de choix pour le diagnostic de l'infarctus du myocarde.","La troponine permet un diagnostic de l'infarctus du myocarde.","La troponine est un marqueur cardiospécifique."],
  'D,E', 'Réponse : DE',
  """
<b>Pourquoi :</b> D et E sont les deux phrases du cours sur la troponine (diagnostic + cardiospécificité tissulaire).
<b>Pièges :</b> A prête la spécificité à la myoglobine (son exact contraire) ; B inverse les horloges (myo 2 h avant CK-MB 4–6 h) ; C ressuscite l'ASAT déclassée.""",
  """
<b>لماذا:</b> D وE هما جملتا الدرس عن التروبونين (التشخيص + النوعية النسيجية القلبية).
<b>الفخاخ:</b> A تُقرض النوعية للميوغلوبين (عكسها تماماً)؛ وB تقلب الساعتين (ميوغلوبين ساعتان قبل CK-MB ‏4–6 سا)؛ وC تُحيي ASAT المسقَطة."""),
 ('PROMO 2019',
  "Quels sont les indications du dosage des troponines :",
  ["Toutes les atteintes cardiaques avec ischémie et souffrance myocardique.","Diagnostic rétrospectif des IDM.","Dysfonctions ventriculaires diastoliques.","Atteinte myocardique au cours des péricardites et des myocardites.","Dyspnées d'étiologie difficile"],
  'A,B,D', 'Réponse : ABD',
  """
<b>Pourquoi :</b> souffrance ischémique (A), diagnostic rétrospectif grâce à la persistance 6–10 j (B), atteinte myocardique des péricardites/myocardites (D) — trois indications du cours.
<b>Pièges :</b> C relève des peptides et de l'ETT ; E (« dyspnées d'étiologie difficile ») est le territoire du BNP/NT-proBNP — l'inversion de famille signature de ce chapitre.""",
  """
<b>لماذا:</b> المعاناة الإقفارية (A)، التشخيص الرجعي بفضل البقاء 6–10 أيام (B)، إصابة العضل في التهابات التامور/عضل القلب (D) — ثلاثة استطبابات من الدرس.
<b>الفخاخ:</b> C من مجال الببتيدات وتخطيط فوق صوتي؛ وE («ضيق نفس صعب السبب») أرض BNP/NT-proBNP — قلبُ العائلة المميز لهذا الفصل."""),
 ('PROMO 2018',
  "Concernant les biomarqueurs cardiaques :",
  ["Un marqueur biologique idéal doit avoir une spécificité et sensibilité élevées","Les biomarqueurs ne permettent pas un diagnostic précoce","Ne peuvent être utilisés qu'en milieu hospitalier","Les troponines cardiaques ont une très bonne spécificité coronarienne","La troponine C représente un marqueur de choix en cardiologie"],
  'A', 'Réponse : A',
  """
<b>Pourquoi :</b> seule A survit : spécificité + sensibilité élevées, le portrait de l'idéal.
<b>Pièges :</b> B est la négation plaquée (la hs-cTn est précoce par construction) ; C invente une restriction de lieu ; D est LE piège d'adjectif du chapitre — spécificité <b>myocardique</b>, pas « coronarienne » ; E prête à TnC (non spécifique) le rôle de I/T.""",
  """
<b>لماذا:</b> A وحدها تنجو: نوعية + حساسية مرتفعتان، صورة المثالي.
<b>الفخاخ:</b> B نفي ملصَق (فائقة الحساسية مبكرة بالتعريف)؛ وC تخترع قيد مكان؛ وD هي فخ الصفة في هذه الحلقة — النوعية <b>عضل-قلبية</b> لا «إكليلية»؛ وE تُقرض TnC (غير النوعية) دور I/T."""),
]
for i, (src, en, props, ans, ansfr, exp_fr, exp_ar) in enumerate(AQ, 1):
    L = 'ABCDE'
    opts = '\n'.join(f'''                        <label class="qopt"><input type="checkbox" value="{L[j]}"><span class="qletter">{L[j]}</span><span>{p}</span></label>'''
                     for j, p in enumerate(props))
    AR[f'ann-exp-{i}'] = exp_ar
    ann += f'''
                <div class="qblock ann-block reveal" data-answer="{ans}">
                    <div class="qhead">
                        <span class="qnum">Q{i}</span>
                        <span class="qsource">{src}</span>
                        <span class="qbadge badge-ann"><i class="fa-solid fa-graduation-cap"></i> Annale réelle</span>
                    </div>
                    <p class="qtext">{en}</p>
                    <div class="qoptions">
{opts}
                    </div>
                    <button class="qcheck btn btn-primary btn-sm"><i class="fa-solid fa-check"></i> Vérifier</button>
                    <div class="qexp" data-tr="ann-exp-{i}" hidden>
                        <p class="qexp-ans"><i class="fa-solid fa-award"></i> {ansfr}</p>
                        {exp_fr}
                    </div>
                </div>
'''
ann += '''
                <div class="score-box" id="annalesScore"></div>
            </section>'''
OUT.append(ann)
# ═══════════════ ENTRAÎNEMENT — 20 (4×1 · 2×2 · 12×3 · 2×4) ═══════════════
entr = '''            <!-- ═══════════════ QCM ENTRAÎNEMENT ═══════════════ -->
            <section class="lsection" id="entrainement">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-bullseye"></i></div>
                    <div>
                        <h2>QCM d'entraînement — profil calqué sur les vraies annales</h2>
                        <div class="lsub">20 questions originales construites <b>uniquement</b> depuis le cours du D<sup>r</sup> Besbes et les verdicts des annales. Le nombre de réponses justes suit la signature des corrigés officiels, et — contrairement aux anciennes annales — chaque correction est ici revendiquée <b>sans coquille</b> : cours d'abord.</div>
                    </div>
                </div>
'''
EQ = [
 ('Section 1 · Définition', 'B',
  "Un biomarqueur cardiaque est, d'après le cours :",
  ['Une substance mesurable uniquement en milieu hospitalier','Une substance mesurable dans le sang, produite ou libérée par le cœur atteint, utilisée pour le diagnostic, le pronostic ou le suivi cardiaque','Un symptôme ressenti par le patient','Un paramètre qui remplace l\'ECG et l\'imagerie','Une protéine exclusivement sécrétée par les oreillettes'],
  'Réponse juste : B',
  """
<b>Pourquoi :</b> définition intégrale du cours : mesurable dans le sang + produite/libérée par le cœur atteint + diagnostic, pronostic, suivi.
<b>Pièges :</b> A reprend l'annale « utilisables qu'en milieu hospitalier » (fausse) ; C n'est pas mesurable dans le sang ; D contredit la conclusion du cours (« complètent, ne remplacent pas ») ; E inverse l'anatomie des peptides (ventriculaires).""",
  """
<b>لماذا:</b> تعريف الدرس كاملاً: قابل للقياس في الدم + من إنتاج/تحرير القلب المصاب + تشخيص وتكهن ومتابعة.
<b>الفخاخ:</b> A تكرّر سؤال «لا تُستعمل إلا في المستشفى» (خاطئة)؛ C لا يُقاس في الدم؛ D تناقض خاتمة الدرس («تُكمل ولا تعوّض»)؛ E تقلب تشريح الببتيدات (بطينية)."""),
 ('Section 1 · Familles', 'A,B,C',
  "Le cours classe les biomarqueurs cardiaques en trois familles :",
  ['Les marqueurs de nécrose myocardique (troponine, CK-MB, myoglobine)','Les marqueurs de fonction myocardique (BNP, NT-proBNP)','Les marqueurs d\'inflammation et de risque cardiovasculaire (hs-CRP, fibrinogène)','Les marqueurs de coagulation (D-dimères, TP)','Les hormones thyroïdiennes (TSH, T4)'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> les trois questions du cours : le myocarde meurt-il ? le ventricule souffre-t-il ? le risque couve-t-il ?
<b>Pièges :</b> D et E sont des familles voisines réelles mais étrangères à cette classification — la famille croisée est le piège n°1 du chapitre.""",
  """
<b>لماذا:</b> أسئلة الدرس الثلاثة: هل يموت العضل؟ هل يعاني البطين؟ هل يختمر الخطر؟
<b>الفخاخ:</b> D وE عائلتان مجاورتان حقيقيتان لكنهما غريبتان عن هذا التصنيف — خلط العائلات هو فخ الفصل الأول."""),
 ('Section 2 · Nécrose', 'A,B,C',
  "Concernant les marqueurs de nécrose myocardique :",
  ['Ils sont des protéines libérées dans le sang lors de la destruction des cellules myocardiques','Ils permettent de diagnostiquer les syndromes coronariens aigus','Ils permettent d\'évaluer la sévérité de l\'atteinte','Ils sont sécrétés par les ventricules en réponse à une distension','Le BNP en est le représentant principal'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> membrane rompue → protéines dans le sang ; deux usages : diagnostiquer et évaluer la sévérité (diapositive du cours).
<b>Pièges :</b> D et E décrivent les peptides natriurétiques (sécrétés, vivants, fonction) — la confusion libérée/sécrétée est correctionée par le corps.""",
  """
<b>لماذا:</b> غشاء متمزّق ← بروتينات في الدم؛ واستعمالان: التشخيص وتقييم الشدة (شريحة الدرس).
<b>الفخاخ:</b> D وE تصفان الببتيدات (مُفرزة، حية، وظيفة) — الخلط حرَّر/أفرز يُصحَّح بالجسم."""),
 ('Section 3 · Complexe ★★', 'A,B,C',
  "Au sein du complexe troponine :",
  ['La troponine C se lie au calcium et déclenche la contraction','La troponine I inhibe l\'interaction actine-myosine','La troponine T fixe le complexe à la tropomyosine','La troponine C est la sous-unité cardiospécifique dosée en routine','La troponine I est présente dans le muscle squelettique'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> C-alcium · I-nhibe · T-ropomyosine — trois métiers, trois phrases du cours.
<b>Pièges :</b> D prête à TnC la carte d'identité de I/T (TnC existe aussi dans le muscle squelettique) ; E fait l'inverse avec TnI, qui est absente du muscle squelettique.""",
  """
<b>لماذا:</b> C-كالسيوم · I-تثبيط · T-تروبوميوسين — ثلاث مهن، ثلاث جمل من الدرس.
<b>الفخاخ:</b> D تُقرض TnC هوية I/T (TnC موجود أيضاً في العضل الهيكلي)؛ وE تفعل العكس بـTnI الغائبة عن العضل الهيكلي."""),
 ('Section 3 · Spécificité ★★', 'C',
  "La particularité qui fait des troponines I et T les marqueurs de référence de la nécrose myocardique est :",
  ['Elles sont aussi présentes dans le muscle squelettique','Elles sont produites par les oreillettes','Elles sont spécifiques du muscle cardiaque','Elles apparaissent toujours avant la myoglobine','Elles sont exclusivement coronariennes'],
  'Réponse juste : C',
  """
<b>Pourquoi :</b> « très sensible et très spécifique du tissu myocardique » — I et T sont absentes du muscle squelettique, c'est toute leur valeur.
<b>Piège d'annale :</b> E remplace myocardique par « coronariennes » : la troponine monte aussi dans la myocardite, l'EP ou le sepsis, sans coronaire""",
  """
<b>لماذا:</b> «حسّاسة جداً ونوعية جداً لنسيج عضل القلب» — I وT غائبتان عن العضل الهيكلي، وهذه قيمتهما كلها.
<b>فخ الامتحان:</b> E تستبدل عضل-قلبية بـ«إكليلية»: التروبونين تصعد أيضاً في التهاب عضل القلب والانصمام والإنتان، دون إكليلي."""),
 ('Section 4 · Hypersensible ★★', 'A,B,C',
  "Concernant la troponine hypersensible (hs-cTn) et les durées :",
  ['Elle est détectable 1 à 2 heures après le début des symptômes','La troponine classique est détectable en 3 à 6 heures','La TnT peut rester élevée jusqu\'à 10 jours','La TnI reste élevée jusqu\'à 10 jours tandis que la TnT seulement 3 à 6 jours','L\'hypersensible est moins sensible que la classique'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> montée hs 1–2 h contre 3–6 h ; durées TnI 3–6 j, TnT ≤ 10 j — dans les deux générations de dosage.
<b>Pièges :</b> D permute les durées (T dure plus que I) ; E nie la définition même de l'hypersensibilité.""",
  """
<b>لماذا:</b> صعود فائق الحساسية 1–2 ساعة مقابل 3–6؛ والمدد TnI ‏3–6 أيام وTnT ≤ 10 أيام — في جيلي القياس.
<b>الفخاخ:</b> D تُبدّل المدتين (T تدوم أكثر من I)؛ وE تنفي تعريف فرط الحساسية نفسه."""),
 ('Section 5 · Variations', 'A,B,C',
  "Les troponines cardiaques augmentent avec :",
  ['L\'âge (plus élevées après 60 ans)','Le sexe masculin par rapport au sexe féminin','L\'insuffisance rénale','Jamais après un exercice intense','Jamais en cas de sepsis'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> deux variations physiologiques du cours (âge, homme) + une cause extracardiaque majeure (rein).
<b>Pièges :</b> D et E portent « jamais » — l'exercice intense prolongé et le sepsis figurent explicitement dans le tableau des causes.""",
  """
<b>لماذا:</b> تغيّران فيزيولوجيان من الدرس (العمر، الرجل) + سبب خارج قلبي كبير (الكلية).
<b>الفخاخ:</b> D وE تحملان «أبداً» — الجهد الشديد المطوّل والإنتان موجودان صراحة في جدول الأسباب."""),
 ('Section 5 · Causes', 'A,B,C,D',
  "Une troponine élevée SANS infarctus coronarien peut s'observer dans :",
  ['La myocardite','L\'embolie pulmonaire','L\'insuffisance cardiaque','La contusion cardiaque post-traumatique','Uniquement l\'infarctus du myocarde'],
  'Réponses justes : A, B, C, D',
  """
<b>Pourquoi :</b> myocardite et contusion (cardiaques), EP (extracardiaque), IC : quatre lignes du tableau du cours — la troponine monte sans aucune coronaire occluse.
<b>Piège :</b> E est l'« uniquement » de l'annale 2022, corrigé faux des deux côtés.""",
  """
<b>لماذا:</b> التهاب عضل القلب والرضّ (قلبيان)، الانصمام (خارج قلبي)، قصور القلب: أربعة أسطر من جدول الدرس — التروبونين تصعد دون أي إكليلي مسدود.
<b>الفخ:</b> E هي «فقط» سؤال 2022، المخطئة في الاتجاهين."""),
 ('Section 6 · STEMI ★★', 'B',
  "Devant un SCA avec sus-décalage du segment ST (STEMI), la conduite qui reflète le cours est :",
  ['Attendre le résultat de la troponine H6 avant de reperfuser','Reperfusion immédiate : le diagnostic est clinique et ECG, sans attendre la troponine','Exclure l\'infarctus si la troponine H0 est normale','Ne jamais doser la troponine, elle est sans intérêt','Attendre la cinétique complète sur deux dosages avant tout geste'],
  'Réponse juste : B',
  """
<b>Pourquoi :</b> le cours oppose STEMI (diagnostic clinique/ECG, reperfusion immédiate) et NSTEMI (la cinétique décide) — le temps, c'est du myocarde.
<b>Pièges :</b> A et E transfèrent au STEMI la patience du NSTEMI ; C oublie qu'à H0 la troponine peut encore être invisible ; D exagère dans l'autre sens (on dose — pour le suivi, pas pour décider).""",
  """
<b>لماذا:</b> الدرس يقابل بين STEMI (تشخيص سريري/تخطيطي، إعادة تروية فورية) وNSTEMI (الحركية تقرّر) — الوقت هو عضل قلب.
<b>الفخاخ:</b> A وE تنقلان إلى STEMI صبر NSTEMI؛ C تنسى أن التروبونين عند H0 قد تكون غير مرئية بعد؛ D تبالغ بالاتجاه الآخر (نقيس — للمتابعة لا للقرار)."""),
 ('Section 6 · Algorithmes ★★', 'A,B,C',
  "Concernant les algorithmes de dosage de la troponine dans le SCA sans sus-décalage :",
  ['En troponine classique : premier dosage à H0 puis contrôle à H6–H9','En troponine hypersensible : H0 puis contrôle à H1–H3','Deux troponines normales (H0 et contrôle) permettent d\'exclure l\'infarctus avec fiabilité','Une seule troponine normale à H0 exclut toujours l\'infarctus','Le diagnostic de NSTEMI repose sur l\'ECG seul'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> les deux horloges du cours + la règle de sortie : normale à H0 ET au contrôle = IDM exclu avec fiabilité.
<b>Pièges :</b> D supprime le contrôle ; E inverse la définition du NSTEMI (sans sus-décalage, c'est la troponine qui fait le diagnostic).""",
  """
<b>لماذا:</b> ساعتا الدرس + قاعدة الخروج: طبيعية عند H0 وعند المراقبة = الاحتشاء مستبعَد بثقة.
<b>الفخاخ:</b> D تلغي المراقبة؛ وE تقلب تعريف NSTEMI (دون ارتفاع ST، التروبونين هي التي تصنع التشخيص)."""),
 ('Section 7 · Myoglobine', 'A,B,C',
  "La myoglobine :",
  ['Apparaît dans le sang dès environ 2 heures après la lésion','Atteint son pic entre 4 et 12 heures','Redevient normale en environ 24 heures','Est spécifique du myocarde','Reste élevée 6 à 10 jours comme la troponine'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> le trio temps complet de la planche : 2 h / pic 4–12 h / normale ~24 h.
<b>Pièges :</b> D nie sa disqualification (présente dans tout le muscle strié) ; E lui prête la longue traîne de la troponine.""",
  """
<b>لماذا:</b> ثلاثي الزمن الكامل في اللوحة: ساعتان / ذروة 4–12 سا / طبيعية ~24 سا.
<b>الفخاخ:</b> D تنفي سبب استبعادها (حاضرة في كل العضل المخطط)؛ وE تُقرضها ذيل التروبونين الطويل."""),
 ('Section 7 · Causes myoglobine', 'A,B',
  "En dehors de l'infarctus, la myoglobine s'élève notamment dans :",
  ['La rhabdomyolyse','Les convulsions prolongées','Uniquement les lésions coronariennes','L\'insuffisance thyroïdienne isolée','La simple élévation du BNP'],
  'Réponses justes : A, B',
  """
<b>Pourquoi :</b> toute souffrance du muscle strié libère de la myoglobine : destruction musculaire massive (rhabdomyolyse) ou contractions prolongées (convulsions) — liste du cours.
<b>Pièges :</b> C est l'exclusivité fausse ; D et E n'ont aucun lien musculaire (E est d'ailleurs sans signification : un marqueur n'en élève pas un autre).""",
  """
<b>لماذا:</b> أي معاناة للعضل المخطط تُحرّر الميوغلوبين: تدمير عضلي ضخم (انحلال عضلي) أو انقباضات مطوّلة (اختلاجات) — قائمة الدرس.
<b>الفخاخ:</b> C حصرية خاطئة؛ وD وE لا علاقة لهما بالعضل (E بلا معنى أصلاً: الواسم لا يرفع واسماً آخر)."""),
 ('Section 8 · CK-MB', 'A,B,C',
  "La CK-MB :",
  ['Est une isoenzyme de la créatine kinase surtout présente dans le myocarde','Monte en 4 à 6 heures et redevient normale en 2 à 3 jours','Servait historiquement au dépistage des réinfarctus précoces','Apparaît plus précocement que la myoglobine','Est aujourd\'hui le marqueur de choix du SCA, devant la troponine'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> nature (isoenzyme), horloge (4–6 h → 2–3 j) et talent historique (une remontée = réinfarctus) — les trois faits du cours.
<b>Pièges :</b> D inverse l'ordre d'arrivée (myo 2 h d'abord) ; E inverse la hiérarchie actuelle (troponine d'abord, CK-MB supplantée).""",
  """
<b>لماذا:</b> الطبيعة (نظير إنزيم)، الساعة (4–6 سا ← 2–3 أيام)، والموهبة التاريخية (صعود جديد = تكرر) — حقائق الدرس الثلاث.
<b>الفخاخ:</b> D تقلب ترتيب الوصول (الميوغلوبين ساعتان أولاً)؛ وE تقلب الهرمية الحالية (التروبونين أولاً وCK-MB مُزاحة)."""),
 ('Section 9 · Qui reste ?', 'D',
  "Huit jours après une douleur thoracique passée inaperçue, le marqueur encore susceptible d'être élevé et d'étayer un diagnostic rétrospectif d'infarctus est :",
  ['La myoglobine','La CK-MB','L\'ASAT','La troponine T','Le BNP'],
  'Réponse juste : D',
  """
<b>Pourquoi :</b> seule la troponine a une longue traîne : TnT jusqu'à 10 jours (TnI 3–6 j) — c'est la phrase d'annale du diagnostic rétrospectif.
<b>Pièges :</b> myoglobine (24 h) et CK-MB (2–3 j) sont redescendues ; l'ASAT est déclassée ; le BNP est un marqueur de fonction, pas de nécrose datée.""",
  """
<b>لماذا:</b> التروبونين وحدها لها ذيل طويل: TnT حتى 10 أيام (TnI ‏3–6 أيام) — إنها جملة الامتحان عن التشخيص الرجعي.
<b>الفخاخ:</b> الميوغلوبين (24 سا) وCK-MB (2–3 أيام) نزلت؛ ASAT مسقَطة؛ وBNP واسم وظيفة لا نخر مؤرَّخ."""),
 ('Section 10 · Naissance des NP ★★', 'A,B,C',
  "Concernant la naissance des peptides natriurétiques :",
  ['Ils sont sécrétés principalement par les ventricules en réponse à une augmentation de volume ou de pression','Le pro-BNP est clivé en BNP et en NT-proBNP','Le BNP induit vasodilatation et natriurèse','Ils sont sécrétés lorsque le volume intracardiaque diminue','Ils activent le système rénine-angiotensine-aldostérone'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> surcharge (volume/pression) → distension ventriculaire → clivage du pro-BNP → BNP qui décharge le cœur (vasodilatation, filtration, natriurèse) — la diapositive de physiologie, complète.
<b>Pièges :</b> D inverse le stimulus ; E inverse l'effet (le BNP inhibe le SRAA).""",
  """
<b>لماذا:</b> فرط حمولة (حجم/ضغط) ← تمدّد بطيني ← شطر pro-BNP ← BNP يفرّغ القلب (توسّع وعائي، ترشيح، إطراح صوديوم) — شريحة الفيزيولوجيا كاملة.
<b>الفخاخ:</b> D تقلب المنبّه؛ وE تقلب الأثر (BNP يثبّط SRAA)."""),
 ('Section 10 · NT-proBNP ★★', 'A,B,C',
  "Le NT-proBNP se distingue du BNP car :",
  ['C\'est un fragment inactif','Il est plus stable et de demi-vie plus longue','Il est éliminé principalement par le rein','C\'est lui l\'hormone vasodilatatrice active','Il est sécrété par les oreillettes uniquement'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> inactif + stable + demi-vie longue + élimination rénale : le portrait qui en fait le témoin pratique du BNP.
<b>Pièges :</b> D intervertit les deux fragments (l'actif est le BNP) ; E remplace les ventricules par les oreillettes.""",
  """
<b>لماذا:</b> غير فعّال + ثابت + نصف عمر أطول + إطراح كلوي: الصورة التي تجعله الشاهد العملي لـBNP.
<b>الفخاخ:</b> D تُبدّل القطعتين (الفعّال هو BNP)؛ وE تستبدل البطينات بالأذينات."""),
 ('Section 11 · Clinique NP ★★', 'A,B,C,D',
  "En pratique clinique, BNP et NT-proBNP servent à :",
  ['Aider au diagnostic de l\'insuffisance cardiaque, en complément de l\'échographie','Différentier une dyspnée cardiaque (valeurs très élevées) d\'une dyspnée pulmonaire (valeurs normales)','Évaluer le pronostic de l\'insuffisance cardiaque','Suivre la réponse au traitement : une baisse suggère une amélioration de la fonction cardiaque','Remplacer complètement l\'échographie cardiaque'],
  'Réponses justes : A, B, C, D',
  """
<b>Pourquoi :</b> les quatre métiers du cours dans l'ordre : diagnostic (avec ETT), orientation de dyspnée, pronostic, suivi thérapeutique.
<b>Piège :</b> E contredit la diapositive même (« en complément de l'ETT ») et la conclusion de la leçon (les marqueurs complètent, ne remplacent pas).""",
  """
<b>لماذا:</b> وظائف الدرس الأربع بالترتيب: التشخيص (مع ETT)، توجيه ضيق النفس، التكهن، المتابعة العلاجية.
<b>الفخ:</b> E تناقض الشريحة نفسها («مكمّلاً لـETT») وخاتمة الدرس (الواسمات تُكمل ولا تعوّض)."""),
 ('Section 11 · Variations NT-proBNP', 'A,B,C',
  "Concernant les variations physiologiques du NT-proBNP :",
  ['Il augmente avec l\'âge','Il est plus élevé chez la femme que chez l\'homme','Il est plus bas en cas d\'obésité','Il augmente en cas d\'obésité','Un effort intense ne le modifie jamais'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> âge ↑, femme ↑, obésité ↓ : le trio de variations du cours — sans oublier la montée transitoire post-effort.
<b>Pièges :</b> D retourne l'obésité (le piège clinique réel : une valeur « normale » chez l'obèse n'exclut pas l'IC) ; E nie l'effet transitoire de l'effort.""",
  """
<b>لماذا:</b> العمر ↑، المرأة ↑، السمنة ↓: ثلاثي تغيّرات الدرس — دون نسيان الصعود العابر بعد الجهد.
<b>الفخاخ:</b> D تقلب السمنة (الفخ السريري الحقيقي: قيمة «طبيعية» عند البدين لا تستبعد قصور القلب)؛ وE تنفي أثر الجهد العابر."""),
 ('Section 11 · Autres causes', 'A,B',
  "Parmi les situations suivantes, lesquelles élèvent aussi le NT-proBNP (selon le cours) ?",
  ['La fibrillation atriale','L\'insuffisance rénale','Uniquement l\'insuffisance cardiaque aiguë','L\'hypothyroïdie de façon caractéristique','Jamais l\'anémie'],
  'Réponses justes : A, B',
  """
<b>Pourquoi :</b> FA et insuffisance rénale figurent dans la longue liste des « autres causes d'augmentation » du cours (avec hypertrophie ventriculaire, HTA/HTAP, anémie, hyperthyroïdie…).
<b>Pièges :</b> C est l'exclusivité ; D inverse la thyroïde (c'est l'hyperthyroïdie) ; E nie l'anémie, pourtant listée.""",
  """
<b>لماذا:</b> الرجفان الأذيني والقصور الكلوي في قائمة الدرس الطويلة لـ«أسباب الارتفاع الأخرى» (مع التضخّم البطيني وفرط الضغط وفقر الدم وفرط الدرقية…).
<b>الفخاخ:</b> C حصرية؛ وD تقلب الدرقية (المقصود فرط الدرقية)؛ وE تنفي فقر الدم المُدرج."""),
 ('Section 12 · Risque', 'A,B,C',
  "Concernant les marqueurs d'inflammation et de risque cardiovasculaire :",
  ['La hs-CRP prédit le risque d\'événements cardiovasculaires','Une hs-CRP supérieure à 3 mg/L indique un risque élevé','Le fibrinogène élevé reflète une inflammation vasculaire et favorise la thrombose','La hs-CRP est le marqueur de référence du diagnostic d\'infarctus','Une hs-CRP inférieure à 1 mg/L indique un risque élevé'],
  'Réponses justes : A, B, C',
  """
<b>Pourquoi :</b> prédire (hs-CRP, échelle &lt;1 / 1–3 / &gt;3) et préparer le thrombus (fibrinogène) : la troisième famille entière.
<b>Pièges :</b> D donne à la hs-CRP le métier de la troponine ; E retourne l'échelle de risque.""",
  """
<b>لماذا:</b> التنبؤ (hs-CRP، السلم <1 / 1–3 / >3) وتحضير الخثرة (الفيبرينوجين): العائلة الثالثة كاملة.
<b>الفخاخ:</b> D تمنح hs-CRP مهنة التروبونين؛ وE تقلب سلم الخطر."""),
]
for i, (theme, ans, en, props, ansfr, exp_fr, exp_ar) in enumerate(EQ, 1):
    L = 'ABCDE'
    opts = '\n'.join(f'''                        <label class="qopt"><input type="checkbox" value="{L[j]}"><span class="qletter">{L[j]}</span><span>{p}</span></label>'''
                     for j, p in enumerate(props))
    AR[f'entr-exp-{i}'] = exp_ar
    entr += f'''
                <div class="qblock reveal" data-answer="{ans}">
                    <div class="qhead">
                        <span class="qnum">Q{i}</span>
                        <span class="qsource">{theme}</span>
                    </div>
                    <p class="qtext">{en}</p>
                    <div class="qoptions">
{opts}
                    </div>
                    <button class="qcheck btn btn-primary btn-sm"><i class="fa-solid fa-check"></i> Vérifier</button>
                    <div class="qexp" data-tr="entr-exp-{i}" hidden>
                        <p class="qexp-ans"><i class="fa-solid fa-bullseye"></i> {ansfr}</p>
                        {exp_fr}
                    </div>
                </div>
'''
entr += '''
                <div class="score-box" id="entrScore"></div>
            </section>'''
OUT.append(entr)

# ═══════════════ FICHE FLASH + RÉSUMÉ TOTAL + FLASHCARDS ═══════════════
fiche = '''            <!-- ═══════════════ FICHE FLASH ═══════════════ -->
            <section class="lsection" id="fiche">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-bolt"></i></div>
                    <div>
                        <h2>Fiche flash — la leçon en un coup d'œil</h2>
                        <div class="lsub">Six planches <b>sans texte suivi</b>, que des formes, des flèches et des repères chiffrés. Si chacune se lit en moins de cinq secondes, le schéma de la leçon est en place.</div>
                    </div>
                </div>

                <div class="flash-grid">
''' + ''.join(f'''                    <figure class="flash-cell reveal"{' data-delay="1"' if k % 2 else ''}>
                        <img src="{IMG}/{im}" alt="{alt}" loading="lazy" {D2}>
                        <figcaption>{cap}</figcaption>
                    </figure>
''' for k, (im, alt, cap) in enumerate([
    ('ff-troponine.webp',
     "Aide-mémoire visuel du complexe troponine sans texte suivi : filament d'actine et tropomyosine avec les trois sous-unités, une libérant des billes vertes de calcium, une posant un verrou qui bloque les têtes de myosine, une ancrée sur la corde de tropomyosine, contre un symbole de muscle squelettique barré",
     '<b>1 · Le trio troponine</b> — calcium / verrou / ancre, et le muscle squelettique barré pour I et T'),
    ('ff-cinetique.webp',
     "Graphique flash des cinétiques sans texte suivi : trois courbes colorées avec horloges, pic éclair orange retombant en vingt-quatre heures, pic bleu retombant en deux à trois jours, long plateau rouge qui court jusqu'à dix jours",
     '<b>2 · Les trois courbes</b> — 24 h, 2–3 jours, 10 jours : une forme par marqueur'),
    ('ff-algo.webp',
     "Organigramme flash du SCA sans texte suivi : tracé ECG avec segment ST surélevé menant à une flèche verte directe vers un cœur jugé, tracé plat menant à deux tubes de sang horodatés zéro et trois heures avec double coche verte ou boussole d'attente",
     '<b>3 · L\'algorithme en deux routes</b> — ST↑ on fonce · sinon deux tubes décident'),
    ('ff-causes.webp',
     "Collage flash des causes de troponine élevée sans infarctus et sans texte suivi : poumon avec caillot, patient septique perfusé, rein avec machine de dialyse, coureur épuisé, cœur enflammé, réunis par une balance d'interprétation",
     '<b>4 · Élevée ≠ coupable</b> — cinq visages d\'une troponine haute sans coronaire'),
    ('ff-bnp.webp',
     "Schéma flash du pro-BNP sans texte suivi : ventricule distendu expulsant une chaîne qui se scinde en un fragment vert actif dilatant un vaisseau et vidant un rein, et un fragment gris stable coché vers un tube de laboratoire",
     '<b>5 · Un précurseur, deux destins</b> — le vert agit, le gris témoigne'),
    ('ff-seuils.webp',
     "Aide-mémoire flash des seuils : échelle colorée de risque hs-CRP en trois segments vert jaune rouge un et trois milligrammes par litre, et ligne de temps avec trois horloges une à deux heures, trois à six heures, dix jours",
     '<b>6 · Les seuils & les heures</b> — 1 / 3 mg·L⁻¹ et 1–2 h / 3–6 h / 10 j'),
])) + '''                </div>

''' + lbox('ff-box1', 'fa-camera', 'La troponine en 20 secondes (à dire à voix haute)',
    [
        '« Marqueur de <b>référence</b> du SCA : <b>TnI et TnT</b> cardiospécifiques, TnC non. <b>Hypersensible 1–2 h</b>, classique 3–6 h ; <b>TnI 3–6 j, TnT 10 j</b> → diagnostic rétrospectif. Élevée <b>≠</b> infarctus (myocardite, IC, EP, sepsis, rein, effort) : on interprète avec <b>anamnèse + clinique + ECG</b>. <b>STEMI</b> : reperfusion sans l\'attendre. <b>NSTEMI</b> : H0 → H1–H3 (hs) ou H6–H9 ; deux normales = exclu. Suivi d\'IC et dyspnée : <b>BNP / NT-proBNP</b>, pas elle. »',
    ],
    arbox('fa-camera', 'التروبونين في 20 ثانية (قلها بصوت عالٍ)', [
        '«الواسم <b>المرجعي</b> للمتلازمة الإكليلية: <b>' + FP % 'TnI وTnT' + '</b> نوعيتان قلبياً، ' + FP % 'TnC' + ' لا. <b>فائق الحساسية 1–2 سا</b>، تقليدي 3–6 سا؛ <b>TnI ‏3–6 أيام وTnT ‏10 أيام</b> ← تشخيص رجعي. ارتفاعها <b>≠</b> احتشاء (التهاب عضل قلب، قصور قلب، انصمام، إنتان، كلية، مجهود): التفسير بـ<b>سوابق + سريرية + تخطيط</b>. في <b>' + FP % 'STEMI' + '</b>: إعادة تروية دون انتظارها. في <b>' + FP % 'NSTEMI' + '</b>: H0 ← H1–H3 (فائق) أو H6–H9؛ قياسان طبيعيان = استبعاد. متابعة قصور القلب وضيق النفس: <b>' + FP % 'BNP/NT-proBNP' + '</b> لا هي.»',
    ])) + '''
            </section>

            <!-- ═══════════════ RÉSUMÉ TOTAL ═══════════════ -->
            <section class="lsection" id="resume-total">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-image"></i></div>
                    <div>
                        <h2>Résumé total — la grande planche</h2>
                        ''' + sub('rt-sub',
                            'Toute la leçon, un seul poster : les trois familles, les cinétiques, l\'algorithme, les pièges. Branche le son : le résumé est raconté en <b>français</b> puis en <b>arabe (ع)</b> dans le dernier chapitre du Ciné.',
                            'الدرس كله في ملصق واحد: العائلات الثلاث، الحركيات، الخوارزمية، الفخاخ. شغّل الصوت: الملخص يُروى بـ<b>الفرنسية</b> ثم بـ<b>العربية (ع)</b> في الفصل الأخير من السينما.') + '''
                    </div>
                </div>

''' + fig('total.webp',
    "Grande planche de synthèse des biomarqueurs cardiaques : trois familles en colonnes nécrose fonction inflammation avec complexe troponine et courbes de cinétique à gauche, clivage du pro-BNP et ses usages au centre, échelle de risque hs-CRP à droite, algorithme STEMI NSTEMI en bas, titres et chiffres français cinq",
    '🖼️ <b>Le poster final</b> — à réexporter dans tes fiches personnelles', dims=D1, cls='total-poster reveal') + '''

''' + spot(8) + '''
            </section>

            <!-- ═══════════════ FLASHCARDS ═══════════════ -->
            <section class="lsection" id="flashcards">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-clone"></i></div>
                    <div>
                        <h2>Flashcards — répétition express</h2>
                        <div class="lsub">25 cartes, un clic pour retourner — une question directe, une réponse sans détour. Barre d'espace pour passer à la suivante ; à jongler dans le bus, au réveil, dans la file (une mémorisation <b>durable</b> vaut mille relectures de la veille).</div>
                    </div>
                </div>

                <div id="flashApp"></div>
            </section>'''
OUT.append(fiche)

KW = [
 ('Biomarqueur cardiaque', "Substance mesurable dans le sang, produite ou libérée par le cœur atteint, pour le diagnostic, le pronostic ou le suivi.", 'واسم قلبي', 'مادة قابلة للقياس في الدم، ينتجها أو يحرّرها القلب المصاب، للتشخيص أو التكهن أو المتابعة.'),
 ('Marqueur idéal', "Sensible, spécifique et précoce — le portrait validé par deux annales.", 'الواسم المثالي', 'حسّاس، نوعي ومبكر — صورة صادق عليها سؤالان.'),
 ('Nécrose myocardique', "Mort des cardiomyocytes (ischémie aiguë) libérant leurs protéines dans le sang.", 'نخر عضل القلب', 'موت خلايا عضل القلب (إقفار حاد) محرّراً بروتيناتها في الدم.'),
 ('Syndrome coronarien aigu (SCA)', "Ischémie aiguë du myocarde, le plus souvent sur athérosclérose ; terrain des marqueurs de nécrose.", 'المتلازمة الإكليلية الحادة', 'إقفار حاد لعضل القلب، غالباً على تصلب؛ أرض واسمات النخر.'),
 ('Infarctus du myocarde (IDM)', "Nécrose ischémique accompagnée de libération de marqueurs mesurables.", 'احتشاء عضل القلب', 'نخر إقفاري مصحوب بتحرّر واسمات قابلة للقياس.'),
 ('Troponine', "Protéine régulatrice de la contraction ; marqueur de référence du SCA, élevée 6–10 j.", 'التروبونين', 'بروتين منظّم للانقباض؛ الواسم المرجعي للمتلازمة الإكليلية، يبقى 6–10 أيام.'),
 ('Troponine C (TnC)', "Lie le calcium, déclenche la contraction ; présente aussi au muscle squelettique → non spécifique.", 'تروبونين C', 'يرتبط بالكالسيوم ويطلق الانقباض؛ حاضر في العضل الهيكلي أيضاً ← غير نوعي.'),
 ('Troponine I (TnI)', "Inhibe l'actine-myosine ; cardiospécifique ; élevée 3–6 jours.", 'تروبونين I', 'يثبّط الأكتين-ميوسين؛ نوعي قلبياً؛ يبقى 3–6 أيام.'),
 ('Troponine T (TnT)', "Fixe le complexe à la tropomyosine ; cardiospécifique ; élevée jusqu'à 10 jours.", 'تروبونين T', 'يثبّت المركّب على التروبوميوسين؛ نوعي قلبياً؛ يبقى حتى 10 أيام.'),
 ('Troponine hypersensible (hs-cTn)', "Dosage détectant des concentrations très faibles : signal dès 1–2 h, excellente VPN.", 'التروبونين فائقة الحساسية', 'قياس يلتقط تراكيز ضئيلة جداً: إشارة من 1–2 ساعة، وقيمة سلبية ممتازة.'),
 ('Cinétique', "L'évolution des taux dans le temps : montée, pic, descente — l'horaire propre à chaque marqueur.", 'الحركية', 'تطوّر المستويات مع الزمن: صعود، ذروة، هبوط — الجدول الخاص بكل واسم.'),
 ('Valeur prédictive négative (VPN)', "Probabilité d'absence de maladie si le test est négatif ; excellente pour la hs-cTn et le NT-proBNP.", 'القيمة التكهنية السالبة', 'احتمال غياب المرض إذا كان الفحص سالباً؛ ممتازة للتروبونين الفائقة وNT-proBNP.'),
 ('STEMI', "SCA avec sus-décalage du segment ST : diagnostic ECG, reperfusion immédiate sans attendre la troponine.", 'احتشاء بصعود ST', 'متلازمة بارتفاع مقطع ST: تشخيص تخطيطي، إعادة تروية فورية دون انتظار التروبونين.'),
 ('NSTEMI', "SCA sans sus-décalage : le diagnostic repose sur l'élévation et la cinétique de la troponine.", 'احتشاء دون صعود ST', 'متلازمة دون ارتفاع ST: التشخيص يعتمد على ارتفاع التروبونين وحركيته.'),
 ('Reperfusion', "Restauration urgente du flux coronaire dans le STEMI — « le temps, c'est du myocarde ».", 'إعادة التروية', 'استعادة طارئة للجريان الإكليلي في STEMI — «الوقت عضل قلب».'),
 ('Algorithme H0/H1–H3', "Protocole hypersensible : dosage à l'admission puis contrôle à 1–3 h (classique : H6–H9).", 'خوارزمية H0/H1–H3', 'بروتوكول فائق الحساسية: قياس عند القبول ثم مراقبة بعد 1–3 ساعات (تقليدي: H6–H9).'),
 ('Myoglobine', "Protéine du muscle strié ; dès 2 h, pic 4–12 h, normale ~24 h ; non spécifique → supplantée.", 'الميوغلوبين', 'بروتين العضل المخطط؛ من ساعتين، ذروة 4–12 سا، طبيعي ~24 سا؛ غير نوعي ← مُزاح.'),
 ('Rhabdomyolyse', "Destruction massive du muscle strié libérant la myoglobine — cause extracardiaque d'élévation.", 'انحلال العضل المخطط', 'تدمير ضخم للعضل المخطط يحرّر الميوغلوبين — سبب خارج قلبي للارتفاع.'),
 ('CK-MB', "Isoenzyme myocardique de la créatine kinase ; 4–6 h → 2–3 j ; voyait les réinfarctus précoces.", 'CK-MB', 'نظير إنزيم الكرياتين كيناز العضل-قلبي؛ 4–6 سا ← 2–3 أيام؛ كان يكشف التكرر المبكر.'),
 ('Réinfarctus (détection)', "Remontée d'un marqueur redescendu vite (CK-MB, myoglobine) signalant un événement nouveau.", 'الاحتشاء المتكرر (كشفه)', 'صعود جديد لواسم نزل سريعاً (CK-MB، ميوغلوبين) يفضح حدثاً جديداً.'),
 ('ASAT / ALAT / LDH', "Anciens marqueurs enzymatiques aujourd'hui déclassés ; présents dans les annales, absents des diapositives.", 'إنزيمات قديمة مسقَطة', 'واسمات إنزيمية قديمة مسقَطة اليوم؛ حاضرة في الأسئلة غائبة عن الشرائح.'),
 ('BNP', "Fragment actif du pro-BNP : vasodilatation, filtration ↑, natriurèse, inhibition du SRAA.", 'BNP', 'القطعة الفعالة من pro-BNP: توسّع وعائي، ترشيح ↑، إطراح صوديوم، تثبيط SRAA.'),
 ('NT-proBNP', "Fragment inactif, stable, demi-vie longue, élimination rénale ; témoin pratique de l'IC.", 'NT-proBNP', 'قطعة غير فعالة ثابتة نصف عمرها طويل وإطراحها كلوي؛ الشاهد العملي لقصور القلب.'),
 ('pro-BNP', "Précurseur clivé en BNP + NT-proBNP lors de la distension ventriculaire.", 'pro-BNP', 'السلف المشطور إلى BNP + NT-proBNP عند تمدّد البطينات.'),
 ('Peptide natriurétique', "Hormone cardiaque favorisant l'excrétion rénale de sodium (et d'eau) pour décharger le ventricule.", 'الببتيد الناتريوري', 'هرمون قلبي يعزّز إفراغ الصوديوم (والماء) كلوياً لتخفيف البطين.'),
 ('Natriurèse', "Excrétion urinaire du sodium, effet majeur du BNP avec la diuresa.", 'الإطراح الناتريوري', 'إطراح الصوديوم بولياً، أثر رئيسي لـBNP مع الإدرار.'),
 ('SRAA', "Système rénine-angiotensine-aldostérone, inhibé par le BNP.", 'جهاز رينين-أنجيوتنسين-ألدوستيرون', 'جهاز الرينين-أنجيوتنسين-ألدوستيرون، يثبّطه BNP.'),
 ('Dyspnée (différentiel)', "Peptides très élevés si cardiaque, normaux si pulmonaire — le geste des urgences.", 'ضيق النفس (التفريقي)', 'ببتيدات مرتفعة جداً إن كان قلبياً، طبيعية إن كان رئوياً — حركة الطوارئ.'),
 ('ETT (échographie)', "Examen d'imagerie que les peptides complètent sans jamais remplacer dans l'IC.", 'تخطيط القلب فوق الصوتي', 'فحص التصوير الذي تُكمله الببتيدات دون أن تعوّضه أبداً في قصور القلب.'),
 ('Insuffisance cardiaque', "Terrain des peptides natriurétiques : diagnostic (avec ETT), pronostic, suivi.", 'قصور القلب', 'أرض الببتيدات: تشخيص (مع ETT)، تكهن، متابعة.'),
 ('hs-CRP', "CRP hypersensible prédisant le risque : <1 faible · 1–3 intermédiaire · >3 mg/L élevé.", 'hs-CRP', 'بروتين C فائق الحساسية متنبئ بالخطر: <1 منخفض · 1–3 متوسط · >3 مغ/ل مرتفع.'),
 ('Fibrinogène', "Protéine de l'inflammation et précurseur de la fibrine : inflammation vasculaire + thrombose.", 'الفيبرينوجين', 'بروتين التهاب وسلف الفيبرين: التهاب وعائي + تخثّر.'),
 ('Cardiospécifique', "Spécifique du tissu myocardique — pas de la maladie « coronarienne » (piège d'annale).", 'نوعي للقلب', 'نوعي لنسيج عضل القلب — لا للداء «الإكليلي» (فخ امتحاني).'),
 ('Diagnostic rétrospectif', "Diagnostiquer un IDM passé grâce à la persistance de la troponine (6–10 j).", 'تشخيص رجعي', 'تشخيص احتشاء ماضٍ بفضل بقاء التروبونين (6–10 أيام).'),
 ('Surcharge (volume/pression)', "Le stimulus de sécrétion des peptides natriurétiques par les ventricules distendus.", 'فرط الحمولة', 'منبّه إفراز الببتيدات من البطينات المتمدّدة.'),
 ('Demi-vie', "Temps de division par deux d'une concentration ; plus longue pour le NT-proBNP que le BNP.", 'نصف العمر', 'الزمن لتقسيم التركيز على اثنين؛ أطول لدى NT-proBNP من BNP.'),
]
KWDATA = {'items': [{'t': t, 'd': d, 'a': {'t': at, 'd': ad}} for t, d, at, ad in KW]}

FC = [
 ('Les trois familles de biomarqueurs cardiaques ?', "Nécrose (troponine, CK-MB, myoglobine) · fonction (BNP, NT-proBNP) · inflammation/risque (hs-CRP, fibrinogène)."),
 ('Le marqueur idéal en trois adjectifs ?', "Sensible, spécifique, précoce."),
 ('TnC, TnI, TnT : les trois métiers ?', "C lie le calcium · I inhibe l'actine-myosine · T fixe la tropomyosine."),
 ('Quelles troponines dose-t-on, et pourquoi pas TnC ?', "TnI et TnT, cardiospécifiques ; TnC existe aussi dans le muscle squelettique."),
 ('Classique vs hypersensible : les heures ?', "Classique détectable en 3–6 h ; hypersensible en 1–2 h."),
 ('TnI ou TnT : qui dure le plus longtemps ?', "TnT, jusqu'à 10 jours (TnI : 3–6 jours)."),
 ("Quatre causes de troponine ↑ hors infarctus ?", "Myocardite, insuffisance cardiaque, embolie pulmonaire, sepsis (aussi IR, AVC, effort, CO…)."),
 ('La troponine varie avec quoi, au repos ?', "L'âge (plus élevée après 60 ans) et le sexe (homme > femme)."),
 ("L'interprétation d'une troponine associe quoi ?", "Anamnèse + clinique + ECG — jamais le chiffre seul."),
 ('STEMI : on attend la troponine ?', "Jamais : diagnostic ECG, reperfusion immédiate."),
 ('NSTEMI : qui fait le diagnostic ?', "L'élévation et la cinétique de la troponine."),
 ("L'algorithme classique, les heures ?", "H0 puis contrôle à H6–H9."),
 ("L'algorithme hypersensible, les heures ?", "H0 puis contrôle à H1–H3 (annale : admission et 2 h)."),
 ("La règle d'exclusion de l'IDM ?", "Troponine normale à H0 ET au contrôle = IDM exclu avec fiabilité."),
 ('Myoglobine : le trio temps ?', "Dès 2 h · pic 4–12 h · normale en ~24 h."),
 ('Pourquoi la myoglobine est-elle déclassée ?', "Présente dans tout le muscle strié → sensible et précoce, mais non cardiospécifique."),
 ('CK-MB : apparition et retour ?', "4–6 h → normale en 2–3 jours."),
 ('Le talent historique de la CK-MB (et de la myoglobine) ?', "Redescendre vite : une remontée signale réinfarctus/récidive précoce."),
 ('Qui permet le diagnostic rétrospectif, pourquoi ?', "La troponine : elle reste élevée 6–10 jours après l'événement."),
 ('Le produit du clivage du pro-BNP ?', "1 BNP (actif) + 1 NT-proBNP (inactif)."),
 ('Trois effets du BNP ?', "Vasodilatation, diurèse/natriurèse, inhibition du SRAA (et du sympathique)."),
 ('BNP ou NT-proBNP : qui est stable et rénal ?', "Le NT-proBNP : inactif, stable, demi-vie longue, éliminé par le rein."),
 ('Dyspnée aux urgences : le peptide tranche comment ?', "Très élevé = cardiaque ; normal = plutôt pulmonaire."),
 ('Trois pièges du NT-proBNP ?', "Âge ↑, femme ↑, insuffisance rénale ↑… et obésité ↓ (valeurs faussement rassurantes)."),
 ("L'échelle hs-CRP ?", "< 1 risque faible · 1–3 intermédiaire · > 3 mg/L risque élevé ; elle prédit, ne diagnostique pas."),
]
FCDATA = [{'q': q, 'a': a} for q, a in FC]

AUD = '../assets/audio/bi-06'
CINE = {'chapters': [
    {'title': 'Chapitre 1 — Le cadre : trois familles, trois questions', 'audio': f'{AUD}/ch1.mp3',
     'images': [f'{IMG}/hero.webp', f'{IMG}/enjeux.webp', f'{IMG}/necrose.webp']},
    {'title': 'Chapitre 2 — La troponine : classique et hypersensible', 'audio': f'{AUD}/ch2.mp3',
     'images': [f'{IMG}/troponine.webp', f'{IMG}/hs.webp']},
    {'title': 'Chapitre 3 — Troponine élevée, pas forcément coupable', 'audio': f'{AUD}/ch3.mp3',
     'images': [f'{IMG}/interpretation.webp']},
    {'title': "Chapitre 4 — L'algorithme des urgences", 'audio': f'{AUD}/ch4.mp3',
     'images': [f'{IMG}/sca.webp']},
    {'title': 'Chapitre 5 — Les deux anciens : myoglobine et CK-MB', 'audio': f'{AUD}/ch5.mp3',
     'images': [f'{IMG}/myoglobine.webp', f'{IMG}/ckmb.webp']},
    {'title': 'Chapitre 6 — La courbe qui résume tout', 'audio': f'{AUD}/ch6.mp3',
     'images': [f'{IMG}/cinetique.webp', f'{IMG}/reel/cinetique.webp']},
    {'title': 'Chapitre 7 — BNP et NT-proBNP, la voix du ventricule', 'audio': f'{AUD}/ch7.mp3',
     'images': [f'{IMG}/peptides.webp']},
    {'title': 'Chapitre 8 — En clinique, et le risque qui couve', 'audio': f'{AUD}/ch8.mp3',
     'images': [f'{IMG}/np-clinique.webp', f'{IMG}/inflammation.webp']},
    {'title': 'Résumé total', 'audio': f'{AUD}/resume.mp3', 'audioAr': f'{AUD}/resume-ar.mp3',
     'images': [f'{IMG}/total.webp', f'{IMG}/mindmap.webp']},
]}

# ═══════════════ ASSEMBLAGE (squelette gold + peau Biochimie) ═══════════════
bottom = SRC.split('</main>')[1]
_old_scripts = '''    <script src="../js/lib/three.min.js"></script>
    <script src="../js/orbital-sphere-bg.js?v=6"></script>
'''
assert _old_scripts in bottom, 'bloc scripts orbital introuvable'
bottom = bottom.replace(_old_scripts, '    <script src="../js/bio-field.js?v=11"></script>\n', 1)
_old_link = '<a href="ra-03-tdm-thoracique.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-right"></i> Autre leçon : La TDM thoracique</a>'
assert _old_link in bottom, 'lien autre leçon gold introuvable'
bottom = bottom.replace(_old_link, '<a href="bi-07-gazometrie.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-right"></i> Autre leçon : La gazométrie</a>', 1)
_old_copy = 'SEENmed — Leçon « Les ultrasons — échographie thoracique » · Radiologie · Dr Z. Belmessabih — Dr G. Abebsi, EHU Oran'
assert _old_copy in bottom, 'ligne copyright gold introuvable'
bottom = bottom.replace(_old_copy, 'SEENmed — Leçon « Les biomarqueurs cardiaques » · Biochimie · Dr Besbes, A', 1)
assert bottom.count('<footer class="footer">') == 1
assert 'a-propos' not in bottom and 'contact.html' not in bottom
assert 'orbital' not in bottom and 'three.min' not in bottom
assert bottom.count('id="backToTop"') == 1 and bottom.count('id="scrollProgress"') == 1, 'fin de page gold'

assert not [k for k in AR if '<bdi class="fr-term">' in AR[k] and '<b>' in AR[k].split('<bdi class="fr-term">')[1].split('</bdi>')[0]]

jd = lambda x: json.dumps(x, ensure_ascii=False, indent=1)
main_close = f'''
            <script type="application/json" id="cineData">{jd(CINE)}</script>
            <script type="application/json" id="kwData">{jd(KWDATA)}</script>
'''
fc_block = f'''    <script type="application/json" id="fcData">{jd(FCDATA)}</script>
    <script type="application/json" id="arData">{jd(AR)}</script>
'''
main_close += '''
        </div>
    </main>
'''
html = top + '\n' + nav + main_open + '\n\n'.join(OUT) + main_close + bottom
html = html.replace('</body>', fc_block + '</body>', 1)

for bid in ('cineData', 'kwData', 'fcData', 'arData'):
    m = re.search(rf'<script type="application/json" id="{bid}">(.*?)</script>', html, re.S)
    json.loads(m.group(1)); print(f'JSON {bid} OK')
ark = set(json.loads(re.search(r'id="arData">(.*?)</script>', html, re.S).group(1)))
trk = set(re.findall(r'data-tr="([^"]+)"', html))
print('arData', len(ark), '| data-tr', len(trk), '| orphans', sorted(trk - ark), '| unused', sorted(ark - trk))
assert ark == trk
print('qblocks', html.count('class="qblock'), '| qcheck', html.count('class="qcheck'), '| spots', html.count('cine-spot'))
assert html.count('class="qcheck') == 30
assert '.png' not in html and 'object-position' not in html
assert html.count('has-bio-field') == 1 and html.count('bio-field.js') == 1 and html.count('id="backToTop"') == 1

missing = [m for m in set(re.findall(r'src="(\.\./assets/img/bi-06/[^"]+)"', html) + [im for c in CINE['chapters'] for im in c['images']])
           if not os.path.exists(os.path.join(MS, 'lecons', m))]
print('IMAGES MANQUANTES (attendu 11, lot 2 au prochain GO):')
for m in sorted(missing): print('  ', m)

out_path = os.path.join(MS, 'lecons/bi-06-biomarqueurs-cardiaques.html')
open(out_path, 'w', encoding='utf-8').write(html)
print('ÉCRIT', out_path, round(len(html) / 1024), 'Ko')

dp = os.path.join(MS, 'js/data.js')
data = open(dp, encoding='utf-8').read()
line = "{ id: 'bi-06', nom: 'Les biomarqueurs cardiaques', qcm: 10, recu: false },"
already = "url: 'lecons/bi-06-biomarqueurs-cardiaques.html'"
if already in data:
    print('data.js bi-06 déjà patché — skip'); line = None
else:
    assert data.count(line) == 1, 'ligne bi-06 data.js introuvable'
new = ("{ id: 'bi-06', nom: 'Les biomarqueurs cardiaques', qcm: 10, entr: 20, recu: true,\n"
       "                  url: 'lecons/bi-06-biomarqueurs-cardiaques.html' },")
open(dp, 'w', encoding='utf-8').write(data.replace(line, new) if line else data)
print('data.js bi-06 OK ->', new)
