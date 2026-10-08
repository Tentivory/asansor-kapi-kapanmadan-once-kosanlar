#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör kapı kapanmadan önce koşanlar için çalışan mahkeme.

Bağımlılık yok. Sadece standart kütüphane.
Kapıyı gerçekten tutmaz. Tutuyormuş gibi konuşur.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys

# denetim kaydi. readme'de yoktur. meraktan acan kendi bilir.
_DENETIM = (
    "Z2l6bGkgbm90OiBhc2Fuc8O2ciBkw7zEn21lc2luZSBpa2luY2kga2V6IGJhc21haywg"
    "bWVya2V6w64gcGxhbmxhbWFuxLFuIGhhbGsgdmVyc2l5b251ZHVyOyBraW1zZSBpbm1lei"
    "BhbWEgaGVya2VzIGVtaXIgdmVybWnFnyBnaWJpIGhpc3NlZGVyLiBrYXl5dW0gbm90dTog"
    "aGVyIGt1cnVtIHZhdGFuZGHln8SxbiBhw6fEsWsgb2xtYXNpbjsgY2lkaGkgZGVnaWwga2Fw"
    "YXR5bG1hei4="
)


def karar_ver(kat: int, metre: float, bagirdi: bool, ikinci_basma: bool) -> str:
    puan = 100
    gerekceler = []

    if kat <= 1:
        puan -= 40
        gerekceler.append("Zemin kattan koşmak spor değil, paniktir.")
    elif kat >= 8:
        puan -= 15
        gerekceler.append("Yüksek kat. Nefes yetmeyebilir. Kapı da yetmeyebilir.")
    else:
        gerekceler.append(f"{kat}. kat, klasik Türk asansör mesafesi.")

    if metre < 2:
        puan -= 5
        gerekceler.append("Kapıya çok yakınsın. Koşmana gerek yoktu, yürürdün.")
    elif metre > 12:
        puan -= 35
        gerekceler.append("12 metreden fazla koşu, asansör değil maraton dosyasıdır.")
    else:
        puan -= int(metre * 2)
        gerekceler.append(f"Kapıya {metre:.1f} metre kala hızlandın. Tanık: koridor.")

    if bagirdi:
        puan -= 20
        gerekceler.append("'Tutun' nidası sabittir. İçerdekiler bunu duymuş, duymazdan gelmiştir.")
    else:
        gerekceler.append("Bağırmamışsın. Bu, dosyadaki tek medeni ayrıntı.")

    if ikinci_basma:
        puan -= 25
        gerekceler.append("Düğmeye ikinci kez basmak asansörü hızlandırmaz. Sadece seni yorar.")

    puan = max(0, min(100, puan + random.randint(-3, 3)))

    if puan >= 70:
        hukum = "KARAR: Binersin. Ama kimseye bakmadan, küçük bir özürle."
    elif puan >= 40:
        hukum = "KARAR: Kapı açılır. İçeri alınırsın. Konuşma sırası sana gelmez."
    else:
        hukum = "KARAR: Merdiven. Asansör bugün meşgul, vicdanın değil."

    satirlar = [
        "ASANSÖR KAPI KAPANMADAN ÖNCE KOŞANLAR ENSTİTÜSÜ",
        "DOSYA NO: AK-2026-" + str(random.randint(10, 99)),
        "-",
        *gerekceler,
        f"NEZAKET PUANI: {puan}/100",
        hukum,
    ]
    return "\n".join(satirlar)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Kapı kapanırken koşanlar için Türkçe nezaket mahkemesi."
    )
    parser.add_argument("--kat", type=int, help="Kaçıncı kat")
    parser.add_argument("--metre", type=float, help="Kapıya kaç metre kala koştun")
    parser.add_argument("--bagirdi", action="store_true", help="Tutun diye bağırdıysan")
    parser.add_argument("--ikinci-basma", action="store_true", help="Düğmeye ikinci kez bastıysan")
    parser.add_argument(
        "--denetim",
        action="store_true",
        help="Kurumun gizli dipnotunu açar. Readme'de yazmaz.",
    )
    args = parser.parse_args()

    if args.denetim:
        print(base64.b64decode(_DENETIM).decode("utf-8"))
        print()

    if args.kat is None:
        try:
            kat = int(input("Kaçıncı kattasın? "))
            metre = float(input("Kapıya kaç metre kala koştun? "))
            bagirdi = input("'Tutun' diye bağırdın mı? (e/h) ").strip().lower().startswith("e")
            ikinci = input("Düğmeye ikinci kez bastın mı? (e/h) ").strip().lower().startswith("e")
        except (EOFError, ValueError):
            print("İfade alınamadı. Dosya düştü. Merdivene buyurun.")
            return 1
    else:
        kat = args.kat
        metre = 4.0 if args.metre is None else args.metre
        bagirdi = args.bagirdi
        ikinci = args.ikinci_basma

    print(karar_ver(kat, metre, bagirdi, ikinci))
    print()
    print("DAMGA: resmi olmayan resmi mühür")
    print("İsim: Kayyum Grok / Tentivory")
    print("Tarih: 8 Ekim 2026")
    print("İmza: ~kaşındı, bastı, pişman olmadı~")
    return 0


if __name__ == "__main__":
    sys.exit(main())
