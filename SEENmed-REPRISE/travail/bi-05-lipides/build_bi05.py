#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder bi-05 — clone le squelette gold ra-02, injecte le contenu lipides (source Dr Besbes. A, N-1)."""
import re, json, os

MS = '/tmp/seenmed-clean/medstudy'
SRC = open(os.path.join(MS, 'lecons/ra-02-ultrasons-echographie-thoracique.html'), encoding='utf-8').read()
AR = {}          # clés data-tr -> HTML arabe
OUT = []         # sections HTML
IMG = '../assets/img/bi-05'
D1 = 'width="1672" height="941"'     # lots 1-2
D2 = 'width="1536" height="1024"'    # lot 3

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

FT = '<bdi class="fr-term">%s</bdi>'   # terme FR gardé dans la phrase arabe
FP = '<bdi class="fr-plain">%s</bdi>'  # chiffre / sigle

# ═══════════════ SQUELETTE (cloné de ra-02) ═══════════════
top = SRC.split('<!-- ============ NAVIGATION DE LEÇON')[0]
top = top.replace('<title>Les ultrasons — échographie thoracique — SEENmed</title>',
                  '<title>Exploration du métabolisme des lipides et lipoprotéines — SEENmed</title>')
top = top.replace('data-lesson-id="ra-02"', 'data-lesson-id="bi-05"')
top = top.replace('has-orbital-sphere', 'has-bio-field')  # peau du module Biochimie
top = top.replace('>Radiologie</a>', '>Biochimie</a>').replace('<span>Leçon 2</span>', '<span>Leçon 5</span>')
top = re.sub(r'<h1>.*?</h1>', '<h1>Exploration du métabolisme des <span class="highlight">lipides et lipoprotéines</span></h1>', top, flags=re.S)
top = re.sub(r'(<div class="lesson-meta">).*?(</div>\s*<div class="lesson-actions">)',
             r'''\1
                <span class="chip chip-mod"><i class="fa-solid fa-flask"></i> Biochimie</span>
                <span class="chip chip-qcm"><i class="fa-solid fa-bullseye"></i> 15 QCM d'annales + 20 d'entraînement</span>
                <span class="chip chip-star"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i> Importance EMD</span>
                <span class="chip"><i class="fa-solid fa-user-doctor"></i> Dr Besbes. A — Biochimie, 2025/2026</span>
                <span class="chip chip-done"><i class="fa-solid fa-check"></i> Cours reçu</span>
            \2''', top, flags=re.S)
top = re.sub(r'(<div class="lesson-actions">).*?(</div>\s*</div>\s*<div class="lesson-hero-visual">)',
             r'''\1
                <a href="#vue" class="btn btn-primary btn-glow"><i class="fa-solid fa-play"></i> Commencer le résumé</a>
                <a href="#annales" class="btn btn-outline"><i class="fa-solid fa-award"></i> Les 15 annales</a>
                <a href="#entrainement" class="btn btn-outline"><i class="fa-solid fa-bullseye"></i> Les 20 QCM</a>
                <button class="btn btn-outline" id="markDoneBtn"><i class="fa-solid fa-graduation-cap"></i> Marquer comme maîtrisée</button>
            \2''', top, flags=re.S)
top = re.sub(r'(<div class="lesson-hero-visual">)\s*<img[^>]*>',
             r'\1\n                <img src="../assets/img/bi-05/hero.webp" alt="Illustration : au laboratoire de biochimie, une technicienne examine à contre-jour un tube de sérum lactescent à côté de tubes clairs, pendant qu\'un analyseur affiche un bilan lipidique — cholestérol total, triglycérides, HDL et LDL" loading="eager" width="1672" height="941">', top)

TABS = [
    ('vue', 'fa-compass', "Vue d'ensemble", True),
    ('mindmap', 'fa-sitemap', 'Mind Map', False),
    ('cine', 'fa-clapperboard', 'Ciné', False),
    ('enjeux', 'fa-heart-pulse', '1. Les enjeux', False),
    ('absorption', 'fa-utensils', '2. Absorption', False),
    ('transport', 'fa-truck-fast', '3. Le transport', False),
    ('familles', 'fa-people-group', '4. Les 5 familles', False),
    ('chiffres', 'fa-scale-balanced', '5. Taille, densité, apo', False),
    ('destinee', 'fa-warehouse', '6. Destinée des lipides', False),
    ('regulation', 'fa-sliders', '7. Régulation', False),
    ('depistage', 'fa-magnifying-glass', '8. Qui dépister ?', False),
    ('bilan1', 'fa-vial', '9. Bilan de 1ʳᵉ intention', False),
    ('valeurs', 'fa-gauge-high', '10. Valeurs &amp; cibles', False),
    ('bilan2', 'fa-dna', '11. Bilan de 2ᵉ intention', False),
    ('fredrickson', 'fa-table-cells-large', '12. Fredrickson I–V', False),
    ('secondaires', 'fa-magnifying-glass-chart', '13. Causes secondaires', False),
    ('cas', 'fa-user-doctor', '14. Deux cas', False),
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
                            'Un cours en <b>trois étages</b> : la <b>physiologie</b> (cinq familles de lipoprotéines qui transportent les lipides), le <b>bilan</b> (EAL de 1ʳᵉ puis 2ᵉ intention, aspect du sérum, quatre chiffres-seuils) et la <b>classification</b> (Fredrickson I–V, causes secondaires à éliminer). Sur 15 annales, <b>Fredrickson et les seuils dominent</b>.',
                            'الدرس على ثلاث طبقات: <b>الفيزيولوجيا</b> (خمس عائلات من ' + FT % 'lipoprotéines' + ' تنقل الدهون)، ثم <b>التحليل</b> (استكشاف الشذوذ الدهني قصداً أول ثم ثانياً، مظهر المصل، وأربعة أرقام-عتبات)، ثم <b>التصنيف</b> (' + FT % 'Fredrickson' + ' من I إلى V، والأسباب الثانوية الواجب استبعادها). من بين 15 سؤال امتحانات، <b>يهيمن Fredrickson والعتبات</b>.') + '''
                    </div>
                </div>

                <div class="overview-grid">
                    <div class="essence reveal">
                        <h3><i class="fa-solid fa-bolt"></i> L'essentiel</h3>
                        <ul>
                            <li><b>Les lipides ne voyagent jamais seuls</b> : hydrophobes, ils circulent dans des <b>lipoprotéines</b> — cœur de triglycérides + esters de cholestérol, coque de phospholipides + <b>apolipoprotéines</b>.</li>
                            <li><b>5 familles</b> : <b>chylomicrons</b> (TG alimentaires, ApoB48) · <b>VLDL</b> (TG du foie, ApoB100) · <b>IDL</b> (restes de VLDL) · <b>LDL</b> (cholestérol → tissus, athérogène) · <b>HDL</b> (retour → foie, protecteur, ApoA).</li>
                            <li><b>Plus la particule est grosse, moins elle est dense</b> : chylomicrons 100 nm–1 µm / 99 % de lipides → HDL 10 nm / 50–70 %.</li>
                            <li><b>EAL de 1ʳᵉ intention</b> : aspect du sérum, <b>CT, TG, HDL, LDL, non-HDL</b>. Sérum <b>lactescent → test de crémage</b> (12 h à +4 °C).</li>
                            <li><b>Les 4 chiffres</b> : CT &lt; <b>2 g/L</b> · TG <b>0,5–1,5 g/L</b> · HDL <b>H 0,4 / F 0,5 g/L</b> · LDL &lt; <b>1,6 g/L</b> — et <b>&lt; 0,70 g/L si haut risque</b>.</li>
                            <li><b>2ᵉ intention</b> : électrophorèse (lipidogramme), <b>ApoB</b> (compte les particules athérogènes), <b>ApoA1</b>, <b>Lp(a)</b> génétique, tests génétiques si forme familiale.</li>
                            <li><b>Fredrickson</b> : I = chylomicrons · IIa = LDL pure · IIb = mixte (40 %) · III = IDL · IV = VLDL (45 %) · V = chylomicrons + VLDL.</li>
                            <li><b>Secondaire d'abord</b> : diabète, hypothyroïdie, syndrome néphrotique, cholestase, médicaments… — <b>jamais l'hypoparathyroïdie</b> (piège d'annale).</li>
                            <li><b>Dépistage</b> : homme ≥ 40 ans, femme ≥ 50 ans, plus tôt si facteurs de risque ; enfant si antécédents familiaux.</li>
                            <li>Le <b>LDL</b> est le <b>paramètre du suivi thérapeutique</b> ; un <b>HDL &lt; 0,40 g/L</b> est un facteur de risque cardiovasculaire.</li>
                        </ul>
                    </div>
                    <div class="roadmap reveal" data-delay="1">
                        <h3><i class="fa-solid fa-route"></i> Où on va — la feuille de route</h3>
                        <ol>
                            <li><b>Les enjeux</b> — rôles des lipides et risque cardiovasculaire</li>
                            <li><b>Absorption</b> — de l'assiette au chylomicron</li>
                            <li><b>Le transport</b> — les trois voies en une image</li>
                            <li><b>Les 5 familles</b> — qui fait quoi</li>
                            <li><b>Taille, densité, apo</b> — le tableau qui tombe ★★</li>
                            <li><b>Destinée</b> — stockage, β-oxydation, synthèses</li>
                            <li><b>Régulation</b> — enzymes, transferts, récepteurs</li>
                            <li><b>Qui dépister ?</b> — les indications de l'EAL</li>
                            <li><b>Bilan de 1ʳᵉ intention</b> — aspect du sérum et crémage ★★</li>
                            <li><b>Valeurs &amp; cibles</b> — les quatre chiffres ★★</li>
                            <li><b>Bilan de 2ᵉ intention</b> — ApoB, Lp(a), Friedewald ★★</li>
                            <li><b>Fredrickson I–V</b> — la classification ★★</li>
                            <li><b>Causes secondaires</b> — avant de dire « primitive » ★★</li>
                            <li><b>Deux cas</b> — les deux dossiers du cours, corrigés</li>
                            <li><b>La méthode de l'examinateur</b> — puis <b>15 annales</b> et <b>20 QCM</b></li>
                        </ol>
                    </div>
                </div>

''' + lbox('vue-box1', 'fa-circle-info', 'Transparence : la source de cette leçon et ses QCM',
    [
        'Cette leçon est construite sur le cours du <b>Dr Besbes. A (2025/2026, 32 diapositives)</b>, lu en entier — tableaux chiffrés et cas cliniques compris. <b>Si une version plus récente du cours arrive, seuls les écarts seront corrigés</b> : la leçon est versionnée pour cela.',
        'Les <b>15 QCM d\'annales</b> de la section « QCM annales » sont <b>authentiques</b> : recueil ELITE CARDIO 3ᵉ année, Biochimie §3 (PROMO 2018 → 2022 + rattrapage 2022), <b>texte et corrigés officiels</b>, repris sans retouche.',
        'Trois notions sont <b>testées en annales mais absentes des diapositives</b> — limites de la formule de <b>Friedewald</b> si TG élevés, <b>confirmation à 2–4 semaines</b>, faible mobilité électrophorétique des chylomicrons : elles sont enseignées <b>au niveau exact où les annales les testent</b>, et signalées comme « à confirmer sur le cours ».',
    ],
    arbox('fa-circle-info', 'شفافية: مصدر هذا الدرس وأسئلته', [
        'هذا الدرس مبنيّ على محاضرة <b>الدكتورة بسبس (2025/2026، 32 شريحة)</b> وقد قُرئت كاملة — بما فيها الجداول الرقمية والحالتان السريريتان. <b>إذا وصلت نسخة أحدث من المحاضرة فلن تُصحَّح إلا الفروقات</b>: الدرس مُرقَّم الإصدار لهذا الغرض.',
        '<b>الأسئلة الخمسة عشر</b> في قسم الامتحانات <b>أصلية</b>: من مجموعة ' + FP % 'ELITE CARDIO' + ' للسنة الثالثة، كيمياء حيوية §3 (دفعات 2018 ← 2022 + استدراك 2022)، <b>بالنص والتصحيح الرسمي</b> دون أي تعديل.',
        'ثلاثة مفاهيم <b>سقطت في الامتحانات لكنها غائبة عن الشرائح</b> — حدود صيغة ' + FT % 'Friedewald' + ' عند ارتفاع ' + FP % 'TG' + '، و<b>التأكيد بعد 2–4 أسابيع</b>، وضعف حركة الـ' + FP % 'chylomicrons' + ' في الرحلان: تُدرَّس <b>بالمستوى نفسه الذي تُختبر به</b> مع التنبيه أنها «للتأكيد من المحاضرة».',
    ])) + '''
            </section>'''
OUT.append(vue)

