#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pn08.py — Construit la page gold pn-08 « Les syndromes médiastinaux ».

Méthode : châssis cloné de pn-01 (page auditée 0 bloquant), contenu généré
depuis contenu_a/b + qcm_pn08 + kw_fc_pn08. Invariant : l'ensemble des
data-tr de la page == l'ensemble des clés arData (vérifié en fin de build).
Patron QCM = ca-02/STANDARD §3 (5 .qexp-item). Pas de data-tr sur
.qcm-focus ni .reel-strip (patron ca-02 ; ar-mode.js casse les valeurs
liste/figure de pn-01 en mode AR).
"""
import re, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenu_a import SECTIONS_A
from contenu_b import (SECTIONS_B, VUE, MM_SUB_FR, MM_SUB_AR, METHODE,
                       CONNEXIONS, FICHE, CINE_CHAPITRES, RT_SUB_FR, RT_SUB_AR)
from qcm_pn08 import ANNALES, ENTRAINEMENT
from kw_fc_pn08 import KW, FC

SITE = "/tmp/site/medstudy"
SRC = open(f"{SITE}/lecons/pn-01-dyspnee.html", encoding="utf-8").read()
OUT = f"{SITE}/lecons/pn-08-syndromes-mediastinaux.html"
AR = {}   # arData, rempli par les renderers

def need(cond, msg):
    if not cond: raise SystemExit("BUILD FAIL: " + msg)

def cut(a, b, name, src=SRC):
    i = src.find(a); need(i >= 0, f"{name}: début introuvable ({a[:40]}…)")
    j = src.find(b, i + len(a)); need(j > i, f"{name}: fin introuvable ({b[:40]}…)")
    return src[i:j]

# ---------- vérifications de patrons pn-01 (affichées pour contrôle) ----------
mh = re.search(r'<div class="lsection-num n1">.*?</div>', SRC, re.S)
print("• patron lsection-num:", mh.group(0) if mh else "ABSENT")
me = re.search(r'id="entrainement".*?<span class="qsrc[^>]*>.*?</span>', SRC, re.S)
print("• qsrc entraînement pn-01:", (me.group(0)[-160:] if me else "ABSENT"))
TRAIN_SRC_FMT = None
if me:
    m2 = re.search(r'<span class="(qsrc[^"]*)"><i class="(fa-solid [^"]+)"></i>', me.group(0))
    if m2: TRAIN_SRC_FMT = (m2.group(1), m2.group(2))
print("• classes qsrc entraînement:", TRAIN_SRC_FMT)

# ---------- 1. HEAD + HERO (clonés pn-01, adaptés) ----------
head = cut("<!DOCTYPE html>", "</header>", "head-hero") + "</header>"
repl = [
 ("<title>Sémiologie de la dyspnée — SEENmed</title>", "<title>Les syndromes médiastinaux — SEENmed</title>"),
 ("../css/keywords.css?v=3", "../css/keywords.css?v=4"),
 ('<body data-lesson-id="pn-01"', '<body data-lesson-id="pn-08"'),
 ("<span>Leçon 1</span>", "<span>Leçon 8</span>"),
 ('<h1>Sémiologie de la <span class="highlight">dyspnée</span></h1>',
  '<h1>Les syndromes <span class="highlight">médiastinaux</span></h1>'),
 ("6 QCM d'annales + 20 d'entraînement", "7 QCM d'annales + 12 d'entraînement"),
 ("Dr Seddini, A — Médecine interne, EHU Oran", "Dr BELMILOUD H — Maître de conférences B, Sémiologie, Faculté de Médecine d’Oran"),
 ("Les 6 annales", "Les 7 annales"), ("Les 20 QCM", "Les 12 QCM"),
]
for a, b in repl:
    need(a in head, f"hero: introuvable «{a[:40]}»"); head = head.replace(a, b, 1)
head = re.sub(r'<img src="\.\./assets/img/pn-01/hero\.webp"[^>]*>',
 '<img src="../assets/img/pn-08/hero.webp" alt="Aux urgences, un patient assis sur un brancard : visage et cou œdémateux, lèvres et mains cyanosées, veines jugulaires saillantes, fine circulation veineuse sur le haut du thorax, le médecin examine son cou, moniteur et matériel d’urgence en arrière-plan" loading="eager" width="1376" height="768">',
 head, count=1)
need('pn-08/hero.webp' in head, "hero img non remplacée")

# ---------- helpers de rendu ----------
def ic(name): return f'fa-solid {name}'
def lsub(key, fr):
    return f'<div class="lsub" data-tr="{key}">{fr}</div>'
def sec_head(num_html, titre, subkey, subfr):
    return (f'<div class="lsection-head">\n                    {num_html}\n'
            f'                    <div>\n                        <h2>{titre}</h2>\n'
            f'                        {lsub(subkey, subfr)}\n                    </div>\n                </div>')
def numdiv(n): return f'<div class="lsection-num n{n}">{n}</div>'
def icondiv(icon): return f'<div class="lsection-num icon-only"><i class="{ic(icon)}"></i></div>'

def render_box(b):
    li_fr = "\n".join(f"                        <li>{x}</li>" for x in b["li"])
    html = (f'<div class="lbox reveal" data-tr="{b["key"]}">\n'
            f'                    <div class="lbox-title"><i class="{ic(b["icon"])}"></i> {b["titre"]}</div>\n'
            f'                    <ul>\n{li_fr}\n                    </ul>\n                </div>')
    AR[b["key"]] = (f'<div class="lbox-title"><i class="{ic(b["icon"])}"></i> {b["titre_ar"]}</div>'
                    f'<ul>' + "".join(f"<li>{x}</li>" for x in b["li_ar"]) + "</ul>")
    return html

def render_mini(b):
    wrap = "lgrid2" if b["cols"] == 2 else "mini-grid cols-3"
    cards = []
    for c in b["cards"]:
        li = "\n".join(f"                            <li>{x}</li>" for x in c["li"])
        cards.append(f'<div class="mini-card {c["acc"]} reveal" data-tr="{c["key"]}">\n'
                     f'                        <h4><i class="{ic(c["icon"])}"></i> {c["titre"]}</h4>\n'
                     f'                        <ul>\n{li}\n                        </ul>\n                    </div>')
        AR[c["key"]] = (f'<h4><i class="{ic(c["icon"])}"></i> {c["titre_ar"]}</h4><ul>'
                        + "".join(f"<li>{x}</li>" for x in c["li_ar"]) + "</ul>")
    return f'<div class="{wrap}">\n' + "\n".join(cards) + "\n                </div>"

def render_table(b):
    th = "".join(f"<th>{h}</th>" for h in b["th"])
    rows = "\n".join("                            <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
    html = (f'<div class="ltable-wrap reveal">\n                    <table class="ltable" data-tr="{b["key"]}">\n'
            f'                        <thead><tr>{th}</tr></thead>\n                        <tbody>\n{rows}\n                        </tbody>\n                    </table>\n                </div>')
    th_ar = "".join(f"<th>{h}</th>" for h in b["th_ar"])
    rows_ar = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows_ar"])
    AR[b["key"]] = f'<thead><tr>{th_ar}</tr></thead><tbody>{rows_ar}</tbody>'
    return html

def render_focus(li):
    items = "\n".join(f"                        <li>{x}</li>" for x in li)
    return ('<div class="qcm-focus reveal">\n'
            '                    <span class="qf-sub">Ce que l’examinateur peut fabriquer avec cette seule section</span>\n'
            f'                    <ul>\n{items}\n                    </ul>\n                </div>')

def render_board(board):
    img, w, h, alt, cap = board
    return (f'<figure class="section-visual reveal">\n'
            f'                    <img src="../assets/img/pn-08/{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}">\n'
            f'                    <figcaption>{cap}</figcaption>\n                </figure>')

def render_reel(reel):
    src_line, figs = reel
    fs = []
    for f, w, h, alt, cap in figs:
        fs.append(f'<figure>\n                            <img src="../assets/img/pn-08/reel/{f}" alt="{alt}" loading="lazy" width="{w}" height="{h}">\n'
                  f'                            <figcaption>{cap}</figcaption>\n                        </figure>')
    return ('<div class="reel-strip reveal">\n'
            f'                    <p class="reel-head">Document original du cours<span class="reel-src">{src_line}</span></p>\n'
            f'                    <div class="reel-grid">\n' + "\n".join(fs) + '\n                    </div>\n                </div>')

def render_section(s, n):
    AR[f"s{n}-sub"] = s["sub_ar"]
    parts = [f'<section class="lsection" id="{s["sid"]}">',
             sec_head(numdiv(n), s["titre"], f"s{n}-sub", s["sub_fr"])]
    if s.get("board"): parts.append(render_board(s["board"]))
    parts.append(f'<div class="cine-spot reveal" data-ch="{s["ch"]}"></div>')
    if s.get("reel") and s["sid"] != "etiologies": parts.append(render_reel(s["reel"]))
    for b in s["blocs"]:
        if b["type"] == "box": parts.append(render_box(b))
        elif b["type"] == "mini": parts.append(render_mini(b))
        elif b["type"] == "table": parts.append(render_table(b))
        elif b["type"] == "focus": parts.append(render_focus(b["li"]))
    if s.get("reel") and s["sid"] == "etiologies": parts.append(render_reel(s["reel"]))
    parts.append("</section>")
    return "\n\n".join(parts)

def render_qblock(q, i, kind, src_fmt):
    key = f"{'ann' if kind=='ann' else 'entr'}-exp-{i}"
    ans_json = "[" + ", ".join(f'"{a}"' for a in q["ans"]) + "]"
    letters = "ABCDE"
    lis = "\n".join(f'<li data-l="{L}"><span class="ql">{L}</span><span class="qtxt">{p}</span><span class="xe"></span></li>'
                    for L, p in zip(letters, q["props"]))
    def items(exp, yes, no):
        return "\n".join(
            f'<div class="qexp-item {tf}"><b>{L} — {yes if tf=="t" else no}</b> {x}</div>'
            for (tf, x), L in zip(exp, letters))
    ans_disp = "".join(q["ans"])
    html = (f'<div class="qblock reveal" data-answer=\'{ans_json}\'>\n'
            f'                  <div class="qhead">\n'
            f'                    <div class="qtext">{i}. {q["q"]}</div>\n'
            f'                    <span class="{src_fmt[0]}"><i class="{src_fmt[1]}"></i> {q["src"]}</span>\n'
            f'                  </div>\n'
            f'                  <ul class="qch">\n{lis}\n                  </ul>\n'
            f'                  <div class="qverdict"></div>\n'
            f'                  <div class="qexp" data-tr="{key}">\n'
            f'                    <div class="qexp-title"><i class="fa-solid fa-circle-check"></i> Réponse : {ans_disp} — correction, proposition par proposition</div>\n'
            + items(q["exp_fr"], "À COCHER.", "À NE PAS COCHER.") + "\n"
            f'                    <div class="qexp-memo"><i class="fa-solid fa-star"></i><div>{q["memo_fr"]}</div></div>\n'
            f'                  </div>\n'
            f'                  <div class="qcheck-row"><button class="btn btn-primary btn-sm qcheck"><i class="fa-solid fa-check"></i> Corriger ma réponse</button></div>\n'
            f'                </div>')
    AR[key] = (f'<div class="qexp-title"><i class="fa-solid fa-circle-check"></i> الإجابة: <bdi class="fr-plain">{ans_disp}</bdi> — التصحيح، اقتراحاً باقتراح</div>'
               + "".join(f'<div class="qexp-item {tf}"><b>{L} — {"تُعلَّم." if tf=="t" else "لا تُعلَّم."}</b> {x}</div>' for (tf, x), L in zip(q["exp_ar"], letters))
               + f'<div class="qexp-memo"><i class="fa-solid fa-star"></i><div>{q["memo_ar"]}</div></div>')
    return html

def qcm_section_head(sid, icon, titre, sub):
    return (f'<section class="lsection" id="{sid}" data-qcm-set="{sid}">\n'
            f'                <div class="lsection-head">\n                    {icondiv(icon)}\n'
            f'                    <div>\n                        <h2>{titre}</h2>\n'
            f'                        <div class="lsub">{sub}</div>\n                    </div>\n                </div>\n'
            f'                <div class="qcm-section-head reveal"><span class="chip chip-qcm"><i class="fa-solid fa-trophy"></i> Score de la session : <span class="qs-val">0 / 0</span></span><span class="chip"><i class="fa-solid fa-circle-info"></i> Plusieurs réponses possibles — coche tout ce qui est juste, puis corrige</span></div>')

# ---------- 2. NAVIGATION DE LEÇON ----------
SECTIONS = SECTIONS_A + SECTIONS_B
tabs = [("vue","fa-compass","Vue d'ensemble",True),("mindmap","fa-sitemap","Mind Map",False),("cine","fa-clapperboard","Ciné",False)]
for i, s in enumerate(SECTIONS, 1):
    tabs.append((s["sid"], s["icon"].replace("fa-","",1) if s["icon"].startswith("fa-") else s["icon"], f"{i}. {s['nav']}", False))
tabs += [("methode","fa-user-secret","Méthode EMD",False),("connexions","fa-link","Connexions",False),
         ("annales","fa-award","QCM annales",False),("entrainement","fa-bullseye","Entraînement",False),
         ("fiche","fa-bolt","Fiche flash",False),("flashcards","fa-clone","Flashcards",False),
         ("resume-total","fa-image","Résumé total",False)]
tab_html = "\n".join(
    f'                <button class="ltab{" active" if act else ""}" data-target="{t}"><i class="fa-solid {icn if icn.startswith("fa-") else "fa-"+icn}"></i> {label}</button>'
    for t, icn, label, act in tabs)
nav = f'''
<!-- ============ NAVIGATION DE LEÇON ============ -->
    <div class="lesson-nav" id="lessonNav">
        <div class="lesson-nav-inner">
            <div class="lesson-tabs">
{tab_html}
            </div>
            <div class="lesson-progress-wrap">
                <span id="lessonProgressPct">0%</span>
                <div class="lesson-progress-bar"><div class="lesson-progress-fill" id="lessonProgressFill"></div></div>
            </div>
        </div>
    </div>

        <!-- ============ CORPS DE LEÇON ============ -->
    <main class="lesson-body">
        <div class="container">
'''

# ---------- 3. VUE D'ENSEMBLE ----------
AR["vue-sub"] = VUE["sub_ar"]
AR["transp"] = (f'<div class="lbox-title"><i class="fa-solid fa-circle-info"></i> {VUE["transp_titre_ar"]}</div><ul>'
                + "".join(f"<li>{x}</li>" for x in VUE["transp_ar"]) + "</ul>")
essence = "\n".join(f"                            <li>{x}</li>" for x in VUE["essence"])
road = "\n".join(f'                            <li><b>{t}</b> — {d} <span class="rm-time">{m}</span></li>' for t, d, m in VUE["roadmap"])
transp = "\n".join(f"                        <li>{x}</li>" for x in VUE["transp"])
vb = VUE["vue_board"]
vue_html = f'''<!-- ═══════════════ VUE D'ENSEMBLE ═══════════════ -->
            <section class="lsection" id="vue">
{ sec_head(icondiv("fa-compass"), "Vue d’ensemble — l’essentiel en 60 secondes", "vue-sub", VUE["sub_fr"]) }

                <div class="overview-grid">
                    <div class="essence reveal">
                        <h3><i class="fa-solid fa-bolt"></i> L’essentiel</h3>
                        <ul>
{essence}
                        </ul>
                    </div>

                    <div class="roadmap reveal" data-delay="1">
                        <h3><i class="fa-solid fa-route"></i> Feuille de route</h3>
                        <ol>
{road}
                        </ol>
                    </div>
                </div>

                                <div class="lbox reveal" data-tr="transp">
                    <div class="lbox-title"><i class="fa-solid fa-circle-info"></i> {VUE["transp_titre"]}</div>
                    <ul>
{transp}
                    </ul>
                </div>

                                <figure class="section-visual reveal">
                    <img src="../assets/img/pn-08/{vb[0]}" alt="{vb[3]}" loading="lazy" width="{vb[1]}" height="{vb[2]}">
                    <figcaption>{vb[4]}</figcaption>
                </figure>
            </section>
'''

# ---------- 4. MINDMAP + CINÉ ----------
AR["mm-sub"] = MM_SUB_AR
mindmap_html = f'''
            <!-- ═══════════════ MIND MAP ═══════════════ -->
            <section class="lsection" id="mindmap">
{ sec_head(icondiv("fa-sitemap"), "Mind map — la leçon en une image", "mm-sub", MM_SUB_FR) }

                                <figure class="total-poster reveal">
                    <img src="../assets/img/pn-08/mindmap.webp" alt="Carte mentale des syndromes médiastinaux dessinée sur un tableau de salle de cours : nœud central avec le médiastin, cinq branches — anatomie en 9 loges, signes respiratoires, syndrome cave supérieur, nerfs, imagerie et étiologies — chacune avec un petit dessin" loading="lazy" width="1376" height="768">
                    <figcaption>🗺️ <b>La carte complète</b> — cinq branches, dans l’ordre où l’examinateur te fait raisonner</figcaption>
                </figure>
            </section>
            <section class="lsection" id="cine"><div class="lsection-head"><div class="lsection-num icon-only"><i class="fa-solid fa-clapperboard"></i></div><div><h2>Ciné-révision — la leçon racontée</h2><div class="lsub">Les planches défilent, la voix explique en reliant les idées : <b>6 chapitres en français</b>, plus le <b>résumé total en français et en arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.</div></div></div><div id="cinePlayer" class="reveal"></div></section>
'''

# ---------- 5. SECTIONS 1-14 ----------
sections_html = "\n\n".join(
    f'            <!-- ═══════════════ {i}. {s["nav"].upper()} ═══════════════ -->\n            ' + render_section(s, i)
    for i, s in enumerate(SECTIONS, 1))

# ---------- 6. MÉTHODE ----------
AR["m-sub"] = METHODE["sub_ar"]
methode_html = f'''
            <!-- ═══════════════ MÉTHODE EMD ═══════════════ -->
            <section class="lsection" id="methode">
{ sec_head(icondiv("fa-user-secret"), METHODE["titre"], "m-sub", METHODE["sub_fr"]) }

{ render_table({"key":"m-tab1","th":METHODE["th"],"rows":METHODE["rows"],"th_ar":METHODE["th_ar"],"rows_ar":METHODE["rows_ar"]}) }

{ render_box({"key":"m-box1","icon":"fa-scale-balanced","titre":METHODE["box_titre"],"li":METHODE["box"],"titre_ar":METHODE["box_titre_ar"],"li_ar":METHODE["box_ar"]}) }

{ render_focus(METHODE["focus"]) }
            </section>
'''

# ---------- 7. CONNEXIONS ----------
AR["cx-sub"] = CONNEXIONS["sub_ar"]
connexions_html = f'''
            <!-- ═══════════════ CONNEXIONS ═══════════════ -->
            <section class="lsection" id="connexions">
{ sec_head(icondiv("fa-link"), CONNEXIONS["titre"], "cx-sub", CONNEXIONS["sub_fr"]) }

{ render_mini({"cols":3,"cards":CONNEXIONS["cards"]}) }

{ render_box({"key":"cx-box","icon":"fa-lightbulb","titre":CONNEXIONS["box_titre"],"li":CONNEXIONS["box"],"titre_ar":CONNEXIONS["box_titre_ar"],"li_ar":CONNEXIONS["box_ar"]}) }
            </section>
'''

# ---------- 8. QCM ----------
ANN_FMT = ("qsrc src-annale", "fa-solid fa-landmark")
TR_FMT = TRAIN_SRC_FMT or ("qsrc", "fa-solid fa-dumbbell")
ann_html = f'''
            <!-- ═══════════════ QCM ANNALES ═══════════════ -->
            {qcm_section_head("annales","fa-award","QCM d’annales — les 7 questions réelles","Recueil <b>ELITE CARDIO 3ᵉ année</b> — Sémiologie UI1 §8 « Syndromes médiastinaux » (4 QCM, p. 22) + Radiologie UI1 §11 « Syndrome médiastinal » (3 QCM, p. 43), PROMO 2018 → 2022. Énoncés et <b>corrigés officiels</b> reproduits à l’identique — aucun choix inventé. Coche, valide, puis lis pourquoi, proposition par proposition.")}

''' + "\n\n".join(render_qblock(q, i, "ann", ANN_FMT) for i, q in enumerate(ANNALES, 1)) + "\n            </section>\n"
entr_html = f'''
            <!-- ═══════════════ ENTRAÎNEMENT ═══════════════ -->
            {qcm_section_head("entrainement","fa-bullseye","Entraînement — 12 QCM calibrés sur les annales","Calibration calquée sur la distribution officielle des 7 annales (1 bonne ×3 · 2 ×2 · 3 ×2) : ici <b>3 questions à 1 bonne réponse</b>, <b>5 à 2</b>, <b>4 à 3</b>. Toutes les réponses sortent des diapos du cours ou des corrigés officiels — rien d’inventé.")}

''' + "\n\n".join(render_qblock(q, i, "entr", TR_FMT) for i, q in enumerate(ENTRAINEMENT, 1)) + "\n            </section>\n"

# ---------- 9. FICHE FLASH ----------
cells = []
for c in FICHE["cells"]:
    lis = "".join(f"<li>{x}</li>" for x in c["li"])
    cells.append(f'<div class="flash-cell {c["cls"]}"><h4><i class="{ic(c["icon"])}"></i> {c["titre"]}</h4>'
                 f'<img class="flash-img" src="../assets/img/pn-08/{c["img"]}" alt="{c["alt"]}" loading="lazy" width="{c["imgw"]}" height="{c["imgh"]}"><ul>{lis}</ul></div>')
fiche_head = ('<section class="lsection" id="fiche">\n'
              '                <div class="lsection-head">\n'
              '                    <div class="lsection-num icon-only"><i class="fa-solid fa-bolt"></i></div>\n'
              '                    <div>\n                        <h2>Fiche flash — la leçon en un coup d’œil</h2>\n'
              '                        <div class="lsub">Quatre cases, quatre planches — les faits et les pièges de dernière minute, à relire dans l’ordre. L’encadré qui suit se récite à voix haute.</div>\n'
              '                    </div>\n                </div>')
AR["ff-box1"] = (f'<div class="lbox-title"><i class="fa-solid fa-camera"></i> {FICHE["box_titre_ar"]}</div>'
                 f'<ul><li>{FICHE["box_ar"]}</li></ul>')
fiche_html = f'''
            <!-- ═══════════════ FICHE FLASH ═══════════════ -->
            {fiche_head}

                <div class="flashsheet ff-2x2 reveal">{"".join(cells)}</div>

                <div class="lbox reveal" data-tr="ff-box1">
                    <div class="lbox-title"><i class="fa-solid fa-camera"></i> {FICHE["box_titre"]}</div>
                    <ul>
                        <li>{FICHE["box"]}</li>
                    </ul>
                </div>
            </section>
'''

# ---------- 10. FLASHCARDS (coquille clonée) + RÉSUMÉ TOTAL ----------
fc_shell = cut('<section class="lsection" id="flashcards">', '<section class="lsection" id="resume-total">', "flashcards")
need("25 cartes" in fc_shell, "flashcards: «25 cartes» introuvable")
fc_shell = fc_shell.replace("25 cartes", "30 cartes").rstrip() + "\n\n"
AR["rt-sub"] = RT_SUB_AR
resume_html = f'''
            <!-- ═══════════════ RÉSUMÉ TOTAL ═══════════════ -->
            <section class="lsection" id="resume-total">
{ sec_head(icondiv("fa-image"), "Résumé total — la grande planche", "rt-sub", RT_SUB_FR) }

                <figure class="total-poster reveal">
                    <img src="../assets/img/pn-08/total.webp" alt="Grande planche de synthèse des syndromes médiastinaux : grille des 9 loges sur coupe sagittale, patient avec signes du syndrome cave supérieur, radio thoracique avec médiastin élargi et trois vignettes d’étiologies par loge — goitre plongeant, masse thymique, tumeur nerveuse paravertébrale" loading="lazy" width="1376" height="768">
                    <figcaption>🖼️ <b>Le poster final</b> — à réexporter dans tes fiches personnelles</figcaption>
                </figure><div class="cine-spot reveal" data-ch="6"></div>
            </section>
'''

# ---------- 11. FOOTER + MOTEURS (clonés pn-01) ----------
i_rt = SRC.find("</section>", SRC.find('id="resume-total"'))
j_main = SRC.find("        </div>\n    </main>", i_rt)
tail = SRC[j_main:SRC.find('<script type="application/json" id="cineData">', j_main)]
need("Autre leçon" in tail, "footer: autre leçon introuvable")
tail = tail.replace('<a href="ca-02-douleurs-thoraciques.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-right"></i> Autre leçon : Les douleurs thoraciques</a>',
                    '<a href="pn-01-dyspnee.html" class="btn btn-outline btn-sm"><i class="fa-solid fa-arrow-right"></i> Autre leçon : Sémiologie de la dyspnée</a>')
tail = tail.replace('Leçon « Sémiologie de la dyspnée » · Pneumologie · Dr Seddini, A — EHU Oran',
                    'Leçon « Les syndromes médiastinaux » · Pneumologie · Dr BELMILOUD H — Faculté de Médecine d’Oran')
need("pn-01-dyspnee.html" in tail and "BELMILOUD" in tail, "footer non adapté")
engines = SRC[SRC.find('<script src="../js/bg-mode.js'):]
need(engines.rstrip().endswith("</html>"), "moteurs: fin de fichier inattendue")

# ---------- 12. JSON ----------
def jsdump(obj):
    s = json.dumps(obj, ensure_ascii=False)
    need("</script>" not in s, "JSON contient </script>")
    return s
cine_json = jsdump({"chapitres": CINE_CHAPITRES})
kw_json = jsdump([{"t": t, "s": s, "n": n, "d": d, "a": a} for t, s, n, d, a in KW])
fc_json = jsdump([{"id": f"pn08-{i:02d}", "q": q, "a": a} for i, (q, a) in enumerate(FC, 1)])
scripts_json = (f'<script type="application/json" id="cineData">{cine_json}</script>\n'
                f'<script type="application/json" id="kwData">{kw_json}</script>\n'
                f'<script type="application/json" id="fcData">{fc_json}</script>\n'
                f'<script type="application/json" id="arData">{jsdump(AR)}</script>\n')

# ---------- 13. ASSEMBLAGE + AUTO-CONTRÔLES ----------
page = (head + nav + vue_html + mindmap_html + sections_html + methode_html +
        connexions_html + ann_html + entr_html + fiche_html +
        "\n            <!-- ═══════════════ FLASHCARDS ═══════════════ -->\n            " + fc_shell +
        resume_html + tail + scripts_json + engines)

tr_keys = set(re.findall(r'data-tr="([^"]+)"', page))
need(tr_keys == set(AR), f"data-tr != arData | page-only={sorted(tr_keys-set(AR))} ar-only={sorted(set(AR)-tr_keys)}")
tr_all = re.findall(r'data-tr="([^"]+)"', page)
need(len(tr_all) == len(set(tr_all)), "data-tr en double")
need(page.count('<div class="qblock') == 19, f"qblocks={page.count('qblock')}")
QEXP_N = page.count('class="qexp-item ')
need(QEXP_N == 19 * 5, f"qexp-item={QEXP_N}")
spots = sorted(int(x) for x in re.findall(r'cine-spot reveal" data-ch="(\d+)"', page))
need(max(spots) == 6 and len(spots) == 15, f"cine-spots={spots}")
imgs = sorted(set(re.findall(r'src="(\.\./assets/[^"]+)"', page)))
missing = [p for p in imgs if not os.path.exists(os.path.join(SITE, p[3:]))]
need(not missing, f"images manquantes: {missing}")
aud = sorted(set(re.findall(r'"(\.\./assets/audio/pn-08/[^"]+)"', cine_json)))
missing_a = [p for p in aud if not os.path.exists(os.path.join(SITE, p[3:]))]
need(not missing_a, f"audios manquants: {missing_a}")
need(page.index('id="arData"') < page.index('../js/bg-mode.js'), "ordre JSON/moteurs")
secs = re.findall(r'<section class="lsection" id="([^"]+)"', page)
tab_targets = re.findall(r'data-target="([^"]+)"', page)
need(secs == tab_targets, f"sections != tabs\n{secs}\n{tab_targets}")

open(OUT, "w", encoding="utf-8").write(page)
print(f"\n✅ PAGE ÉCRITE : {OUT} ({len(page)//1024} Ko)")
print(f"   sections={len(secs)} · data-tr/arData={len(tr_keys)} · qblocks=19 · qexp-item=95")
print(f"   cine-spots={spots}")
print(f"   images référencées={len(imgs)} (toutes présentes) · audios={len(aud)}")
print(f"   kwData={len(KW)} · fcData={len(FC)} · chapitres={len(CINE_CHAPITRES)}")
