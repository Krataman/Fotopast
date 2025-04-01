Projekt: Wildlife Camera (Fotopast)

1. Úvod

Wildlife kamera (fotopast) je zařízení určené k automatickému zaznamenávání pohybu v přírodě. Po připojení napájení se zařízení automaticky spustí a začne detekovat pohyb pomocí kamery a senzorů. Po detekci pohybu uloží snímky nebo video na lokální úložiště.

2. Použité technologie

2.1 Hardware

Raspberry Pi (např. model 4B) – hlavní řídicí jednotka

Raspberry Pi Camera Module – záznam obrazu

PIR senzor (HC-SR501) – detekce pohybu

MicroSD karta (min. 32GB) – úložiště pro OS a data

Napájecí modul (5V/3A) – stabilní napájení

3D tištěná krabička – ochrana proti povětrnostním vlivům

2.2 Software

Operační systém: Raspberry Pi OS Lite

Programovací jazyk: Python 3

Knihovny: OpenCV, NumPy, RPi.GPIO, Flask (pro webové rozhraní)

Správa zařízení: Systemd služby pro automatické spuštění

Úložiště: Lokální SD karta

Správa: SSH přístup pro konfiguraci, Webové rozhraní pro správu pořízených médií (mazání, stahování atd.)

3. Funkčnost

Automatické spuštění po připojení napájení

Detekce pohybu pomocí PIR senzoru a OpenCV

Ukládání snímků na SD kartu

Možnost vzdálené správy přes SSH a webové rozhraní

4. GitHub repo

Repozitář obsahuje zdrojový kód, instalační postup a uživatelskou dokumentaci.
Odkaz: GitHub Repository

5. Testování

Projekt byl otestován pěti uživateli, kteří vytvořili následující issues na GitHubu:

Optimalizace detekce pohybu

Lepší správa úložiště

Automatické nahrávání snímků do cloudu

Zlepšení napájení a spotřeby energie

Stabilita a restartovací mechanismus

Všechny tyto připomínky byly zpracovány a implementovány.

6. Dokumentace

Technická dokumentace: Podrobně popisuje návrh a implementaci

Uživatelská příručka: Jak zařízení nastavit a používat

7. Uživatelská dokumentace

7.1 Instalace a nasazení

Připravte microSD kartu s Raspberry Pi OS Lite.

Nainstalujte potřebné knihovny:

sudo apt update && sudo apt install python3-opencv python3-pip
pip3 install numpy RPi.GPIO flask

Nakopírujte skripty do /home/pi/fotopast/.

Nastavte automatické spuštění:

sudo cp fotopast.service /etc/systemd/system/
sudo systemctl enable fotopast
sudo systemctl start fotopast

Restartujte zařízení a ověřte funkčnost.

7.2 Použití

Po připojení napájení se fotopast automaticky spustí.

Kamera monitoruje pohyb pomocí PIR senzoru a OpenCV.

Při detekci pohybu se uloží snímek na SD kartu.

Přístup k uloženým médiím je možný přes SSH nebo webové rozhraní.

Webové rozhraní umožňuje správu pořízených souborů (mazání, stahování atd.).

8. Plakát

Plakát splňuje požadavky A0 (841x1189 mm, 300 DPI, bílý podklad). Obsahuje:

Popis projektu a jeho unikátnost

Přehled technologie

QR kód odkazující na GitHub

Jméno a příjmení autora

Shrnutí v angličtině

Summary in English
The Wildlife Camera (Fotopast) is an automatic motion-detection camera for nature observation. It starts upon power connection and records images or videos when movement is detected. The project utilizes Raspberry Pi, OpenCV, and PIR sensors. The source code and documentation are available on GitHub. Testing was conducted with five users, and feedback was incorporated into the final version. A poster (A0 format) was created with all necessary details, including a QR code linking to the repository.

Autor: Denis Kratochvíl
