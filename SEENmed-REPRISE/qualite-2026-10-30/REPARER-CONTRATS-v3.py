#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REPARER-CONTRATS-v3 — réparation structurelle phase 1 (STANDARD-OR-v3).

Convertit bi-06 / pn-01 / pn-04 vers les contrats RÉELS des moteurs du site
(QCM gold + scores, Ciné {chapitres} + section #cine + spots recâblés,
mots-clés tableau {t,s,n,d,a}, deck flashcards unique avec IDs, fiche flash
.flashsheet 4 macro-cellules, JSON de données AVANT les moteurs, flashcards
avant resume-total) et installe la peau pneumologie « Air alvéolaire »
(js/pneumo-field.js dérivé de bio-field.js + identité CSS 4 thèmes +
sélecteurs de modes + racine pneumo-root). Stdlib uniquement.
Ne régénère AUCUN contenu médical : il re-câble l'existant. Les
Explications restent globales (Pourquoi/Pièges) emballées en
.qexp-item + .qexp-memo — le proposition-par-proposition est la phase 2.

Usage : python3 REPARER-CONTRATS-v3.py <dossier-site> [bi-06 pn-01 pn-04]
Ensuite, OBLIGATOIRE : AUDIT-LECON-GOLD-v3.py (0 bloquant) puis
RUNTIME-DOM-v3.test.cjs / RUNTIME-SMOKE-v3.test.cjs (tout vert).
"""
import json, re, sys, unicodedata
from pathlib import Path

META = {'Vue','vue','cine','mindmap','annales','entrainement','fiche','flashcards','resume-total','pointscles','methode','connexions'}

# ---------- utilitaires balises ----------
def element_end(s, start, tag):
    m = re.compile(rf'<{tag}\b[^>]*>|</{tag}\s*>', re.S)
    depth = 0
    for t in m.finditer(s, start):
        tok = t.group(0)
        if tok.startswith('</'):
            depth -= 1
            if depth == 0:
                return t.end()
        elif not tok.rstrip().endswith('/>'):
            depth += 1
    raise ValueError(f'fin de <{tag}> introuvable depuis {start}')

def section_span(s, sid):
    m = re.search(rf'<section\b[^>]*\bid="{re.escape(sid)}"[^>]*>', s)
    if not m: return None
    return (m.start(), element_end(s, m.start(), 'section'))

def all_section_ids(s):
    return re.findall(r'<section\b[^>]*\bid="([^"]+)"', s)

def get_section(s, sid):
    sp = section_span(s, sid)
    return s[sp[0]:sp[1]] if sp else None

def replace_section(s, sid, new):
    sp = section_span(s, sid)
    assert sp, sid
    return s[:sp[0]] + new + s[sp[1]:]

def plain(html):
    x = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S)
    x = re.sub(r'<[^>]+>', ' ', x)
    return re.sub(r'\s+', ' ', x).strip()

def norm(x):
    x = unicodedata.normalize('NFD', x.lower())
    x = ''.join(c for c in x if unicodedata.category(c) != 'Mn')
    x = x.replace('œ','oe').replace('æ','ae')
    return re.sub(r'[^a-z0-9]+', ' ', x).strip()

def json_blocks(s, bid):
    out=[]
    for m in re.finditer(r'<script\b([^>]*)>(.*?)</script>', s, re.S):
        if re.search(rf'\bid="{re.escape(bid)}"', m.group(1)):
            out.append(json.loads(m.group(2)))
    return out

def script_json(bid, data):
    return f'<script type="application/json" id="{bid}">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script>'

# ---------- QCM ----------
def wrap_exp(inner, answers, lang='fr'):
    x = inner.strip()
    ans_html = ''
    m = re.search(r'<p class="qexp-ans">.*?</p>', x, re.S)
    if m:
        ans_html = m.group(0)
        x = (x[:m.start()] + x[m.end():]).strip()
    # déballer un unique <p>…</p>
    mp = re.fullmatch(r'<p>(.*)</p>', x, re.S)
    if mp: x = mp.group(1).strip()
    if lang == 'fr':
        parts = re.split(r'(<b>Piège[^<]*</b>)', x, maxsplit=1)
        why = parts[0]
        rest = ''.join(parts[1:]) if len(parts) > 1 else ''
        why = re.sub(r'^\s*<b>Pourquoi\s*:</b>\s*', '', why).strip()
        rest = re.sub(r'^\s*<b>Piège[^<]*</b>\s*', '', rest).strip()
        title = '<div class="qexp-title"><i class="fa-solid fa-circle-check"></i> Correction — pourquoi, et où sont les pièges</div>'
        item = f'<div class="qexp-item"><b>Pourquoi —</b> {why}</div>' if why else ''
        memo = f'<div class="qexp-memo"><i class="fa-solid fa-star"></i><div><b>Pièges :</b> {rest}</div></div>' if rest else ''
        return ans_html + title + item + memo
    else:
        parts = re.split(r'(<b>الفخ[^<]*</b>)', x, maxsplit=1)
        why = parts[0]
        rest = ''.join(parts[1:]) if len(parts) > 1 else ''
        why = re.sub(r'^\s*<b>لماذا\s*:</b>\s*', '', why).strip()
        rest = re.sub(r'^\s*<b>الفخ[^<]*</b>\s*', '', rest).strip()
        letters = ''.join(answers)
        title = f'<div class="qexp-title"><i class="fa-solid fa-circle-check"></i> الإجابة: {letters} — لماذا، وأين الفخاخ</div>'
        item = f'<div class="qexp-item"><b>لماذا —</b> {why}</div>' if why else ''
        memo = f'<div class="qexp-memo"><i class="fa-solid fa-star"></i><div><b>الفخاخ:</b> {rest}</div></div>' if rest else ''
        return title + item + memo

def convert_qcm_section(sec, setname, ar_by_key_answers):
    # attribut de score sur la section
    sec = re.sub(rf'(<section\b[^>]*\bid="{setname}")', rf'\1 data-qcm-set="{setname}"', sec, count=1)
    # bandeau score après l'en-tête de section
    hm = re.search(r'<div class="lsection-head">', sec)
    hend = element_end(sec, hm.start(), 'div')
    score = ('\n                <div class="qcm-section-head reveal">'
             '<span class="chip chip-qcm"><i class="fa-solid fa-trophy"></i> Score de la session : <span class="qs-val">0 / 0</span></span>'
             '<span class="chip"><i class="fa-solid fa-circle-info"></i> Plusieurs réponses possibles — coche tout ce qui est juste, puis corrige</span></div>\n')
    sec = sec[:hend] + score + sec[hend:]
    sec = re.sub(r'<div class="score-box"[^>]*></div>', '', sec)
    # convertir chaque qblock, de la fin vers le début
    starts = [m.start() for m in re.finditer(r'<div class="qblock\b', sec)]
    for st in reversed(starts):
        en = element_end(sec, st, 'div')
        blk = sec[st:en]
        am = re.search(r'data-answer="([^"]+)"', blk)
        answers = [a.strip() for a in am.group(1).split(',') if a.strip()]
        qnum = re.search(r'<span class="qnum">Q?(\d+)</span>', blk).group(1)
        src = re.search(r'<span class="qsource">(.*?)</span>', blk, re.S).group(1)
        qtext = re.search(r'<p class="qtext">(.*?)</p>', blk, re.S).group(1)
        choices = re.findall(r'<label class="qopt"><input[^>]*value="([A-E])"[^>]*><span class="qletter">[A-E]</span><span>(.*?)</span>\s*</label>', blk, re.S)
        assert len(choices) == 5, (setname, qnum, choices)
        em = re.search(r'<div class="qexp" data-tr="([^"]+)" hidden>', blk)
        trk = em.group(1)
        eend = element_end(blk, em.start(), 'div')
        exp_inner = blk[em.end():eend-len('</div>')]
        ar_by_key_answers[trk] = answers
        is_ann = (setname == 'annales')
        src_cls = 'src-annale' if is_ann else 'src-new'
        src_icon = 'fa-award' if is_ann else 'fa-bullseye'
        lis = ''.join(f'<li data-l="{l}"><span class="ql">{l}</span><span class="qtxt">{t}</span><span class="xe"></span></li>' for l, t in choices)
        new = (f'<div class="qblock reveal" data-answer=\'{json.dumps(answers)}\'>'
               f'<div class="qhead"><div class="qtext">{qnum}. {qtext}</div>'
               f'<span class="qsrc {src_cls}"><i class="fa-solid {src_icon}"></i> {src}</span></div>'
               f'<ul class="qch">{lis}</ul><div class="qverdict"></div>'
               f'<div class="qexp" data-tr="{trk}">{wrap_exp(exp_inner, answers, "fr")}</div>'
               '<div class="qcheck-row"><button class="btn btn-primary btn-sm qcheck"><i class="fa-solid fa-check"></i> Corriger ma réponse</button></div></div>')
        sec = sec[:st] + new + sec[en:]
    return sec

# ---------- mots-clés ----------
def convert_kw(page, kw_old, overrides):
    items = kw_old['items'] if isinstance(kw_old, dict) else kw_old
    cand = [sid for sid in all_section_ids(page) if sid not in META]
    texts = {}
    for sid in cand:
        texts[sid] = norm(plain(get_section(page, sid) or ''))
    out = []
    log = []
    for it in items:
        t = it['t']; nt = norm(t)
        best, bestn = None, -1
        for sid in cand:
            c = texts[sid].count(' ' + nt + ' ') + (1 if texts[sid].startswith(nt + ' ') else 0)
            if c == 0 and nt:
                continue
            if c > bestn: best, bestn = sid, c
        if best is None or bestn <= 0:
            toks = [w for w in nt.split() if len(w) >= 4]
            scores = {sid: sum(texts[sid].count(w) for w in toks) for sid in cand}
            best = max(scores, key=lambda k: scores[k]); bestn = scores[best]
            log.append(f'  ~ repli tokens : {t} -> {best} ({bestn})')
        if t in overrides:
            best = overrides[t]; log.append(f'  ! surcharge : {t} -> {best}')
        a = it.get('a') or {}
        out.append({'t': t, 's': best, 'n': str(cand.index(best) + 1),
                    'd': it.get('d',''), 'a': (a.get('d','') if isinstance(a, dict) else a)})
    out.sort(key=lambda x: int(x['n']))
    return out, cand, log

# ---------- Ciné ----------
def convert_cine(cine_old):
    chs = []
    for c in cine_old.get('chapters', []):
        chs.append({'t': c.get('title',''), 'imgs': c.get('images', []),
                    'fr': c.get('audio'), 'ar': c.get('audioAr')})
    return {'chapitres': chs}

def cine_section(cine):
    chs = cine['chapitres']; n = len(chs)
    n_ar = sum(1 for c in chs if c.get('ar'))
    if n_ar == n:
        sub = f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres + le résumé</b>, piste <b>française ou arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.'
    elif n_ar:
        sub = f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres en français</b>, plus le <b>résumé total en français et en arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.'
    else:
        sub = f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres + le résumé, en français</b>, vitesse réglable. Rien ne se lance sans ton clic.'
    return ('\n            <section class="lsection" id="cine">'
            '<div class="lsection-head"><div class="lsection-num icon-only"><i class="fa-solid fa-clapperboard"></i></div>'
            f'<div><h2>Ciné-révision — la leçon racontée</h2><div class="lsub">{sub}</div></div></div>'
            '<div id="cinePlayer" class="reveal"></div></section>\n')

def insert_spot(sec, ch):
    spot = f'<div class="cine-spot reveal" data-ch="{ch}"></div>'
    fm = re.search(r'<figure\b[^>]*class="[^"]*lfig[^"]*"[^>]*>', sec) or re.search(r'<figure\b', sec)
    if fm:
        pos = element_end(sec, fm.start(), 'figure')
        tail = sec[pos:]
        m2 = re.match(r'\s*(<!--.*?-->\s*)?<div class="reel-strip\b', tail, re.S)
        if m2:
            dstart = pos + tail.index('<div class="reel-strip')
            pos = element_end(sec, dstart, 'div')
        return sec[:pos] + '\n' + spot + sec[pos:]
    hm = re.search(r'<div class="lsection-head">', sec)
    pos = element_end(sec, hm.start(), 'div')
    return sec[:pos] + '\n' + spot + sec[pos:]

# ---------- flashcards ----------
DECK = ('<div class="sr-panel reveal" id="fcDeck"><div class="sr-head"><div class="sr-count" id="fcCount"></div>'
        '<span class="chip chip-qcm"><i class="fa-solid fa-clock-rotate-left"></i> SM-2 : J+1 → J+3 → J+7 → J+16 → J+35</span></div>'
        '<div class="fc-stage" id="fcStage"><div class="fc-card" id="fcCard">'
        '<div class="fc-face fc-front" id="fcFront"></div><div class="fc-face fc-back" id="fcBack"></div></div></div>'
        '<div class="sr-controls">'
        '<button class="sr-btn again" id="fcAgain"><i class="fa-solid fa-rotate-left"></i> À revoir <small>(1)</small></button>'
        '<button class="sr-btn hard" id="fcHard"><i class="fa-solid fa-face-frown"></i> Difficile <small>(2)</small></button>'
        '<button class="sr-btn good" id="fcGood"><i class="fa-solid fa-face-smile"></i> Bien <small>(3)</small></button>'
        '<button class="sr-btn easy" id="fcEasy"><i class="fa-solid fa-face-laugh"></i> Facile <small>(4)</small></button></div>'
        '<div class="sr-done" id="fcDone" style="display:none;"></div></div>')

# ---------- fiches flash (contenu repris des pages elles-mêmes) ----------
FICHES = {
 'bi-06': [
  ('fc-red','fa-heart-pulse','LA TROPONINE — la référence du SCA','ff-troponine.webp','Complexe troponine sur le filament d’actine : les trois sous-unités C, I et T, le calcium, le verrou sur la myosine et l’ancre sur la tropomyosine',[
   '★★ Le trio : <b>TnC</b> fixe le calcium, <b>TnI</b> verrouille, <b>TnT</b> s’ancre à la tropomyosine',
   '★★ <b>TnI et TnT cardiospécifiques</b> — TnC ne l’est pas (muscle squelettique barré)',
   '★ Détection : <b>hypersensible 1–2 h</b>, classique <b>3–6 h</b>',
   '★★ Élevée <b>≠</b> infarctus : myocardite, IC, embolie pulmonaire, sepsis, rein, effort — on interprète avec <b>anamnèse + clinique + ECG</b>',
   '★ Piège de vocabulaire : <b>cardiospécifique</b> veut dire spécifique du <b>tissu myocardique</b>, pas de la maladie coronarienne']),
  ('fc-blue','fa-chart-line','LES CINÉTIQUES — trois horloges, trois destins','ff-cinetique.webp','Trois courbes de marqueurs après douleur : le pic éclair retombant en 24 heures, le pic intermédiaire en 2 à 3 jours et le long plateau jusqu’à 10 jours',[
   '★ Le pic éclair : retombe en <b>24 h</b> — le marqueur précoce et bref',
   '★ Le pic intermédiaire : retombe en <b>2–3 jours</b>',
   '★★ Le long plateau : <b>TnI 3–6 jours, TnT 10 jours</b> → c’est lui qui permet le <b>diagnostic rétrospectif</b>',
   '★ Seuils hs-CRP du risque : <b>1 et 3 mg·L⁻¹</b> — trois segments vert, jaune, rouge',
   '★★ Retiens la phrase : <b>1–2 h / 3–6 h / 10 j</b> — détection hs, détection classique, durée TnT']),
  ('fc-teal','fa-route','LE SCA — deux routes, aucune attente','ff-algo.webp','Algorithme du SCA : ECG avec ST surélevé vers la reperfusion immédiate, ECG sans sus-décalage vers deux tubes horodatés qui décident',[
   '★★ <b>STEMI (ST↑)</b> : reperfusion <b>sans attendre</b> la troponine',
   '★★ <b>NSTEMI</b> : troponine à <b>H0</b>, contrôle <b>H1–H3</b> (hypersensible) ou <b>H6–H9</b>',
   '★★ Deux dosages normaux = infarctus <b>exclu</b>',
   '★ La troponine <b>complète</b> l’ECG et la clinique — elle ne les remplace jamais']),
  ('fc-amber','fa-droplet','BNP / NT-proBNP — le ventricule qui souffre','ff-bnp.webp','Le pro-BNP libéré par un ventricule distendu se scinde en BNP actif qui dilate et fait uriner, et en NT-proBNP stable dosé au laboratoire',[
   '★★ Un précurseur, deux destins : le <b>BNP agit</b> (vasodilatation, natriurèse), le <b>NT-proBNP témoigne</b> (stable, dosé)',
   '★★ Leur question : dyspnée <b>cardiaque ou pulmonaire</b> ? — jamais « le myocarde est-il nécrosé ? »',
   '★ Suivi d’<b>insuffisance cardiaque</b> et dyspnée : <b>BNP / NT-proBNP</b>, pas la troponine',
   '★ Aux urgences : peptides <b>très élevés si la dyspnée est cardiaque</b>, normaux si elle est pulmonaire — ils <b>complètent l’ETT</b>, sans la remplacer',
   '★★ Trois familles, trois questions : <b>nécrose</b> (troponine) · <b>fonction</b> (peptides) · <b>inflammation/risque</b> (hs-CRP)']),
 ],
 'pn-01': [
  ('fc-red','fa-comments','DÉFINITION & INTERROGATOIRE — la plainte et la mesure','ff-composantes.webp','Les deux composantes de la dyspnée : la plainte subjective du patient et la mesure objective du médecin, reliées par une double flèche',[
   '★★ Dyspnée = <b>difficulté à respirer</b>, mouvement ventilatoire pénible : composante <b>subjective</b> (patient) + <b>objective</b> (médecin) — jamais l’une sans l’autre',
   '★★ On interroge : <b>terrain</b>, installation <b>aiguë ou chronique</b>, <b>horaire</b>, facteurs déclenchants',
   '★★ Position : <b>orthopnée</b> = aggravée couché · <b>platypnée</b> = aggravée à l’orthostatisme',
   '★ Le nombre d’<b>oreillers</b> chiffre l’orthopnée au lit du malade']),
  ('fc-blue','fa-stairs','LA NYHA — quatre marches d’effort','ff-nyha.webp','Les quatre stades NYHA en escalier, du coureur sans gêne au patient dyspnéique de repos, avec la pile d’oreillers de l’orthopnée',[
   '★★ <b>4 stades</b> : du <b>I</b> (aucune gêne) au <b>IV</b> (dyspnée <b>permanente de repos</b>)',
   '★★ La NYHA gradue l’<b>effort toléré</b> — elle ne grade ni la position ni la cause',
   '★ Le repère du cours : <b>2 étages</b> séparent le « monte sans gêne » du « s’arrête »',
   '★ Piège d’annale : l’<b>orthopnée n’a pas de stade NYHA</b> — familles différentes']),
  ('fc-teal','fa-wind','PHASE, FRÉQUENCE, RYTHME — ce que l’œil lit','ff-phases.webp','Les trois temps du cycle respiratoire : inspiration bloquée en haut, expiration bloquée en bas, et les deux temps bloqués, avec leurs courbes',[
   '★★ Phase <b>inspiratoire</b> = larynx et trachée · phase <b>expiratoire</b> = bronches · <b>mixte</b> = les deux',
   '★★ Fréquence : la ventilation minute s’écrit <b>VE = VT × FR</b>',
   '★★ Rythmes signatures : <b>Kussmaul = acidose</b> · <b>Cheyne-Stokes = bas débit central</b>',
   '★ Trois lectures, un seul examen : <b>où</b> ça bloque, <b>combien</b> de cycles, <b>quel</b> dessin']),
  ('fc-amber','fa-triangle-exclamation','GRAVITÉ & ORIENTATION — ne rien rater','ff-gravite.webp','Les signes de gravité de la dyspnée : tirage des muscles accessoires, cyanose, sueurs, le moniteur en alarme et le silence auscultatoire',[
   '★★ Gravité : <b>tirage</b>, <b>cyanose</b>, <b>sueurs</b>, <b>FC &gt; 120/min</b>, <b>SpO₂ sous 90 %</b>, troubles de conscience, <b>silence auscultatoire</b>',
   '★ Le piège du chiffre « presque juste » : grave <b>en dessous</b> de 90 %, pas à 90 %',
   '★★ Orientation : <b>avec</b> anomalies auscultatoires (crépitants, sibilants, asymétrie) ou <b>sans</b> — embolie, tamponnade, acidose, anémie, causes neurologiques',
   '★★ <b>BNP sous 300</b> et <b>D-dimères sous 500</b> : ils <b>excluent</b>, ils n’affirment jamais']),
 ],
 'pn-04': [
  ('fc-red','fa-burst','DÉFINITION — toujours pathologique','ff-pieges.webp','Les pièges de l’expectoration : la femme et l’enfant qui déglutissent, le tubage gastrique, et le principe qu’elle est toujours pathologique',[
   '★★ Expectoration = <b>expulsion par la bouche, au cours d’un effort de toux, de produits pathologiques des voies bronchopulmonaires</b>',
   '★★ C’est le <b>satellite de la toux</b> — sauf chez la <b>femme</b> et l’<b>enfant de moins de 12 ans</b> qui <b>déglutissent</b> : chez eux, <b>tubage gastrique à jeun</b>',
   '★ Le mucus normal n’est <b>pas</b> une expectoration : <b>100 mL/j</b>, <b>95 % d’eau</b>, régulé par le <b>vague</b>, épuré par les <b>cils</b>',
   '★★ La conclusion du cours, mot pour mot : <b>toute expectoration est toujours pathologique</b>']),
  ('fc-blue','fa-flask','L’EXAMEN — dans un verre gradué','ff-bronchorrhee.webp','Le verre gradué de la bronchorrhée : quatre couches superposées numérotées, 150 à 200 cm³ recueillis le matin',[
   '★★ On examine dans un <b>verre gradué</b> : abondance, couleur, odeur, transparence, consistance, aération, horaire',
   '★★ Couleurs repères : <b>blanchâtre</b> = muqueux · <b>jaune</b> = purulent · rouille · rosé saumon · marron chocolat',
   '★ Odeurs : <b>fade de plâtre frais</b> = suppuration banale · <b>fétide</b> = anaérobies',
   '★★ L’horaire signe : <b>le matin = la toilette des bronches</b>']),
  ('fc-teal','fa-layer-group','LES CINQ TYPES — du blanc d’œuf au sang','ff-types.webp','Les cinq types d’expectoration en cinq verres : muqueuse transparente, purulente jaune, muco-purulente, séreuse rosée et hémoptoïque striée de sang',[
   '★★ <b>Muqueuse</b> : blanc d’œuf, <b>perles de Laennec</b>, <b>moules</b> bronchiques',
   '★★ <b>Purulente</b> : pus franc, <b>inodore ou putride</b>',
   '★★ <b>Muco-purulente</b> : la <b>bronchorrhée, 150–200 cm³/24 h en 4 couches</b>',
   '★★ <b>Séreuse</b> : mousseuse <b>rosé saumoné</b> de l’<b>OAP</b> · <b>Hémoptoïque</b> : hémoptysie de <b>petite abondance</b>']),
  ('fc-amber','fa-cloud-burst','LA VOMIQUE — l’irruption','ff-vomique.webp','Les trois formes de la vomique : le jet unique massif, les projections fractionnées et les crachats nummulaires rapprochés',[
   '★★ <b>Brutale</b>, souvent <b>massive</b>, « comme un vomissement »',
   '★★ <b>Purulente</b> (poumon, plèvre, sous-phrénique) ou <b>eau de roche</b> (kyste hydatique)',
   '★★ Trois formes : <b>massive</b>, <b>fractionnée</b>, <b>nummulaire</b>',
   '★ Devant toute vomique : demander <b>d’où vient le liquide</b> avant de nommer la maladie']),
 ],
}

SPOTS_PN01 = {'enjeu':0,'respiration':1,'interrogatoire':2,'nyha':3,'phase':4,'frequence':5,'rythme':5,
              'gravite':6,'examens':7,'seuils':7,'auscultation':7,'sans-anomalies':7,'pointscles':8}
SPOTS_PN04 = {'place':0,'definition':0,'origine':1,'composition':2,'valeur':3,'caracteres':4,'muqueuse':5,
              'purulente':6,'mucopurulente':6,'sereuse':7,'hemoptoique':7,'vomique':8,'etiologies':9,'pointscles':9}
KW_OVERRIDES = {
 'bi-06': {'Syndrome coronarien aigu (SCA)':'sca','Infarctus du myocarde (IDM)':'sca',
           'Valeur prédictive négative (VPN)':'hs','Cinétique':'cinetique',
           'Biomarqueur cardiaque':'enjeux','Nécrose myocardique':'necrose','NSTEMI':'sca',
           'CK-MB':'ckmb','ASAT / ALAT / LDH':'necrose','Fibrinogène':'inflammation',
           'Diagnostic rétrospectif':'troponine','Peptide natriurétique':'peptides'},
 'pn-01': {'Dyspnée':'enjeu','Dyspnée aiguë':'interrogatoire','Dyspnée expiratoire':'phase',
           'NYHA':'nyha','Tachypnée':'frequence','Ventilation minute (VE)':'frequence',
           'Embolie pulmonaire':'sans-anomalies'},
 'pn-04': {'Expectoration':'definition','Satellite de la toux':'definition',
           'Femme et enfant < 12 ans':'definition','Conclusion du cours':'definition',
           'Glandes bronchiques':'origine','Cellules caliciformes':'origine',
           'Cils vibratiles':'origine','Vague (X)':'origine','100 mL par jour':'origine',
           '95 % d\'eau':'composition','5 % de solides':'composition',
           'Expectoration pathologique':'composition','Abondance':'valeur',
           'Crachat jaune':'valeur','Expectoration séreuse':'sereuse','OAP':'sereuse',
           'Crachats rouillés':'etiologies'},
}

def build_fiche(sec, lid):
    # récupérer dimensions des images ff existantes
    dims = {}
    for m in re.finditer(r'<img src="([^"]+)"[^>]*width="(\d+)" height="(\d+)"', sec):
        dims[m.group(1).split('/')[-1]] = (m.group(2), m.group(3))
    cells = []
    for cls, icon, title, img, alt, bullets in FICHES[lid]:
        w, h = dims.get(img, ('1376','768'))
        lis = ''.join(f'<li>{b}</li>' for b in bullets)
        cells.append(f'<div class="flash-cell {cls}"><h4><i class="fa-solid {icon}"></i> {title}</h4>'
                     f'<img class="flash-img" src="../assets/img/{lid}/{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}">'
                     f'<ul>{lis}</ul></div>')
    sheet = '<div class="flashsheet ff-2x2 reveal">' + ''.join(cells) + '</div>'
    gm = re.search(r'<div class="flash-grid">', sec)
    gend = element_end(sec, gm.start(), 'div')
    sec = sec[:gm.start()] + sheet + sec[gend:]
    sec = re.sub(r'(<div class="lsub">).*?(</div>)', r'\1Quatre cases, quatre planches — les faits et les pièges de dernière minute, à relire dans l’ordre. L’encadré qui suit se récite à voix haute.\2', sec, count=1, flags=re.S)
    return sec

def repair(path_in, path_out, lid):
    s = Path(path_in).read_text(encoding='utf-8')
    # --- données d'origine
    cine_old = json_blocks(s, 'cineData')[0]
    kw_old = json_blocks(s, 'kwData')[0]
    fc_old = json_blocks(s, 'fcData')[-1]   # le sien est le dernier
    ar = json_blocks(s, 'arData')[-1]
    cine = convert_cine(cine_old)
    kw, cand, kwlog = convert_kw(s, kw_old, KW_OVERRIDES.get(lid, {}))
    prefix = lid.replace('-', '')
    fc = []
    for i, c in enumerate(fc_old, 1):
        nc = dict(c); nc['id'] = f'{prefix}-{i:02d}'
        fc.append({'id': nc['id'], **{k: v for k, v in nc.items() if k != 'id'}})
    print(f'[{lid}] KW sections candidates : {cand}')
    for line in kwlog: print(line)
    for k in kw: print(f"   KW {k['t']} -> {k['s']} (n={k['n']})")

    # --- peau
    if lid.startswith('pn-'):
        s = re.sub(rf'(<body data-lesson-id="{lid}")', rf'\1 class="has-pneumo-field"', s, count=1)
        s = re.sub(r'(<body\b[^>]*>)', r'\1\n<canvas id="pneumoFieldCanvas" aria-hidden="true"></canvas>', s, count=1)
    elif lid == 'bi-06' and 'bioFieldCanvas' not in s:
        s = re.sub(r'(<body\b[^>]*>)', r'\1\n<canvas id="bioFieldCanvas" aria-hidden="true"></canvas>', s, count=1)

    # --- QCM + arabe des corrections
    answers_by_key = {}
    for setname in ('annales', 'entrainement'):
        sec = get_section(s, setname)
        s = replace_section(s, setname, convert_qcm_section(sec, setname, answers_by_key))
    for k, ans in answers_by_key.items():
        if k in ar: ar[k] = wrap_exp(ar[k], ans, 'ar')

    # --- Ciné : section centrale (pn) + spots
    if lid.startswith('pn-'):
        sp = section_span(s, 'mindmap')
        s = s[:sp[1]] + cine_section(cine) + s[sp[1]:]
        s = re.sub(r'<div class="cine-spot[^"]*" data-ch="\d+"></div>', '', s)
        spots = SPOTS_PN01 if lid == 'pn-01' else SPOTS_PN04
        # appliquer dans l'ordre inverse du document pour ne pas décaler les positions
        order = all_section_ids(s)
        for sid in sorted(spots, key=lambda x: -order.index(x)):
            sec = get_section(s, sid)
            s = replace_section(s, sid, insert_spot(sec, spots[sid]))

    # --- Flashcards : deck + déplacement avant le résumé
    sec = get_section(s, 'flashcards')
    sec = sec.replace('<div id="flashApp"></div>', DECK)
    sec = re.sub(r'(<div class="lsub">).*?(</div>)',
                 rf'\g<1>{len(fc)} cartes — retourne la carte (clic ou barre d’espace), évalue-toi (touches 1–4) : le système reprogramme chaque carte au bon jour (SM-2).\2',
                 sec, count=1, flags=re.S)
    s = replace_section(s, 'flashcards', sec)
    fsp = section_span(s, 'flashcards'); rsp = section_span(s, 'resume-total')
    if fsp[0] > rsp[0]:
        block = s[fsp[0]:fsp[1]]
        s = s[:fsp[0]] + s[fsp[1]:]
        rsp = section_span(s, 'resume-total')
        s = s[:rsp[0]] + block + '\n\n' + s[rsp[0]:]

    # --- Fiche flash
    s = replace_section(s, 'fiche', build_fiche(get_section(s, 'fiche'), lid))

    # --- scripts : retirer données + moteurs, réémettre dans l'ordre canonique
    ENGINES = ('bg-mode.js','progress.js','main.js','bio-field.js','cardio-field.js','lesson.js','ar-mode.js','keywords.js','cine.js')
    def drop(m):
        head = m.group(1)
        if any(f'id="{i}"' in head for i in ('cineData','kwData','fcData','arData')): return ''
        if any(e in head for e in ENGINES): return ''
        return m.group(0)
    s = re.sub(r'<script\b([^>]*)>.*?</script>', drop, s, flags=re.S)
    field = ('<script src="../js/pneumo-field.js?v=1"></script>' if lid.startswith('pn-')
             else '<script src="../js/bio-field.js?v=11"></script>')
    tail = '\n'.join([
        script_json('cineData', cine), script_json('kwData', kw),
        script_json('fcData', fc), script_json('arData', ar),
        '<script src="../js/bg-mode.js?v=14"></script>',
        '<script src="../js/progress.js?v=6"></script>',
        '<script src="../js/main.js?v=6"></script>', field,
        '<script src="../js/lesson.js?v=12"></script>',
        '<script src="../js/ar-mode.js?v=1"></script>',
        '<script src="../js/keywords.js?v=2"></script>',
        '<script src="../js/cine.js?v=3"></script>', ''])
    s = s.replace('</body>', tail + '</body>', 1)
    Path(path_out).write_text(s, encoding='utf-8')
    print(f'[{lid}] écrit {path_out} ({len(s)} caractères)')



# ---------- peau pneumologie « Air alvéolaire » (STANDARD-OR-v3 §9) ----------
SKIN_CSS_STYLE = '/* ============================================================\n   IDENTITÉ CHROMATIQUE DU MODULE PNEUMOLOGIE — body.has-pneumo-field\n   « Air alvéolaire » : les pages pn-* quittent le bleu/turquoise de\n   la plateforme pour un couple CYAN GLACIER + ROSE ALVÉOLE : l\'air\n   oxygéné qui descend l\'arbre bronchique, le tissu où il échange.\n   Une atmosphère propre par thème (STANDARD-OR-v3 §9.1) :\n     Sombre → air nocturne       cyan glacier + rose alvéole\n     Clair  → air clair          bleu respiratoire + rose profond\n     Aurore → brume alvéolaire   violet brume + rose aurore\n     Océan  → oxygène dissous    turquoise dissous + bulles d\'air\n   Les variables étant redéclarées sur <body>, tout en hérite :\n   boutons, badges, onglets, tableaux, QCM, flashcards, lueurs.\n   ============================================================ */\nbody.has-pneumo-field {\n    --blue:        #35d0ff;\n    --blue-dark:   #1599c2;\n    --blue-bright: #67e3ff;\n    --blue-soft:   #9beaff;\n    --blue-rgb:    53, 208, 255;\n    --blue-glow:   rgba(53, 208, 255, 0.3);\n\n    --teal:        #ff7aa8;\n    --teal-dark:   #e14d82;\n    --teal-soft:   #ffb0c7;\n    --teal-rgb:    255, 122, 168;\n\n    --bg:          #05141f;\n    --bg-card:     #0a2233;\n    --bg-hover:    #0f2d42;\n    --bg-input:    #143850;\n\n    --text:        #effaff;\n    --text-dim:    #9fc3d4;\n    --text-muted:  #5d8296;\n\n    --border:      #173a52;\n    --border-soft: rgba(125, 220, 255, 0.15);\n    --accent-rgb:  125, 220, 255;\n\n    /* le « vrai » des QCM reste un vert franc, distinct du cyan et du rose */\n    --green:       #4ade80;\n\n    --grad-brand:  linear-gradient(135deg, #35d0ff 0%, #ff7aa8 100%);\n    --grad-deep:   linear-gradient(160deg, #0a2a3f 0%, #05141f 60%);\n    --shadow-card: 0 2px 10px rgba(1, 8, 14, 0.55), 0 18px 44px -18px rgba(0, 150, 210, 0.3);\n    --shadow-pop:  0 8px 20px rgba(0, 0, 0, 0.38), 0 0 0 1px rgba(125, 220, 255, 0.16), 0 24px 70px -20px rgba(53, 208, 255, 0.45);\n\n    background: var(--bg);\n}\nbody.has-pneumo-field::after {\n    background:\n        radial-gradient(ellipse 55% 40% at 12% -5%, rgba(53, 208, 255, 0.13) 0%, transparent 65%),\n        radial-gradient(ellipse 45% 35% at 95% 8%, rgba(255, 122, 168, 0.08) 0%, transparent 60%),\n        radial-gradient(ellipse 60% 50% at 50% 115%, rgba(53, 208, 255, 0.07) 0%, transparent 70%);\n}\n/* barre de défilement du document (portée par <html>) */\nhtml.pneumo-root { scrollbar-color: #1d5d7d #05141f; }\nhtml.pneumo-root ::-webkit-scrollbar-track { background: #05141f; }\nhtml.pneumo-root ::-webkit-scrollbar-thumb {\n    background: linear-gradient(180deg, #1d5d7d, #123e56);\n    border-color: #05141f;\n}\n\n/* ---- variante claire : bleu respiratoire + rose profond sur papier d\'air ---- */\nhtml[data-theme="light"] body.has-pneumo-field {\n    --blue:        #087ea4;\n    --blue-dark:   #066583;\n    --blue-bright: #0b93bd;\n    --blue-soft:   #075f7d;\n    --blue-rgb:    8, 126, 164;\n    --blue-glow:   rgba(8, 126, 164, 0.22);\n\n    --teal:        #be3455;\n    --teal-dark:   #992844;\n    --teal-soft:   #a52d4a;\n    --teal-rgb:    190, 52, 85;\n\n    --bg:          #eef8fb;\n    --bg-card:     #ffffff;\n    --bg-hover:    #e2f2f7;\n    --bg-input:    #d9edf4;\n\n    --text:        #0b2536;\n    --text-dim:    #3e6074;\n    --text-muted:  #7d9aa9;\n\n    --border:      #cfe6ef;\n    --border-soft: rgba(8, 126, 164, 0.15);\n    --accent-rgb:  8, 126, 164;\n    --green:       #15803d;\n\n    --grad-brand:  linear-gradient(135deg, #087ea4 0%, #be3455 100%);\n    --shadow-card: 0 2px 8px rgba(8, 90, 120, 0.07), 0 16px 40px -18px rgba(8, 90, 120, 0.22);\n}\nhtml[data-theme="light"] body.has-pneumo-field::after { display: none !important; }\nhtml[data-theme="light"] body.has-pneumo-field { background: #eef8fb; }\nhtml[data-theme="light"] body.has-pneumo-field .navbar { background: rgba(238, 248, 251, 0.85); border-bottom-color: rgba(8, 126, 164, 0.12); }\nhtml[data-theme="light"] body.has-pneumo-field .navbar.scrolled { background: rgba(238, 248, 251, 0.96); box-shadow: 0 8px 30px rgba(8, 90, 120, 0.12); }\nhtml[data-theme="light"] body.has-pneumo-field .nav-link { color: #3e6074; }\nhtml[data-theme="light"] body.has-pneumo-field .nav-link:hover,\nhtml[data-theme="light"] body.has-pneumo-field .nav-link.active { color: #0b2536; background: rgba(8, 126, 164, 0.09); }\nhtml[data-theme="light"] body.has-pneumo-field .nav-menu { background: #eef8fb; }\nhtml[data-theme="light"].pneumo-root { scrollbar-color: #9ccadb #eef8fb; }\nhtml[data-theme="light"].pneumo-root ::-webkit-scrollbar-track { background: #eef8fb; }\nhtml[data-theme="light"].pneumo-root ::-webkit-scrollbar-thumb {\n    background: linear-gradient(180deg, #9ccadb, #77b3c9); border-color: #eef8fb;\n}\n\n/* ---------- AURORE : brume alvéolaire, violet + rose aurore ---------- */\nhtml[data-theme="aurora"] body.has-pneumo-field {\n    --blue:        #a78bfa;\n    --blue-dark:   #7c5ae0;\n    --blue-bright: #bda6ff;\n    --blue-soft:   #d8ccff;\n    --blue-rgb:    167, 139, 250;\n    --blue-glow:   rgba(167, 139, 250, 0.32);\n\n    --teal:        #f9a8d4;\n    --teal-dark:   #e56aa6;\n    --teal-soft:   #ffc4df;\n    --teal-rgb:    249, 168, 212;\n\n    --bg:          #140b24;\n    --bg-card:     #201236;\n    --bg-hover:    #2a1947;\n    --bg-input:    #34205a;\n\n    --text:        #f8f3ff;\n    --text-dim:    #c3b1e0;\n    --text-muted:  #7d6a9f;\n\n    --border:      #37205c;\n    --border-soft: rgba(190, 160, 255, 0.16);\n    --accent-rgb:  190, 160, 255;\n    --green:       #86efac;\n\n    --grad-brand:  linear-gradient(135deg, #a78bfa 0%, #f9a8d4 100%);\n    --grad-deep:   linear-gradient(160deg, #28174a 0%, #140b24 60%);\n    --shadow-card: 0 2px 10px rgba(8, 2, 18, 0.55), 0 18px 44px -18px rgba(140, 90, 250, 0.3);\n    --shadow-pop:  0 8px 20px rgba(0,0,0,.4), 0 0 0 1px rgba(190, 160, 255, .18), 0 24px 70px -20px rgba(167, 139, 250, .45);\n\n    background: var(--bg);\n}\nhtml[data-theme="aurora"] body.has-pneumo-field::after {\n    background:\n        radial-gradient(ellipse 55% 40% at 12% -5%, rgba(167, 139, 250, 0.15) 0%, transparent 65%),\n        radial-gradient(ellipse 45% 35% at 95% 8%, rgba(249, 168, 212, 0.08) 0%, transparent 60%),\n        radial-gradient(ellipse 60% 50% at 50% 115%, rgba(167, 139, 250, 0.08) 0%, transparent 70%);\n}\nhtml[data-theme="aurora"].pneumo-root { scrollbar-color: #54398c #140b24; }\nhtml[data-theme="aurora"].pneumo-root ::-webkit-scrollbar-track { background: #140b24; }\nhtml[data-theme="aurora"].pneumo-root ::-webkit-scrollbar-thumb {\n    background: linear-gradient(180deg, #54398c, #39255f); border-color: #140b24;\n}\n\n/* ---------- OCÉAN : oxygène dissous, turquoise + bulles d\'air ---------- */\nhtml[data-theme="ocean"] body.has-pneumo-field {\n    --blue:        #2dd4bf;\n    --blue-dark:   #14a394;\n    --blue-bright: #5eead4;\n    --blue-soft:   #99f6e4;\n    --blue-rgb:    45, 212, 191;\n    --blue-glow:   rgba(45, 212, 191, 0.3);\n\n    --teal:        #7dd3fc;\n    --teal-dark:   #38a8dd;\n    --teal-soft:   #bae6fd;\n    --teal-rgb:    125, 211, 252;\n\n    --bg:          #03202b;\n    --bg-card:     #06303f;\n    --bg-hover:    #0a4052;\n    --bg-input:    #0e4b61;\n\n    --text:        #ecfeff;\n    --text-dim:    #93c8d5;\n    --text-muted:  #548293;\n\n    --border:      #0d465c;\n    --border-soft: rgba(120, 225, 235, 0.15);\n    --accent-rgb:  120, 225, 235;\n    --green:       #86efac;\n\n    --grad-brand:  linear-gradient(135deg, #2dd4bf 0%, #7dd3fc 100%);\n    --grad-deep:   linear-gradient(160deg, #074052 0%, #03202b 60%);\n    --shadow-card: 0 2px 10px rgba(0, 10, 14, 0.55), 0 18px 44px -18px rgba(0, 180, 190, 0.3);\n    --shadow-pop:  0 8px 20px rgba(0,0,0,.38), 0 0 0 1px rgba(120, 225, 235, .18), 0 24px 70px -20px rgba(45, 212, 191, .45);\n\n    background: var(--bg);\n}\nhtml[data-theme="ocean"] body.has-pneumo-field::after {\n    background:\n        radial-gradient(ellipse 55% 40% at 12% -5%, rgba(45, 212, 191, 0.14) 0%, transparent 65%),\n        radial-gradient(ellipse 45% 35% at 95% 8%, rgba(125, 211, 252, 0.08) 0%, transparent 60%),\n        radial-gradient(ellipse 60% 50% at 50% 115%, rgba(45, 212, 191, 0.07) 0%, transparent 70%);\n}\nhtml[data-theme="ocean"].pneumo-root { scrollbar-color: #14606e #03202b; }\nhtml[data-theme="ocean"].pneumo-root ::-webkit-scrollbar-track { background: #03202b; }\nhtml[data-theme="ocean"].pneumo-root ::-webkit-scrollbar-thumb {\n    background: linear-gradient(180deg, #14606e, #0b3e49); border-color: #03202b;\n}\n'
SKIN_CSS_LESSON = '/* ---- fond PNEUMOLOGIE : même moteur que bio-field, palette air/alvéole ---- */\n#pneumoFieldCanvas {\n    position: fixed;\n    inset: 0;\n    z-index: -1;\n    pointer-events: none;\n}\nbody.has-pneumo-field {\n    background: var(--bg);\n}\nhtml[data-theme="light"] body.has-pneumo-field {\n    background: #e8f4f9;\n}\n'
PALETTE_JS = "    /* ---------------- palette PNEUMOLOGIE ---------------- */\n    /* cyan glacier = l'air oxygéné qui entre dans les voies aériennes\n       rose alvéole  = le tissu où l'échange se fait, grappe par grappe */\n    /* alignée exactement sur l'identité CSS has-pneumo-field (STANDARD-OR-v3 §9.1) */\n    var COL = { main: [53, 208, 255], sec: [255, 122, 168], acc: [154, 165, 212] };\n    /* une atmosphère par thème, calée sur la palette CSS correspondante */\n    var THEME_MAP = {\n        '':        [[ 53, 208, 255], [255, 122, 168]],   /* air nocturne : cyan + rose   */\n        dark:      [[ 53, 208, 255], [255, 122, 168]],\n        light:     [[  8, 126, 164], [190,  52,  85]],   /* air clair : bleu + rose prof. */\n        aurora:    [[167, 139, 250], [249, 168, 212]],   /* brume alvéolaire              */\n        ocean:     [[ 45, 212, 191], [125, 211, 252]]    /* oxygène dissous + bulles      */\n    };\n"

def apply_skin(site):
    site = Path(site)
    bio = site / 'js' / 'bio-field.js'
    out = site / 'js' / 'pneumo-field.js'
    if bio.exists() and not out.exists():
        s = bio.read_text(encoding='utf-8')
        s = s.replace('CHAMP DE RÉACTIFS (bio-field v1)', 'CHAMP D’AIR ALVÉOLAIRE (pneumo-field v1)')
        s = re.sub(r'palette BIOCHIMIE :.*?sérum doré »\.', 'palette PNEUMOLOGIE :\n   cyan glacier « air oxygéné » + rose « tissu alvéolaire ».', s, count=1, flags=re.S)
        s = s.replace("document.getElementById('bioFieldCanvas')", "document.getElementById('pneumoFieldCanvas')")
        old = re.search(r"    /\* ---------------- palette BIOCHIMIE ---------------- \*/.*?    \};\n", s, re.S)
        assert old, 'bloc palette bio introuvable dans bio-field.js'
        s = s[:old.start()] + PALETTE_JS + s[old.end():]
        s = s.replace('rgba(238, 250, 242,', 'rgba(240, 251, 255,')
        s = s.replace('window.__heroField', 'window.__pneumoField')
        out.write_text(s, encoding='utf-8')
        print('[peau] js/pneumo-field.js créé')
    p = site / 'css' / 'style.css'
    s = p.read_text(encoding='utf-8')
    if 'has-pneumo-field' not in s:
        marker = '/* ============================================================\n   INDICE DU CHAMP'
        assert marker in s, 'marqueur INDICE introuvable dans style.css'
        s = s.replace(marker, SKIN_CSS_STYLE + '\n' + marker, 1)
        for old, new in [
            ('body.fond-fixe #cardioFieldCanvas,', 'body.fond-fixe #cardioFieldCanvas,\nbody.fond-fixe #pneumoFieldCanvas,'),
            ('body.fond-photo-pris #cardioFieldCanvas,', 'body.fond-photo-pris #cardioFieldCanvas,\nbody.fond-photo-pris #pneumoFieldCanvas,')]:
            assert old in s, old
            s = s.replace(old, new, 1)
        p.write_text(s, encoding='utf-8')
        print('[peau] style.css : identité pneumo + sélecteurs de modes')
    p = site / 'css' / 'lesson.css'
    s = p.read_text(encoding='utf-8')
    if 'pneumoFieldCanvas' not in s:
        anchor = 'html[data-theme="light"] body.has-cardio-field {\n    background: #f7ecec;\n}\n'
        s = s.replace(anchor, anchor + '\n' + SKIN_CSS_LESSON, 1) if anchor in s else s + '\n' + SKIN_CSS_LESSON
        p.write_text(s, encoding='utf-8')
        print('[peau] lesson.css : canvas pneumo')
    p = site / 'js' / 'main.js'
    s = p.read_text(encoding='utf-8')
    if 'pneumo-root' not in s:
        anchor = "    if (document.body.classList.contains('has-bio-field')) {\n        htmlEl.classList.add('bio-root');\n    }\n"
        assert anchor in s, 'ancre bio-root introuvable dans main.js'
        s = s.replace(anchor, anchor + "\n    /* ---------- MODULE PNEUMOLOGIE : teinter aussi <html> ---------- */\n    if (document.body.classList.contains('has-pneumo-field')) {\n        htmlEl.classList.add('pneumo-root');\n    }\n", 1)
        p.write_text(s, encoding='utf-8')
        print('[peau] main.js : racine pneumo-root')

if __name__ == '__main__':
    PAGES = {'bi-06': 'bi-06-biomarqueurs-cardiaques.html',
             'pn-01': 'pn-01-dyspnee.html',
             'pn-04': 'pn-04-expectoration.html'}
    site = Path(sys.argv[1])
    lids = sys.argv[2:] or list(PAGES)
    apply_skin(site)
    for lid in lids:
        f = site / 'lecons' / PAGES[lid]
        repair(str(f), str(f), lid)
