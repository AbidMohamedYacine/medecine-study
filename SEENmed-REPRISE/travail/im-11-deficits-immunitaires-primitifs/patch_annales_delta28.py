# -*- coding: utf-8 -*-
"""PATCH DELTA 28 — ajoute les 17 annales vérifiées à la page im-11 LIVRÉE (delta 27).
Patch différentiel sur les octets livrés (règle N-1 → N) : aucune reconstruction de châssis.
Entrées : bench (page delta 27 + pn-01 pour TRAIN_SRC_FMT), annales_im11.py, build_im11.py (renderers)."""
import re, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = "/tmp/site/medstudy/lecons/im-11-deficits-immunitaires-primitifs.html"

# ── renderers du builder (tête du fichier, avant la navigation) ──
builder = open(os.path.join(HERE, "build_im11.py"), encoding="utf-8").read()
head_src = builder.split("# ---------- 2. NAVIGATION DE LEÇON")[0]
ns = {"__name__": "builder_head", "__file__": os.path.join(HERE, "build_im11.py")}
exec(compile(head_src, "build_im11_head", "exec"), ns)
render_qblock = ns["render_qblock"]; qcm_section_head = ns["qcm_section_head"]; AR = ns["AR"]
ANN_FMT = ("qsrc src-annale", "fa-solid fa-landmark")

from annales_im11 import ANNALES
ann_html = (
    "\n            <!-- ═══════════════ ANNALES ═══════════════ -->\n            "
    + qcm_section_head("annales", "fa-landmark",
        "QCM d’annales — 21 questions d’examens (Oran, P2014–P2022)",
        "Questions réelles des promotions 2014, 2018 à 2022 (recueil « CURE – IMMUNO 3<sup>ème</sup> (Oran) », chapitre <i>Déficits Immunitaires</i>), corrigés revérifiés proposition par proposition contre le cours. Distribution : <b>8 questions à 1 bonne réponse</b> (dont 4 au format « la réponse fausse »), <b>4 à 2</b>, <b>8 à 3</b>, <b>1 à 4</b>.")
    + "\n\n" + "\n\n".join(render_qblock(q, i, "ann", ANN_FMT) for i, q in enumerate(ANNALES, 1))
    + "\n            </section>\n")

h = open(PAGE, encoding="utf-8").read()
orig_len = len(h)

def rep(old, new, n=1):
    global h
    assert h.count(old) == n, (old[:70], h.count(old))
    h = h.replace(old, new)

# 1. Section annales avant l'entraînement
rep("            <!-- ═══════════════ ENTRAÎNEMENT ═══════════════ -->",
    ann_html + "\n            <!-- ═══════════════ ENTRAÎNEMENT ═══════════════ -->")

# 2. Onglet nav avant l'onglet entraînement
rep('<button class="ltab" data-target="entrainement"><i class="fa-solid fa-bullseye"></i> QCM entraînement</button>',
    '<button class="ltab" data-target="annales"><i class="fa-solid fa-landmark"></i> QCM d\'annales</button>\n                '
    '<button class="ltab" data-target="entrainement"><i class="fa-solid fa-bullseye"></i> QCM entraînement</button>')

# 3. Chip hero + bouton annales
rep('<span class="chip chip-qcm"><i class="fa-solid fa-bullseye"></i> 15 QCM d\'entraînement</span>',
    '<span class="chip chip-qcm"><i class="fa-solid fa-bullseye"></i> 21 QCM d\'annales + 15 d\'entraînement</span>')
rep('<a href="#entrainement" class="btn btn-outline">',
    '<a href="#annales" class="btn btn-outline"><i class="fa-solid fa-award"></i> Les 21 annales</a>\n                    <a href="#entrainement" class="btn btn-outline">')

# 4. Sous-titre entraînement (FR plain)
rep("Aucun recueil d’annales d’immunologie n’est disponible pour ce module : ces 15 QCM sont construits <b>uniquement depuis les diapos du cours</b> du Dr Ouikhlef — rien d’inventé.",
    "Après les annales, l’entraînement maison : ces 15 QCM sont construits <b>uniquement depuis les diapos du cours</b> du Dr Ouikhlef — mêmes leurres (âge échangé, germe déplacé, étage confondu), rien d’inventé.")

