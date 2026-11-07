#!/usr/bin/env python3
"""Ébauche de rendu des neuf QCM du recueil ; pas une page livrée.

Contrat observé dans js/lesson.js : .qblock[data-answer JSON], .qch li[data-l],
.qverdict, .qexp, .qcheck. Le corrigé est celui imprimé par le recueil, sans
le présenter comme officiel. ar-mode.js remplace le contenu data-tr : renvoyer
un dictionnaire arData à fusionner avec celui de la page. Les textes arabes
restent à relire avant intégration. Les 2 libellés incertains sont signalés.
"""
from html import escape
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def render_recueil():
    questions = json.loads((HERE / "QCM-RECUEIL-REVUS.json").read_text(encoding="utf-8"))
    if [q["numero"] for q in questions] != list(range(1, 10)):
        raise ValueError("Le recueil doit contenir les neuf questions, dans l'ordre")
    ar_data = {}
    blocks = []
    for q in questions:
        i = q["numero"]
        if list(q["propositions"]) != list("ABCDE") or list(q["explications"]) != list("ABCDE"):
            raise ValueError(f"Q{i}: cinq propositions A–E et cinq explications nécessaires")
        ans = q["reponse_recueil"]
        if not ans or any(x not in "ABCDE" for x in ans):
            raise ValueError(f"Q{i}: réponse invalide")
        src = escape(q["source"])
        options = ''.join(f'<li data-l="{letter}"><span class="ql">{letter}</span>'
                          f'<span class="qtxt">{escape(text)}</span><span class="xe"></span></li>'
                          for letter, text in q["propositions"].items())
        fr, ar = [], []
        for letter, exp in q["explications"].items():
            klass = "t" if letter in ans else "f"
            label_fr = 'À COCHER' if klass == 't' else 'NON RETENU PAR LE RECUEIL'
            label_ar = 'اختاره المرجع' if klass == 't' else 'لم يختره المرجع'
            fr.append(f'<div class="qexp-item {klass}"><b>{letter} — {label_fr}.</b> {escape(exp["fr"])}</div>')
            ar.append(f'<div class="qexp-item {klass}"><b><bdi class="fr-plain">{letter}</bdi> — {label_ar}.</b> {escape(exp["ar"])}</div>')
        # Le formatage des nombres est isolé en LTR là où des chiffres ASCII apparaissent.
        import re
        ar = [re.sub(r'(?<![\w>])([0-9]+(?:[–/.-][0-9]+)*)(?![\w<])', r'<bdi class="fr-plain">\1</bdi>', x) for x in ar]
        ar_data[f"recueil-{i}-exp"] = ('<div class="qexp-title">شرح كل اقتراح وفق جواب المرجع المطبوع</div>' + ''.join(ar) +
                                       f'<div class="qexp-memo">جواب المرجع المطبوع: <bdi class="fr-plain">{escape("".join(ans))}</bdi>. ليس هذا بالضرورة تصحيحا رسميا مستقلا.</div>')
        encoded_ans = escape(json.dumps(ans, ensure_ascii=False), quote=True)
        blocks.append(f'''<div class="qblock reveal" data-answer="{encoded_ans}">
  <div class="qhead"><div class="qtext">{i}. {escape(q["enonce"])}</div><span class="qsrc">Recueil ELITE CARDIO — {src}</span></div>
  <ul class="qch">{options}</ul>
  <div class="qverdict"></div>
  <div class="qexp" data-tr="recueil-{i}-exp"><div class="qexp-title">Corrigé imprimé dans le recueil ; analyse proposition par proposition</div>{''.join(fr)}
  <div class="qexp-memo">Réponse imprimée : <b>{escape(''.join(ans))}</b> ; ce n'est pas un corrigé officiel indépendant.</div></div>
  <button class="btn btn-primary btn-sm qcheck" type="button">Corriger</button>
</div>''')
    return '\n'.join(blocks), ar_data


if __name__ == '__main__':
    html, translations = render_recueil()
    print(f'{len(translations)} QCM, {html.count("qexp-item ")} explications françaises ; brouillon non livré')