# ═══════════════ MIND MAP + CINÉ ═══════════════
OUT.append('''            <!-- ═══════════════ MIND MAP ═══════════════ -->
            <section class="lsection" id="mindmap">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-sitemap"></i></div>
                    <div>
                        <h2>Mind Map — la leçon vue du ciel</h2>
                        <div class="lsub">Un <b>fleuve métabolique</b> : l'intestin et le foie déversent leurs particules dans le sang, les tissus les déchargent, les HDL ramènent le cholestérol au foie — et au bord du fleuve, le laboratoire lit le bilan. Clique pour agrandir.</div>
                    </div>
                </div>

''' + fig('mindmap.webp',
    "Mind map en fleuve métabolique : l'intestin déverse les chylomicrons, le foie déverse les VLDL devenant IDL puis LDL vers les tissus, les HDL remontent le courant avec le cholestérol vers le foie ; sur la berge, le bilan lipidique avec aspect du sérum, cholestérol total, triglycérides, HDL, LDL, puis la classification de Fredrickson et les causes secondaires",
    '🗺️ <b>La carte mentale :</b> intestin → chylomicrons · foie → VLDL → LDL → tissus · HDL → retour au foie · et le bilan qui lit le fleuve') + '''
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
OUT.append(section('enjeux', 1, 'Les enjeux — à quoi servent les lipides, pourquoi on les dose',
    sub('enj-sub',
        'Le cours s\'ouvre sur une évidence à double face : les lipides sont <b>indispensables</b> (énergie, membranes, molécules signal), mais leur déséquilibre — la <b>dyslipidémie</b> — est un <b>facteur de risque cardiovasculaire majeur</b>. Toute la leçon sert à apprendre à le mesurer.',
        'يفتتح الدرس بحقيقة ذات وجهين: الدهون <b>لا غنى عنها</b> (طاقة، أغشية، جزيئات إشارة)، لكن اختلالها — <b>اضطراب دهنيات الدم</b> — عامل خطر <b>قلبي وعائي رئيسي</b>. الدرس كله يعلّم كيف نقيسه.'),
    [
        fig('enjeux.webp',
            "Planche des enjeux : à gauche les trois rôles des lipides — réserve d'énergie du tissu adipeux, membrane cellulaire en double couche de phospholipides, hormones et signaux ; à droite une artère en coupe dont la plaque d'athérome jaune rétrécit la lumière, avec le cœur en arrière-plan",
            '💡 <b>La double face :</b> énergie, structure, signaux — mais en excès, la plaque d\'athérome'),
        spot(0),
        lbox('enj-box1', 'fa-quote-left', 'Les trois rôles des lipides, tels que le cours les pose',
            [
                '<b>Rôle énergétique</b> : les triglycérides sont la <b>réserve d\'énergie</b> de l\'organisme, stockée dans le tissu adipeux, mobilisable par la β-oxydation.',
                '<b>Rôle structural</b> : phospholipides et cholestérol bâtissent les <b>membranes cellulaires</b> — pas de cellule sans lipides.',
                '<b>Rôle fonctionnel</b> : précurseurs de molécules actives (hormones stéroïdes, médiateurs) et véhicules des vitamines liposolubles.',
                'Le revers : une <b>dyslipidémie</b> (excès de cholestérol et/ou de triglycérides circulants) nourrit l\'<b>athérosclérose</b> — c\'est un <b>FRCV majeur</b>, au même titre que l\'HTA, le diabète et le tabac.',
            ],
            arbox('fa-quote-left', 'أدوار الدهون الثلاثة كما يطرحها الدرس', [
                '<b>دور طاقي</b>: الـ' + FP % 'triglycérides' + ' هي <b>مخزون الطاقة</b> في الجسم، مخزّنة في النسيج الشحمي وقابلة للتعبئة بالأكسدة بيتا.',
                '<b>دور بنيوي</b>: الـ' + FP % 'phospholipides' + ' والكولسترول يبنيان <b>الأغشية الخلوية</b> — لا خلية بلا دهون.',
                '<b>دور وظيفي</b>: طلائع لجزيئات فعّالة (هرمونات ستيرويدية، وسائط) وناقلات للفيتامينات الذوّابة في الدهون.',
                'الوجه الآخر: <b>اضطراب دهنيات الدم</b> (فائض كولسترول و/أو دهون ثلاثية جائلة) يغذّي <b>تصلّب الشرايين</b> — وهو عامل خطر قلبي <b>رئيسي</b> كارتفاع الضغط والسكري والتدخين.',
            ])),
        grid2(
            mini('enj-mini1', 'blue', 'fa-bullseye', 'À QUOI SERT L\'EAL (EXPLORATION D\'UNE ANOMALIE LIPIDIQUE)',
                [
                    '<b>Diagnostiquer</b> une dyslipidémie — chiffrer l\'anomalie, pas la deviner',
                    '<b>Classer</b> — rattacher le bilan à un type (Fredrickson) et à une cause (primitive ou secondaire)',
                    '<b>Évaluer le risque cardiovasculaire</b> global du patient, pour décider des cibles et du suivi',
                ],
                armini('fa-bullseye', 'ما فائدة استكشاف الشذوذ الدهني؟', [
                    '<b>التشخيص</b>: قياس الشذوذ بالأرقام لا تخمينه',
                    '<b>التصنيف</b>: ربط التحليل بنمط (' + FT % 'Fredrickson' + ') وبسبب (بدئي أو ثانوي)',
                    '<b>تقييم الخطر القلبي الوعائي</b> الإجمالي للمريض لتحديد الأهداف والمتابعة',
                ])),
            mini('enj-mini2', 'teal', 'fa-triangle-exclamation', 'LE MOT « BON / MAUVAIS CHOLESTÉROL »',
                [
                    'Le cholestérol est <b>le même</b> partout : c\'est le <b>véhicule</b> qui change le pronostic',
                    '<b>LDL = « mauvais »</b> : il livre le cholestérol aux tissus et à la paroi artérielle → <b>athérogène</b>',
                    '<b>HDL = « bon »</b> : il récupère le cholestérol des tissus vers le foie → <b>protecteur</b>',
                    'Une annale le teste mot pour mot : « le LDL représente le bon cholestérol » → <b>faux</b>',
                ],
                armini('fa-triangle-exclamation', 'عبارة «الكولسترول الجيّد / السيّئ»', [
                    'الكولسترول <b>هو نفسه</b> في كل مكان: ما يغيّر المآل هو <b>الناقل</b>',
                    '<b>' + FP % 'LDL' + ' = «السيّئ»</b>: يسلّم الكولسترول إلى الأنسجة وجدار الشريان ← <b>مصلِّب للشرايين</b>',
                    '<b>' + FP % 'HDL' + ' = «الجيّد»</b>: يسترجع الكولسترول من الأنسجة نحو الكبد ← <b>حامٍ</b>',
                    'سؤال امتحان يختبرها حرفياً: «الـ' + FP % 'LDL' + ' هو الكولسترول الجيد» ← <b>خطأ</b>',
                ]), delay='1')),
        focus([
            '<b>Inversion de sens (⑤)</b> : « le LDL est le bon cholestérol, le HDL le mauvais » — le couple est permuté.',
            '<b>Bon concept au mauvais endroit (②)</b> : « rôle structural des triglycérides » — le structural appartient aux phospholipides et au cholestérol, les TG sont l\'énergie.',
            '<b>Négation plaquée (⑥)</b> : « la dyslipidémie n\'est pas un facteur de risque cardiovasculaire » — le cours la pose comme FRCV <b>majeur</b>.',
        ]),
    ], '1. LES ENJEUX'))

# ═══════════════ 2. ABSORPTION ═══════════════
OUT.append(section('absorption', 2, 'Absorption intestinale — de l\'assiette au chylomicron',
    sub('abs-sub',
        'Les lipides alimentaires sont <b>démontés</b> dans la lumière intestinale, absorbés en pièces détachées, puis <b>remontés et emballés</b> dans l\'entérocyte : le colis sortant s\'appelle <b>chylomicron</b>, et il prend la <b>lymphe</b>, pas la veine porte.',
        'تُفكَّك دهون الغذاء في لمعة الأمعاء، وتُمتصّ قطعاً مفكّكة، ثم <b>تُعاد تركيبها وتغليفها</b> داخل الخلية المعوية: الطرد الخارج اسمه ' + FT % 'chylomicron' + '، ويسلك <b>اللمف</b> لا الوريد البابي.'),
    [
        fig('absorption.webp',
            "Planche de l'absorption intestinale : coupe d'une villosité intestinale, les graisses alimentaires sont démontées en acides gras libres, monoglycérides et cholestérol qui traversent l'entérocyte, s'y réassemblent en triglycérides emballés dans un gros chylomicron coiffé d'ApoB48, qui sort vers le vaisseau lymphatique central",
            '💡 <b>La chaîne :</b> démonter (lumière) → absorber (entérocyte) → remballer en chylomicron → lymphe'),
        spot(0),
        lbox('abs-box1', 'fa-gears', 'Les trois temps de l\'absorption',
            [
                '<b>1. Démontage</b> : dans la lumière, les triglycérides alimentaires sont hydrolysés en <b>acides gras libres</b> et <b>monoglycérides</b> ; le <b>cholestérol</b> alimentaire est absorbé tel quel.',
                '<b>2. Remballage</b> : dans l\'entérocyte, les pièces sont <b>re-estérifiées</b> en triglycérides et emballées dans le <b>chylomicron</b>, coiffé de l\'<b>ApoB48</b> — sa carte d\'identité intestinale.',
                '<b>3. Sortie par la lymphe</b> : trop gros pour les capillaires sanguins, le chylomicron emprunte les <b>chylifères</b> puis le canal thoracique, et rejoint le sang <b>après</b> le foie — les tissus périphériques se servent en premier.',
                'Conséquence visible au laboratoire : après un repas gras, le sérum devient <b>lactescent</b> — c\'est la marée des chylomicrons (d\'où le bilan <b>à jeun</b>).',
            ],
            arbox('fa-gears', 'أطوار الامتصاص الثلاثة', [
                '<b>1. التفكيك</b>: في اللمعة تُحلَّل الـ' + FP % 'triglycérides' + ' الغذائية إلى <b>أحماض دهنية حرة</b> و<b>أحاديات غليسريد</b>؛ أما كولسترول الغذاء فيُمتصّ كما هو.',
                '<b>2. إعادة التغليف</b>: داخل الخلية المعوية تُعاد أسترة القطع إلى ' + FP % 'triglycérides' + ' وتُغلَّف في الـ' + FT % 'chylomicron' + ' المتوَّج بـ' + FP % 'ApoB48' + ' — بطاقة هويته المعوية.',
                '<b>3. الخروج عبر اللمف</b>: لكبر حجمه يعجز عن الشعيرات الدموية، فيسلك <b>الأوعية اللبنية</b> ثم القناة الصدرية ويلتحق بالدم <b>بعد</b> الكبد — الأنسجة المحيطية تتزوّد أولاً.',
                'النتيجة المرئية في المختبر: بعد وجبة دسمة يصبح المصل <b>لبني المظهر</b> — إنها موجة الـ' + FP % 'chylomicrons' + ' (لذا يُجرى التحليل <b>صائماً</b>).',
            ])),
        grid2(
            mini('abs-mini1', 'blue', 'fa-box-open', 'CE QUI EST ABSORBÉ (LES PIÈCES)',
                [
                    '<b>Acides gras libres</b> — le carburant',
                    '<b>Monoglycérides</b> — la moitié d\'un TG',
                    '<b>Cholestérol libre</b> — absorbé en l\'état',
                    'Jamais de triglycéride <b>entier</b> qui traverse : il est toujours démonté puis remonté',
                ],
                armini('fa-box-open', 'ما الذي يُمتصّ (القطع)', [
                    '<b>الأحماض الدهنية الحرة</b> — الوقود',
                    '<b>أحاديات الغليسريد</b> — نصف ' + FP % 'TG' + '',
                    '<b>الكولسترول الحر</b> — يُمتصّ على حاله',
                    'لا يعبر ' + FP % 'triglycéride' + ' <b>كاملٌ</b> أبداً: يُفكَّك دائماً ثم يُعاد تركيبه',
                ])),
            mini('abs-mini2', 'purple', 'fa-route', 'LE DÉTOUR LYMPHATIQUE — POURQUOI IL COMPTE',
                [
                    'Sucres et acides aminés → <b>veine porte → foie d\'abord</b> ; chylomicrons → <b>lymphe → sang général d\'abord</b>',
                    'Les tissus (muscle, tissu adipeux) prélèvent les TG <b>avant</b> que le foie voie les restes',
                    'Ce qui arrive finalement au foie = les <b>restes (remnants)</b> de chylomicrons, appauvris en TG, enrichis en cholestérol',
                ],
                armini('fa-route', 'الالتفاف اللمفاوي — لماذا يهمّ', [
                    'السكريات والأحماض الأمينية ← <b>الوريد البابي ← الكبد أولاً</b>؛ الـ' + FP % 'chylomicrons' + ' ← <b>اللمف ← الدم العام أولاً</b>',
                    'الأنسجة (عضلات، نسيج شحمي) تأخذ الـ' + FP % 'TG' + ' <b>قبل</b> أن يرى الكبد البقايا',
                    'ما يصل أخيراً إلى الكبد = <b>بقايا</b> الـ' + FP % 'chylomicrons' + ' المفقَرة من ' + FP % 'TG' + ' والمغنّاة بالكولسترول',
                ]), delay='1')),
        focus([
            '<b>Faux voisin (①)</b> : « les chylomicrons portent l\'ApoB100 » — l\'intestin fabrique la <b>B48</b> ; B100 est la signature du foie.',
            '<b>Bon concept au mauvais endroit (②)</b> : « les chylomicrons rejoignent le foie par la veine porte » — ils passent par la <b>lymphe</b>.',
            '<b>Annale réelle</b> : « concentration des chylomicrons plus élevée en période postprandiale » → <b>vrai</b> — ils sont la marée d\'après-repas.',
        ]),
    ], '2. ABSORPTION'))

# ═══════════════ 3. TRANSPORT ═══════════════
OUT.append(section('transport', 3, 'Le transport — trois voies, un seul fleuve',
    sub('tra-sub',
        'Les lipides étant <b>hydrophobes</b>, le sang les transporte en colis : les <b>lipoprotéines</b>. Le schéma du cours organise tout en <b>trois voies</b> — exogène (depuis l\'intestin), endogène (depuis le foie), et le <b>transport inverse</b> du cholestérol par les HDL.',
        'بما أن الدهون <b>كارهة للماء</b>، ينقلها الدم في طرود: الـ' + FT % 'lipoprotéines' + '. مخطط الدرس ينظّم الكل في <b>ثلاثة مسارات</b> — خارجي (من الأمعاء)، داخلي (من الكبد)، و<b>النقل العكسي</b> للكولسترول عبر ' + FP % 'HDL' + '.'),
    [
        fig('transport.webp',
            "Planche du transport des lipides en trois voies : la voie exogène de l'intestin par les chylomicrons vers les tissus puis les restes vers le foie, la voie endogène du foie par les VLDL devenant IDL puis LDL vers les tissus, et le transport inverse du cholestérol par les HDL des tissus vers le foie",
            '💡 <b>Le fleuve complet :</b> intestin → tissus → foie · foie → tissus · tissus → foie (HDL)'),
        spot(1),
        lbox('tra-box1', 'fa-sitemap', 'Les trois voies du schéma du cours',
            [
                '<b>Voie exogène</b> : intestin → <b>chylomicrons</b> (TG alimentaires) → tissus qui déchargent les TG → <b>restes</b> captés par le foie.',
                '<b>Voie endogène</b> : foie → <b>VLDL</b> (TG fabriqués par le foie) → déchargées en route → <b>IDL</b> → <b>LDL</b>, qui livrent le cholestérol aux tissus.',
                '<b>Transport inverse</b> : les <b>HDL</b> collectent le cholestérol excédentaire des tissus (et des macrophages des parois) et le <b>ramènent au foie</b> — c\'est la voie « retour », protectrice.',
                'Point de passage obligé des trois voies : le <b>foie</b>, plaque tournante qui reçoit les restes, fabrique les VLDL et reçoit le cholestérol des HDL.',
            ],
            arbox('fa-sitemap', 'المسارات الثلاثة في مخطط الدرس', [
                '<b>المسار الخارجي</b>: الأمعاء ← ' + FP % 'chylomicrons' + ' (دهون الغذاء) ← الأنسجة تفرّغ الـ' + FP % 'TG' + ' ← <b>البقايا</b> يلتقطها الكبد.',
                '<b>المسار الداخلي</b>: الكبد ← ' + FP % 'VLDL' + ' (دهون صنعها الكبد) ← تُفرَّغ في الطريق ← ' + FP % 'IDL' + ' ← ' + FP % 'LDL' + ' التي تسلّم الكولسترول للأنسجة.',
                '<b>النقل العكسي</b>: الـ' + FP % 'HDL' + ' تجمع فائض كولسترول الأنسجة (وبلعمات الجدران) و<b>تعيده إلى الكبد</b> — إنه مسار «العودة» الحامي.',
                'نقطة العبور الإلزامية للمسارات الثلاثة: <b>الكبد</b>، المحور الذي يستقبل البقايا ويصنع الـ' + FP % 'VLDL' + ' ويستقبل كولسترول الـ' + FP % 'HDL' + '.',
            ])),
        reels('D<sup>r</sup> Besbes. A — « Transport des lipides », diapositive 6 du cours', [
            ('transport-schema.webp', 803, 578,
             "Schéma original du cours montrant le transport des lipides : les chylomicrons de l'intestin, les VLDL du foie devenant IDL puis LDL, et les HDL du transport inverse vers le foie",
             '<b>Le schéma du professeur</b> — les trois voies d\'un coup d\'œil : c\'est CE dessin qu\'il faut savoir refaire de mémoire'),
        ]),
        focus([
            '<b>Inversion de sens (⑤)</b> : « les HDL livrent le cholestérol aux tissus » — elles font le trajet <b>inverse</b> ; la livraison, c\'est les LDL.',
            '<b>Chaînon permuté (②)</b> : « VLDL → LDL → IDL » — l\'ordre est <b>VLDL → IDL → LDL</b>, la particule maigrit au fil de la route.',
            '<b>Faux point de départ (②)</b> : « la voie exogène part du foie » — exogène = <b>intestin</b> ; endogène = <b>foie</b>.',
        ]),
    ], '3. LE TRANSPORT'))

# ═══════════════ 4. FAMILLES ═══════════════
OUT.append(section('familles', 4, 'Les 5 familles de lipoprotéines — qui fait quoi',
    sub('fam-sub',
        'Cinq véhicules, une même carrosserie (cœur lipidique + coque + apolipoprotéines), des missions opposées : <b>livrer les triglycérides</b> (chylomicrons, VLDL), <b>livrer le cholestérol</b> (LDL), ou le <b>rapporter au foie</b> (HDL). Les IDL sont l\'étape intermédiaire.',
        'خمس مركبات بهيكل واحد (قلب دهني + غلاف + ' + FT % 'apolipoprotéines' + ') ومهام متعاكسة: <b>تسليم الدهون الثلاثية</b> (' + FP % 'chylomicrons' + '، ' + FP % 'VLDL' + '، <b>تسليم الكولسترول</b> (' + FP % 'LDL' + ')، أو <b>إعادته إلى الكبد</b> (' + FP % 'HDL' + '). أما ' + FP % 'IDL' + ' فهي المرحلة الوسيطة.'),
    [
        fig('familles.webp',
            "Planche des cinq familles de lipoprotéines en coupe à l'échelle : l'énorme chylomicron intestinal riche en triglycérides alimentaires, la VLDL hépatique, l'IDL intermédiaire, la LDL petite et pleine de cholestérol qui se dirige vers une paroi artérielle, et la minuscule HDL dense qui repart vers le foie avec son cholestérol",
            '💡 <b>La flotte entière :</b> deux camions à TG, un livreur de cholestérol, un camion de retour — et l\'IDL entre deux'),
        spot(1),
        lbox('fam-box1', 'fa-id-card', 'La carte d\'identité de chaque famille',
            [
                '<b>Chylomicrons</b> — nés dans l\'<b>intestin</b>, ils transportent les <b>TG exogènes</b> (alimentaires) vers les tissus ; marque : <b>ApoB48</b>. Présents surtout <b>après les repas</b>.',
                '<b>VLDL</b> — nées dans le <b>foie</b>, elles transportent les <b>TG endogènes</b> (fabriqués par le foie) vers les tissus ; marque : <b>ApoB100</b>.',
                '<b>IDL</b> — ce que devient une VLDL <b>déchargée</b> d\'une partie de ses TG : les « restes de VLDL », à mi-chemin vers le LDL.',
                '<b>LDL</b> — produit final de la voie endogène, il livre le <b>cholestérol aux tissus</b> ; marque : <b>ApoB100 seule</b>. C\'est la particule <b>athérogène</b> — celle que le traitement vise à abaisser.',
                '<b>HDL</b> — les plus petites et les plus denses ; elles assurent le <b>transport inverse</b> du cholestérol vers le foie ; marque : <b>ApoA</b>. Particule <b>protectrice</b>.',
            ],
            arbox('fa-id-card', 'بطاقة هوية كل عائلة', [
                '<b>' + FP % 'Chylomicrons' + '</b> — تولد في <b>الأمعاء</b> وتنقل <b>الدهون الخارجية</b> (الغذائية) إلى الأنسجة؛ علامتها: <b>' + FP % 'ApoB48' + '</b>. تحضر خاصة <b>بعد الوجبات</b>.',
                '<b>' + FP % 'VLDL' + '</b> — تولد في <b>الكبد</b> وتنقل <b>الدهون الداخلية</b> (صنعها الكبد) إلى الأنسجة؛ علامتها: <b>' + FP % 'ApoB100' + '</b>.',
                '<b>' + FP % 'IDL' + '</b> — ما تصبحه الـ' + FP % 'VLDL' + ' بعد <b>تفريغ</b> قسم من دهونها: «بقايا VLDL» في منتصف الطريق نحو ' + FP % 'LDL' + '.',
                '<b>' + FP % 'LDL' + '</b> — المنتج النهائي للمسار الداخلي، يسلّم <b>الكولسترول إلى الأنسجة</b>؛ علامته: <b>' + FP % 'ApoB100' + ' وحده</b>. إنه الجسيم <b>المصلِّب للشرايين</b> — هدف العلاج.',
                '<b>' + FP % 'HDL' + '</b> — الأصغر والأكثف؛ تؤمّن <b>النقل العكسي</b> للكولسترول نحو الكبد؛ علامتها: <b>' + FP % 'ApoA' + '</b>. جسيم <b>حامٍ</b>.',
            ])),
        grid2(
            mini('fam-mini1', 'amber', 'fa-truck', 'LES DEUX CAMIONS À TRIGLYCÉRIDES',
                [
                    'Même cargaison (TG), <b>deux provenances</b> : alimentaire → <b>chylomicrons</b> ; hépatique → <b>VLDL</b>',
                    'Ce sont <b>elles</b> qui troublent le sérum : grosses et riches en TG, elles diffusent la lumière (sérum opalescent ou lactescent)',
                    'À jeun, les chylomicrons ont <b>disparu</b> ; les VLDL, elles, circulent en permanence',
                ],
                armini('fa-truck', 'شاحنتا الدهون الثلاثية', [
                    'حمولة واحدة (' + FP % 'TG' + ') و<b>مصدران</b>: الغذاء ← ' + FP % 'chylomicrons' + '؛ الكبد ← ' + FP % 'VLDL' + '',
                    '<b>هما</b> من يعكّران المصل: جسيمات كبيرة غنية بـ' + FP % 'TG' + ' تشتّت الضوء (مصل عَكِر أو لبني)',
                    'في الصيام <b>تختفي</b> الـ' + FP % 'chylomicrons' + '؛ أما الـ' + FP % 'VLDL' + ' فتجول باستمرار',
                ])),
            mini('fam-mini2', 'red', 'fa-heart-crack', 'LE DUO DU CHOLESTÉROL : LDL CONTRE HDL',
                [
                    '<b>LDL</b> : foie → tissus. En excès, le cholestérol se dépose dans la <b>paroi artérielle</b> → plaque d\'athérome',
                    '<b>HDL</b> : tissus → foie. Plus il y en a, plus le cholestérol est « rapatrié » → effet <b>protecteur</b>',
                    'Le risque se lit dans l\'<b>équilibre des deux</b> — d\'où les seuils croisés de la section 10',
                ],
                armini('fa-heart-crack', 'ثنائي الكولسترول: LDL ضد HDL', [
                    '<b>' + FP % 'LDL' + '</b>: الكبد ← الأنسجة. عند فائضه يترسّب الكولسترول في <b>جدار الشريان</b> ← العصيدة',
                    '<b>' + FP % 'HDL' + '</b>: الأنسجة ← الكبد. كلما زاد «أُعيد» الكولسترول أكثر ← تأثير <b>حامٍ</b>',
                    'يُقرأ الخطر في <b>توازن الاثنين</b> — ومن هنا العتبات المتقاطعة في القسم 10',
                ]), delay='1')),
        focus([
            '<b>Permutation B48/B100 (⑧)</b> : « les chylomicrons contiennent majoritairement l\'ApoB100 » — annale réelle, corrigée <b>fausse</b> : B48 = intestin.',
            '<b>Provenance croisée (②)</b> : « les VLDL transportent les TG alimentaires » — alimentaire = chylomicrons ; VLDL = TG <b>du foie</b>.',
            '<b>Rôle croisé (⑤)</b> : « les HDL livrent le cholestérol aux tissus » — c\'est le LDL ; les HDL <b>rapportent</b>.',
        ]),
    ], '4. LES 5 FAMILLES'))

# ═══════════════ 5. CHIFFRES ★★ ═══════════════
OUT.append(section('chiffres', 5, 'Taille, densité, apolipoprotéines — le tableau qui tombe ★★',
    sub('chi-sub',
        'Le tableau des caractéristiques du cours est <b>la zone la plus cochable de la leçon</b> : quatre lignes, trois colonnes, et une logique unique — <b>plus une particule contient de lipides (légers), plus elle est grosse et moins elle est dense</b>.',
        'جدول خصائص الدرس هو <b>أكثر منطقة قابلة للسؤال في الدرس</b>: أربعة أسطر وثلاثة أعمدة ومنطق واحد — <b>كلما ازداد دهن الجسيم (الخفيف) كبر حجمه وقلّت كثافته</b>.'),
    [
        fig('chiffres.webp',
            "Planche des caractéristiques chiffrées : les quatre lipoprotéines alignées de la plus grosse à la plus petite au-dessus d'un gradient de densité, chylomicrons 100 nanomètres à 1 micromètre et 99 pour cent de lipides ApoB48, VLDL 50 nanomètres 90 pour cent ApoB100, LDL 20 nanomètres 80 pour cent ApoB100, HDL 10 nanomètres 50 à 70 pour cent ApoA, avec la flèche taille descendante densité ascendante",
            '💡 <b>La règle qui génère tout le tableau :</b> taille ↓ pendant que densité ↑'),
        spot(2),
        table('chi-tab1',
            ['Famille', 'Taille', '% de lipides', 'Apolipoprotéine(s)'],
            [
                ['<b>Chylomicrons</b>', '<b>100 nm – 1 µm</b>', '<b>99 %</b>', '<b>ApoB48</b> (+ C, E)'],
                ['<b>VLDL</b>', '<b>≈ 50 nm</b>', '<b>90 %</b>', '<b>ApoB100</b> (+ C, E)'],
                ['<b>LDL</b>', '<b>≈ 20 nm</b>', '<b>80 %</b>', '<b>ApoB100</b>'],
                ['<b>HDL</b>', '<b>≈ 10 nm</b>', '<b>50–70 %</b>', '<b>ApoA</b>'],
            ],
            '<thead><tr><th>العائلة</th><th>الحجم</th><th>نسبة الدهون %</th><th>' + FP % 'Apolipoprotéine(s)' + '</th></tr></thead><tbody>'
            '<tr><td><b>' + FP % 'Chylomicrons' + '</b></td><td><b>' + FP % '100 nm – 1 µm' + '</b></td><td><b>' + FP % '99 %' + '</b></td><td><b>' + FP % 'ApoB48' + '</b> (+ C, E)</td></tr>'
            '<tr><td><b>' + FP % 'VLDL' + '</b></td><td><b>' + FP % '≈ 50 nm' + '</b></td><td><b>' + FP % '90 %' + '</b></td><td><b>' + FP % 'ApoB100' + '</b> (+ C, E)</td></tr>'
            '<tr><td><b>' + FP % 'LDL' + '</b></td><td><b>' + FP % '≈ 20 nm' + '</b></td><td><b>' + FP % '80 %' + '</b></td><td><b>' + FP % 'ApoB100' + '</b></td></tr>'
            '<tr><td><b>' + FP % 'HDL' + '</b></td><td><b>' + FP % '≈ 10 nm' + '</b></td><td><b>' + FP % '50–70 %' + '</b></td><td><b>' + FP % 'ApoA' + '</b></td></tr></tbody>'),
        lbox('chi-box1', 'fa-brain', 'Pourquoi densité et taille marchent en sens inverse',
            [
                'Les <b>lipides sont légers</b> (ils flottent), les <b>protéines sont denses</b> (elles coulent) : la densité d\'une particule n\'est que le reflet de son ratio lipides/protéines.',
                'Le chylomicron, <b>99 % de lipides</b>, est un ballon quasi pur de graisse : densité minimale, taille maximale.',
                'La HDL, <b>jusqu\'à moitié protéine</b> (50–70 % de lipides seulement), est la plus petite et la plus dense — d\'où leurs noms : <b>Very Low / Low / High Density</b> Lipoproteins.',
                'Corollaire d\'annale : ce sont les <b>HDL, les plus riches en protéines</b> — « les VLDL sont les plus riches en protéines » est corrigé <b>faux</b>.',
            ],
            arbox('fa-brain', 'لماذا تسيران الكثافة والحجم بالعكس', [
                '<b>الدهون خفيفة</b> (تطفو) و<b>البروتينات كثيفة</b> (تغوص): كثافة الجسيم ليست إلا انعكاساً لنسبة دهونه إلى بروتيناته.',
                'الـ' + FT % 'chylomicron' + '، بـ<b>99 % دهون</b>، بالون شحم شبه صافٍ: كثافة دنيا وحجم أقصى.',
                'الـ' + FP % 'HDL' + '، <b>حتى نصفها بروتين</b> (50–70 % دهون فقط)، هي الأصغر والأكثف — ومن هنا أسماؤها: ' + FP % 'Very Low / Low / High Density' + '.',
                'نتيجة امتحانية: الـ' + FP % 'HDL' + ' هي <b>الأغنى بالبروتينات</b> — وعبارة «الـ' + FP % 'VLDL' + ' هي الأغنى بالبروتينات» مصحَّحة <b>خطأ</b>.',
            ])),
        reels('D<sup>r</sup> Besbes. A — « Caractéristiques des lipoprotéines », diapositives 9–10 du cours', [
            ('caracteristiques.webp', 1696, 1280,
             "Tableau original du cours des caractéristiques des lipoprotéines : taille, pourcentage de lipides et apolipoprotéines des chylomicrons, VLDL, LDL et HDL",
             '<b>Le tableau du professeur, mot pour mot</b> — c\'est de lui que les QCM tirent leurs chiffres'),
            ('densite-taille.webp', 606, 463,
             "Schéma original du cours de la relation inverse entre taille et densité des lipoprotéines, des chylomicrons aux HDL",
             '<b>La relation inverse taille ↔ densité</b> — le schéma qui accompagne le tableau dans le cours'),
        ]),
        focus([
            '<b>Chiffre déplacé (⑦)</b> : « HDL : 100 nm, 99 % de lipides » — vrais chiffres, mauvaise ligne : ils appartiennent aux <b>chylomicrons</b>.',
            '<b>Annale réelle</b> : « ce sont les plus volumineuses des lipoprotéines » (chylomicrons) → <b>vrai</b> ; « très mobiles à l\'électrophorèse » → <b>faux</b>, les plus grosses migrent le moins (notion testée en annale, à confirmer sur le cours).',
            '<b>Apo croisée (⑧)</b> : « l\'ApoA marque les LDL » — ApoA = <b>HDL</b> ; le LDL ne porte que <b>B100</b>.',
        ]),
    ], '5. TAILLE, DENSITÉ, APO'))

# ═══════════════ 6. DESTINÉE ═══════════════
OUT.append(section('destinee', 6, 'Destinée des lipides — stocker, brûler, construire',
    sub('des-sub',
        'Une fois livrés aux tissus, les lipides ont <b>trois sorts possibles</b> : être <b>stockés</b> (tissu adipeux), <b>brûlés</b> pour produire de l\'énergie (β-oxydation), ou <b>utilisés comme matériaux</b> de synthèse. L\'équilibre des trois fait la santé métabolique.',
        'بعد تسليمها إلى الأنسجة، للدهون <b>ثلاثة مصائر</b>: أن <b>تُخزَّن</b> (النسيج الشحمي)، أو <b>تُحرق</b> لإنتاج الطاقة (الأكسدة بيتا)، أو <b>تُستعمل موادَّ</b> للتركيب. وتوازن الثلاثة هو الصحة الاستقلابية.'),
    [
        fig('destinee.webp',
            "Planche de la destinée des lipides en trois destins : le stockage dans l'adipocyte rempli d'une goutte de triglycérides, la combustion dans le muscle par bêta-oxydation mitochondriale produisant de l'énergie, et les synthèses cellulaires membranes et hormones stéroïdes",
            '💡 <b>Trois destins :</b> la réserve (adipocyte), la chaudière (muscle), l\'atelier (synthèses)'),
        spot(2),
        grid2(
            mini('des-mini1', 'blue', 'fa-warehouse', 'STOCKAGE ET COMBUSTION',
                [
                    '<b>Stockage</b> : les TG non utilisés sont mis en réserve dans les <b>adipocytes</b> — la forme de stockage énergétique la plus concentrée',
                    '<b>β-oxydation</b> : dans les mitochondries (muscle, foie), les acides gras sont découpés en unités de 2 carbones pour produire de l\'<b>énergie</b>',
                    'Stockage et combustion sont les deux plateaux de la balance : l\'excès chronique du premier fait l\'<b>obésité</b>, complice des dyslipidémies',
                ],
                armini('fa-warehouse', 'التخزين والاحتراق', [
                    '<b>التخزين</b>: الـ' + FP % 'TG' + ' غير المستعملة تُدَّخر في <b>الخلايا الشحمية</b> — أكثف أشكال تخزين الطاقة',
                    '<b>الأكسدة بيتا</b>: في المتقدّرات (عضلات، كبد) تُقطَّع الأحماض الدهنية إلى وحدات ثنائية الكربون لإنتاج <b>الطاقة</b>',
                    'التخزين والاحتراق كفّتا الميزان: الفرط المزمن في الأول يصنع <b>السمنة</b>، شريكة اضطرابات الدهون',
                ])),
            mini('des-mini2', 'teal', 'fa-hammer', 'LES SYNTHÈSES',
                [
                    'Le <b>cholestérol</b> livré aux cellules sert aux <b>membranes</b> et de précurseur aux <b>hormones stéroïdes</b> et aux <b>sels biliaires</b>',
                    'Au foie, le cholestérol récupéré (restes + HDL) peut être <b>éliminé par la bile</b> — la seule vraie porte de sortie du cholestérol',
                    'C\'est ce rôle de sortie qui rend le transport inverse des HDL <b>protecteur</b> : il ramène le cholestérol vers sa seule issue',
                ],
                armini('fa-hammer', 'التركيبات', [
                    '<b>الكولسترول</b> المسلَّم إلى الخلايا يخدم <b>الأغشية</b> ويُشكّل طليعة <b>الهرمونات الستيرويدية</b> و<b>الأملاح الصفراوية</b>',
                    'في الكبد، يمكن <b>إطراح</b> الكولسترول المُسترجع (بقايا + ' + FP % 'HDL' + ') <b>عبر الصفراء</b> — منفذ الكولسترول الحقيقي الوحيد',
                    'دور المخرج هذا هو ما يجعل النقل العكسي عبر ' + FP % 'HDL' + ' <b>حامياً</b>: يعيد الكولسترول نحو منفذه الوحيد',
                ]), delay='1')),
        focus([
            '<b>Bon concept au mauvais endroit (②)</b> : « la β-oxydation stocke les acides gras » — elle les <b>brûle</b> ; le stockage est l\'adipocyte.',
            '<b>Inversion (⑤)</b> : « le cholestérol s\'élimine par le rein » — sa sortie est <b>biliaire</b>, via le foie.',
        ]),
    ], '6. DESTINÉE'))

# ═══════════════ 7. RÉGULATION ═══════════════
OUT.append(section('regulation', 7, 'Régulation — enzymes, transferts, récepteurs',
    sub('reg-sub',
        'Le trafic des particules n\'est pas libre : des <b>enzymes</b> déchargent et remodèlent les cargaisons (LPL, LCAT), une protéine <b>échange</b> les lipides entre particules (CETP), et des <b>récepteurs</b> décident qui entre dans le foie ou la cellule (récepteur LDL, ABCA1).',
        'حركة الجسيمات ليست حرّة: <b>إنزيمات</b> تفرّغ الحمولات وتعيد تشكيلها (' + FP % 'LPL' + '، ' + FP % 'LCAT' + '، وبروتين <b>يتبادل</b> الدهون بين الجسيمات (' + FP % 'CETP' + '، و<b>مستقبلات</b> تقرّر من يدخل الكبد أو الخلية (مستقبل ' + FP % 'LDL' + '، ' + FP % 'ABCA1' + ').'),
    [
        fig('regulation.webp',
            "Planche de la régulation du métabolisme des lipoprotéines : le récepteur LDL du foie captant LDL et restes, la lipoprotéine lipase libérant les acides gras pour le muscle et le tissu adipeux, la LCAT estérifiant le cholestérol des HDL, la CETP échangeant les esters de cholestérol entre particules, et ABCA1 avec ApoA1 faisant sortir le cholestérol des macrophages",
            '💡 <b>Les aiguilleurs :</b> LPL décharge · LCAT verrouille · CETP échange · récepteurs captent'),
        spot(3),
        lbox('reg-box1', 'fa-traffic-light', 'Les cinq aiguilleurs du schéma du cours',
            [
                '<b>LPL (lipoprotéine lipase)</b> — accrochée aux capillaires des tissus, elle <b>hydrolyse les TG</b> des chylomicrons et des VLDL et libère les acides gras pour le <b>muscle et le tissu adipeux</b> : c\'est elle qui « décharge les camions ».',
                '<b>Récepteur LDL du foie</b> — il reconnaît l\'ApoB100/E et <b>capte LDL et restes</b> : c\'est la principale sortie du LDL circulant (sa mutation = hypercholestérolémie familiale, annales).',
                '<b>LCAT</b> — elle <b>estérifie le cholestérol</b> à la surface des HDL : le cholestérol devient hydrophobe, plonge au cœur de la particule, et la HDL peut continuer à en collecter.',
                '<b>CETP</b> — protéine d\'<b>échange</b> : elle transfère des esters de cholestérol des HDL vers les particules à ApoB (VLDL/LDL) contre des TG — un troc entre familles.',
                '<b>ABCA1 + ApoA1</b> — la porte de sortie du cholestérol des <b>macrophages</b> vers les HDL naissantes : la première étape du transport inverse, celle qui vide la paroi artérielle.',
            ],
            arbox('fa-traffic-light', 'الموجّهون الخمسة في مخطط الدرس', [
                '<b>' + FP % 'LPL' + '</b> — متعلّقة بشعيرات الأنسجة، <b>تحلّل ' + FP % 'TG' + '</b> الـ' + FP % 'chylomicrons' + ' والـ' + FP % 'VLDL' + ' وتحرّر الأحماض الدهنية إلى <b>العضلات والنسيج الشحمي</b>: هي من «يفرّغ الشاحنات».',
                '<b>مستقبل ' + FP % 'LDL' + ' الكبدي</b> — يتعرّف على ' + FP % 'ApoB100/E' + ' و<b>يلتقط ' + FP % 'LDL' + ' والبقايا</b>: إنه المخرج الرئيسي للـ' + FP % 'LDL' + ' الجائل (طفرته = فرط كولسترول الدم العائلي، أسئلة امتحانات).',
                '<b>' + FP % 'LCAT' + '</b> — <b>تؤستر الكولسترول</b> على سطح ' + FP % 'HDL' + ': يصبح كارهاً للماء فيغوص إلى قلب الجسيم، وتواصل الـ' + FP % 'HDL' + ' جمعها.',
                '<b>' + FP % 'CETP' + '</b> — بروتين <b>تبادل</b>: ينقل إسترات الكولسترول من ' + FP % 'HDL' + ' نحو جسيمات ' + FP % 'ApoB' + ' مقابل ' + FP % 'TG' + ' — مقايضة بين العائلات.',
                '<b>' + FP % 'ABCA1 + ApoA1' + '</b> — باب خروج الكولسترول من <b>البلعمات</b> نحو ' + FP % 'HDL' + ' الوليدة: الخطوة الأولى من النقل العكسي، التي تفرّغ جدار الشريان.',
            ])),
        reels('D<sup>r</sup> Besbes. A — « Régulation du métabolisme des lipoprotéines », diapositive 12 du cours', [
            ('regulation.webp', 1416, 917,
             "Schéma original du cours de la régulation des lipoprotéines : enzymes, protéines de transfert et récepteurs autour des voies exogène, endogène et du transport inverse",
             '<b>Le schéma de régulation du professeur</b> — à comparer trait pour trait avec la planche ci-dessus'),
        ]),
        focus([
            '<b>Rôles permutés (⑧)</b> : « la CETP estérifie le cholestérol des HDL » — c\'est la <b>LCAT</b> ; la CETP <b>échange</b>.',
            '<b>Annale réelle</b> : le type IIa « peut être dû à une mutation du gène du récepteur de l\'Apo B/E » → <b>vrai</b> — le récepteur LDL est LA serrure génétique de la leçon.',
            '<b>Mauvais organe (②)</b> : « la LPL agit dans le foie » — elle agit aux <b>capillaires des tissus utilisateurs</b> (muscle, tissu adipeux).',
        ]),
    ], '7. RÉGULATION'))

# ═══════════════ 8. DÉPISTAGE ═══════════════
OUT.append(section('depistage', 8, 'Qui dépister, et quand ? — les indications de l\'EAL',
    sub('dep-sub',
        'L\'exploration d\'une anomalie lipidique ne se fait pas au hasard : le cours fixe des <b>âges-seuils</b> (homme 40 ans, femme 50 ans) et des <b>situations</b> qui avancent l\'horloge — facteurs de risque, signes cliniques, histoire familiale.',
        'استكشاف الشذوذ الدهني لا يتم عشوائياً: يحدّد الدرس <b>أعماراً عتبية</b> (الرجل 40 عاماً، المرأة 50 عاماً) و<b>حالات</b> تُقدّم الموعد — عوامل خطر، علامات سريرية، سوابق عائلية.'),
    [
        fig('depistage.webp',
            "Planche du dépistage des dyslipidémies : un médecin reçoit un homme de 40 ans, une femme de 50 ans et un adolescent dont la famille compte une maladie cardiovasculaire précoce, avec les cartouches des âges de dépistage et des situations qui font avancer le bilan",
            '💡 <b>La règle :</b> 40 ans (homme) · 50 ans (femme) · plus tôt si le terrain parle'),
        spot(3),
        lbox('dep-box1', 'fa-calendar-check', 'Les indications posées par le cours',
            [
                '<b>Dépistage systématique</b> : chez l\'<b>homme dès 40 ans</b>, chez la <b>femme dès 50 ans</b> — les deux âges à connaître au chiffre près.',
                '<b>Plus tôt</b> en présence de <b>facteurs de risque cardiovasculaire</b> (diabète, HTA, tabac, obésité…) : l\'annale valide « chez tous les adultes de moins de 80 ans avec au moins un facteur de risque ».',
                '<b>Chez l\'enfant</b> : en cas d\'<b>antécédents familiaux</b> de dyslipidémie ou de maladie cardiovasculaire précoce — c\'est ainsi qu\'on dépiste les formes familiales (cas n°2 du cours).',
                '<b>Autres situations</b> : signes cliniques évocateurs, suspicion de <b>cause secondaire</b>, et <b>suivi d\'un traitement</b> hypolipémiant déjà en place.',
            ],
            arbox('fa-calendar-check', 'الاستطبابات كما يضعها الدرس', [
                '<b>تقصٍّ منهجي</b>: عند <b>الرجل من 40 عاماً</b> وعند <b>المرأة من 50 عاماً</b> — عمران يُحفظان بالرقم.',
                '<b>أبكر</b> عند وجود <b>عوامل خطر قلبية وعائية</b> (سكري، ضغط، تدخين، سمنة…): سؤال الامتحان يصحّح «عند كل البالغين دون 80 عاماً مع عامل خطر واحد على الأقل».',
                '<b>عند الطفل</b>: عند وجود <b>سوابق عائلية</b> لاضطراب دهون أو مرض قلبي مبكر — هكذا تُكشف الصور العائلية (حالة الدرس رقم 2).',
                '<b>حالات أخرى</b>: علامات سريرية موحية، اشتباه <b>سبب ثانوي</b>، و<b>متابعة علاج</b> خافض للدهون قائم.',
            ])),
        focus([
            '<b>Âges permutés (⑧)</b> : « femme dès 40 ans, homme dès 50 ans » — le cours dit l\'inverse : l\'homme est dépisté <b>plus tôt</b>.',
            '<b>Annale réelle</b> : « l\'exploration est recommandée chez les sujets jeunes » → <b>faux</b> tel quel : il faut un âge-seuil ou un facteur de risque, pas « jeunes » en général.',
            '<b>Énumération tronquée (③)</b> : oublier l\'enfant à antécédents familiaux — c\'est pourtant la porte d\'entrée des formes génétiques.',
        ]),
    ], '8. QUI DÉPISTER ?'))

# ═══════════════ 9. BILAN 1 ★★ ═══════════════
OUT.append(section('bilan1', 9, 'Bilan de 1ʳᵉ intention — regarder le sérum avant de le doser ★★',
    sub('b1-sub',
        'Le premier examen du bilan lipidique ne coûte rien : c\'est l\'<b>aspect du sérum</b>. Clair, opalescent ou lactescent, il oriente avant tout dosage — et s\'il est lactescent, le <b>test de crémage</b> (12 h à +4 °C) départage chylomicrons et VLDL.',
        'أول فحص في التحليل الدهني لا يكلّف شيئاً: إنه <b>مظهر المصل</b>. صافياً كان أو عَكِراً أو لبنياً، يوجّه قبل أي قياس — وإذا كان لبنياً فـ<b>اختبار التكرييم</b> (12 ساعة في +4°) يفصل بين ' + FP % 'chylomicrons' + ' و' + FP % 'VLDL' + '.'),
    [
        fig('bilan1.webp',
            "Planche du bilan de première intention : trois tubes de sérum à jeun d'aspect clair, opalescent et lactescent, le tube lactescent après douze heures au réfrigérateur avec sa couche crémeuse surnageante au test de crémage, et la liste des dosages de première intention aspect, cholestérol total, triglycérides, HDL, LDL et non-HDL",
            '💡 <b>L\'ordre du bilan :</b> d\'abord les yeux (aspect + crémage), ensuite les chiffres'),
        spot(4),
        lbox('b1-box1', 'fa-list-check', 'Le contenu du bilan de 1ʳᵉ intention',
            [
                '<b>Selon le cours</b> : <b>aspect du sérum, triglycérides, cholestérol total, HDL, LDL et non-HDL</b> — prélevés <b>à jeun</b> (les chylomicrons postprandiaux faussent TG et aspect).',
                '<b>Selon les annales</b> (« bilan lipidique de base ») : <b>CT + TG + LDLc</b> (calculé ou dosé) — <b>ApoB et ApoA1 sont corrigés « 2ᵉ intention »</b>. Retenir les deux formulations : le cours pour comprendre, l\'annale pour cocher.',
                '<b>Le non-HDL</b> (CT − HDL) reflète <b>toutes les particules athérogènes</b> d\'un coup ; il reste <b>fiable quand les TG sont élevés</b>, là où le LDL calculé décroche (annale : « plus indicatif que le LDLc pour le risque » → vrai).',
                '<b>Confirmation</b> (testé en annale, à confirmer sur le cours) : un premier bilan anormal se <b>répète à 2–4 semaines</b>, sans régime ni médicament intercurrent, avant de conclure.',
            ],
            arbox('fa-list-check', 'محتوى تحليل القصد الأول', [
                '<b>حسب الدرس</b>: <b>مظهر المصل، ' + FP % 'TG' + '، الكولسترول الكلي، ' + FP % 'HDL' + '، ' + FP % 'LDL' + '، و' + FP % 'non-HDL' + '</b> — بسحبٍ <b>صائماً</b> (لأن ' + FP % 'chylomicrons' + ' ما بعد الوجبة تحرّف ' + FP % 'TG' + ' والمظهر).',
                '<b>حسب الامتحانات</b> («التحليل الأساسي»): <b>' + FP % 'CT + TG + LDLc' + '</b> — و<b>' + FP % 'ApoB' + ' و' + FP % 'ApoA1' + ' مصحَّحان «قصداً ثانياً»</b>. احفظ الصيغتين: الدرس للفهم، والامتحان للتأشير.',
                '<b>الـ' + FP % 'non-HDL' + '</b> (الكلي − ' + FP % 'HDL' + ') يعكس <b>كل الجسيمات المصلِّبة</b> دفعة واحدة؛ ويبقى <b>موثوقاً عند ارتفاع ' + FP % 'TG' + '</b> حيث ينحرف ' + FP % 'LDL' + ' المحسوب (امتحان: «أدلّ من ' + FP % 'LDLc' + ' على الخطر» ← صحيح).',
                '<b>التأكيد</b> (سقط في الامتحان، للتثبت من الدرس): التحليل الأول الشاذ <b>يُعاد بعد 2–4 أسابيع</b> دون حمية ولا دواء طارئ قبل الاستنتاج.',
            ])),
        grid2(
            mini('b1-mini1', 'amber', 'fa-eye', 'L\'ASPECT DU SÉRUM EN 3 MOTS',
                [
                    '<b>Clair</b> : pas d\'excès de grosses particules (un LDL élevé seul ne trouble <b>pas</b> le sérum)',
                    '<b>Opalescent</b> : excès de <b>VLDL</b> — le trouble des TG endogènes',
                    '<b>Lactescent</b> : excès de <b>chylomicrons</b> (± VLDL) → <b>test de crémage obligatoire</b>',
                ],
                armini('fa-eye', 'مظهر المصل في 3 كلمات', [
                    '<b>صافٍ</b>: لا فائض جسيمات كبيرة (ارتفاع ' + FP % 'LDL' + ' وحده <b>لا</b> يعكّر المصل)',
                    '<b>عَكِر (opalescent)</b>: فائض <b>' + FP % 'VLDL' + '</b> — عكارة الدهون الداخلية',
                    '<b>لبني (lactescent)</b>: فائض <b>' + FP % 'chylomicrons' + '</b> (± ' + FP % 'VLDL' + ') ← <b>اختبار التكرييم إلزامي</b>',
                ])),
            mini('b1-mini2', 'purple', 'fa-snowflake', 'LE TEST DE CRÉMAGE (12 H À +4 °C)',
                [
                    '<b>Couche crémeuse + culot clair</b> → <b>chylomicrons seuls</b> (ils surnagent : ce sont les moins denses)',
                    '<b>Pas de crème, sérum opalescent</b> → <b>VLDL seules</b>',
                    '<b>Couche crémeuse + culot trouble</b> → <b>les deux</b> (chylomicrons + VLDL)',
                    'La physique de la section 5 au travail : ce qui est plein de graisse <b>flotte</b>',
                ],
                armini('fa-snowflake', 'اختبار التكرييم (12 ساعة في +4°)', [
                    '<b>طبقة قشدية + قاع صافٍ</b> ← <b>' + FP % 'chylomicrons' + ' وحدها</b> (تطفو: هي الأقل كثافة)',
                    '<b>لا قشدة، مصل عَكِر</b> ← <b>' + FP % 'VLDL' + ' وحدها</b>',
                    '<b>طبقة قشدية + قاع عَكِر</b> ← <b>الاثنان معاً</b> (' + FP % 'chylomicrons + VLDL' + ')',
                    'فيزياء القسم 5 تعمل هنا: ما امتلأ دهناً <b>يطفو</b>',
                ]), delay='1')),
        reels('D<sup>r</sup> Besbes. A — « Aspect du sérum » et « Test de crémage », diapositives 16–17 du cours', [
            ('aspect-serum.webp', 1544, 649,
             "Photographie originale du cours de trois tubes de sérum d'aspect clair, opalescent et lactescent côte à côte",
             '<b>Clair · opalescent · lactescent</b> — les trois aspects réels photographiés dans le cours'),
            ('test-cremage.webp', 425, 660,
             "Schéma original du cours du test de crémage après douze heures à plus quatre degrés : couche crémeuse surnageante et culot, selon la présence de chylomicrons et de VLDL",
             '<b>Le crémage du cours</b> — 12 h à +4 °C, puis on lit : crème ? culot clair ou trouble ?'),
        ]),
        focus([
            '<b>Annale réelle</b> : sérum lactescent → « présence en excès de chylomicrons » + « nécessite un test de crémage » = les deux bonnes ; « augmentation des LDL » → <b>faux</b>, le LDL ne trouble pas.',
            '<b>Intention permutée (②)</b> : « ApoB = bilan de base » — les annales le rangent en <b>2ᵉ intention</b>, avec ApoA1 et le lipidogramme.',
            '<b>Résultat de crémage croisé (⑧)</b> : crème + culot <b>Clair</b> = chylomicrons seuls ; culot <b>trouble</b> = il reste des VLDL en dessous.',
        ]),
    ], '9. BILAN DE 1ʳᵉ INTENTION'))

# ═══════════════ 10. VALEURS ★★ ═══════════════
OUT.append(section('valeurs', 10, 'Valeurs usuelles et cibles — les quatre chiffres ★★',
    sub('val-sub',
        'Quatre chiffres du cours, une cible annale : <b>CT &lt; 2 g/L</b>, <b>TG 0,5–1,5 g/L</b>, <b>HDL ≥ 0,4 (homme) / 0,5 (femme) g/L</b>, <b>LDL &lt; 1,6 g/L</b> — et chez le patient à <b>haut risque</b>, le LDL doit descendre sous <b>0,70 g/L</b>.',
        'أربعة أرقام من الدرس وهدف من الامتحانات: <b>الكلي &lt; ' + FP % '2 g/L' + '</b>، <b>' + FP % 'TG' + ' بين 0,5–1,5</b>، <b>' + FP % 'HDL' + ' ≥ 0,4 (رجل) / 0,5 (امرأة)</b>، <b>' + FP % 'LDL' + ' &lt; 1,6</b> — وعند <b>عالي الخطورة</b> يجب أن ينزل الـ' + FP % 'LDL' + ' تحت <b>0,70</b>.'),
    [
        fig('valeurs.webp',
            "Planche des valeurs usuelles : un compte-rendu de laboratoire avec quatre jauges colorées, cholestérol total moins de 2 grammes par litre soit 5,2 millimoles, triglycérides 0,5 à 1,5, HDL homme 0,4 femme 0,5 en dessous risque augmenté, LDL moins de 1,6 et moins de 0,70 à haut risque",
            '💡 <b>À réciter comme une table de multiplication :</b> 2 · 0,5–1,5 · 0,4/0,5 · 1,6 → 0,70'),
        spot(5),
        table('val-tab1',
            ['Paramètre', 'Valeur usuelle (cours)', 'Repère d\'annale'],
            [
                ['<b>Cholestérol total</b>', '<b>&lt; 2 g/L</b> (5,2 mmol/L)', 'La borne « 2 » est le repère de tri rapide'],
                ['<b>Triglycérides</b>', '<b>0,5 – 1,5 g/L</b>', 'Au-delà : sérum trouble, Friedewald en danger'],
                ['<b>HDL-cholestérol</b>', '<b>Homme 0,4 · Femme 0,5 g/L</b>', '<b>&lt; 0,40 g/L = facteur de risque</b> (2 annales)'],
                ['<b>LDL-cholestérol</b>', '<b>&lt; 1,6 g/L</b>', '<b>&lt; 0,70 g/L si haut risque</b> · paramètre du suivi'],
            ],
            '<thead><tr><th>المؤشر</th><th>القيمة الاعتيادية (الدرس)</th><th>معلم امتحاني</th></tr></thead><tbody>'
            '<tr><td><b>الكولسترول الكلي</b></td><td><b>&lt; ' + FP % '2 g/L' + '</b> (' + FP % '5,2 mmol/L' + ')</td><td>حدّ «2» هو معلم الفرز السريع</td></tr>'
            '<tr><td><b>' + FP % 'Triglycérides' + '</b></td><td><b>' + FP % '0,5 – 1,5 g/L' + '</b></td><td>فوقها: مصل عَكِر وصيغة ' + FT % 'Friedewald' + ' في خطر</td></tr>'
            '<tr><td><b>' + FP % 'HDL' + '</b></td><td><b>رجل ' + FP % '0,4' + ' · امرأة ' + FP % '0,5 g/L' + '</b></td><td><b>&lt; ' + FP % '0,40' + ' = عامل خطر</b> (سؤالان)</td></tr>'
            '<tr><td><b>' + FP % 'LDL' + '</b></td><td><b>&lt; ' + FP % '1,6 g/L' + '</b></td><td><b>&lt; ' + FP % '0,70' + ' عند عالي الخطورة</b> · مؤشر المتابعة</td></tr></tbody>'),
        lbox('val-box1', 'fa-gauge-high', 'Comment ces chiffres travaillent le jour de l\'EMD',
            [
                '<b>HDL bas = danger</b> : un HDL <b>&lt; 0,40 g/L</b> est compté comme <b>facteur de risque cardiovasculaire</b> (deux annales, dont une au rattrapage 2022) — l\'hypoHDLémie de l\'homme se suspecte donc <b>sous 0,4</b>, pas sous 0,6 ni 1,0.',
                '<b>LDL = la cible</b> : le risque augmente de façon <b>exponentielle</b> avec le LDLc, et c\'est le <b>principal paramètre du suivi thérapeutique</b> (annale 2022) — on traite un chiffre de LDL, on suit un chiffre de LDL.',
                '<b>La cible se durcit avec le risque</b> : &lt; 1,6 g/L en valeur usuelle, <b>&lt; 0,70 g/L chez le haut risque</b> cardiovasculaire. « &lt; 1 g/L chez les sujets sans facteur de risque » est corrigé <b>faux</b> — ce n\'est pas le repère.',
                '<b>TG = le perturbateur</b> : élevées, elles troublent le sérum <b>et</b> invalident le calcul du LDL — le non-HDL prend alors le relais.',
            ],
            arbox('fa-gauge-high', 'كيف تعمل هذه الأرقام يوم الامتحان', [
                '<b>انخفاض ' + FP % 'HDL' + ' = خطر</b>: ' + FP % 'HDL' + ' <b>&lt; 0,40</b> يُحسب <b>عامل خطر قلبي وعائي</b> (سؤالان، أحدهما استدراك 2022) — نقص ' + FP % 'HDL' + ' عند الرجل يُشتبه إذن <b>تحت 0,4</b> لا تحت 0,6 ولا 1,0.',
                '<b>' + FP % 'LDL' + ' = الهدف</b>: الخطر يتزايد <b>أسياً</b> مع ' + FP % 'LDLc' + '، وهو <b>مؤشر المتابعة العلاجية الرئيسي</b> (امتحان 2022) — نعالج رقم ' + FP % 'LDL' + ' ونتابع رقم ' + FP % 'LDL' + '.',
                '<b>الهدف يشتدّ مع الخطر</b>: &lt; 1,6 قيمة اعتيادية، <b>&lt; 0,70 عند عالي الخطورة</b>. وعبارة «&lt; 1 عند من لا عامل خطر له» مصحَّحة <b>خطأ</b> — ليست هي المعلم.',
                '<b>' + FP % 'TG' + ' = المشوِّش</b>: مرتفعةً تعكّر المصل <b>و</b>تُبطل حساب ' + FP % 'LDL' + ' — فيتولّى الـ' + FP % 'non-HDL' + ' المهمة.',
            ])),
        focus([
            '<b>Chiffre déplacé (⑦) — la fabrique n°1 ici</b> : les annales proposent HDL &lt; 0,6 / &lt; 1,0 / &lt; 1,3 : un seul seuil est le bon (<b>0,4 chez l\'homme</b>).',
            '<b>Inversion de protection (⑤)</b> : « un HDL à 0,20 g/L est protecteur » — c\'est un <b>facteur de risque</b> (annale).',
            '<b>Cible permutée (⑧)</b> : 0,70 g/L appartient au <b>haut risque</b> ; 1,6 g/L est la valeur usuelle — ne pas échanger les deux patients.',
        ]),
    ], '10. VALEURS & CIBLES'))

# ═══════════════ 11. BILAN 2 ★★ ═══════════════
OUT.append(section('bilan2', 11, 'Bilan de 2ᵉ intention — préciser le risque ★★',
    sub('b2-sub',
        'Quand le premier bilan ne suffit pas, la 2ᵉ intention <b>compte les particules</b> (ApoB, ApoA1), <b>photographie la répartition</b> (électrophorèse) et traque le risque <b>génétique</b> (Lp(a), tests ciblés). C\'est aussi ici que la formule de Friedewald montre ses limites.',
        'حين لا يكفي التحليل الأول، يقوم القصد الثاني بـ<b>عدّ الجسيمات</b> (' + FP % 'ApoB' + '، ' + FP % 'ApoA1' + ') و<b>تصوير توزيعها</b> (الرحلان) وتتبّع الخطر <b>الوراثي</b> (' + FP % 'Lp(a)' + '، اختبارات موجّهة). وهنا أيضاً تظهر حدود صيغة ' + FT % 'Friedewald' + '.'),
    [
        fig('bilan2.webp',
            "Planche du bilan de deuxième intention : un gel d'électrophorèse des lipoprotéines avec ses bandes bleues à côté d'un analyseur automatique, et les cartouches électrophorèse qui sépare selon la charge, ApoB qui compte les particules athérogènes, ApoA1 reflet des HDL, Lp(a) risque génétique indépendant, tests génétiques si suspicion familiale, Friedewald invalide si triglycérides très élevés",
            '💡 <b>La 2ᵉ intention en une phrase :</b> compter (Apo), séparer (électrophorèse), hériter (Lp(a))'),
        spot(5),
        lbox('b2-box1', 'fa-microscope', 'Les cinq outils de la 2ᵉ intention',
            [
                '<b>Électrophorèse des lipoprotéines (lipidogramme)</b> : elle sépare les familles selon leur <b>charge/mobilité</b> — c\'est l\'outil historique qui a fondé la classification de <b>Fredrickson (OMS)</b> ; le cours note son <b>déclin en routine</b>, remplacée par les dosages directs.',
                '<b>ApoB</b> : chaque particule athérogène (VLDL, IDL, LDL) ne porte qu\'<b>une seule ApoB</b> → doser l\'ApoB, c\'est <b>compter les particules athérogènes</b>.',
                '<b>ApoA1</b> : le reflet des <b>HDL</b> ; le <b>rapport ApoB/ApoA1</b> oppose les deux camps et résume le <b>risque global</b>.',
                '<b>Lp(a)</b> : particule à taux <b>génétiquement déterminé</b>, facteur de risque <b>indépendant</b> — elle explique des événements que le bilan classique ne prévoit pas.',
                '<b>Tests génétiques</b> : en cas de suspicion de forme familiale (récepteur ApoB/E et gènes voisins) — le cas de l\'enfant du cours.',
            ],
            arbox('fa-microscope', 'أدوات القصد الثاني الخمس', [
                '<b>رحلان الـ' + FT % 'lipoprotéines' + ' (' + FT % 'lipidogramme' + ')</b>: يفصل العائلات حسب <b>الشحنة/الحركية</b> — إنه الأداة التاريخية التي أسّست تصنيف <b>' + FT % 'Fredrickson' + '</b>؛ ويلاحظ الدرس <b>تراجعه روتينياً</b> لصالح القياسات المباشرة.',
                '<b>' + FP % 'ApoB' + '</b>: كل جسيم مصلِّب (' + FP % 'VLDL, IDL, LDL' + ') يحمل <b>' + FP % 'ApoB' + ' واحدة فقط</b> ← قياس ' + FP % 'ApoB' + ' هو <b>عدّ الجسيمات المصلِّبة</b>.',
                '<b>' + FP % 'ApoA1' + '</b>: انعكاس <b>' + FP % 'HDL' + '</b>؛ ونسبة <b>' + FP % 'ApoB/ApoA1' + '</b> تقابل المعسكرين وتلخّص <b>الخطر الإجمالي</b>.',
                '<b>' + FP % 'Lp(a)' + '</b>: جسيم تحدّده <b>الوراثة</b>، عامل خطر <b>مستقل</b> — يفسّر أحداثاً لا يتوقّعها التحليل الكلاسيكي.',
                '<b>الاختبارات الوراثية</b>: عند اشتباه صورة عائلية (مستقبل ' + FP % 'ApoB/E' + ' والجينات المجاورة) — حالة طفل الدرس.',
            ])),
        grid2(
            mini('b2-mini1', 'red', 'fa-calculator', 'FRIEDEWALD : LE CALCUL QUI A SES LIMITES',
                [
                    'Le LDL est souvent <b>calculé</b> (formule de Friedewald, à partir de CT, TG et HDL) plutôt que dosé directement',
                    '<b>Testé en annales</b> (à confirmer sur le cours) : le calcul <b>n\'est pas applicable quand les TG sont très élevés</b> — les corrigés rejettent son usage à <b>5,0 g/L</b> et à <b>4,38 g/L</b> de TG',
                    'Le seuil exact n\'est pas donné par la source : <b>ne pas inventer de chiffre</b> le jour J — retenir « TG très élevés → calcul invalide, penser non-HDL / dosage direct »',
                ],
                armini('fa-calculator', 'Friedewald: حسابٌ له حدوده', [
                    'الـ' + FP % 'LDL' + ' غالباً <b>محسوب</b> (صيغة ' + FT % 'Friedewald' + ' من الكلي و' + FP % 'TG' + ' و' + FP % 'HDL' + ') لا مقاس مباشرة',
                    '<b>سقط في الامتحانات</b> (للتثبت من الدرس): الحساب <b>لا ينطبق عند ارتفاع ' + FP % 'TG' + ' الشديد</b> — التصحيحات ترفض استعماله عند <b>' + FP % '5,0' + '</b> و<b>' + FP % '4,38 g/L' + '</b>',
                    'العتبة الدقيقة غير معطاة في المصدر: <b>لا تخترع رقماً</b> يوم الامتحان — احفظ «' + FP % 'TG' + ' مرتفعة جداً ← حساب باطل، فكّر في ' + FP % 'non-HDL' + ' / القياس المباشر»',
                ])),
            mini('b2-mini2', 'blue', 'fa-scale-balanced', 'APOB CONTRE APOA1 : LE COMPTE DES CAMPS',
                [
                    '<b>1 particule athérogène = 1 ApoB</b> : le dosage compte les véhicules, là où le LDLc ne pèse que leur cargaison de cholestérol',
                    'Deux patients au même LDLc peuvent avoir des <b>nombres de particules très différents</b> — l\'ApoB les départage',
                    'Le rapport <b>ApoB/ApoA1</b> : numérateur = agression, dénominateur = protection',
                ],
                armini('fa-scale-balanced', 'ApoB ضد ApoA1: عدّ المعسكرين', [
                    '<b>جسيم مصلِّب واحد = ' + FP % 'ApoB' + ' واحدة</b>: القياس يعدّ المركبات، بينما ' + FP % 'LDLc' + ' يزن حمولتها من الكولسترول فقط',
                    'مريضان بنفس ' + FP % 'LDLc' + ' قد يختلفان كثيراً في <b>عدد الجسيمات</b> — الـ' + FP % 'ApoB' + ' يفرّقهما',
                    'نسبة <b>' + FP % 'ApoB/ApoA1' + '</b>: البسط = العدوان، المقام = الحماية',
                ]), delay='1')),
        reels('D<sup>r</sup> Besbes. A — « Électrophorèse des lipoprotéines », diapositive 23 du cours', [
            ('electrophorese.webp', 700, 578,
             "Image originale du cours d'une électrophorèse des lipoprotéines montrant la séparation des fractions selon leur mobilité",
             '<b>Le lipidogramme du cours</b> — la séparation qui a donné naissance aux types de Fredrickson'),
        ]),
        focus([
            '<b>Annales réelles (×3)</b> : « bilan de 2ᵉ intention » = <b>ApoB, ApoA1, lipidogramme</b> ; CT et TG y sont les intrus (c\'est la 1ʳᵉ intention).',
            '<b>Friedewald piégé (④)</b> : tout énoncé « Friedewald applicable » collé à des TG <b>élevés</b> est faux — 5,0 et 4,38 g/L dans les annales.',
            '<b>Mobilité croisée (⑤)</b> : les <b>gros</b> chylomicrons sont les <b>moins mobiles</b> à l\'électrophorèse (testé en annale) — la taille freine la migration.',
        ]),
    ], '11. BILAN DE 2ᵉ INTENTION'))

# ═══════════════ 12. FREDRICKSON ★★ ═══════════════
OUT.append(section('fredrickson', 12, 'Classification de Fredrickson — les types I à V ★★',
    sub('fre-sub',
        'Six cases (I, IIa, IIb, III, IV, V), une seule question par case : <b>quelle particule s\'accumule ?</b> C\'est <b>la zone la plus tombable du cours</b> — 6 des 15 annales la testent directement.',
        'ست خانات (I، IIa، IIb، III، IV، V) وسؤال واحد لكل خانة: <b>أيّ جسيم يتراكم؟</b> إنها <b>أكثر منطقة سقوطاً في الدرس</b> — 6 من الأسئلة الخمسة عشر تختبرها مباشرة.'),
    [
        fig('fredrickson.webp',
            "Frise de la classification de Fredrickson sur des tubes de sérum : type I chylomicrons sérum lactescent, type IIa LDL cholestérol élevé sérum clair, type IIb mixte LDL et VLDL quarante pour cent, type III IDL restes rare, type IV VLDL triglycérides élevés quarante-cinq pour cent, type V chylomicrons et VLDL",
            '💡 <b>La frise à photographier :</b> I chylo · IIa LDL · IIb les deux · III restes · IV VLDL · V chylo+VLDL'),
        spot(6),
        table('fre-tab1',
            ['Type', 'Particule élevée', 'CT / TG', 'Repères'],
            [
                ['<b>I</b>', '<b>Chylomicrons</b>', 'TG ↑↑↑', 'Très rare (&lt; 1 %) · sérum lactescent'],
                ['<b>IIa</b>', '<b>LDL</b>', '<b>CT ↑</b>, TG normaux', 'Hypercholestérolémie <b>pure</b> · athérogène · sérum <b>non lactescent</b>'],
                ['<b>IIb</b>', '<b>LDL + VLDL</b>', '<b>CT ↑ et TG ↑</b>', 'Mixte · <b>40 %</b> des cas · athérogène'],
                ['<b>III</b>', '<b>IDL (restes)</b>', 'CT ↑ et TG ↑', 'Très rare (&lt; 1 %) · athérogène'],
                ['<b>IV</b>', '<b>VLDL</b>', 'TG ↑', 'Le plus fréquent : <b>45 %</b> · sérum opalescent · souvent associé au diabète'],
                ['<b>V</b>', '<b>Chylomicrons + VLDL</b>', 'CT ↑, TG ↑↑', 'Crème + culot trouble au crémage'],
            ],
            '<thead><tr><th>النمط</th><th>الجسيم المرتفع</th><th>' + FP % 'CT / TG' + '</th><th>معالم</th></tr></thead><tbody>'
            '<tr><td><b>' + FP % 'I' + '</b></td><td><b>' + FP % 'Chylomicrons' + '</b></td><td>' + FP % 'TG ↑↑↑' + '</td><td>نادر جداً (&lt; 1 %) · مصل لبني</td></tr>'
            '<tr><td><b>' + FP % 'IIa' + '</b></td><td><b>' + FP % 'LDL' + '</b></td><td><b>' + FP % 'CT ↑' + '</b>، ' + FP % 'TG' + ' طبيعية</td><td>فرط كولسترول <b>صرف</b> · مصلِّب · مصل <b>غير لبني</b></td></tr>'
            '<tr><td><b>' + FP % 'IIb' + '</b></td><td><b>' + FP % 'LDL + VLDL' + '</b></td><td><b>' + FP % 'CT ↑ وTG ↑' + '</b></td><td>مختلط · <b>40 %</b> من الحالات · مصلِّب</td></tr>'
            '<tr><td><b>' + FP % 'III' + '</b></td><td><b>' + FP % 'IDL' + ' (بقايا)</b></td><td>' + FP % 'CT ↑ وTG ↑' + '</td><td>نادر جداً (&lt; 1 %) · مصلِّب</td></tr>'
            '<tr><td><b>' + FP % 'IV' + '</b></td><td><b>' + FP % 'VLDL' + '</b></td><td>' + FP % 'TG ↑' + '</td><td>الأكثر شيوعاً: <b>45 %</b> · مصل عَكِر · يرافق السكري غالباً</td></tr>'
            '<tr><td><b>' + FP % 'V' + '</b></td><td><b>' + FP % 'Chylomicrons + VLDL' + '</b></td><td>' + FP % 'CT ↑, TG ↑↑' + '</td><td>قشدة + قاع عَكِر في التكرييم</td></tr></tbody>'),
        lbox('fre-box1', 'fa-star', 'Les trois types que les annales dissèquent',
            [
                '<b>Type IIa</b> — hypercholestérolémie <b>pure par augmentation des LDL</b> : TG normaux donc sérum <b>non lactescent</b>, pouvoir <b>athérogène fort</b>, pouvant relever d\'une <b>mutation du récepteur ApoB/E</b>. Deux annales le passent au crible proposition par proposition.',
                '<b>Type IIb</b> — l\'<b>hyperlipidémie mixte</b> (LDL + VLDL : CT et TG montent ensemble), 40 % des cas. « IIb = hypercholestérolémie pure » est corrigé <b>faux</b>.',
                '<b>Type III</b> — accumulation d\'<b>IDL</b> (particules de taille intermédiaire) avec CT et TG élevés. L\'annale piège avec le « déficit en LPL » (qui signe plutôt les chylomicrons) et le sérum « limpide ».',
                '<b>Types athérogènes</b> selon les annales : <b>IIa, IIb et III</b> — ceux qui accumulent les particules à ApoB riches en cholestérol.',
                '⚠️ Le recueil ELITE écrit deux fois « <b>type VI</b> » (associé au diabète, sérum opalescent, synthèse hépatique de VLDL) : il n\'existe pas de type VI — c\'est le <b>type IV</b>. Les annales sont reproduites telles quelles, corrigées avec cette clé.',
            ],
            arbox('fa-star', 'الأنماط الثلاثة التي تشرّحها الامتحانات', [
                '<b>النمط ' + FP % 'IIa' + '</b> — فرط كولسترول <b>صرف بارتفاع ' + FP % 'LDL' + '</b>: ' + FP % 'TG' + ' طبيعية إذن مصل <b>غير لبني</b>، قدرة <b>مصلِّبة قوية</b>، قد يعود إلى <b>طفرة مستقبل ' + FP % 'ApoB/E' + '</b>. سؤالان يمرّرانه اقتراحاً اقتراحاً.',
                '<b>النمط ' + FP % 'IIb' + '</b> — فرط الدهون <b>المختلط</b> (' + FP % 'LDL + VLDL' + ': يرتفع الكلي والـ' + FP % 'TG' + ' معاً)، 40 % من الحالات. وعبارة «' + FP % 'IIb' + ' = فرط كولسترول صرف» مصحَّحة <b>خطأ</b>.',
                '<b>النمط ' + FP % 'III' + '</b> — تراكم <b>' + FP % 'IDL' + '</b> (جسيمات متوسطة الحجم) مع ارتفاع الكلي والـ' + FP % 'TG' + '. الامتحان يصطاد بـ«نقص ' + FP % 'LPL' + '» (يوقّع الـ' + FP % 'chylomicrons' + ' بالأحرى) وبالمصل «الصافي».',
                '<b>الأنماط المصلِّبة</b> حسب الامتحانات: <b>' + FP % 'IIa' + ' و' + FP % 'IIb' + ' و' + FP % 'III' + '</b> — ما يراكم جسيمات ' + FP % 'ApoB' + ' الغنية بالكولسترول.',
                '⚠️ مجموعة ' + FP % 'ELITE' + ' تكتب مرتين «<b>النمط ' + FP % 'VI' + '</b>» (مرتبط بالسكري، مصل عَكِر، تركيب كبدي للـ' + FP % 'VLDL' + '): لا يوجد نمط ' + FP % 'VI' + ' — إنه <b>النمط ' + FP % 'IV' + '</b>. الأسئلة منقولة كما هي ومصحَّحة بهذا المفتاح.',
            ])),
        reels('D<sup>r</sup> Besbes. A — « Classification de Fredrickson », diapositive 25 du cours', [
            ('fredrickson.webp', 510, 336,
             "Tableau original du cours de la classification de Fredrickson : lipoprotéine élevée, cholestérol total, triglycérides, athérogénicité et fréquence des types I à V",
             '<b>Le tableau Fredrickson du professeur</b> — fréquences comprises (IIb 40 %, IV 45 %)'),
        ]),
        focus([
            '<b>La permutation reine (⑧)</b> : IIa ↔ IIb ↔ IV — pur (LDL) / mixte (LDL+VLDL) / TG (VLDL). Toute la zone tient dans ces trois étiquettes.',
            '<b>Aspect du sérum croisé (②)</b> : « IIa = sérum lactescent » → faux deux fois en annales : sans TG, pas de lait.',
            '<b>Pouvoir athérogène nié (⑥)</b> : « IIa = faible pouvoir athérogène » → faux : c\'est le type du LDL pur, le plus directement athérogène.',
        ]),
    ], '12. FREDRICKSON I–V'))

# ═══════════════ 13. SECONDAIRES ★★ ═══════════════
OUT.append(section('secondaires', 13, 'Secondaire d\'abord — chercher la cause avant de conclure primitive ★★',
    sub('sec-sub',
        'Le réflexe professionnel du cours : devant toute dyslipidémie, <b>éliminer d\'abord une cause secondaire</b> — maladie ou médicament qui dérègle les lipides. Conclure « primitive » (génétique) n\'a de sens qu\'après cette chasse.',
        'الانعكاس المهني في الدرس: أمام أي اضطراب دهني <b>استبعِد أولاً سبباً ثانوياً</b> — مرضاً أو دواءً يخلّ بالدهون. ولا معنى لاستنتاج «بدئي» (وراثي) إلا بعد هذه المطاردة.'),
    [
        fig('secondaires.webp',
            "Planche des causes secondaires d'hyperlipoprotéinémie autour d'un tube de sérum lactescent : hypothyroïdie, diabète, syndrome néphrotique et insuffisance rénale, cholestase hépatique, médicaments corticoïdes thiazidiques bêtabloquants œstrogènes, obésité alcool syndrome métabolique, et le piège d'annale l'hypoparathyroïdie ne donne pas d'hyperlipoprotéinémie secondaire",
            '💡 <b>Cinq portes à ouvrir avant « primitive » :</b> thyroïde, sucre, rein, foie, médicaments — plus le terrain'),
        spot(6),
        lbox('sec-box1', 'fa-list-check', 'La liste du cours, à réciter dans l\'ordre',
            [
                '<b>Endocrino-métaboliques</b> : <b>diabète</b> (surtout type 2), <b>hypothyroïdie</b> — les deux classiques à doser/chercher en premier.',
                '<b>Rénales</b> : <b>syndrome néphrotique</b> et <b>insuffisance rénale chronique</b>.',
                '<b>Hépatique</b> : la <b>cholestase</b> (le cholestérol ne peut plus sortir par la bile, il reflue).',
                '<b>Médicamenteuses</b> : <b>corticoïdes, diurétiques thiazidiques, β-bloquants, œstrogènes, antirétroviraux</b> — relire l\'ordonnance fait partie du bilan.',
                '<b>Terrain</b> : <b>obésité, alcool, syndrome métabolique</b> — souvent associés entre eux (cas n°1 du cours).',
                '⛔ <b>L\'intrus des annales</b> : l\'<b>hypoparathyroïdie</b> ne donne <b>PAS</b> d\'hyperlipoprotéinémie secondaire — c\'est la réponse de la toute première annale du chapitre.',
            ],
            arbox('fa-list-check', 'قائمة الدرس، تُروى بالترتيب', [
                '<b>غدية-استقلابية</b>: <b>السكري</b> (خاصة النمط 2)، <b>قصور الدرقية</b> — الكلاسيكيان اللذان يُبحث عنهما أولاً.',
                '<b>كلوية</b>: <b>المتلازمة الكلوية (النفروزية)</b> و<b>القصور الكلوي المزمن</b>.',
                '<b>كبدية</b>: <b>الركود الصفراوي</b> (الكولسترول يعجز عن الخروج بالصفراء فيرتدّ).',
                '<b>دوائية</b>: <b>الكورتيكويدات، الثيازيدات، حاصرات بيتا، الأستروجينات، مضادات الفيروسات القهقرية</b> — إعادة قراءة الوصفة جزء من التحليل.',
                '<b>الأرضية</b>: <b>السمنة، الكحول، المتلازمة الاستقلابية</b> — غالباً مجتمعة (حالة الدرس رقم 1).',
                '⛔ <b>دخيل الامتحانات</b>: <b>قصور جارات الدرقية</b> <b>لا</b> يعطي فرط دهنيات ثانوياً — إنها إجابة أول سؤال في الفصل.',
            ])),
        focus([
            '<b>L\'intrus lexical (①)</b> : hypo<b>para</b>thyroïdie glissée entre diabète, hypo<b>thyroïdie</b>, néphrotique et cholestase — l\'annale n°1 entière tient dans ce « para ».',
            '<b>Sens thyroïdien inversé (⑤)</b> : c\'est l\'<b>hypo</b>thyroïdie qui élève les lipides ; l\'<b>hyper</b>thyroïdie proposée en annale est corrigée fausse.',
            '<b>Oubli de l\'ordonnance (③)</b> : une liste de causes sans les <b>médicaments</b> est une liste tronquée — thiazidiques et corticoïdes en tête.',
        ]),
    ], '13. CAUSES SECONDAIRES'))

# ═══════════════ 14. CAS ═══════════════
OUT.append(section('cas', 14, 'Deux cas pour s\'entraîner — les dossiers du cours',
    sub('cas-sub',
        'Le cours se ferme sur <b>deux cas corrigés</b> qui résument toute la démarche : un adulte au profil « mixte + syndrome métabolique », un enfant dont le bilan hurle « familial ». Savoir les raisonner, c\'est savoir faire la leçon entière.',
        'يُغلق الدرس بـ<b>حالتين مصحَّحتين</b> تلخّصان المنهج كله: بالغ بملف «مختلط + متلازمة استقلابية»، وطفل يصرخ تحليله «عائلي». معرفة استدلالهما هي معرفة الدرس كله.'),
    [
        fig('cas.webp',
            "Planche des deux cas du cours : à gauche un homme de 45 ans obèse IMC 32 dont on prend la tension, cholestérol total 2,70 LDL 1,90 HDL 0,35 triglycérides 2,10 grammes par litre, réponse dyslipidémie mixte syndrome métabolique ; à droite un garçon de 13 ans examiné avec sa mère, cholestérol total 3,10 LDL 2,45 triglycérides normaux, père infarctus à 42 ans, réponse hypercholestérolémie familiale",
            '💡 <b>Deux patients, deux logiques :</b> le terrain métabolique contre la génétique'),
        spot(7),
        lbox('cas-box1', 'fa-user-doctor', 'Cas 1 — l\'homme de 45 ans (dyslipidémie mixte + syndrome métabolique)',
            [
                '<b>Le bilan</b> : homme 45 ans, <b>IMC 32</b> — CT <b>2,70</b>, LDL <b>1,90</b>, HDL <b>0,35</b>, TG <b>2,10 g/L</b> : tout est anormal, dans les deux sens.',
                '<b>Le raisonnement</b> : cholestérol <b>et</b> triglycérides élevés = profil <b>mixte (type IIb)</b> ; HDL effondré sous 0,40 = facteur de risque ajouté ; obésité abdominale en toile de fond.',
                '<b>La conclusion du cours</b> : <b>dyslipidémie mixte dans un syndrome métabolique</b> — démarche : confirmer le bilan, chercher le <b>diabète</b> et les autres causes secondaires, évaluer le risque global, fixer la cible de LDL.',
            ],
            arbox('fa-user-doctor', 'الحالة 1 — الرجل البالغ 45 عاماً (مختلط + متلازمة استقلابية)', [
                '<b>التحليل</b>: رجل 45 عاماً، <b>كتلة جسدية 32</b> — الكلي <b>2,70</b>، ' + FP % 'LDL' + ' <b>1,90</b>، ' + FP % 'HDL' + ' <b>0,35</b>، ' + FP % 'TG' + ' <b>2,10</b>: كل شيء شاذ في الاتجاهين.',
                '<b>الاستدلال</b>: كولسترول <b>و</b>دهون ثلاثية مرتفعة = ملف <b>مختلط (نمط ' + FP % 'IIb' + ')</b>؛ ' + FP % 'HDL' + ' منهارة تحت 0,40 = عامل خطر مضاف؛ سمنة بطنية في الخلفية.',
                '<b>استنتاج الدرس</b>: <b>اضطراب دهني مختلط ضمن متلازمة استقلابية</b> — المنهج: تأكيد التحليل، البحث عن <b>السكري</b> والأسباب الثانوية الأخرى، تقييم الخطر الإجمالي، تحديد هدف ' + FP % 'LDL' + '.',
            ])),
        lbox('cas-box2', 'fa-child', 'Cas 2 — le garçon de 13 ans (hypercholestérolémie familiale)',
            [
                '<b>Le bilan</b> : garçon 13 ans — CT <b>3,10</b>, LDL <b>2,45 g/L</b>, <b>TG normaux</b> : une hypercholestérolémie <b>pure</b> (profil IIa), massive pour l\'âge.',
                '<b>L\'indice qui parle</b> : le <b>père a fait un infarctus à 42 ans</b> — maladie cardiovasculaire précoce dans la famille, exactement l\'indication de dépistage de l\'enfant (section 8).',
                '<b>La conclusion du cours</b> : <b>hypercholestérolémie familiale</b> — démarche : éliminer une cause secondaire (hypothyroïdie en tête), <b>enquête familiale</b>, envisager le test génétique (récepteur ApoB/E), prise en charge précoce.',
            ],
            arbox('fa-child', 'الحالة 2 — الفتى البالغ 13 عاماً (فرط كولسترول عائلي)', [
                '<b>التحليل</b>: فتى 13 عاماً — الكلي <b>3,10</b>، ' + FP % 'LDL' + ' <b>2,45</b>، <b>' + FP % 'TG' + ' طبيعية</b>: فرط كولسترول <b>صرف</b> (ملف ' + FP % 'IIa' + ') ضخم بالنسبة للعمر.',
                '<b>الدليل الناطق</b>: <b>الأب أصيب باحتشاء في 42 عاماً</b> — مرض قلبي مبكر في العائلة، وهو بالضبط استطباب تقصّي الطفل (القسم 8).',
                '<b>استنتاج الدرس</b>: <b>فرط كولسترول الدم العائلي</b> — المنهج: استبعاد سبب ثانوي (قصور الدرقية أولاً)، <b>تحرٍّ عائلي</b>، النظر في الاختبار الوراثي (مستقبل ' + FP % 'ApoB/E' + '، تكفّل مبكر.',
            ])),
        grid2(
            mini('cas-mini1', 'blue', 'fa-list-check', 'LE RÉFLEXE EN 4 TEMPS DEVANT TOUT BILAN ANORMAL',
                [
                    '<b>1. Confirmer</b> — répéter le bilan (2–4 semaines selon les annales) avant d\'étiqueter',
                    '<b>2. Chercher le secondaire</b> — thyroïde, sucre, rein, foie, ordonnance, terrain',
                    '<b>3. Classer</b> — quel type de Fredrickson dessinent les chiffres ?',
                    '<b>4. Risque global</b> — fixer la cible de LDL selon le niveau de risque, pas selon l\'humeur',
                ],
                armini('fa-list-check', 'الانعكاس الرباعي أمام كل تحليل شاذ', [
                    '<b>1. التأكيد</b> — إعادة التحليل (2–4 أسابيع حسب الامتحانات) قبل الوسم',
                    '<b>2. البحث عن الثانوي</b> — درقية، سكر، كلى، كبد، وصفة، أرضية',
                    '<b>3. التصنيف</b> — أي نمط ' + FT % 'Fredrickson' + ' ترسمه الأرقام؟',
                    '<b>4. الخطر الإجمالي</b> — تحديد هدف ' + FP % 'LDL' + ' حسب مستوى الخطر لا حسب المزاج',
                ])),
            mini('cas-mini2', 'amber', 'fa-magnifying-glass', 'CE QUI DÉPARTAGE LES DEUX CAS',
                [
                    'Cas 1 : <b tout monte</b> (CT + TG) chez un adulte en surcharge → penser <b>terrain métabolique / secondaire</b>',
                    'Cas 2 : <b>LDL seul, très haut, très jeune</b> + histoire familiale → penser <b>génétique</b>',
                    'Le même chiffre de LDL ne raconte pas la même histoire à 13 ans et à 45 ans',
                ],
                armini('fa-magnifying-glass', 'ما الذي يفرّق الحالتين', [
                    'الحالة 1: <b>كل شيء يرتفع</b> (كلي + ' + FP % 'TG' + ') عند بالغ مفرط الوزن ← فكّر في <b>أرضية استقلابية / ثانوي</b>',
                    'الحالة 2: <b>' + FP % 'LDL' + ' وحده مرتفع جداً وفي سنّ صغيرة</b> + قصة عائلية ← فكّر في <b>الوراثة</b>',
                    'رقم ' + FP % 'LDL' + ' نفسه لا يروي القصة ذاتها في 13 عاماً و45 عاماً',
                ]), delay='1')),
        focus([
            '<b>Conclusion hâtive (⑥)</b> : « LDL élevé chez l\'enfant = primitive, dossier clos » — le cours impose d\'abord la chasse au <b>secondaire</b>, même à 13 ans.',
            '<b>Profil croisé (⑧)</b> : TG normaux + LDL massif = <b>IIa</b> ; CT et TG élevés ensemble = <b>IIb</b> — les deux cas sont les deux cases du tableau, en chair et en os.',
        ]),
    ], '14. DEUX CAS'))

# ═══════════════ MÉTHODE EMD ═══════════════
OUT.append('''            <!-- ═══════════════ MÉTHODE EMD ═══════════════ -->
            <section class="lsection" id="methode">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-user-secret"></i></div>
                    <div>
                        <h2>La méthode de l'examinateur — penser comme celui qui écrit le sujet</h2>
                        ''' + sub('met-sub',
                            'Le moule vient de la dissection des <b>15 QCM d\'annales authentiques</b> de ce chapitre (recueil ELITE, PROMO 2018 → rattrapage 2022). Ici, pas besoin d\'inventer le profil : il est <b>mesuré</b>, question par question.',
                            'القالب مستخرج من تشريح <b>الأسئلة الخمسة عشر الأصلية</b> لهذا الفصل (مجموعة ' + FP % 'ELITE' + '، دفعات 2018 ← استدراك 2022). هنا لا حاجة لاختراع الأسلوب: إنه <b>مقاس</b> سؤالاً سؤالاً.') + '''
                    </div>
                </div>

''' + grid2(
    mini('met-mini1', 'blue', 'fa-ruler-combined', 'LA FORME, MESURÉE SUR 15 QUESTIONS RÉELLES',
        [
            '<b>Toujours 5 propositions</b>, de A à E. Aucune exception sur les 15.',
            '<b>Énoncé nominal court</b> : « Le bilan lipidique de base comprend : », « Le LDLc : », « Un sérum lactescent : ».',
            'Cadrage <b>positif</b> 14 fois sur 15 — l\'unique négatif (« laquelle <b>ne</b> donne <b>pas</b>… ») est la question des causes secondaires : c\'est elle qui piège les pressés.',
            '<b>Nombre de bonnes réponses : 1 (×5), 2 (×2), 3 (×8).</b> La réponse triple est la signature de ce chapitre — plus d\'une question sur deux.',
            '<b>Zones tombées</b> : Fredrickson ≈ 6/15 · seuils HDL/LDL ≈ 4/15 · 1ʳᵉ/2ᵉ intention ≈ 3/15 · aspect du sérum 2/15 · secondaires 1/15.',
        ],
        armini('fa-ruler-combined', 'الشكل، مقاساً على 15 سؤالاً حقيقياً', [
            '<b>خمسة اقتراحات دائماً</b> من ' + FP % 'A' + ' إلى ' + FP % 'E' + '. لا استثناء في الخمسة عشر.',
            '<b>نصّ اسمي قصير</b>: «التحليل الدهني الأساسي يشمل:»، «الـ' + FP % 'LDLc' + ':»، «مصل لبني:».',
            'صياغة <b>موجبة</b> 14 مرة من 15 — والسلبي الوحيد («أيّها <b>لا</b> يعطي…») هو سؤال الأسباب الثانوية: إنه مصيدة العجِلين.',
            '<b>عدد الإجابات الصحيحة: 1 (×5)، 2 (×2)، 3 (×8).</b> الإجابة الثلاثية هي بصمة هذا الفصل — أكثر من سؤال من اثنين.',
            '<b>المناطق الساقطة</b>: ' + FT % 'Fredrickson' + ' ≈ 6/15 · عتبات ' + FP % 'HDL/LDL' + ' ≈ 4/15 · القصدان الأول/الثاني ≈ 3/15 · مظهر المصل 2/15 · الثانوية 1/15.',
        ])),
    mini('met-mini2', 'red', 'fa-screwdriver-wrench', 'LES FABRIQUES, VERSION BIOCHIMIE DES LIPIDES',
        [
            '<b>① Faux voisin lexical</b> — hypo<b>para</b>thyroïdie glissée parmi les vraies causes (annale n°1).',
            '<b>② Bon concept au mauvais endroit</b> — ApoB rangée au « bilan de base » ; IIa accusée d\'augmenter les IDL.',
            '<b>④ Ordre de grandeur / seuil</b> — Friedewald « applicable » à TG 5,0 ou 4,38 g/L ; HDL « &lt; 1,3 g/L » chez l\'homme.',
            '<b>⑤ Inversion de sens</b> — « le LDL, bon cholestérol » ; « IIa, faible pouvoir athérogène » ; chylomicrons « très mobiles ».',
            '<b>⑦ Chiffre déplacé</b> — les seuils HDL 0,6 / 1,0 proposés à la place du <b>0,4</b> ; LDL « &lt; 1 g/L sans facteur de risque ».',
            '<b>⑧ Paire antagoniste</b> — lactescent/opalescent, IIa/IIb, 1ʳᵉ/2ᵉ intention : les deux membres sont présents, un seul est à sa place.',
            '<b>⑨ Composite</b> — « IIa : hypercholestérolémie pure <b>et</b> familiale combinée » : vrai + faux soudés, la proposition tombe entière.',
        ],
        armini('fa-screwdriver-wrench', 'المصانع، بصيغة كيمياء الدهون', [
            '<b>① جار لفظي زائف</b> — قصور <b>جارات</b> الدرقية مدسوساً بين الأسباب الحقيقية (السؤال رقم 1).',
            '<b>② مفهوم صحيح في مكان خاطئ</b> — ' + FP % 'ApoB' + ' مصنّفة في «التحليل الأساسي»؛ ' + FP % 'IIa' + ' متّهمة برفع ' + FP % 'IDL' + '.',
            '<b>④ رتبة مقدار / عتبة</b> — ' + FT % 'Friedewald' + ' «قابلة للتطبيق» عند ' + FP % 'TG' + ' بقيمة 5,0 أو 4,38؛ ' + FP % 'HDL' + ' «&lt; 1,3» عند الرجل.',
            '<b>⑤ قلب المعنى</b> — «الـ' + FP % 'LDL' + '، الكولسترول الجيد»؛ «' + FP % 'IIa' + ' ضعيفة الإصلاح»؛ الـ' + FP % 'chylomicrons' + ' «شديدة الحركية».',
            '<b>⑦ رقم مزاح</b> — عتبات ' + FP % 'HDL' + ' بقيمة 0,6 / 1,0 بدل <b>0,4</b>؛ ' + FP % 'LDL' + ' «&lt; 1 دون عامل خطر».',
            '<b>⑧ زوج متقابل</b> — لبني/عَكِر، ' + FP % 'IIa/IIb' + '، القصد الأول/الثاني: الطرفان حاضران وواحد فقط في مكانه.',
            '<b>⑨ مركَّب</b> — «' + FP % 'IIa' + ': فرط كولسترول صرف <b>و</b>عائلي مركّب»: صواب ملحوم بخطأ، يسقط الاقتراح كله.',
        ]), delay='1')) + '''

''' + lbox('met-box1', 'fa-chess-knight', 'Comment cela se traduit dans tes entraînement et tes annales',
    [
        '<b>Section « QCM annales »</b> : les 15 questions <b>authentiques</b>, texte du recueil ELITE et <b>corrigés officiels</b>, disséqués choix par choix avec le nom de la fabrique quand il y en a une.',
        '<b>Section « Entraînement »</b> : 20 questions <b>neuves</b> écrites dans le même moule — 5 propositions, cadrage positif (une seule négative, comme l\'original), distribution calquée : <b>7 à une réponse · 3 à deux · 10 à trois</b>.',
        '<b>Transparence</b> : le recueil écrit deux fois « type VI » — reproduit tel quel dans les annales, avec la clé en correction (c\'est le <b>type IV</b>). Le seuil exact de validité de Friedewald n\'étant pas dans la source, aucun entraînement ne te fera deviner un chiffre absent.',
        '<b>La matière des pièges</b> : 2 · 0,5–1,5 · 0,4/0,5 · 1,6 · 0,70 — B48/B100 — IIa/IIb/IV — Clair/opalescent/lactescent — hypo<b>para</b>thyroïdie. Verrouille ces couples, les fabriques ①④⑤⑦⑧ sont désamorcées.',
    ],
    arbox('fa-chess-knight', 'كيف ينعكس هذا في تدريبك وامتحاناتك', [
        '<b>قسم «أسئلة الامتحانات»</b>: الأسئلة الخمسة عشر <b>الأصلية</b> بنصّ مجموعة ' + FP % 'ELITE' + ' و<b>تصحيحاتها الرسمية</b>، مشروحة اختياراً اختياراً مع اسم المصنع عند وجوده.',
        '<b>قسم «التدريب»</b>: 20 سؤالاً <b>جديداً</b> بنفس القالب — خمسة اقتراحات، صياغة موجبة (سلبي واحد كالأصل)، توزيع منسوخ: <b>7 بإجابة واحدة · 3 بإجابتين · 10 بثلاث</b>.',
        '<b>شفافية</b>: المجموعة تكتب مرتين «النمط ' + FP % 'VI' + '» — منقولاً كما هو مع المفتاح في التصحيح (إنه <b>النمط ' + FP % 'IV' + '</b>). وعتبة ' + FT % 'Friedewald' + ' الدقيقة غير موجودة في المصدر، فلن يجعلك أي تدريب تخمّن رقماً غائباً.',
        '<b>مادة المصائد</b>: 2 · 0,5–1,5 · 0,4/0,5 · 1,6 · 0,70 — ' + FP % 'B48/B100' + ' — ' + FP % 'IIa/IIb/IV' + ' — صافٍ/عَكِر/لبني — قصور <b>جارات</b> الدرقية. أَقفِل هذه الثنائيات تتعطّل المصانع ①④⑤⑦⑧.',
    ])) + '''
            </section>''')

# ═══════════════ CONNEXIONS ═══════════════
OUT.append('''            <!-- ═══════════════ CONNEXIONS ═══════════════ -->
            <section class="lsection" id="connexions">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-link"></i></div>
                    <div>
                        <h2>Connexions — ce cours ne vit pas seul</h2>
                        ''' + sub('cnx-sub',
                            'Le bilan lipidique est un <b>carrefour</b> : en amont, la technique du prélèvement ; en aval, la plaque d\'athérome et tout le risque cardiovasculaire que les leçons de cardiologie additionnent.',
                            'التحليل الدهني <b>ملتقى طرق</b>: قبله تقنية السحب، وبعده العصيدة وكل الخطر القلبي الوعائي الذي تجمعه دروس القلبية.') + '''
                    </div>
                </div>

''' + grid2(
    mini('cnx-mini1', 'red', 'fa-heart-pulse', 'AVEC « ATHÉROSCLÉROSE » (an-04)',
        [
            'Là-bas, la plaque se <b>décrit</b> (chape fibreuse, cœur lipidique) ; ici, on dose ce qui la <b>nourrit</b> : le LDL et les particules à ApoB',
            'Le macrophage spumeux de la plaque est le même que celui dont <b>ABCA1/ApoA1</b> extraient le cholestérol dans la section régulation',
            'Un même raisonnement en deux langues : l\'anatomopathologie montre la cible, la biochimie donne le chiffre à abaisser',
        ],
        armini('fa-heart-pulse', 'مع «تصلّب الشرايين» (an-04)', [
            'هناك تُوصف العصيدة (غطاء ليفي، قلب دهني)؛ وهنا نقيس ما <b>يغذّيها</b>: الـ' + FP % 'LDL' + ' وجسيمات ' + FP % 'ApoB' + '',
            'بلعمة العصيدة الرغوية هي نفسها التي يستخرج منها <b>' + FP % 'ABCA1/ApoA1' + '</b> الكولسترول في قسم التنظيم',
            'استدلال واحد بلغتين: التشريح المرضي يُري الهدف، والكيمياء الحيوية تعطي الرقم الواجب خفضه',
        ])),
    mini('cnx-mini2', 'blue', 'fa-stethoscope', 'AVEC LE RISQUE CARDIOVASCULAIRE GLOBAL (ca-04, ca-08)',
        [
            '« HDL &lt; 0,40 g/L » figure tel quel dans la liste des <b>FRCV</b> des annales de cardiologie — le même chiffre, deux modules',
            'Les risques se <b>multiplient</b> : dyslipidémie + HTA + tabac + diabète — c\'est ce produit qui fixe la cible de LDL (&lt; 0,70 au haut risque)',
            'Le cas n°1 (syndrome métabolique) est un patient de cardiologie avant d\'être un bilan de biochimie',
        ],
        armini('fa-stethoscope', 'مع الخطر القلبي الإجمالي (ca-04, ca-08)', [
            '«' + FP % 'HDL' + ' &lt; 0,40» وارد كما هو في قائمة <b>عوامل الخطر</b> بامتحانات القلبية — نفس الرقم في وحدتين',
            'الأخطار <b>تتضاعف ضرباً</b>: دهون + ضغط + تدخين + سكري — هذا الجداء هو ما يحدّد هدف ' + FP % 'LDL' + ' (&lt; 0,70 عند عالي الخطورة)',
            'الحالة رقم 1 (المتلازمة الاستقلابية) مريض قلبيات قبل أن يكون تحليل كيمياء',
        ]), delay='1')) + '''

''' + grid2(
    mini('cnx-mini3', 'teal', 'fa-vials', 'AVEC « ÉTAPES DE L\'ANALYSE » (bi-01, bi-02)',
        [
            'Le bilan lipidique est l\'exemple-école du <b>pré-analytique</b> : patient <b>à jeun</b>, sinon les chylomicrons faussent aspect et TG',
            'Juste avant ce chapitre, le recueil ELITE teste le <b>prélèvement sanguin</b> (hémolyse, ordre des tubes) — la même rigueur s\'applique ici',
            '« Valeur usuelle » contre « cible » : bi-01 pose les références du sujet sain, cette leçon y ajoute les <b>cibles selon le risque</b>',
        ],
        armini('fa-vials', 'مع «مراحل التحليل» (bi-01, bi-02)', [
            'التحليل الدهني هو المثال المدرسي لما <b>قبل التحليل</b>: مريض <b>صائم</b> وإلا حرّفت الـ' + FP % 'chylomicrons' + ' المظهر والـ' + FP % 'TG' + '',
            'قبل هذا الفصل مباشرة تختبر مجموعة ' + FP % 'ELITE' + ' <b>سحب الدم</b> (انحلال، ترتيب الأنابيب) — نفس الدقة تنطبق هنا',
            '«قيمة اعتيادية» ضد «هدف»: ' + FP % 'bi-01' + ' يضع مراجع الصحيح، وهذا الدرس يضيف <b>الأهداف حسب الخطر</b>',
        ])),
    mini('cnx-mini4', 'purple', 'fa-pills', 'AVEC LA PHARMACOLOGIE — EN AMONT DES TRAITEMENTS',
        [
            'Cette leçon dit <b>quoi mesurer et quelles cibles viser</b> ; les médicaments qui abaissent le LDL viendront en pharmacologie',
            'Deux notions d\'ici y seront centrales : le <b>récepteur LDL hépatique</b> (la serrure que les traitements rouvrent) et le <b>LDL comme paramètre de suivi</b>',
            'Attention au sens inverse dès maintenant : certains médicaments <b>créent</b> la dyslipidémie (section 13) — la pharmacologie commence dans l\'ordonnance du patient',
        ],
        armini('fa-pills', 'مع علم الأدوية — قبل العلاجات', [
            'هذا الدرس يقول <b>ماذا نقيس وما الأهداف</b>؛ أما أدوية خفض ' + FP % 'LDL' + ' فستأتي في علم الأدوية',
            'مفهومان من هنا سيكونان محورين هناك: <b>مستقبل ' + FP % 'LDL' + ' الكبدي</b> (القفل الذي تعيد العلاجات فتحه) و<b>' + FP % 'LDL' + ' مؤشرَ متابعة</b>',
            'انتبه من الآن للاتجاه المعاكس: بعض الأدوية <b>تُحدث</b> اضطراب الدهون (القسم 13) — علم الأدوية يبدأ في وصفة المريض',
        ]), delay='1')) + '''
            </section>''')

# ═══════════════ MOTEUR QCM ═══════════════
def qexp_inner(exp, memo, lang='fr'):
    if lang == 'fr':
        s = '<div class="qexp-title"><i class="fa-solid fa-lightbulb"></i> Proposition par proposition</div>'
        for i, (ok, fr, ar) in enumerate(exp):
            L = 'ABCDE'[i]; c = 't' if ok else 'f'; sym = '✓' if ok else '✗'; v = 'VRAI' if ok else 'FAUX'
            s += f'<div class="qexp-item {c}"><span class="xe {c}">{sym}</span><div><b>{L} — {v}.</b> {fr}</div></div>'
        s += f'<div class="qexp-memo"><i class="fa-solid fa-star"></i><div><b>Mémo :</b> {memo[0]}</div></div>'
    else:
        s = '<div class="qexp-title"><i class="fa-solid fa-lightbulb"></i> اقتراحاً باقتراح</div>'
        for i, (ok, fr, ar) in enumerate(exp):
            L = 'ABCDE'[i]; c = 't' if ok else 'f'; sym = '✓' if ok else '✗'; v = 'صحيح' if ok else 'خطأ'
            s += f'<div class="qexp-item {c}"><span class="xe {c}">{sym}</span><div><b><bdi class="fr-plain">{L}</bdi> — {v}.</b> {ar}</div></div>'
        s += f'<div class="qexp-memo"><i class="fa-solid fa-star"></i><div><b>للحفظ:</b> {memo[1]}</div></div>'
    return s

def qblock(n, qtext, src, choices, answers, key, exp, memo, annale=False):
    AR[key] = qexp_inner(exp, memo, 'ar')
    ans = json.dumps(answers)
    src_cls = 'src-annale' if annale else 'src-new'
    src_icon = 'fa-award' if annale else 'fa-bullseye'
    lis = '\n'.join(
        f'                        <li data-l="{"ABCDE"[i]}"><span class="ql">{"ABCDE"[i]}</span><span class="qtxt">{c}</span><span class="xe"></span></li>'
        for i, c in enumerate(choices))
    return f'''                <!-- {'A' if annale else 'E'}{n} -->
                <div class="qblock reveal" data-answer='{ans}'>
                    <div class="qhead">
                        <div class="qtext">{n}. {qtext}</div>
                        <span class="qsrc {src_cls}"><i class="fa-solid {src_icon}"></i> {src}</span>
                    </div>
                    <ul class="qch">
{lis}
                    </ul>
                    <div class="qverdict"></div>
                    <div class="qexp" data-tr="{key}">
                        {qexp_inner(exp, memo, 'fr')}
                    </div>
                    <div class="qcheck-row"><button class="btn btn-primary btn-sm qcheck"><i class="fa-solid fa-check"></i> Corriger ma réponse</button></div>
                </div>'''

# ═══════════════ LES 15 ANNALES (ELITE CARDIO 3ᵉ, Biochimie §3 — texte et corrigés officiels) ═══════════════
ANNALES = []
ANNALES.append(qblock(1, 'Parmi les pathologies suivantes, laquelle ne donne pas une hyperlipoprotéinémie secondaire :',
    'PROMO 2021',
    ['Le diabète de type 2.', "L'hypothyroïdie.", "L'hypoparathyroïdie.", 'Le syndrome néphrotique.', 'La cholestase.'],
    ['C'], 'a01-exp',
    [(False, 'Le diabète de type 2 est <b>la</b> cause secondaire métabolique de référence — donc pas la réponse à cette question négative.', 'السكري النمط 2 هو السبب الثانوي الاستقلابي المرجعي — إذن ليس إجابة هذا السؤال السلبي.'),
     (False, "L'<b>hypothyroïdie</b> est une cause secondaire classique, à chercher devant tout LDL élevé.", '<b>قصور الدرقية</b> سبب ثانوي كلاسيكي يُبحث عنه أمام كل ' + FP % 'LDL' + ' مرتفع.'),
     (True, "<i>Faux voisin lexical (①)</i> : hypo<b>para</b>thyroïdie ≠ hypothyroïdie. Les parathyroïdes règlent le calcium, pas les lipides — c'est l'intrus, et la question est négative.", '<i>جار لفظي زائف (①)</i>: قصور <b>جارات</b> الدرقية ≠ قصور الدرقية. جارات الدرقية تنظّم الكالسيوم لا الدهون — إنها الدخيلة، والسؤال سلبي.'),
     (False, 'Le syndrome néphrotique fait monter les lipoprotéines — cause secondaire rénale du cours.', 'المتلازمة الكلوية ترفع الـ' + FT % 'lipoprotéines' + ' — سبب ثانوي كلوي في الدرس.'),
     (False, 'La cholestase bloque la sortie biliaire du cholestérol : cause secondaire hépatique.', 'الركود الصفراوي يسدّ مخرج الكولسترول الصفراوي: سبب ثانوي كبدي.')],
    (' Quatre vraies causes + un « para » : le jour J, lis les mots <b>en entier</b>. Seule question négative du chapitre.',
     'أربعة أسباب حقيقية + «جارات» واحدة: يوم الامتحان اقرأ الكلمات <b>كاملة</b>. إنه السؤال السلبي الوحيد في الفصل.'), annale=True))

ANNALES.append(qblock(2, 'Les chylomicrons sont caractérisés par :',
    'PROMO 2021',
    ['Ils sont composés en majeure partie de triglycérides.', "Ils contiennent majoritairement de l'apo B100.", "Ils sont très mobiles à l'électrophorèse.", 'La concentration plasmatique est plus élevée en période postprandiale.', 'Ce sont les plus volumineuses des lipoprotéines plasmatiques.'],
    ['A', 'D', 'E'], 'a02-exp',
    [(True, '<b>99 % de lipides</b>, presque que des TG alimentaires — c\'est leur définition.', '<b>99 % دهون</b>، جلّها دهون غذائية — هذا تعريفها.'),
     (False, "<i>Paire antagoniste (⑧)</i> : l'intestin fabrique l'<b>ApoB48</b> ; B100 signe le foie.", '<i>زوج متقابل (⑧)</i>: الأمعاء تصنع <b>' + FP % 'ApoB48' + '</b>؛ و' + FP % 'B100' + ' توقيع الكبد.'),
     (False, "<i>Inversion (⑤)</i> : les plus grosses particules sont les <b>moins mobiles</b> à l'électrophorèse (notion d'annale, à confirmer sur le cours).", '<i>قلب (⑤)</i>: أكبر الجسيمات هي <b>الأقل حركية</b> في الرحلان (مفهوم امتحاني للتثبت من الدرس).'),
     (True, "Ils naissent des repas : marée <b>postprandiale</b>, disparus à jeun — d'où le prélèvement à jeun.", 'تولد من الوجبات: موجة <b>ما بعد الأكل</b> وتختفي صائماً — ومن هنا السحب صائماً.'),
     (True, '<b>100 nm – 1 µm</b> : les plus volumineuses, et donc les moins denses.', '<b>' + FP % '100 nm – 1 µm' + '</b>: الأضخم، وبالتالي الأقل كثافة.')],
    (' Chylomicron = <b>gros, gras, B48, après repas</b>. Tout le reste est permutation.',
     'الـ' + FP % 'chylomicron' + ' = <b>ضخم، دسم، B48، بعد الوجبة</b>. كل ما عداه تبديل.'), annale=True))

ANNALES.append(qblock(3, 'Concernant les lipoprotéines, quelles sont les propositions exactes ?',
    'PROMO 2021',
    ['Les VLDL sont les lipoprotéines les plus riches en protéines.', "L'hyperlipoprotéinémie de type III est caractérisée par la présence d'IDL.", "L'hyperlipoprotéinémie de type IIb correspond à une hyperlipidémie mixte.", 'Une concentration basse de HDL-cholestérol est un facteur de risque cardiovasculaire.', 'Le calcul du LDL-cholestérol par la formule de Friedewald est applicable pour une triglycéridémie à 5,0 g/L.'],
    ['B', 'C', 'D'], 'a03-exp',
    [(False, "<i>Inversion (⑤)</i> : 90 % de lipides pour les VLDL — les plus riches en protéines sont les <b>HDL</b>.", '<i>قلب (⑤)</i>: 90 % دهون للـ' + FP % 'VLDL' + ' — الأغنى بالبروتين هي <b>' + FP % 'HDL' + '</b>.'),
     (True, 'Type III = accumulation d\'<b>IDL</b> (restes de VLDL) : la définition même de la case.', 'النمط III = تراكم <b>' + FP % 'IDL' + '</b> (بقايا ' + FP % 'VLDL' + '): تعريف الخانة نفسه.'),
     (True, 'IIb = LDL <b>et</b> VLDL élevés : CT et TG montent ensemble = <b>mixte</b>.', 'النمط IIb = ارتفاع ' + FP % 'LDL' + ' <b>و</b>' + FP % 'VLDL' + ': الكلي والدهون يصعدان معاً = <b>مختلط</b>.'),
     (True, 'HDL bas = <b>facteur de risque</b> : moins de transport inverse, moins de protection.', 'انخفاض ' + FP % 'HDL' + ' = <b>عامل خطر</b>: نقل عكسي أقل، حماية أقل.'),
     (False, "<i>Ordre de grandeur (④)</i> : à <b>5,0 g/L</b> de TG, Friedewald est <b>invalide</b> (notion d'annale).", '<i>رتبة مقدار (④)</i>: عند <b>' + FP % '5,0 g/L' + '</b> من ' + FP % 'TG' + '، صيغة ' + FT % 'Friedewald' + ' <b>باطلة</b> (مفهوم امتحاني).')],
    (' Trois signatures propres : <b>III=IDL · IIb=mixte · HDL bas=risque</b>.',
     'ثلاثة توقيعات نظيفة: <b>III=IDL · IIb=مختلط · انخفاض HDL=خطر</b>.'), annale=True))

ANNALES.append(qblock(4, 'Parmi les examens suivants, quels sont ceux qui font partie du bilan lipidique de deuxième intention ?',
    'PROMO 2020',
    ['Le dosage du cholestérol total.', 'Le dosage des triglycérides.', "Le dosage de l'apoprotéine B.", "Le dosage de l'apoprotéine A1.", 'Lipidogramme.'],
    ['C', 'D', 'E'], 'a04-exp',
    [(False, "<i>Bon concept au mauvais endroit (②)</i> : le CT est le pilier de la <b>1ʳᵉ intention</b>.", '<i>مفهوم في مكان خاطئ (②)</i>: الكلي ركن <b>القصد الأول</b>.'),
     (False, 'Idem : les TG ouvrent le bilan, ils ne le précisent pas en 2ᵉ ligne.', 'كذلك: الـ' + FP % 'TG' + ' تفتح التحليل ولا تأتي في الصف الثاني.'),
     (True, "L'<b>ApoB</b> compte les particules athérogènes : outil de <b>2ᵉ intention</b>.", 'الـ<b>' + FP % 'ApoB' + '</b> تعدّ الجسيمات المصلِّبة: أداة <b>قصد ثانٍ</b>.'),
     (True, "L'<b>ApoA1</b>, reflet des HDL : 2ᵉ intention, symétrique de la précédente.", 'الـ<b>' + FP % 'ApoA1' + '</b> انعكاس ' + FP % 'HDL' + ': قصد ثانٍ، مرآة سابقتها.'),
     (True, "Le <b>lipidogramme</b> (électrophorèse) classe les fractions : 2ᵉ intention.", 'الـ<b>' + FT % 'lipidogramme' + '</b> (الرحلان) يصنّف الكسور: قصد ثانٍ.')],
    (' 2ᵉ intention = <b>ApoB + ApoA1 + lipidogramme</b>. CT/TG sont les gardiens de la 1ʳᵉ.',
     'القصد الثاني = <b>ApoB + ApoA1 + lipidogramme</b>. الكلي والدهون حارسا الأول.'), annale=True))

ANNALES.append(qblock(5, "Parmi les propositions suivantes concernant l'hyperlipidémie primitive de type IIa, indiquez laquelle (lesquelles) est (sont) exacte(s) :",
    'P 2022 / P 2020',
    ["L'aspect du sérum est lactescent.", 'Est une hypertriglycéridémie pure.', 'Est une hyperlipidémie familiale combinée.', 'Peut être due à une mutation du gène du récepteur de l\'apo B100.', 'Présente un faible pouvoir athérogène.'],
    ['D'], 'a05-exp',
    [(False, "<i>Aspect croisé (②)</i> : IIa = LDL sans TG élevés → sérum <b>non lactescent</b> (Clair).", '<i>مظهر متقاطع (②)</i>: IIa = ألدون دون دهون مرتفعة ← مصل <b>غير لبني</b> (صافٍ).'),
     (False, "<i>Signature permutée (⑧)</i> : IIa est une hyper<b>cholestérolémie</b> pure ; TG pure évoque I/IV.", '<i>توقيع مبدَّل (⑧)</i>: IIa فرط <b>كولسترول</b> صرف؛ أما الدهون الصرفة فتشير إلى I/IV.'),
     (False, "<i>Composite (⑨)</i> : « familiale combinée » est le visage du <b>IIb</b> (mixte), pas du IIa.", '<i>مركَّب (⑨)</i>: «العائلي المركّب» وجه <b>IIb</b> (المختلط) لا IIa.'),
     (True, 'La forme génétique du IIa touche le <b>récepteur de l\'ApoB (B/E)</b> : le foie ne capte plus le LDL.', 'الصورة الوراثية لـIIa تصيب <b>مستقبل ' + FP % 'ApoB (B/E)' + '</b>: الكبد لا يعود يلتقط ' + FP % 'LDL' + '.'),
     (False, "<i>Inversion (⑤)</i> : LDL pur en excès = pouvoir athérogène <b>fort</b>.", '<i>قلب (⑤)</i>: ' + FP % 'LDL' + ' صرف فائض = قدرة إصلاح <b>قوية</b>.')],
    (' IIa = <b>LDL pur, sérum clair, athérogène, parfois génétique</b> — quatre cadenas, une clé (D).',
     'IIa = <b>LDL صرف، مصل صافٍ، مصلِّب، وراثي أحياناً</b> — أربعة أقفال ومفتاح واحد (D).'), annale=True))

ANNALES.append(qblock(6, 'Le bilan lipidique de base comprend :',
    'P 2022 / P 2019',
    ['Le dosage du cholestérol total (CT).', 'Le dosage des triglycérides (TG).', 'Le calcul ou dosage direct du LDLc.', "Le dosage de l'apoprotéine B.", "Le dosage de l'apoprotéine A1."],
    ['A', 'B', 'C'], 'a06-exp',
    [(True, 'Le <b>CT</b> ouvre tout bilan lipidique.', 'الـ<b>الكلي</b> يفتح كل تحليل دهني.'),
     (True, 'Les <b>TG</b> : le deuxième pilier — et le perturbateur du sérum.', 'الـ<b>' + FP % 'TG' + '</b>: الركن الثاني — ومشوِّش المصل.'),
     (True, 'Le <b>LDLc</b>, calculé (Friedewald) ou dosé : c\'est la cible thérapeutique, donc dès la base.', 'الـ<b>' + FP % 'LDLc' + '</b> محسوباً أو مقاساً: إنه الهدف العلاجي، إذن منذ الأساس.'),
     (False, "<b>ApoB = 2ᵉ intention</b> (même piège qu'à l'annale n°4, en miroir).", '<b>' + FP % 'ApoB' + ' = قصد ثانٍ</b> (نفس فخ السؤال 4، مرآةً).'),
     (False, '<b>ApoA1 = 2ᵉ intention</b> également.', '<b>' + FP % 'ApoA1' + ' = قصد ثانٍ</b> أيضاً.')],
    (' Base d\'annale = <b>CT + TG + LDLc</b> ; le cours y ajoute aspect, HDL et non-HDL. Les Apo attendent la 2ᵉ ligne.',
     'أساس الامتحان = <b>كلي + TG + LDLc</b>؛ والدرس يضيف المظهر و' + FP % 'HDL' + ' و' + FP % 'non-HDL' + '. الـ' + FP % 'Apo' + ' تنتظر الصف الثاني.'), annale=True))

ANNALES.append(qblock(7, "L'hyperlipidémie primitive de type IIa :",
    'PROMO 2019',
    ['Est une hypercholestérolémie par augmentation des IDL.', 'Est une hypercholestérolémie pure par augmentation des LDL.', 'Est une hyperlipidémie familiale combinée.', "Peut être due à une mutation du gène du récepteur de l'Apo B/E.", 'Présente un faible pouvoir athérogène.'],
    ['B', 'D'], 'a07-exp',
    [(False, "IDL = case du <b>type III</b> <i>(②)</i>.", 'الـ' + FP % 'IDL' + ' خانة <b>النمط III</b> <i>(②)</i>.'),
     (True, 'La définition mot pour mot : <b>pure, par les LDL</b>.', 'التعريف حرفياً: <b>صرف، بالـ' + FP % 'LDL' + '</b>.'),
     (False, '« Combinée » = mixte = <b>IIb</b> <i>(⑨)</i>.', '«المركّب» = مختلط = <b>' + FP % 'IIb' + '</b> <i>(⑨)</i>.'),
     (True, 'Mutation du <b>récepteur ApoB/E</b> : la serrure génétique du IIa (déjà tombée à l\'annale n°5).', 'طفرة <b>مستقبل ' + FP % 'ApoB/E' + '</b>: قفل IIa الوراثي (سقطت في السؤال 5 أيضاً).'),
     (False, 'Pouvoir athérogène <b>fort</b>, jamais faible <i>(⑤)</i>.', 'قدرة إصلاح <b>قوية</b> لا ضعيفة أبداً <i>(⑤)</i>.')],
    (' Même dissection qu\'à l\'annale n°5 : l\'examinateur <b>recycle ses pièges</b> — la paire gagnante est B+D.',
     'نفس تشريح السؤال 5: الممتحن <b>يعيد تدوير مصائده</b> — الثنائي الفائز B+D.'), annale=True))

ANNALES.append(qblock(8, "Chez un patient atteint d'hyperlipidémie de type III, on observe :",
    'PROMO 2018',
    ['Une augmentation importante des chylomicrons par déficit en lipoprotéine lipase.', 'La présence de lipoprotéines de taille intermédiaire IDL.', 'Un phénotype E1/E1.', 'Une augmentation des triglycérides et du cholestérol total.', 'Un aspect limpide du sérum.'],
    ['B'], 'a08-exp',
    [(False, 'Déficit en LPL → chylomicrons = logique du <b>type I</b>, pas du III <i>(②)</i>.', 'نقص ' + FP % 'LPL' + ' ← ' + FP % 'chylomicrons' + ' = منطق <b>النمط I</b> لا III <i>(②)</i>.'),
     (True, "IDL = « <b>I</b>ntermediate Density » : la taille intermédiaire EST le type III.", 'الـ' + FP % 'IDL' + ' = «متوسطة الكثافة»: الحجم الوسيط هو النمط III بعينه.'),
     (False, 'Le phénotype classique associé est <b>E2/E2</b>, pas E1/E1 <i>(① faux voisin de lettre)</i>.', 'النمط الظاهري الكلاسيكي هو <b>' + FP % 'E2/E2' + '</b> لا ' + FP % 'E1/E1' + ' <i>(① جار حرفي)</i>.'),
     (False, '<b>FAUX au corrigé officiel</b> — alors que le tableau du cours montre CT et TG élevés dans le type III. Flottement du recueil : on retient la grille (B seul), en sachant la proposition <b>discutable</b>.', '<b>خطأ في التصحيح الرسمي</b> — بينما جدول الدرس يُظهر ارتفاع الكلي والدهون في النمط III. تذبذب في المجموعة: نحفظ الشبكة (B وحدها) مع علمنا أن الاقتراح <b>قابل للنقاش</b>.'),
     (False, 'Des restes riches en TG <b>troublent</b> le sérum — « limpide » est l\'inverse attendu <i>(⑤)</i>.', 'بقايا غنية بالدهون <b>تعكّر</b> المصل — «صافٍ» هو العكس المنتظر <i>(⑤)</i>.')],
    (' La seule réponse blindée : <b>III = IDL</b>. La D est un flottement signalé — en copie réelle, la grille officielle gagne.',
     'الإجابة المدرّعة الوحيدة: <b>III = IDL</b>. والـD تذبذب مُنبَّه إليه — في الامتحان الحقيقي تنتصر الشبكة الرسمية.'), annale=True))

ANNALES.append(qblock(9, 'Concernant les hyperlipoprotéinémies, quelles sont les propositions exactes ?',
    'PROMO 2018',
    ["L'hyperlipoprotéinémie de type IIb est une hypercholestérolémie pure.", 'Le calcul du LDL-cholestérol par la formule de Friedewald est applicable pour un taux de triglycéride à 4,38 g/L.', 'Les types IIa, IIb et III sont athérogènes.', 'Un taux de HDL-cholestérol à 0,20 g/L est un facteur de risque cardiovasculaire.', 'Le type VI est fréquemment associé au diabète sucré.'],
    ['C', 'D', 'E'], 'a09-exp',
    [(False, 'IIb est <b>mixte</b> (LDL + VLDL) — « pure » est la signature du IIa <i>(⑧)</i>.', 'النمط IIb <b>مختلط</b> (' + FP % 'LDL + VLDL' + ') — «الصرف» توقيع IIa <i>(⑧)</i>.'),
     (False, 'TG à <b>4,38 g/L</b> : Friedewald <b>invalide</b> — même piège qu\'à 5,0 <i>(④)</i>.', 'دهون عند <b>' + FP % '4,38' + '</b>: صيغة ' + FT % 'Friedewald' + ' <b>باطلة</b> — نفس فخ 5,0 <i>(④)</i>.'),
     (True, 'Le trio athérogène officiel : <b>IIa, IIb, III</b> — les accumulateurs d\'ApoB cholestérolées.', 'الثالوث المصلِّب الرسمي: <b>IIa، IIb، III</b> — مراكمات ' + FP % 'ApoB' + ' الكولسترولية.'),
     (True, 'HDL à 0,20 = très bas = <b>facteur de risque</b> (le seuil de danger est 0,40).', 'الـ' + FP % 'HDL' + ' عند 0,20 = منخفض جداً = <b>عامل خطر</b> (عتبة الخطر 0,40).'),
     (True, '<b>VRAI au corrigé</b> — mais lis « type <b>IV</b> » : le recueil écrit « VI » (coquille), et le IV (VLDL) est bien le compagnon du diabète.', '<b>صحيح في التصحيح</b> — لكن اقرأه «النمط <b>IV</b>»: المجموعة تكتب «VI» (زلّة)، والـIV (' + FP % 'VLDL' + ') هو رفيق السكري فعلاً.')],
    (' Le « VI » se lit « IV » : avec cette clé, C+D+E deviennent évidents.',
     'تُقرأ «VI» بأنها «IV»: بهذا المفتاح يصبح C+D+E بديهياً.'), annale=True))

ANNALES.append(qblock(10, "Concernant l'hypertriglycéridémie familiale type VI [lire : type IV] de Fredrickson, quelles sont les propositions exactes ?",
    'PROMO 2018',
    ['Augmentation de la synthèse hépatique des VLDL.', 'Le cholestérol total &gt; 6 g/L.', 'Les triglycérides sont augmentés.', 'Aspect du sérum opalescent.', "S'observe dans l'hyperthyroïdie."],
    ['A', 'C', 'D'], 'a10-exp',
    [(True, 'Type IV = le foie <b>surproduit des VLDL</b> : la mécanique même du type.', 'النمط IV = الكبد <b>يفرط في إنتاج ' + FP % 'VLDL' + '</b>: آلية النمط ذاتها.'),
     (False, "<i>Ordre de grandeur (④)</i> : le type IV est une affaire de <b>TG</b>, pas d'un CT délirant.", '<i>رتبة مقدار (④)</i>: النمط IV شأن <b>دهون ثلاثية</b> لا كولسترول كلي هذياني.'),
     (True, "L'énoncé le dit : hyper<b>triglycéridémie</b>.", 'النص يقوله: فرط <b>الدهون الثلاثية</b>.'),
     (True, 'VLDL en excès = sérum <b>opalescent</b> (le lactescent appartient aux chylomicrons).', 'فائض ' + FP % 'VLDL' + ' = مصل <b>عَكِر</b> (اللبني ملك ' + FP % 'chylomicrons' + ').'),
     (False, "C'est l'<b>hypo</b>thyroïdie qui élève les lipides <i>(⑧ paire thyroïdienne)</i>.", '<b>قصور</b> الدرقية هو من يرفع الدهون <i>(⑧ ثنائية درقية)</i>.')],
    (' « VI » = IV : <b>VLDL fabriquées en trop → TG ↑ → sérum opalescent</b>. La chaîne complète vaut trois coches.',
     '«VI» = IV: <b>VLDL مصنوعة زيادة ← دهون ↑ ← مصل عَكِر</b>. السلسلة الكاملة تساوي ثلاث تأشيرات.'), annale=True))

ANNALES.append(qblock(11, 'Parmi les facteurs de risque cardiovasculaire, on peut citer :',
    'RATTRAPAGE 2022',
    ["Un âge supérieur à 50 ans chez l'homme.", "Un âge inférieur à 50 ans chez la femme.", 'Une hypotension artérielle permanente.', 'Un HDLc &lt; 0,40 g/L.', 'Diabète de type 1.'],
    ['D'], 'a11-exp',
    [(False, '<b>Non retenu par la grille officielle</b> de ce rattrapage — l\'âge-seuil n\'est pas le repère attendu ici. On retient la grille du recueil.', '<b>غير محتفظ به في الشبكة الرسمية</b> لهذا الاستدراك — العمر العتبي ليس المعلم المنتظر هنا. نحفظ شبكة المجموعة.'),
     (False, "<i>Inversion (⑤)</i> : le risque monte <b>avec</b> l'âge, pas en dessous de 50 ans.", '<i>قلب (⑤)</i>: الخطر يصعد <b>مع</b> العمر لا دونه.'),
     (False, "L'<b>hyper</b>tension est le facteur — l'hypotension est son miroir <i>(⑧)</i>.", '<b>فرط</b> الضغط هو العامل — والانخفاض مرآته <i>(⑧)</i>.'),
     (True, 'Le chiffre du chapitre : <b>HDL &lt; 0,40 g/L = FRCV</b>, validé tel quel.', 'رقم الفصل: <b>' + FP % 'HDL &lt; 0,40' + ' = عامل خطر</b>، مصادق كما هو.'),
     (False, '<b>Non retenu par la grille</b> : dans ce chapitre, le diabète cité comme moteur lipidique est le <b>type 2</b> (syndrome métabolique). Retenir la grille officielle.', '<b>غير محتفظ به في الشبكة</b>: السكري المذكور محركاً دهنياً في هذا الفصل هو <b>النمط 2</b> (المتلازمة الاستقلابية). احفظ الشبكة الرسمية.')],
    (' Question-piège de rattrapage : une seule réponse blindée — le <b>HDL &lt; 0,40</b> de ton cours.',
     'سؤال فخ استدراكي: إجابة مدرّعة واحدة — <b>' + FP % 'HDL &lt; 0,40' + '</b> من درسك.'), annale=True))

ANNALES.append(qblock(12, "Concernant l'exploration d'une anomalie lipidique :",
    'RATTRAPAGE 2022',
    ['Recommandée chez les sujets jeunes.', 'Recommandée chez tous les adultes âgés de moins de 80 ans avec au moins un facteur de risque.', 'Si le bilan initial est anormal, il faut le répéter pour confirmation 2 à 4 semaines plus tard, sans régime ni médication.', "L'estimation du non-HDL-cholestérol (non-HDLc) fait partie du bilan de deuxième intention.", "Le non-HDLc est actuellement considéré plus indicatif que la fraction de LDL-cholestérol pour l'évaluation du risque de maladie cardiovasculaire."],
    ['B', 'C', 'E'], 'a12-exp',
    [(False, '« Sujets jeunes » sans seuil ni facteur : trop vague — le cours donne des <b>âges et des situations</b>.', '«شباب» دون عتبة ولا عامل: غامض جداً — الدرس يعطي <b>أعماراً وحالات</b>.'),
     (True, 'La porte d\'entrée validée : <b>&lt; 80 ans + au moins un facteur de risque</b>.', 'بوابة الدخول المصادقة: <b>&lt; 80 عاماً + عامل خطر واحد على الأقل</b>.'),
     (True, 'La règle de confirmation — <b>2 à 4 semaines</b>, terrain inchangé (notion d\'annale, à confirmer sur le cours).', 'قاعدة التأكيد — <b>2 إلى 4 أسابيع</b> دون تغيير الأرضية (مفهوم امتحاني للتثبت من الدرس).'),
     (False, 'Le non-HDLc appartient au bilan de <b>1ʳᵉ intention</b> du cours <i>(②)</i>.', 'الـ' + FP % 'non-HDLc' + ' من تحليل <b>القصد الأول</b> في الدرس <i>(②)</i>.'),
     (True, 'Corrigé <b>vrai</b> : le non-HDLc embrasse toutes les particules athérogènes — d\'où sa valeur pronostique.', 'مصحَّح <b>صحيحاً</b>: الـ' + FP % 'non-HDLc' + ' يحتضن كل الجسيمات المصلِّبة — ومن هنا قيمته التكهنية.')],
    (' La démarche en trois coches : <b>qui</b> (B), <b>confirmer</b> (C), <b>non-HDL</b> (E).',
     'المنهج في ثلاث تأشيرات: <b>من</b> (B)، <b>التأكيد</b> (C)، <b>non-HDL</b> (E).'), annale=True))

ANNALES.append(qblock(13, 'Un sérum lactescent :',
    'RATTRAPAGE 2022',
    ['Peut témoigner de la présence en excès des VLDL.', 'Peut témoigner de la présence en excès des chylomicrons.', "Peut témoigner d'une augmentation des LDL.", 'Nécessite de faire un test de crémage.', "Témoigne d'un bilan lipidique normal."],
    ['B', 'D'], 'a13-exp',
    [(False, '<b>Non retenu</b> : l\'excès isolé de VLDL donne un sérum <b>opalescent</b> ; le lactescent signe les chylomicrons.', '<b>غير محتفظ به</b>: فائض ' + FP % 'VLDL' + ' المنفرد يعطي مصلاً <b>عَكِراً</b>؛ اللبني يوقّع ' + FP % 'chylomicrons' + '.'),
     (True, '<b>Chylomicrons</b> : assez gros pour rendre le sérum laiteux.', 'الـ<b>' + FP % 'chylomicrons' + '</b>: كبيرة بما يكفي لجعل المصل لبنياً.'),
     (False, 'Le LDL, petit et sans TG, <b>ne trouble pas</b> le sérum <i>(②)</i>.', 'الـ' + FP % 'LDL' + ' صغير وبلا دهون، <b>لا يعكّر</b> المصل <i>(②)</i>.'),
     (True, 'Lactescent → <b>crémage 12 h à +4 °C</b> pour départager chylomicrons et VLDL.', 'لبني ← <b>تكرييم 12 ساعة في +4°</b> للفصل بين ' + FP % 'chylomicrons' + ' و' + FP % 'VLDL' + '.'),
     (False, 'Un sérum laiteux n\'a rien de normal <i>(⑥ négation déguisée)</i>.', 'المصل اللبني ليس طبيعياً إطلاقاً <i>(⑥ نفي متنكّر)</i>.')],
    (' Lactescent = <b>chylomicrons + crémage</b>. Opalescent = VLDL : ne mélange jamais les deux adjectifs.',
     'لبني = <b>chylomicrons + تكرييم</b>. عَكِر = ' + FP % 'VLDL' + ': لا تخلط النعتين أبداً.'), annale=True))

ANNALES.append(qblock(14, 'Une hypoHDLémie (diminution de la fraction HDLc) est suspectée devant :',
    'RATTRAPAGE 2022',
    ["Un taux inférieur à 0,6 g/L chez l'homme.", 'Un taux inférieur à 1 g/L quel que soit le sexe.', "Un taux inférieur à 0,4 g/L chez l'homme.", "Un taux supérieur à 0,5 g/L chez la femme.", "Un taux inférieur à 1,3 g/L chez l'homme."],
    ['C'], 'a14-exp',
    [(False, "<i>Chiffre déplacé (⑦)</i> : 0,6 est un seuil d'emprunt.", '<i>رقم مزاح (⑦)</i>: 0,6 عتبة مُعارة.'),
     (False, 'Pas de seuil « quel que soit le sexe » : les repères sont <b>sexués</b> (H 0,4 / F 0,5).', 'لا عتبة «أياً كان الجنس»: المعالم <b>جنسية</b> (رجل 0,4 / امرأة 0,5).'),
     (True, 'Le seuil du cours et des annales : <b>&lt; 0,4 g/L chez l\'homme</b>.', 'عتبة الدرس والامتحانات: <b>&lt; 0,4 عند الرجل</b>.'),
     (False, "<i>Inversion (⑤)</i> : au-dessus de 0,5 chez la femme, le HDL est du bon côté.", '<i>قلب (⑤)</i>: فوق 0,5 عند المرأة فالـ' + FP % 'HDL' + ' في الجانب الجيد.'),
     (False, '1,3 g/L : un HDL <b>élevé</b>, pas une hypoHDLémie <i>(④)</i>.', '1,3: ' + FP % 'HDL' + ' <b>مرتفع</b> لا ناقص <i>(④)</i>.')],
    (' Cinq seuils proposés, un seul vrai : la fabrique ⑦ à l\'état pur — <b>0,4 chez l\'homme</b>.',
     'خمس عتبات مقترحة وواحدة صحيحة: المصنع ⑦ بحالته النقية — <b>0,4 عند الرجل</b>.'), annale=True))

ANNALES.append(qblock(15, 'Le LDLc :',
    'RATTRAPAGE 2022',
    ['Il doit être inférieur à 1 g/L chez les patients sans facteurs de risque.', 'Représente le bon cholestérol.', 'Le risque cardiovasculaire augmente de façon exponentielle avec le taux de LDLc.', 'Il doit être inférieur à 0,70 g/L chez les patients à haut risque cardiovasculaire.', "Est le principal paramètre d'évaluation du suivi thérapeutique des patients."],
    ['C', 'D', 'E'], 'a15-exp',
    [(False, "<i>Chiffre déplacé (⑦)</i> : le repère usuel est <b>&lt; 1,6 g/L</b> ; le « 1 » n'est pas celui du cours.", '<i>رقم مزاح (⑦)</i>: المعلم الاعتيادي <b>&lt; 1,6</b>؛ والـ«1» ليس رقم الدرس.'),
     (False, 'Le « bon » cholestérol, c\'est le <b>HDL</b> — inversion classique <i>(⑤)</i>.', '«الجيّد» هو <b>' + FP % 'HDL' + '</b> — قلب كلاسيكي <i>(⑤)</i>.'),
     (True, 'Relation <b>exponentielle</b> risque ↔ LDLc : d\'où l\'obsession des cibles.', 'علاقة <b>أسية</b> خطر ↔ ' + FP % 'LDLc' + ': ومن هنا هوس الأهداف.'),
     (True, 'La cible gravée : <b>&lt; 0,70 g/L au haut risque</b>.', 'الهدف المنقوش: <b>&lt; 0,70 عند عالي الخطورة</b>.'),
     (True, 'Le LDLc est <b>le paramètre du suivi</b> — on ajuste le traitement sur lui.', 'الـ' + FP % 'LDLc' + ' هو <b>مؤشر المتابعة</b> — تُضبط المعالجة عليه.')],
    (' Le portrait du LDL en trois vraies phrases : <b>risque exponentiel · cible 0,70 · suivi</b>.',
     'بورتريه ' + FP % 'LDL' + ' في ثلاث جمل صحيحة: <b>خطر أسي · هدف 0,70 · متابعة</b>.'), annale=True))

# ═══════════════ 20 QCM D'ENTRAÎNEMENT (neufs, moule mesuré : 7×1 · 3×2 · 10×3) ═══════════════
ENTR = []
E = ENTRAINEMENT_SRC = 'Entraînement'
ENTR.append(qblock(1, 'Concernant les rôles des lipides :', E,
    ['Les triglycérides sont le composant structural principal des membranes cellulaires.', "Les triglycérides constituent la réserve énergétique stockée dans le tissu adipeux.", "Le cholestérol ne joue aucun rôle dans les membranes.", "La dyslipidémie n'est pas un facteur de risque cardiovasculaire.", 'Les lipides, hydrosolubles, circulent librement dans le plasma.'],
    ['B'], 'q01-exp',
    [(False, "<i>Bon concept au mauvais endroit (②)</i> : le structural appartient aux <b>phospholipides et au cholestérol</b>.", '<i>مفهوم في مكان خاطئ (②)</i>: البنيوي يخص <b>الفوسفوليبيدات والكولسترول</b>.'),
     (True, "Rôle <b>énergétique</b> : réserve d'énergie, mobilisable par β-oxydation.", 'دور <b>طاقي</b>: مخزون طاقة قابل للتعبئة بالأكسدة بيتا.'),
     (False, 'Le cholestérol est un constituant <b>des membranes</b>.', 'الكولسترول مكوّن <b>للأغشية</b>.'),
     (False, "<i>Négation plaquée (⑥)</i> : la dyslipidémie est un FRCV <b>majeur</b>.", '<i>نفي ملصق (⑥)</i>: اضطراب الدهون عامل خطر <b>رئيسي</b>.'),
     (False, "Les lipides sont <b>hydrophobes</b> — c'est pour cela qu'il existe des lipoprotéines.", 'الدهون <b>كارهة للماء</b> — ولهذا وُجدت الـ' + FT % 'lipoprotéines' + '.')],
    (' Un rôle par molécule : <b>TG = énergie</b>, phospholipides/cholestérol = membranes.',
     'دور لكل جزيء: <b>TG = طاقة</b>، فوسفوليبيدات/كولسترول = أغشية.')))
ENTR.append(qblock(2, "L'absorption intestinale des lipides :", E,
    ["Les acides gras libres font partie des produits absorbés.", 'Les triglycérides traversent tels quels la muqueuse intestinale.', 'Les monoglycérides font partie des produits absorbés.', "Les chylomicrons rejoignent le foie par la veine porte.", "L'entérocyte ré-estérifie les lipides absorbés avant de les emballer en chylomicrons."],
    ['A', 'C', 'E'], 'q02-exp',
    [(True, 'Produit de l\'hydrolyse luminale — absorbé.', 'نتاج التحلّل اللمعي — يُمتصّ.'),
     (False, 'Jamais entier : <b>démonté puis remonté</b>.', 'أبداً كاملاً: <b>يُفكَّك ثم يُركَّب</b>.'),
     (True, 'La moitié d\'un TG, absorbée elle aussi.', 'نصف ' + FP % 'TG' + '، يُمتصّ أيضاً.'),
     (False, 'Ils prennent la <b>lymphe</b> (chylifères → canal thoracique).', 'يسلكون <b>اللمف</b> (الأوعية اللبنية ← القناة الصدرية).'),
     (True, 'Ré-estérification puis emballage : le travail de l\'entérocyte.', 'إعادة أسترة ثم تغليف: عمل الخلية المعوية.')],
    (' Démonter → absorber les <b>pièces</b> → remballer → <b>lymphe</b>.',
     'فكّك ← امتصّ <b>القطع</b> ← أعد التغليف ← <b>اللمف</b>.')))
ENTR.append(qblock(3, 'La voie exogène du transport des lipides :', E,
    ['Part du foie via les VLDL.', "Part de l'intestin via les chylomicrons.", 'Est assurée par les HDL.', 'Ramène le cholestérol des tissus vers le foie.', 'Se termine par la production de LDL.'],
    ['B'], 'q03-exp',
    [(False, 'Foie + VLDL = voie <b>endogène</b>.', 'كبد + ' + FP % 'VLDL' + ' = المسار <b>الداخلي</b>.'),
     (True, 'Exogène = qui vient du dehors (l\'assiette) : <b>intestin → chylomicrons</b>.', 'خارجي = آتٍ من الخارج (الصحن): <b>أمعاء ← ' + FP % 'chylomicrons' + '</b>.'),
     (False, 'Les HDL font le <b>transport inverse</b>.', 'الـ' + FP % 'HDL' + ' تقوم بـ<b>النقل العكسي</b>.'),
     (False, 'Le retour au foie appartient aux HDL, pas à la voie exogène.', 'العودة إلى الكبد تخص ' + FP % 'HDL' + ' لا المسار الخارجي.'),
     (False, 'La production de LDL clôt la voie <b>endogène</b> ; l\'exogène finit en <b>restes</b> captés par le foie.', 'إنتاج ' + FP % 'LDL' + ' يختم المسار <b>الداخلي</b>؛ والخارجي ينتهي بـ<b>بقايا</b> يلتقطها الكبد.')],
    (' Exo = intestin · Endo = foie · Inverse = HDL : trois points de départ, zéro confusion.',
     'خارجي = أمعاء · داخلي = كبد · عكسي = ' + FP % 'HDL' + ': ثلاث بدايات، صفر خلط.')))
ENTR.append(qblock(4, 'Concernant les familles de lipoprotéines :', E,
    ["L'ApoB48 est la marque des chylomicrons.", 'Les VLDL transportent les triglycérides fabriqués par le foie.', 'Les LDL assurent le transport inverse du cholestérol.', "L'ApoA est la marque des HDL.", 'Les IDL sont le produit final de la voie exogène.'],
    ['A', 'B', 'D'], 'q04-exp',
    [(True, 'B48 = carte d\'identité <b>intestinale</b>.', FP % 'B48' + ' = بطاقة هوية <b>معوية</b>.'),
     (True, 'TG <b>endogènes</b> : la cargaison des VLDL.', 'دهون <b>داخلية</b>: حمولة ' + FP % 'VLDL' + '.'),
     (False, 'Le transport inverse est le travail des <b>HDL</b> — le LDL livre <i>(⑤)</i>.', 'النقل العكسي عمل <b>' + FP % 'HDL' + '</b> — والـ' + FP % 'LDL' + ' يسلّم <i>(⑤)</i>.'),
     (True, 'ApoA = signature des HDL.', FP % 'ApoA' + ' = توقيع ' + FP % 'HDL' + '.'),
     (False, 'IDL = étape de la voie <b>endogène</b> ; l\'exogène finit en restes de chylomicrons.', 'الـ' + FP % 'IDL' + ' مرحلة المسار <b>الداخلي</b>؛ والخارجي ينتهي ببقايا ' + FP % 'chylomicrons' + '.')],
    (' B48 intestin · B100 foie/LDL · ApoA HDL : les plaques d\'immatriculation de la flotte.',
     'B48 أمعاء · B100 كبد/LDL · ApoA لــHDL: لوحات ترقيم الأسطول.')))
ENTR.append(qblock(5, 'Le tableau des caractéristiques des lipoprotéines :', E,
    ['Les chylomicrons contiennent environ 99 % de lipides.', 'Les HDL mesurent environ 10 nm.', 'Les LDL mesurent environ 50 nm et contiennent 90 % de lipides.', "Les VLDL portent l'ApoB100.", 'Plus une lipoprotéine est grosse, plus elle est dense.'],
    ['A', 'B', 'D'], 'q05-exp',
    [(True, '99 % : le ballon de graisse quasi pur.', '99 %: بالون الشحم شبه الصافي.'),
     (True, '10 nm : la plus petite (et la plus dense).', '10 نانومتر: الأصغر (والأكثف).'),
     (False, "<i>Chiffres de la mauvaise ligne (⑦)</i> : 50 nm / 90 % = <b>VLDL</b> ; LDL = 20 nm / 80 %.", '<i>أرقام السطر الخاطئ (⑦)</i>: 50/90 % = <b>' + FP % 'VLDL' + '</b>؛ والـ' + FP % 'LDL' + ' = 20/80 %.'),
     (True, 'B100 : fabriquée par le foie, comme la VLDL.', FP % 'B100' + ': يصنعها الكبد كالـ' + FP % 'VLDL' + '.'),
     (False, 'C\'est l\'inverse : gros = léger = <b>moins dense</b> <i>(⑤)</i>.', 'العكس: ضخم = خفيف = <b>أقل كثافة</b> <i>(⑤)</i>.')],
    (' 99/98... non : <b>99 · 90 · 80 · 50–70</b> en descendant de taille, densité en grimpant.',
     '<b>99 · 90 · 80 · 50–70</b> نزولاً في الحجم، صعوداً في الكثافة.')))
ENTR.append(qblock(6, 'La destinée des lipides dans les tissus :', E,
    ['La β-oxydation des acides gras produit de l\'énergie.', 'Les triglycérides en excès sont stockés dans les adipocytes.', 'Le cholestérol s\'élimine principalement par le rein.', 'La β-oxydation est la voie de stockage des acides gras.', "Les triglycérides n'ont aucun rôle énergétique."],
    ['A', 'B'], 'q06-exp',
    [(True, 'La chaudière mitochondriale.', 'مرجل المتقدّرات.'),
     (True, 'La réserve : tissu adipeux.', 'المخزون: النسيج الشحمي.'),
     (False, "La sortie du cholestérol est <b>biliaire</b>, via le foie.", 'مخرج الكولسترول <b>صفراوي</b> عبر الكبد.'),
     (False, 'La β-oxydation <b>brûle</b> — elle ne stocke pas <i>(⑤)</i>.', 'الأكسدة بيتا <b>تحرق</b> — لا تخزّن <i>(⑤)</i>.'),
     (False, 'C\'est leur rôle premier <i>(⑥)</i>.', 'إنه دورها الأول <i>(⑥)</i>.')],
    (' Stocker (adipocyte) ou brûler (β-oxydation) — et le cholestérol sort par la bile.',
     'خزّن (شحمية) أو احرق (أكسدة بيتا) — والكولسترول يخرج بالصفراء.')))
ENTR.append(qblock(7, 'La lipoprotéine lipase (LPL) :', E,
    ['Estérifie le cholestérol à la surface des HDL.', 'Échange les esters de cholestérol entre les particules.', 'Hydrolyse les triglycérides des chylomicrons et des VLDL au contact des tissus.', 'Capte les LDL au niveau du foie.', 'Fait sortir le cholestérol des macrophages vers les HDL.'],
    ['C'], 'q07-exp',
    [(False, "C'est la <b>LCAT</b> <i>(⑧)</i>.", 'تلك <b>' + FP % 'LCAT' + '</b> <i>(⑧)</i>.'),
     (False, "C'est la <b>CETP</b> <i>(⑧)</i>.", 'تلك <b>' + FP % 'CETP' + '</b> <i>(⑧)</i>.'),
     (True, 'La LPL « décharge les camions » : TG → acides gras pour muscle et tissu adipeux.', 'الـ' + FP % 'LPL' + ' «تفرّغ الشاحنات»: دهون ← أحماض دهنية للعضلات والشحم.'),
     (False, "C'est le <b>récepteur LDL</b> hépatique.", 'ذلك <b>مستقبل ' + FP % 'LDL' + '</b> الكبدي.'),
     (False, "C'est le couple <b>ABCA1/ApoA1</b>.", 'ذلك الثنائي <b>' + FP % 'ABCA1/ApoA1' + '</b>.')],
    (' Cinq aiguilleurs, cinq métiers : ne permute jamais les casquettes.',
     'خمسة موجّهين، خمس مهن: لا تبدّل القبعات أبداً.')))
ENTR.append(qblock(8, "L'exploration d'une anomalie lipidique est indiquée :", E,
    ["Chez l'homme dès 40 ans.", 'Chez la femme dès 50 ans.', "Chez l'enfant en cas d'antécédents familiaux de maladie cardiovasculaire précoce.", 'Chez tous les sujets jeunes, sans condition.', 'Jamais avant 40 ans, même avec des facteurs de risque.'],
    ['A', 'B', 'C'], 'q08-exp',
    [(True, "L'âge-seuil masculin du cours.", 'العمر العتبي الذكوري في الدرس.'),
     (True, "L'âge-seuil féminin — dix ans plus tard.", 'العمر العتبي الأنثوي — بعد عشر سنوات.'),
     (True, 'La porte des formes familiales (cas n°2 du cours).', 'بوابة الصور العائلية (حالة الدرس 2).'),
     (False, 'Sans âge-seuil ni facteur, c\'est exactement la proposition rejetée à l\'annale n°12.', 'دون عتبة ولا عامل، إنه بالضبط الاقتراح المرفوض في سؤال 12.'),
     (False, 'Les facteurs de risque <b>avancent</b> l\'horloge <i>(⑥)</i>.', 'عوامل الخطر <b>تقدّم</b> الساعة <i>(⑥)</i>.')],
    (' 40 (homme) · 50 (femme) · enfant ciblé familial — et les facteurs avancent tout.',
     '40 (رجل) · 50 (امرأة) · طفل عائلي مستهدف — والعوامل تقدّم كل شيء.')))
ENTR.append(qblock(9, 'Le bilan lipidique de 1ʳᵉ intention :', E,
    ["Comprend l'aspect du sérum.", 'Se prélève chez un patient à jeun.', "Comprend le dosage de l'ApoB.", 'Comprend le non-HDL selon le cours.', 'Un sérum clair permet d\'exclure un LDL élevé.'],
    ['A', 'B', 'D'], 'q09-exp',
    [(True, "L'œil avant l'analyseur.", 'العين قبل جهاز التحليل.'),
     (True, 'À jeun, sinon la marée de chylomicrons fausse TG et aspect.', 'صائماً، وإلا حرّفت موجة ' + FP % 'chylomicrons' + ' الدهون والمظهر.'),
     (False, 'ApoB = <b>2ᵉ intention</b>, deux annales le verrouillent.', 'الـ' + FP % 'ApoB' + ' = <b>قصد ثانٍ</b>، سؤالان يقفلانه.'),
     (True, 'Le cours range le non-HDL dès la 1ʳᵉ intention (annale n°12 le confirme en creux).', 'الدرس يضع ' + FP % 'non-HDL' + ' منذ القصد الأول (ويؤكده سؤال 12 ضمنياً).'),
     (False, 'Le LDL ne trouble pas : un sérum <b>Clair peut cacher un LDL très élevé</b> (c\'est le IIa).', 'الـ' + FP % 'LDL' + ' لا يعكّر: مصل <b>صافٍ قد يخفي LDL مرتفعاً جداً</b> (إنه IIa).')],
    (' Aspect + jeûne + non-HDL dès la 1ʳᵉ — et « clair » ne veut jamais dire « rassuré ».',
     'مظهر + صيام + non-HDL منذ الأولى — و«صافٍ» لا يعني أبداً «مطمئناً».')))
ENTR.append(qblock(10, 'Au test de crémage (12 h à +4 °C), une couche crémeuse surnageante sur un culot clair traduit :', E,
    ['Un excès isolé de VLDL.', 'Un excès de chylomicrons seuls.', 'Un excès de LDL.', 'Un excès de HDL.', 'Un excès associé de chylomicrons et de VLDL.'],
    ['B'], 'q10-exp',
    [(False, 'VLDL seules : <b>pas de crème</b>, sérum opalescent homogène.', FP % 'VLDL' + ' وحدها: <b>لا قشدة</b>، مصل عَكِر متجانس.'),
     (True, 'Les moins denses surnagent : crème = chylomicrons ; culot clair = plus rien en dessous.', 'الأقل كثافة تطفو: القشدة = ' + FP % 'chylomicrons' + '؛ القاع الصافي = لا شيء تحتها.'),
     (False, 'Le LDL ne participe pas au crémage.', 'الـ' + FP % 'LDL' + ' لا يشارك في التكرييم'),
     (False, 'Idem pour les HDL, les plus denses de toutes.', 'كذلك ' + FP % 'HDL' + '، الأكثر كثافة.'),
     (False, 'Les deux donneraient un culot <b>trouble</b> <i>(⑧)</i>.', 'الاثنان معاً = قاع <b>عَكِر</b> <i>(⑧)</i>.')],
    (' Crème + clair = chylo · pas de crème + opalescent = VLDL · crème + trouble = les deux.',
     'قشدة + صافٍ = كيلوميكرونات · لا قشدة + عَكِر = VLDL · قشدة + عَكِر = الاثنان.')))
ENTR.append(qblock(11, 'Les valeurs usuelles du bilan lipidique :', E,
    ['Cholestérol total inférieur à 2 g/L.', 'Triglycérides entre 0,5 et 1,5 g/L.', "HDL : 0,4 g/L chez la femme et 0,5 g/L chez l'homme.", 'LDL inférieur à 1,6 g/L.', 'Un HDL inférieur à 0,40 g/L est protecteur.'],
    ['A', 'B', 'D'], 'q11-exp',
    [(True, 'La borne « 2 » (5,2 mmol/L).', 'حدّ «2» (5,2 mmol/L).'),
     (True, 'La fourchette des TG.', 'مجال الدهون الثلاثية.'),
     (False, 'Permutés ! <b>Homme 0,4 · Femme 0,5</b> <i>(⑧)</i>.', 'مقلوبان! <b>رجل 0,4 · امرأة 0,5</b> <i>(⑧)</i>.'),
     (True, 'La valeur usuelle du LDL (la cible 0,70 est pour le haut risque).', 'القيمة الاعتيادية للـ' + FP % 'LDL' + ' (هدف 0,70 لعالي الخطورة).'),
     (False, 'Sous 0,40 = <b>facteur de risque</b>, jamais protection <i>(⑤)</i>.', 'تحت 0,40 = <b>عامل خطر</b> لا حماية أبداً <i>(⑤)</i>.')],
    (' 2 · 0,5–1,5 · H0,4/F0,5 · 1,6 : récite-les à voix haute avant d\'entrer.',
     '2 · 0,5–1,5 · رجل0,4/امرأة0,5 · 1,6: رتّلها بصوت عالٍ قبل الدخول.')))
ENTR.append(qblock(12, 'Concernant le LDL-cholestérol :', E,
    ['Il doit être inférieur à 0,70 g/L chez les patients à haut risque cardiovasculaire.', "C'est le principal paramètre du suivi thérapeutique.", 'Il doit être inférieur à 1 g/L chez les patients sans facteur de risque, selon le cours.', 'Le risque cardiovasculaire diminue quand le LDLc augmente.', 'Il représente le « bon cholestérol ».'],
    ['A', 'B'], 'q12-exp',
    [(True, "La cible du haut risque (annale n°15).", 'هدف عالي الخطورة (سؤال 15).'),
     (True, 'On traite et on suit sur le LDLc (annale n°15).', 'نعالج ونتابع على ' + FP % 'LDLc' + ' (سؤال 15).'),
     (False, "L'annale n°15 corrige ce « 1 g/L » en <b>faux</b>.", 'سؤال 15 يصحّح هذا الـ«1» <b>خطأ</b>.'),
     (False, 'La relation est <b>directe et exponentielle</b> <i>(⑤)</i>.', 'العلاقة <b>مباشرة وأسية</b> <i>(⑤)</i>.'),
     (False, 'Le « bon » est le <b>HDL</b>.', '«الجيّد» هو <b>' + FP % 'HDL' + '</b>.')],
    (' Question-miroir de l\'annale n°15 : si tu hésites ici, refais l\'annale.',
     'سؤال مرآة لسؤال 15: إن تردّدت هنا أعِد حله.')))
ENTR.append(qblock(13, 'Font partie du bilan de 2ᵉ intention :', E,
    ["Le dosage de l'ApoB.", 'Le lipidogramme (électrophorèse des lipoprotéines).', 'Le dosage du cholestérol total.', 'Le dosage de la Lp(a), facteur génétiquement déterminé.', 'La formule de Friedewald, applicable quel que soit le taux de triglycérides.'],
    ['A', 'B', 'D'], 'q13-exp',
    [(True, "Compter les particules athérogènes.", 'عدّ الجسيمات المصلِّبة.'),
     (True, 'Séparer les fractions — l\'outil historique de Fredrickson.', 'فصل الكسور — أداة ' + FT % 'Fredrickson' + ' التاريخية.'),
     (False, 'Le CT est la première pierre de la <b>1ʳᵉ intention</b>.', 'الكلي أول حجر في <b>القصد الأول</b>.'),
     (True, 'Lp(a) : risque indépendant, hérité.', FP % 'Lp(a)' + ': خطر مستقل موروث.'),
     (False, '« Quel que soit » = le piège : Friedewald <b>décroche</b> quand les TG sont très élevés.', '«مهما يكن» = الفخ: ' + FT % 'Friedewald' + ' <b>تنهار</b> عند ارتفاع ' + FP % 'TG' + ' الشديد.')],
    (' 2ᵉ intention = compter (ApoB), séparer (lipidogramme), hériter (Lp(a)).',
     'القصد الثاني = عَدّ (ApoB)، فصل (lipidogramme)، وراثة (Lp(a)).')))
ENTR.append(qblock(14, "L'apolipoprotéine B (ApoB) :", E,
    ['Reflète la fraction HDL protectrice.', 'Permet de compter les particules athérogènes, chaque particule en portant une seule.', 'Fait partie du bilan lipidique de base des annales.', "Est l'autre nom de l'ApoA1.", "N'est dosée que chez l'enfant."],
    ['B'], 'q14-exp',
    [(False, "Le reflet des HDL, c'est l'<b>ApoA1</b> <i>(⑧)</i>.", 'انعكاس ' + FP % 'HDL' + ' هو <b>' + FP % 'ApoA1' + '</b> <i>(⑧)</i>.'),
     (True, '1 particule = 1 ApoB : le dosage devient un <b>comptage</b>.', 'جسيم واحد = ApoB واحدة: القياس يصبح <b>عدّاً</b>.'),
     (False, 'Les annales n°4 et n°6 la rangent en <b>2ᵉ intention</b>.', 'سؤالا 4 و6 يضعانها في <b>القصد الثاني</b>.'),
     (False, 'ApoB et ApoA1 sont les deux camps <b>opposés</b> (leur rapport évalue le risque).', 'الـ' + FP % 'ApoB' + ' والـ' + FP % 'ApoA1' + ' معسكران <b>متعاكسان</b> (نسبتهما تقيّم الخطر).'),
     (False, 'Rien ne la réserve à l\'enfant <i>(⑥ invention)</i>.', 'لا شيء يحصرها في الطفل <i>(⑥ اختراع)</i>.')],
    (' ApoB = le nombre de camions ennemis ; ApoA1 = celui des camions de retour.',
     'الـApoB = عدد شاحنات العدو؛ والـApoA1 = عدد شاحنات العودة.')))
ENTR.append(qblock(15, 'Selon les fréquences du cours (classification de Fredrickson) :', E,
    ['Le type IIb représente environ 40 % des cas.', 'Le type IV représente environ 10 % des cas.', 'Le type I est le plus fréquent des types.', 'Le type III représente environ 40 % des cas.', 'Le type V est le plus fréquent des types.'],
    ['A'], 'q15-exp',
    [(True, 'IIb = 40 % (le mixte).', FP % 'IIb' + ' = 40 % (المختلط).'),
     (False, 'IV = <b>45 %</b>, le plus fréquent de tous <i>(⑦)</i>.', FP % 'IV' + ' = <b>45 %</b>، الأكثر شيوعاً <i>(⑦)</i>.'),
     (False, 'Type I : très rare (&lt; 1 %).', 'النمط I: نادر جداً (&lt; 1 %).'),
     (False, 'III : très rare aussi (&lt; 1 %).', 'النمط III: نادر جداً أيضاً (&lt; 1 %).'),
     (False, 'Ni le V — le podium est IV (45 %) puis IIb (40 %).', 'ولا الـV — المنصة لـIV ‏(45 %) ثم IIb ‏(40 %).')],
    (' <b>IV 45 % + IIb 40 % = 85 %</b> du réel ; I et III sont des raretés.',
     '<b>IV ‏45 % + IIb ‏40 % = 85 %</b> من الواقع؛ وI وIII نوادر.')))
ENTR.append(qblock(16, 'Les types de Fredrickson :', E,
    ['Le type IIa est une hypercholestérolémie pure par augmentation des LDL.', 'Le type IIa donne un sérum lactescent.', 'Le type IIb associe une élévation des LDL et des VLDL.', 'Le type IV, par excès de VLDL, donne un sérum opalescent.', 'Le type III est dû à une accumulation de chylomicrons.'],
    ['A', 'C', 'D'], 'q16-exp',
    [(True, 'La définition du IIa.', 'تعريف IIa.'),
     (False, 'Sans TG élevés, le sérum du IIa reste <b>Clair</b>.', 'دون دهون مرتفعة يبقى مصل IIa <b>صافياً</b>.'),
     (True, 'IIb = les deux élévations, le mixte.', 'النمط IIb = الارتفاعان معاً، المختلط.'),
     (True, 'VLDL → opalescent : la signature du IV.', FP % 'VLDL' + ' ← عَكِر: توقيع IV.'),
     (False, 'III = <b>IDL</b> ; les chylomicrons signent I (et V) <i>(②)</i>.', 'النمط III = <b>' + FP % 'IDL' + '</b>؛ والـ' + FP % 'chylomicrons' + ' توقّع I (وV) <i>(②)</i>.')],
    (' IIa pur-clair · IIb mixte · IV opalescent : la paire type↔sérum est indissociable.',
     'IIa صرف-صافٍ · IIb مختلط · IV عَكِر: ثنائية النمط↔المصل لا تنفصم.')))
ENTR.append(qblock(17, 'Toutes ces situations peuvent donner une hyperlipoprotéinémie secondaire, SAUF une :', E,
    ['Le diabète de type 2.', "L'hypothyroïdie.", "L'hypoparathyroïdie.", 'Le syndrome néphrotique.', 'La cholestase.'],
    ['C'], 'q17-exp',
    [(False, 'Cause vraie — donc pas le SAUF.', 'سبب حقيقي — إذن ليس المستثنى.'),
     (False, 'Cause vraie et classique.', 'سبب حقيقي وكلاسيكي.'),
     (True, 'Le « para » de l\'annale n°1 — ici entraîné en version SAUF <i>(①)</i>.', '«جارات» سؤال 1 — مدروسة هنا بصيغة «عدا» <i>(①)</i>.'),
     (False, 'Cause rénale vraie.', 'سبب كلوي حقيقي.'),
     (False, 'Cause hépatique vraie.', 'سبب كبدي حقيقي.')],
    (' La seule question négative de l\'entraînement — comme dans les annales. Lis l\'énoncé <b>jusqu\'au SAUF</b>.',
     'السؤال السلبي الوحيد في التدريب — كالامتحانات. اقرأ النص <b>حتى «عدا»</b>.')))
ENTR.append(qblock(18, 'Parmi les causes secondaires de dyslipidémie, les médicaments en cause comprennent :', E,
    ['Les corticoïdes.', 'Les diurétiques thiazidiques.', 'Les β-bloquants.', "Aucun médicament ne modifie le bilan lipidique.", "L'hyperthyroïdie est la cause endocrine classique."],
    ['A', 'B', 'C'], 'q18-exp',
    [(True, 'Les corticoïdes désorganisent lipides et glycémie.', 'الكورتيكويدات تخلّ بالدهون والسكر.'),
     (True, 'Thiazidiques : sur la liste du cours.', 'الثيازيدات: في قائمة الدرس.'),
     (True, 'β-bloquants : également listés.', 'حاصرات بيتا: مدرجة أيضاً.'),
     (False, "C'est exactement ce que la section 13 interdit de dire <i>(⑥)</i>.", 'هذا بالضبط ما يمنعه القسم 13 <i>(⑥)</i>.'),
     (False, "C'est l'<b>hypo</b>thyroïdie, sa sœur inversée <i>(⑧)</i>.", 'إنه <b>قصور</b> الدرقية، أختها المقلوبة <i>(⑧)</i>.')],
    (' Relire l\'ordonnance fait partie du bilan : corticoïdes · thiazidiques · β-bloquants · œstrogènes · ARV.',
     'إعادة قراءة الوصفة جزء من التحليل: كورتيكويدات · ثيازيدات · بيتا · أستروجينات · مضادات قهقرية.')))
ENTR.append(qblock(19, 'Un garçon de 13 ans présente : CT 3,10 g/L — LDL 2,45 g/L — TG normaux ; son père a fait un infarctus à 42 ans :', E,
    ['Le profil est celui d\'une hypercholestérolémie pure (type IIa).', "Il faut évoquer une hypercholestérolémie familiale et mener l'enquête familiale.", 'Le diagnostic de forme primitive peut être posé sans éliminer de cause secondaire.', 'Des triglycérides normaux excluent toute dyslipidémie.', 'Le sérum est nécessairement lactescent.'],
    ['A', 'B'], 'q19-exp',
    [(True, 'LDL massif + TG normaux = pure = IIa (cas n°2 du cours).', FP % 'LDL' + ' ضخم + دهون طبيعية = صرف = IIa (حالة الدرس 2).'),
     (True, 'Âge + chiffre + père à 42 ans : le trio « familial ».', 'سنّ + رقم + أب في 42: ثلاثي «عائلي».'),
     (False, 'Jamais : le secondaire (hypothyroïdie…) s\'élimine <b>d\'abord</b>, même à 13 ans.', 'أبداً: الثانوي (قصور الدرقية…) يُستبعد <b>أولاً</b> ولو في 13 عاماً.'),
     (False, 'Le IIa vit justement avec des TG normaux <i>(⑥)</i>.', 'الـIIa يعيش بالضبط بدهون طبيعية <i>(⑥)</i>.'),
     (False, 'Sans excès de TG, sérum <b>non lactescent</b>.', 'دون فائض دهون، مصل <b>غير لبني</b>.')],
    (' C\'est le cas du cours déguisé en QCM : la démarche complète tient en A+B.',
     'إنها حالة الدرس متنكّرة في سؤال: المنهج الكامل في A+B.')))
ENTR.append(qblock(20, "Devant un bilan lipidique anormal, la démarche correcte comprend :", E,
    ['Compter un HDL à 0,35 g/L chez un homme comme un facteur de risque cardiovasculaire.', "S'appuyer sur le non-HDL quand les triglycérides sont très élevés.", 'Confirmer le bilan anormal avant de conclure (répétition à 2–4 semaines selon les annales).', 'Ne pas utiliser le LDLc pour le suivi thérapeutique.', 'Appliquer la formule de Friedewald à des triglycérides de 6 g/L.'],
    ['A', 'B', 'C'], 'q20-exp',
    [(True, '0,35 &lt; 0,40 : le seuil du cours est franchi.', '0,35 &lt; 0,40: تجاوزَ عتبة الدرس.'),
     (True, 'Le non-HDL reste fiable quand le LDL calculé décroche.', 'الـ' + FP % 'non-HDL' + ' يبقى موثوقاً حين ينحرف الحساب'),
     (True, "La confirmation avant l'étiquette (annale n°12).", 'التأكيد قبل الوسم (سؤال 12).'),
     (False, "Le LDLc EST le paramètre de suivi (annale n°15) <i>(⑤)</i>.", 'الـ' + FP % 'LDLc' + ' هو مؤشر المتابعة (سؤال 15) <i>(⑤)</i>.'),
     (False, 'À 6 g/L de TG, Friedewald est hors course — les annales rejettent déjà 5,0 et 4,38.', 'عند 6 من الدهون، ' + FT % 'Friedewald' + ' خارج السباق — الامتحانات ترفض 5,0 و4,38 أصلاً.')],
    (' La synthèse de la leçon : <b>seuil HDL, non-HDL de secours, confirmation</b> — trois réflexes, trois coches.',
     'خلاصة الدرس: <b>عتبة HDL، non-HDL احتياطياً، تأكيد</b> — ثلاثة انعكاسات، ثلاث تأشيرات.')))

# ═══════════════ SECTIONS ANNALES + ENTRAÎNEMENT ═══════════════
def qcm_section(sid, setname, icon, h2, lsub, chips3, blocks):
    return f'''            <!-- ═══════════════ {sid.upper()} ═══════════════ -->
            <section class="lsection" id="{sid}" data-qcm-set="{setname}">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid {icon}"></i></div>
                    <div>
                        <h2>{h2}</h2>
                        <div class="lsub">{lsub}</div>
                    </div>
                </div>

                <div class="qcm-section-head reveal">
                    <span class="chip chip-qcm"><i class="fa-solid fa-trophy"></i> Score de la session : <span class="qs-val">0 / 0</span></span>
                    <span class="chip"><i class="fa-solid fa-circle-info"></i> Plusieurs réponses possibles — coche tout ce qui est juste</span>
                    <span class="chip"><i class="fa-solid fa-repeat"></i> {chips3}</span>
                </div>

''' + '\n\n'.join(blocks) + '''
            </section>'''

annales_sec = qcm_section('annales', 'annales', 'fa-award',
    'Les 15 QCM d\'annales — énoncés authentiques',
    'Texte <b>exact</b> du recueil ELITE CARDIO 3ᵉ année (Biochimie §3, PROMO 2018 → rattrapage 2022), <b>corrigés officiels</b>, correction choix par choix. Les deux « type VI » du recueil se lisent « type IV » (clé donnée en correction). Coche d\'abord, corrige ensuite.',
    'Les types IIa/IIb et les seuils reviennent <b>d\'année en année</b>', ANNALES)

entr_sec = qcm_section('entrainement', 'entrainement', 'fa-bullseye',
    '20 QCM d\'entraînement — écrits dans le moule de l\'examinateur',
    '<b>Ce ne sont pas des annales.</b> Questions neuves calquées sur le profil mesuré des 15 vraies : 5 propositions, cadrage positif (une seule négative, comme l\'original), <b>7 à une réponse · 3 à deux · 10 à trois</b>. Chaque correction nomme le piège employé.',
    'La réponse <b>trois coches</b> est la signature de ce chapitre', ENTR)

# ═══════════════ FICHE FLASH (6 cases, 1 image/case) ═══════════════
def cell(cls, icon, title, img, alt, items, dims, delay=''):
    dl = f' data-delay="{delay}"' if delay else ''
    lis = '\n'.join(f'                            <li>{i}</li>' for i in items)
    return f'''                    <div class="flash-cell {cls} reveal"{dl}>
                        <h4><i class="fa-solid {icon}"></i> {title}</h4>
                        <img class="flash-img" src="{IMG}/{img}" alt="{alt}" loading="lazy" {dims}>
                        <ul>
{lis}
                        </ul>
                    </div>'''

fiche = '''            <!-- ═══════════════ FICHE FLASH ═══════════════ -->
            <section class="lsection" id="fiche">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-bolt"></i></div>
                    <div>
                        <h2>⚡ Fiche flash — à relire 5 minutes avant l'EMD</h2>
                        <div class="lsub">Tout le condensé critique du cours — chaque case a sa fiche image (clique pour agrandir) + la liste écrite.</div>
                    </div>
                </div>

                <div class="flashsheet">
''' + cell('fc-blue', 'fa-people-group', 'LES FAMILLES & LEURS CHIFFRES', 'ff-familles.webp',
    "Fiche flash des quatre familles chiffrées : chylomicrons 100 nanomètres à 1 micromètre 99 pour cent de lipides ApoB48, VLDL 50 nanomètres 90 pour cent ApoB100, LDL 20 nanomètres 80 pour cent ApoB100, HDL 10 nanomètres 50 à 70 pour cent ApoA, plus la particule est grosse moins elle est dense",
    ['<b>Chylomicrons</b> : 100 nm–1 µm · 99 % · <b>B48</b> · TG de l\'assiette',
     '<b>VLDL</b> : 50 nm · 90 % · <b>B100</b> · TG du foie',
     '<b>LDL</b> : 20 nm · 80 % · <b>B100</b> · cholestérol → tissus (athérogène)',
     '<b>HDL</b> : 10 nm · 50–70 % · <b>ApoA</b> · retour → foie (protecteur)',
     '<b>IDL</b> = VLDL déchargée, en route vers le LDL',
     'Règle : <b>taille ↓ = densité ↑</b>'], D2) + '\n' + cell('fc-teal', 'fa-eye', 'ASPECT DU SÉRUM & CRÉMAGE', 'ff-serum.webp',
    "Fiche flash de l'aspect du sérum : trois tubes clair opalescent lactescent devant un réfrigérateur, clair pas d'excès de grosses particules, opalescent VLDL, lactescent chylomicrons faire un crémage, crémage douze heures à plus quatre degrés crémeuse plus culot clair égale chylomicrons reste opalescent égale VLDL",
    ['<b>Clair</b> : pas d\'excès de grosses particules (LDL seul ne trouble pas)',
     '<b>Opalescent</b> = <b>VLDL</b>',
     '<b>Lactescent</b> = <b>chylomicrons</b> → <b>crémage</b>',
     'Crémage 12 h +4 °C : <b>crème + clair = chylo</b> · <b>opalescent = VLDL</b> · <b>crème + trouble = les deux</b>',
     'Toujours <b>à jeun</b> : sinon la marée postprandiale fausse tout'], D1, delay='1') + '\n' + cell('fc-amber', 'fa-gauge-high', 'LES QUATRE CHIFFRES', 'ff-seuils.webp',
    "Fiche flash des quatre chiffres sur un tableau de bord à quatre jauges : cholestérol total moins de 2 grammes par litre, triglycérides 0,5 à 1,5, HDL homme 0,4 femme 0,5 bas égal risque, LDL moins de 1,6 et moins de 0,70 à haut risque",
    ['<b>CT &lt; 2 g/L</b> (5,2 mmol/L)',
     '<b>TG 0,5 – 1,5 g/L</b>',
     '<b>HDL : H 0,4 · F 0,5 g/L</b> — <b>&lt; 0,40 = FRCV</b>',
     '<b>LDL &lt; 1,6 g/L</b> → <b>&lt; 0,70 si haut risque</b>',
     'LDL = <b>paramètre du suivi</b> · risque <b>exponentiel</b>',
     'Dépistage : <b>H 40 ans · F 50 ans</b> · enfant si familial'], D1, delay='2') + '\n' + cell('fc-purple', 'fa-table-cells-large', 'FREDRICKSON I–V', 'ff-fredrickson.webp',
    "Fiche flash de la classification de Fredrickson sur six tubes : type I chylomicrons triglycérides très élevés, type IIa LDL cholestérol élevé, type IIb LDL plus VLDL mixte quarante pour cent, type III restes IDL rare, type IV VLDL triglycérides élevés quarante-cinq pour cent, type V chylomicrons plus VLDL",
    ['<b>I</b> = chylomicrons · TG↑↑↑ · rare',
     '<b>IIa</b> = LDL · <b>pur</b> · sérum clair · athérogène · R-ApoB/E',
     '<b>IIb</b> = LDL+VLDL · <b>mixte</b> · 40 %',
     '<b>III</b> = IDL · rare · athérogène',
     '<b>IV</b> = VLDL · opalescent · <b>45 %</b> · diabète',
     '<b>V</b> = chylo + VLDL · Athérogènes d\'annale : <b>IIa, IIb, III</b>'], D2, delay='3') + '\n' + cell('fc-blue', 'fa-magnifying-glass', 'SECONDAIRE D\'ABORD', 'ff-secondaires.webp',
    "Fiche flash des causes secondaires à éliminer : hypothyroïdie et diabète, syndrome néphrotique et insuffisance rénale, cholestase, médicaments corticoïdes thiazidiques bêtabloquants œstrogènes, et le non en rouge hypoparathyroïdie",
    ['<b>Diabète · hypothyroïdie</b>',
     '<b>Néphrotique · IRC · cholestase</b>',
     '<b>Médicaments</b> : corticoïdes, thiazidiques, β-bloquants, œstrogènes, ARV',
     '<b>Obésité · alcool · syndrome métabolique</b>',
     '⛔ <b>Jamais</b> : hypo<b>para</b>thyroïdie (l\'intrus d\'annale)',
     '« Primitive » seulement <b>après</b> la chasse'], D1, delay='4') + '\n' + cell('fc-teal', 'fa-user-doctor', 'RÉFLEXES & CAS', 'ff-cas.webp',
    "Fiche flash penser familial : arbre généalogique avec grand-père AVC à 50 ans, père infarctus à 42 ans, enfant LDL très élevé triglycérides normaux, égale hypercholestérolémie familiale, et une main montrant un xanthome tendineux",
    ['Bilan anormal → <b>confirmer</b> (2–4 sem., annales) → <b>secondaire ?</b> → <b>classer</b> → <b>risque global</b>',
     'Cas 1 : 45 ans, tout monte + HDL bas = <b>mixte + syndrome métabolique</b>',
     'Cas 2 : 13 ans, LDL 2,45 isolé + père IDM 42 ans = <b>familiale</b>',
     'Friedewald : <b>invalide si TG très élevés</b> (✗ 5,0 et 4,38 en annales)',
     '2ᵉ intention : <b>ApoB · ApoA1 · lipidogramme · Lp(a)</b>'], D1, delay='5') + '''
                </div>
            </section>'''

# ═══════════════ FLASHCARDS (squelette gold verbatim) ═══════════════
flashcards_sec = '<!-- ═══════════════ FLASHCARDS' + SRC.split('<!-- ═══════════════ FLASHCARDS')[1].split('<!-- ═══════════════ RÉSUMÉ TOTAL')[0].rstrip()

# ═══════════════ RÉSUMÉ TOTAL ═══════════════
resume_total = '''            <!-- ═══════════════ RÉSUMÉ TOTAL ═══════════════ -->
            <section class="lsection" id="resume-total">
                <div class="lsection-head">
                    <div class="lsection-num icon-only"><i class="fa-solid fa-image"></i></div>
                    <div>
                        <h2>Le résumé total — toute la leçon en une image</h2>
                        <div class="lsub">La fiche ultime : le <b>tombable développé</b> (les voies, les quatre chiffres, le réflexe « secondaire d'abord »), le reste compressé — <b>sans les réponses des QCM</b>.</div>
                    </div>
                </div>

''' + fig('total.webp',
    "Résumé total des lipides et lipoprotéines : à gauche l'intestin qui émet les chylomicrons et le foie qui émet les VLDL devenant LDL avec les HDL en retour du cholestérol au foie, à droite le compte-rendu de laboratoire cholestérol total moins de 2, triglycérides 0,5 à 1,5, HDL homme 0,4 femme 0,5, LDL moins de 1,6 grammes par litre, et le bandeau toujours éliminer une cause secondaire avant de conclure primitive",
    '🖼️ <b>La fiche totale :</b> les trois voies + les quatre chiffres + le réflexe — <b>sans les réponses</b>, pour pouvoir te tester dessus',
    dims=D2, cls='section-visual total-visual reveal') + '''

''' + spot(8) + '''
            </section>'''

# ═══════════════ DONNÉES JSON ═══════════════
CINE = {"chapitres": [
    {"t": "Ouverture — pourquoi doser les lipides ? De l'assiette au chylomicron", "imgs": [f"{IMG}/hero.webp", f"{IMG}/enjeux.webp", f"{IMG}/absorption.webp"], "fr": "../assets/audio/bi-05/ch1-fr.mp3"},
    {"t": "Le transport en trois voies et les cinq familles", "imgs": [f"{IMG}/transport.webp", f"{IMG}/familles.webp"], "fr": "../assets/audio/bi-05/ch2-fr.mp3"},
    {"t": "Taille, densité, apolipoprotéines — et les trois destins", "imgs": [f"{IMG}/chiffres.webp", f"{IMG}/destinee.webp"], "fr": "../assets/audio/bi-05/ch3-fr.mp3"},
    {"t": "Les aiguilleurs du trafic, et qui dépister", "imgs": [f"{IMG}/regulation.webp", f"{IMG}/depistage.webp"], "fr": "../assets/audio/bi-05/ch4-fr.mp3"},
    {"t": "Le bilan de première intention — l'œil avant l'analyseur", "imgs": [f"{IMG}/bilan1.webp", f"{IMG}/reel/aspect-serum.webp"], "fr": "../assets/audio/bi-05/ch5-fr.mp3"},
    {"t": "Les quatre chiffres, puis la deuxième intention", "imgs": [f"{IMG}/valeurs.webp", f"{IMG}/bilan2.webp"], "fr": "../assets/audio/bi-05/ch6-fr.mp3"},
    {"t": "Fredrickson I–V, et la chasse aux causes secondaires", "imgs": [f"{IMG}/fredrickson.webp", f"{IMG}/secondaires.webp"], "fr": "../assets/audio/bi-05/ch7-fr.mp3"},
    {"t": "Deux patients pour tout résumer", "imgs": [f"{IMG}/cas.webp", f"{IMG}/ff-cas.webp"], "fr": "../assets/audio/bi-05/ch8-fr.mp3"},
    {"t": "Résumé total — toute la leçon en une écoute", "imgs": [f"{IMG}/total.webp"], "fr": "../assets/audio/bi-05/resume-fr.mp3", "ar": "../assets/audio/bi-05/resume-ar.mp3"},
]}

def kw(t, s, n, d, a): return {"t": t, "s": s, "n": str(n), "d": d, "a": a}
KW = [
 kw('Lipides', 'enjeux', 1, 'Molécules <b>hydrophobes</b> : énergie (triglycérides), structure (phospholipides, cholestérol) et signaux. Leur hydrophobie impose le transport par lipoprotéines.', 'جزيئات <b>كارهة للماء</b>: طاقة (' + FP % 'triglycérides' + ' وبنية (' + FP % 'phospholipides' + '، كولسترول) وإشارات. كرهها للماء يفرض نقلها بالـ' + FP % 'lipoprotéines' + '.'),
 kw('Triglycérides (TG)', 'enjeux', 1, 'Trois acides gras sur un glycérol : la <b>réserve énergétique</b>. Valeur usuelle <b>0,5–1,5 g/L</b> ; en excès, ils troublent le sérum.', 'ثلاثة أحماض دهنية على غليسرول: <b>مخزون الطاقة</b>. القيمة الاعتيادية <b>0,5–1,5</b>؛ وفائضها يعكّر المصل.'),
 kw('Cholestérol', 'enjeux', 1, 'Lipide des <b>membranes</b>, précurseur des stéroïdes et des sels biliaires. Il est le même partout : c\'est son <b>véhicule</b> (LDL ou HDL) qui fait le pronostic.', 'دهن <b>الأغشية</b>، طليعة الستيرويدات والأملاح الصفراوية. هو نفسه في كل مكان: <b>ناقله</b> (' + FP % 'LDL' + ' أو ' + FP % 'HDL' + ') هو من يصنع المآل.'),
 kw('Lipoprotéine', 'transport', 3, 'Le colis sanguin des lipides : <b>cœur</b> de TG + esters de cholestérol, <b>coque</b> de phospholipides + apolipoprotéines.', 'طرد الدهون الدموي: <b>قلب</b> من ' + FP % 'TG' + ' وإسترات كولسترول، و<b>غلاف</b> من فوسفوليبيدات و' + FP % 'apolipoprotéines' + '.'),
 kw('Apolipoprotéine (Apo)', 'familles', 4, 'La protéine « carte d\'identité » de surface : elle dit <b>d\'où vient</b> la particule et <b>où elle peut entrer</b> (B48 intestin, B100 foie/LDL, A pour HDL).', 'بروتين «بطاقة الهوية» السطحي: يقول <b>من أين أتى</b> الجسيم و<b>أين يدخل</b> (' + FP % 'B48' + ' أمعاء، ' + FP % 'B100' + ' كبد/' + FP % 'LDL' + '، ' + FP % 'A' + ' لـ' + FP % 'HDL' + ').'),
 kw('Chylomicron', 'familles', 4, 'La plus grosse (<b>100 nm–1 µm, 99 % de lipides, ApoB48</b>) : transporte les TG <b>alimentaires</b>, présent après les repas, rend le sérum lactescent.', 'الأضخم (<b>100 نانومتر–1 ميكرون، 99 % دهون، ' + FP % 'ApoB48' + '</b>): ينقل دهون <b>الغذاء</b>، يحضر بعد الوجبات، يجعل المصل لبنياً.'),
 kw('VLDL', 'familles', 4, 'Née au <b>foie</b> (≈ 50 nm, 90 % de lipides, <b>ApoB100</b>) : transporte les TG <b>endogènes</b> ; en excès, sérum opalescent ; mère des IDL puis des LDL.', 'تولد في <b>الكبد</b> (≈ 50 نانومتر، 90 % دهون، <b>' + FP % 'ApoB100' + '</b>): تنقل الدهون <b>الداخلية</b>؛ فائضها يجعل المصل عَكِراً؛ أمّ الـ' + FP % 'IDL' + ' ثم ' + FP % 'LDL' + '.'),
 kw('IDL', 'familles', 4, 'La VLDL <b>déchargée</b> (« restes de VLDL »), taille intermédiaire, en route vers le LDL. Son accumulation définit le <b>type III</b>.', 'الـ' + FP % 'VLDL' + ' <b>المفرَّغة</b> («بقايا VLDL»)، حجم وسيط في طريق ' + FP % 'LDL' + '. تراكمها يعرّف <b>النمط III</b>.'),
 kw('LDL', 'familles', 4, 'Le livreur de cholestérol aux tissus (≈ 20 nm, <b>ApoB100 seule</b>) : la particule <b>athérogène</b>, <b>cible &lt; 1,6 g/L</b> (0,70 au haut risque).', 'مسلّم الكولسترول إلى الأنسجة (≈ 20 نانومتر، <b>' + FP % 'ApoB100' + ' وحدها</b>): الجسيم <b>المصلِّب</b>، <b>هدف &lt; 1,6</b> (0,70 لعالي الخطورة).'),
 kw('HDL', 'familles', 4, 'La plus petite et dense (≈ 10 nm, <b>ApoA</b>) : elle assure le <b>transport inverse</b> du cholestérol vers le foie — protectrice. <b>&lt; 0,40 g/L = FRCV</b>.', 'الأصغر والأكثف (≈ 10 نانومتر، <b>' + FP % 'ApoA' + '</b>): تؤمّن <b>النقل العكسي</b> للكولسترول نحو الكبد — حامية. <b>&lt; 0,40 = عامل خطر</b>.'),
 kw('Voie exogène', 'transport', 3, 'Intestin → chylomicrons → tissus → restes vers le foie. C\'est le trajet des lipides <b>de l\'assiette</b>.', 'أمعاء ← ' + FP % 'chylomicrons' + ' ← أنسجة ← بقايا نحو الكبد. إنه مسار دهون <b>الصحن</b>.'),
 kw('Voie endogène', 'transport', 3, 'Foie → VLDL → IDL → LDL → tissus. Le trajet des lipides <b>fabriqués par le foie</b>.', 'كبد ← ' + FP % 'VLDL' + ' ← ' + FP % 'IDL' + ' ← ' + FP % 'LDL' + ' ← أنسجة. مسار الدهون <b>المصنوعة في الكبد</b>.'),
 kw('Transport inverse', 'transport', 3, 'Le retour du cholestérol des tissus vers le foie par les <b>HDL</b> — la voie protectrice, qui débouche sur la sortie biliaire.', 'عودة الكولسترول من الأنسجة إلى الكبد عبر <b>' + FP % 'HDL' + '</b> — المسار الحامي المؤدي إلى المخرج الصفراوي.'),
 kw('Densité (relation inverse)', 'chiffres', 5, 'Lipides légers contre protéines denses : <b>plus la particule est grosse et grasse, moins elle est dense</b> — la logique de tout le tableau.', 'دهون خفيفة ضد بروتينات كثيفة: <b>كلما كبر الجسيم وازداد دهنه قلّت كثافته</b> — منطق الجدول كله.'),
 kw('β-oxydation', 'destinee', 6, 'La <b>combustion</b> mitochondriale des acides gras en unités de 2 carbones pour produire de l\'énergie.', '<b>احتراق</b> الأحماض الدهنية في المتقدّرات إلى وحدات ثنائية الكربون لإنتاج الطاقة.'),
 kw('LPL (lipoprotéine lipase)', 'regulation', 7, 'L\'enzyme qui <b>décharge</b> chylomicrons et VLDL aux capillaires des tissus : TG → acides gras pour muscle et tissu adipeux.', 'الإنزيم الذي <b>يفرّغ</b> ' + FP % 'chylomicrons' + ' و' + FP % 'VLDL' + ' عند شعيرات الأنسجة: دهون ← أحماض دهنية للعضلات والشحم.'),
 kw('LCAT', 'regulation', 7, 'Elle <b>estérifie</b> le cholestérol des HDL : il plonge au cœur de la particule, qui peut continuer sa collecte.', '<b>تؤستر</b> كولسترول ' + FP % 'HDL' + ': يغوص إلى قلب الجسيم فتواصل جمعها.'),
 kw('CETP', 'regulation', 7, 'La protéine de <b>troc</b> : esters de cholestérol des HDL contre TG des particules à ApoB.', 'بروتين <b>المقايضة</b>: إسترات كولسترول ' + FP % 'HDL' + ' مقابل دهون جسيمات ' + FP % 'ApoB' + '.'),
 kw('Récepteur LDL (ApoB/E)', 'regulation', 7, 'La serrure hépatique qui <b>capte LDL et restes</b>. Sa mutation = hypercholestérolémie familiale (type IIa génétique).', 'القفل الكبدي الذي <b>يلتقط ' + FP % 'LDL' + ' والبقايا</b>. طفرته = فرط كولسترول عائلي (IIa الوراثي).'),
 kw('EAL', 'depistage', 8, '<b>Exploration d\'une Anomalie Lipidique</b> : diagnostiquer, classer, évaluer le risque. Homme dès 40 ans, femme dès 50 ans, enfant si histoire familiale.', '<b>استكشاف الشذوذ الدهني</b>: تشخيص، تصنيف، تقييم خطر. رجل من 40، امرأة من 50، طفل عند قصة عائلية.'),
 kw('Aspect du sérum', 'bilan1', 9, 'Le premier examen, à l\'œil : <b>Clair</b> (rien de gros en excès), <b>opalescent</b> (VLDL), <b>lactescent</b> (chylomicrons).', 'أول فحص، بالعين: <b>صافٍ</b> (لا شيء ضخماً فائضاً)، <b>عَكِر</b> (' + FP % 'VLDL' + '، <b>لبني</b> (' + FP % 'chylomicrons' + ').'),
 kw('Lactescent', 'bilan1', 9, 'Sérum laiteux : signature des <b>chylomicrons</b> (gros diffuseurs de lumière). Impose le <b>test de crémage</b>.', 'مصل لبني: توقيع <b>' + FP % 'chylomicrons' + '</b> (مشتّتات ضوء ضخمة). يفرض <b>اختبار التكرييم</b>.'),
 kw('Opalescent', 'bilan1', 9, 'Sérum trouble sans être laiteux : signature des <b>VLDL</b>.', 'مصل عَكِر دون أن يكون لبنياً: توقيع <b>' + FP % 'VLDL' + '</b>.'),
 kw('Test de crémage', 'bilan1', 9, '<b>12 h à +4 °C</b> : crème + culot clair = chylomicrons · opalescent sans crème = VLDL · crème + culot trouble = les deux.', '<b>12 ساعة في +4°</b>: قشدة + قاع صافٍ = ' + FP % 'chylomicrons' + ' · عَكِر بلا قشدة = ' + FP % 'VLDL' + ' · قشدة + قاع عَكِر = الاثنان.'),
 kw('Non-HDL-cholestérol', 'bilan1', 9, 'CT − HDL : <b>toutes les particules athérogènes</b> en un chiffre, fiable même quand les TG sont très élevés.', 'الكلي − ' + FP % 'HDL' + ': <b>كل الجسيمات المصلِّبة</b> في رقم واحد، موثوق حتى عند ارتفاع ' + FP % 'TG' + ' الشديد.'),
 kw('ApoB (dosage)', 'bilan2', 11, 'Une ApoB par particule athérogène : le dosage <b>compte</b> les particules. Outil de <b>2ᵉ intention</b>.', 'ApoB واحدة لكل جسيم مصلِّب: القياس <b>يعدّ</b> الجسيمات. أداة <b>قصد ثانٍ</b>.'),
 kw('ApoA1 (dosage)', 'bilan2', 11, 'Reflet des HDL ; le <b>rapport ApoB/ApoA1</b> résume le risque global (agression/protection). 2ᵉ intention.', 'انعكاس ' + FP % 'HDL' + '؛ ونسبة <b>' + FP % 'ApoB/ApoA1' + '</b> تلخّص الخطر الإجمالي (عدوان/حماية). قصد ثانٍ.'),
 kw('Lipidogramme', 'bilan2', 11, 'L\'<b>électrophorèse</b> des lipoprotéines : sépare selon charge/mobilité ; outil historique de Fredrickson, en déclin en routine.', '<b>رحلان</b> الـ' + FP % 'lipoprotéines' + ': يفصل حسب الشحنة/الحركية؛ أداة ' + FT % 'Fredrickson' + ' التاريخية، متراجع روتينياً.'),
 kw('Lp(a)', 'bilan2', 11, 'Particule à taux <b>génétiquement déterminé</b> : facteur de risque cardiovasculaire <b>indépendant</b>.', 'جسيم يحدّد معدله <b>الوراثة</b>: عامل خطر قلبي <b>مستقل</b>.'),
 kw('Formule de Friedewald', 'bilan2', 11, 'Le <b>calcul</b> du LDLc (depuis CT, TG, HDL). <b>Invalide si TG très élevés</b> (annales : rejetée à 5,0 et 4,38 g/L).', '<b>حساب</b> ' + FP % 'LDLc' + ' (من الكلي والدهون و' + FP % 'HDL' + '). <b>باطلة عند ارتفاع ' + FP % 'TG' + ' الشديد</b> (الامتحانات: مرفوضة عند 5,0 و4,38).'),
 kw('Classification de Fredrickson', 'fredrickson', 12, 'I chylomicrons · IIa LDL pure · IIb mixte (40 %) · III IDL · IV VLDL (45 %) · V chylo+VLDL. Athérogènes : <b>IIa, IIb, III</b>.', 'الأول كيلوميكرونات · IIa ‏LDL صرف · IIb مختلط (40 %) · الثالث IDL · الرابع VLDL ‏(45 %) · الخامس الاثنان. المصلِّبة: <b>IIa، IIb، III</b>.'),
 kw('Hyperlipoprotéinémie secondaire', 'secondaires', 13, 'Dyslipidémie <b>conséquence</b> d\'une maladie (diabète, hypothyroïdie, néphrotique, cholestase) ou d\'un médicament — à éliminer avant « primitive ».', 'اضطراب دهني <b>نتيجة</b> مرض (سكري، قصور درقية، نفروز، ركود صفراوي) أو دواء — يُستبعد قبل «بدئي».'),
 kw('Hypercholestérolémie familiale', 'cas', 14, 'Forme génétique (récepteur ApoB/E) : LDL très élevé <b>dès l\'enfance</b>, événements précoces dans la famille. Le cas du garçon de 13 ans.', 'صورة وراثية (مستقبل ' + FP % 'ApoB/E' + '): ' + FP % 'LDL' + ' مرتفع جداً <b>منذ الطفولة</b> وأحداث مبكرة عائلياً. حالة الفتى البالغ 13 عاماً.'),
 kw('Syndrome métabolique', 'cas', 14, 'Le terrain du cas n°1 : obésité abdominale + TG élevés + HDL bas (+ glycémie, tension) — un produit de risques, pas une addition.', 'أرضية الحالة 1: سمنة بطنية + دهون مرتفعة + ' + FP % 'HDL' + ' منخفضة (+ سكر، ضغط) — جداء أخطار لا جمعها.'),
 kw('Dyslipidémie mixte', 'fredrickson', 12, 'CT <b>et</b> TG élevés ensemble (LDL + VLDL) : le <b>type IIb</b>, 40 % des cas.', 'الكلي <b>و</b>الدهون مرتفعة معاً (' + FP % 'LDL + VLDL' + '): <b>النمط IIb</b>، 40 % من الحالات.'),
 kw('Facteur de risque cardiovasculaire', 'valeurs', 10, 'Ce qui multiplie la probabilité d\'événement : LDL élevé, <b>HDL &lt; 0,40</b>, diabète, HTA, tabac, âge, histoire familiale.', 'ما يضاعف احتمال الحدث: ' + FP % 'LDL' + ' مرتفع، <b>' + FP % 'HDL &lt; 0,40' + '</b>، سكري، ضغط، تدخين، عمر، قصة عائلية.'),
]

def fc(q, a): return {"q": q, "a": a}
FC = [
 fc('Les trois rôles des lipides ?', '<b>Énergétique</b> (TG = réserve) · <b>structural</b> (membranes) · <b>fonctionnel</b> (précurseurs, signaux).'),
 fc('Que contient une lipoprotéine ?', 'Un <b>cœur</b> de triglycérides + esters de cholestérol, une <b>coque</b> de phospholipides + <b>apolipoprotéines</b>.'),
 fc('Les produits absorbés par l\'intestin ?', '<b>Acides gras libres, monoglycérides, cholestérol libre</b> — jamais un TG entier ; ré-estérification dans l\'entérocyte.'),
 fc('Pourquoi les chylomicrons passent-ils par la lymphe ?', 'Trop <b>gros</b> pour les capillaires sanguins : chylifères → canal thoracique → sang <b>après</b> le foie.'),
 fc('Les trois voies du transport ?', '<b>Exogène</b> (intestin, chylomicrons) · <b>endogène</b> (foie, VLDL→IDL→LDL) · <b>inverse</b> (HDL → foie).'),
 fc('Carte d\'identité du chylomicron ?', 'Intestin · <b>100 nm–1 µm · 99 % de lipides · ApoB48</b> · TG alimentaires · postprandial.'),
 fc('VLDL contre LDL ?', 'VLDL : foie, <b>50 nm, 90 %, TG endogènes</b> · LDL : <b>20 nm, 80 %, cholestérol aux tissus</b>, B100 les deux.'),
 fc('La règle taille ↔ densité ?', '<b>Plus c\'est gros et gras, moins c\'est dense</b> — les lipides flottent, les protéines coulent.'),
 fc('Que deviennent les lipides livrés ?', '<b>Stockage</b> (adipocyte) · <b>β-oxydation</b> (énergie) · <b>synthèses</b> (membranes, stéroïdes, bile).'),
 fc('LPL, LCAT, CETP : qui fait quoi ?', '<b>LPL</b> décharge les TG aux tissus · <b>LCAT</b> estérifie le cholestérol des HDL · <b>CETP</b> échange entre familles.'),
 fc('Qui dépister ?', '<b>Homme 40 ans · femme 50 ans</b> · plus tôt si FR · <b>enfant</b> si antécédents familiaux.'),
 fc('Le bilan de 1ʳᵉ intention (cours) ?', '<b>Aspect du sérum, TG, CT, HDL, LDL, non-HDL</b> — à jeun. (Base d\'annale : CT + TG + LDLc.)'),
 fc('Clair, opalescent, lactescent ?', '<b>Clair</b> : pas de grosses particules · <b>opalescent</b> : VLDL · <b>lactescent</b> : chylomicrons.'),
 fc('Le test de crémage, protocole + lecture ?', '<b>12 h à +4 °C</b> : crème + clair = <b>chylo</b> · sans crème opalescent = <b>VLDL</b> · crème + trouble = <b>les deux</b>.'),
 fc('Les quatre chiffres ?', '<b>CT &lt; 2 · TG 0,5–1,5 · HDL H0,4/F0,5 · LDL &lt; 1,6 g/L</b> (0,70 au haut risque).'),
 fc('HDL bas : quel seuil, quel sens ?', '<b>&lt; 0,40 g/L</b> = <b>facteur de risque</b> cardiovasculaire (deux annales).'),
 fc('Que dose la 2ᵉ intention ?', '<b>ApoB</b> (compte les particules) · <b>ApoA1</b> · <b>lipidogramme</b> · <b>Lp(a)</b> · génétique si familiale.'),
 fc('La limite de Friedewald ?', 'Calcul du LDLc <b>invalide si TG très élevés</b> — rejeté en annales à 5,0 et 4,38 g/L. Relais : non-HDL.'),
 fc('Fredrickson en une ligne ?', 'I chylo · IIa LDL pure · IIb mixte 40 % · III IDL · IV VLDL 45 % · V chylo+VLDL.'),
 fc('Le portrait du type IIa ?', '<b>LDL pur, TG normaux, sérum clair, fort athérogène</b>, parfois mutation du <b>récepteur ApoB/E</b>.'),
 fc('Les types athérogènes (annales) ?', '<b>IIa, IIb et III</b> — les accumulateurs de particules à ApoB riches en cholestérol.'),
 fc('Les causes secondaires à réciter ?', 'Diabète · hypothyroïdie · néphrotique/IRC · cholestase · médicaments · obésité/alcool/syndrome métabolique.'),
 fc('L\'intrus qui ne donne PAS d\'hyperlipoprotéinémie secondaire ?', 'L\'<b>hypoparathyroïdie</b> — le « para » de l\'annale n°1.'),
 fc('Les deux cas du cours, conclusions ?', '45 ans tout élevé : <b>mixte + syndrome métabolique</b> · 13 ans LDL 2,45 isolé : <b>hypercholestérolémie familiale</b>.'),
 fc('La distribution des annales de ce chapitre ?', '15 QCM : <b>5 à une réponse · 2 à deux · 8 à trois</b> — la triple coche est la signature.'),
]
for i, c in enumerate(FC, 1): c2 = {"id": f"l{i}"}; c2.update(c); FC[i-1] = c2

# ═══════════════ ASSEMBLAGE ═══════════════
main_close_m = re.search(r'</section>\s*(</div>\s*</main>)', SRC)
main_close = main_close_m.group(1) if main_close_m else '</div>\n    </main>'
footer_scripts = '<script src="../js/bg-mode.js' + SRC.split('<script src="../js/bg-mode.js', 1)[1]
footer_scripts = re.sub(r'\s*<script src="\.\./js/lib/three\.min\.js"></script>', '', footer_scripts)
footer_scripts = footer_scripts.replace('orbital-sphere-bg.js?v=6', 'bio-field.js?v=11')

body = '\n\n'.join(OUT) + '\n\n' + annales_sec + '\n\n' + entr_sec + '\n\n' + fiche + '\n\n' + flashcards_sec + '\n\n' + resume_total
jsons = (
    '            <script type="application/json" id="cineData">' + json.dumps(CINE, ensure_ascii=False) + '</script>\n'
    '            <script type="application/json" id="kwData">' + json.dumps(KW, ensure_ascii=False) + '</script>\n'
    '            <script type="application/json" id="arData">' + json.dumps(AR, ensure_ascii=False) + '</script>\n'
    '    <script id="fcData" type="application/json">\n' + json.dumps(FC, ensure_ascii=False, indent=1) + '\n    </script>\n'
)
FOOTER_HTML = '''
    <!-- ============ FOOTER DE LEÇON ============ -->
    <footer class="footer">
        <div class="container">
            <div class="footer-bottom" style="border-top:none; padding-top:0;">
                <p style="margin-bottom:14px;">
                    <a href="../index.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-left"></i> Retour au tableau de bord</a>
                    &nbsp;
                    <a href="bi-06-biomarqueurs-cardiaques.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-right"></i> Autre leçon : Les biomarqueurs cardiaques</a>
                    &nbsp;
                    <a href="#vue" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-up"></i> Revoir la leçon</a>
                </p>
                <p>© <span id="footerYear">2026</span> SEENmed — Leçon « Exploration du métabolisme des lipides et lipoprotéines » · Biochimie · Dr Besbes. A</p>
            </div>
        </div>
    </footer>

    <div id="scrollProgress"></div>
    <button id="backToTop" aria-label="Retour en haut"><i class="fa-solid fa-arrow-up"></i></button>

    <!-- Données flashcards -->
'''
_jp = jsons.split('    <script id="fcData"')
html = top + nav + main_open + body + '\n\n        </div>\n\n' + _jp[0] + '    </main>' + FOOTER_HTML + '    <script id="fcData"' + _jp[1] + '\n' + footer_scripts
html = html.replace('<b tout monte</b>', '<b>Tout monte</b>')

OUTFILE = os.path.join(MS, 'lecons/bi-05-lipides-lipoproteines.html')
open(OUTFILE, 'w', encoding='utf-8').write(html)

# validation data-tr <-> arData
tr = set(re.findall(r'data-tr="([^"]+)"', html))
print('page KB:', len(html) // 1024, '| data-tr:', len(tr), '| arData:', len(AR),
      '| missing AR:', sorted(tr - set(AR)), '| extra AR:', sorted(set(AR) - tr))
print('qblocks:', html.count('class="qblock'), '| kw:', len(KW), '| fc:', len(FC), '| chapitres:', len(CINE['chapitres']))
refs = sorted(set(re.findall(r'(?:src|href)="(\.\./[^"]+)"', html) +
                  re.findall(r'"(\.\./assets/[^"]+)"', json.dumps(CINE))))
missing = [r for r in refs if not os.path.exists(os.path.normpath(os.path.join(MS, 'lecons', r)))]
print('refs locales:', len(refs), '| manquantes:', len(missing))
for r in missing: print('  MISSING:', r)

# patch data.js
dj_path = os.path.join(MS, 'js/data.js')
dj = open(dj_path, encoding='utf-8').read()
new_dj, n = re.subn(r"\{ id: 'bi-05'[^}]*\}",
    "{ id: 'bi-05', nom: 'Exploration du métabolisme des lipides et lipoprotéines', qcm: 15, entr: 20, recu: true,\n                  url: 'lecons/bi-05-lipides-lipoproteines.html' }", dj)
assert n == 1, f'data.js patch failed ({n})'
open(dj_path, 'w', encoding='utf-8').write(new_dj)
print('data.js patché ✔ ->', OUTFILE)