# 5. Transparence FR (boîte Vue)
m = re.search(r"<li>Les annales :.*?</li>", h)
assert m, "li annales transparence introuvable"
h = h.replace(m.group(0),
 "<li>Les annales : recueil « CURE – IMMUNO 3<sup>ème</sup> (Oran) », chapitre Déficits Immunitaires — <b>21 QCM officiels retenus (P2014, P2018–P2022)</b>, corrigés revérifiés contre le cours et le second recueil « Immunologie et Pathologies Associées ». Exclus et signalés : 2 questions rédactionnelles (QROC), 5 questions VIH hors périmètre de ce cours, 4 corrigés contredisant le cours et les corrigés illisibles du recueil — jamais reconstruits. Les 15 QCM d’entraînement restent construits uniquement depuis les diapos, sans fait inventé.</li>", 1)

# 6. MÉTHODE sub FR + focus
rep("Sans annales pour ce module, la méthode se construit sur les <b>inversions logiques du cours</b>",
    "Les annales le confirment : l’examinateur joue sur les <b>inversions logiques du cours</b>")
rep("Chaque proposition d’entraînement se vérifie <b>contre une diapo précise</b>",
    "Chaque proposition — annales comme entraînement — se vérifie <b>contre une diapo précise</b>")

# 7. arData : ann-exp-* + m-sub + transp
m = re.search(r'(<script type="application/json" id="arData">)(.*?)(</script>)', h, re.S)
assert m, "arData introuvable"
ard = json.loads(m.group(2))
for k, v in AR.items():
    assert k not in ard, k
    ard[k] = v
ard["m-sub"] = "تؤكدها الامتحانات الرسمية: يلعب المصحح على <b>قلبات الدرس المنطقية</b> — عمر مبادل، جرثوم منقول، طابق مخلوط. إليك الشِّراك التي يجعلها الدرس نفسه ممكنة — والمنعكس الذي يفككها."
old_tr = ard["transp"]
li_m = re.search(r"<li>الامتحانات:.*?</li>", old_tr)
assert li_m, "li AR transparence introuvable"
ard["transp"] = old_tr.replace(li_m.group(0),
 "<li>الامتحانات: مرجع «CURE – IMMUNO 3ème (Oran)»، فصل العجوزات المناعية — <b>21 سؤالاً رسمياً معتمداً (P2014 وP2018–P2022)</b>، تصحيحات أعيد التحقق منها مقابل الدرس والمرجع الثاني «Immunologie et Pathologies Associées». ومستبعدة ومعلنة: سؤالا تحرير (QROC) و5 أسئلة VIH خارج نطاق الدرس و4 تصحيحات تناقض الدرس وتصحيحات غير قابلة للقراءة — لم يُعد بناؤها أبداً. وتبقى أسئلة التدريب الخمسة عشر مبنية فقط من الشرائح، دون اختراع.</li>", 1)
h = h[:m.start()] + m.group(1) + json.dumps(ard, ensure_ascii=False) + m.group(3) + h[m.end():]

# ── asserts finaux ──
assert h.count('data-qcm-set="annales"') == 1
assert h.count('data-qcm-set="entrainement"') == 1
assert h.count('<div class="qblock') == 36, h.count('<div class="qblock')
assert "Aucun recueil d’annales" not in h and "Sans annales pour ce module" not in h
assert h.count('data-target="annales"') == 1
ardt = json.loads(re.search(r'<script type="application/json" id="arData">(.*?)</script>', h, re.S).group(1))
assert sum(1 for k in ardt if k.startswith("ann-exp-")) == 21
# ordre DOM : annales avant entrainement (sections + onglets)
assert h.index('id="annales"') < h.index('id="entrainement"')
assert h.index('data-target="annales"') < h.index('data-target="entrainement"')

open(PAGE, "w", encoding="utf-8").write(h)
import hashlib
print(f"✅ PATCH OK — page {orig_len} -> {len(h)} octets · MD5 {hashlib.md5(h.encode()).hexdigest()}")
