#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OUTIL-verifier-data-monotone — porte anti-régression pour js/data.js (delta 30, 01/11/2026).

Contexte : le tableau de bord n'affiche le bouton « Ouvrir » d'une leçon que si son
entrée data.js possède un `url`. Un data.js bâti sur une lignée ancienne et livré
dans un ZIP écrase le data.js courant → les boutons des leçons déjà livrées
disparaissent (constat utilisateur 01/11 : module respiratoire entier).

Règle : un nouveau data.js ne doit JAMAIS perdre ce que l'ancien savait.
  BLOQUANT (exit 1) : leçon absente · url présente avant, absente/différente après ·
                      recu true → false/absent.
  AVERTISSEMENT     : qcm/entr en baisse (à justifier dans le LISEZ-MOI).

Usage : python3 OUTIL-verifier-data-monotone.py <ancien_data.js> <nouveau_data.js>
À passer AVANT toute livraison contenant un data.js (ancien = data_COURANT le plus
récent du Drive). Voir aussi : js/data-merge.js + js/data-patches/<id>.js (delta 30)
et REGLE-FORMAT-LIVRAISON-ZIP, section DATA.
"""
import re
import sys


def parse(path):
    txt = open(path, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"\{\s*id:\s*'([^']+)'([^{}]*)\}", txt):
        lid, body = m.group(1), m.group(2)
        url = re.search(r"url:\s*'([^']*)'", body)
        recu = re.search(r"recu:\s*(true|false)", body)
        qcm = re.search(r"qcm:\s*(\d+)", body)
        entr = re.search(r"entr:\s*(\d+)", body)
        out[lid] = {
            "url": url.group(1) if url else None,
            "recu": recu.group(1) == "true" if recu else False,
            "qcm": int(qcm.group(1)) if qcm else None,
            "entr": int(entr.group(1)) if entr else None,
        }
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    old, new = parse(sys.argv[1]), parse(sys.argv[2])
    print(f"ancien : {len(old)} leçons, {sum(1 for v in old.values() if v['url'])} avec url")
    print(f"nouveau: {len(new)} leçons, {sum(1 for v in new.values() if v['url'])} avec url")
    pertes, avert = [], []
    for lid, o in old.items():
        n = new.get(lid)
        if n is None:
            pertes.append(f"{lid} : ABSENTE du nouveau data.js")
            continue
        if o["url"] and n["url"] != o["url"]:
            pertes.append(f"{lid} : url perdue/modifiée ({o['url']} → {n['url']}) — bouton « Ouvrir » en danger")
        if o["recu"] and not n["recu"]:
            pertes.append(f"{lid} : recu true → false")
        for f in ("qcm", "entr"):
            if o[f] is not None and n[f] is not None and n[f] < o[f]:
                avert.append(f"{lid} : {f} en baisse ({o[f]} → {n[f]}) — à justifier")
    for a in avert:
        print("  ⚠", a)
    if pertes:
        print(f"\n❌ {len(pertes)} PERTE(S) — NE PAS LIVRER ce data.js :")
        for p in pertes:
            print("  ✗", p)
        return 1
    print("✅ MONOTONE : aucune leçon ne perd son url ni son recu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
