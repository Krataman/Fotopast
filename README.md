# Projekt: Fotopast

## 1. Úvod
Wildlife kamera (fotopast) je zařízení určené k automatickému zaznamenávání pohybu v přírodě. Po připojení napájení se zařízení automaticky spustí a začne detekovat pohyb pomocí kamery a senzorů. Po detekci pohybu uloží snímky nebo video na lokální úložiště.

## 2. Použité technologie
- **Hardware:** Raspberry Pi 5 (8GB RAM), kamera, PIR senzor, microSD karta, napájecí modul
- **Software:** Python, OpenCV, v4l2-ctl, systémové služby pro automatické spuštění
- **Úložiště:** Lokální SD karta
- **Správa:** SSH přístup pro konfiguraci, **Filebrowser** pro webové rozhraní pro správu pořízených medií (mazání, stahování atd.)

## 3. Funkčnost
- Automatické spuštění po připojení napájení
- Detekce pohybu pomocí PIR senzoru a OpenCV
- Ukládání snímků a videí
- Možnost vzdálené správy prostřednictvím webového rozhraní Filebrowser

## 4. GitHub repo
Repozitář obsahuje zdrojový kód, instalační postup a uživatelskou dokumentaci.
**Odkaz:** [GitHub Repository](https://github.com/example/fotopast)

## 5. Testování
Projekt byl otestován pěti uživateli, kteří poskytli zpětnou vazbu prostřednictvím GitHub Issues. Veškeré připomínky byly zapracovány do finální verze.

## 6. Dokumentace

### 6.1 Technická dokumentace
Fotopast je postavena na platformě Raspberry Pi 5 s 8 GB RAM, což zajišťuje dostatečný výkon pro zpracování obrazových dat v reálném čase. Kamera je připojena k Raspberry Pi a snímky/video jsou zachyceny při detekci pohybu pomocí PIR senzoru.

Software je napsán v Pythonu a využívá knihovnu OpenCV pro detekci pohybu. Používá také nástroj `v4l2-ctl` pro správu kamery. Po detekci pohybu systém automaticky uloží snímky a/nebo video na microSD kartu.

Systém je navržen tak, aby byl co nejvíce automatizovaný, což znamená, že po připojení napájení fotopast automaticky začne detekovat pohyb a zaznamenávat data.

Pro správu souborů a konfiguraci zařízení je použito webové rozhraní **Filebrowser**, které umožňuje uživatelům vzdáleně přistupovat k pořízeným snímkům a videím.

### 6.2 Uživatelská příručka
#### Instalace a konfigurace
1. **Připojení zařízení**  
   - Připojte Raspberry Pi k napájení.
   - Připojte kameru a PIR senzor k Raspberry Pi.

2. **Připojení k síti**  
   - Zařízení se připojí k místní síti pomocí Ethernetu nebo Wi-Fi.
   - Ujistěte se, že máte přístup k zařízení přes SSH.

3. **Správa pomocí Filebrowser**  
   - Po nastavení připojení můžete přistupovat k zařízení prostřednictvím webového rozhraní **Filebrowser**.
   - Přihlaste se do Filebrowser pomocí webového prohlížeče na IP adrese Raspberry Pi.
   - Pomocí rozhraní můžete prohlížet, mazat nebo stahovat pořízené snímky a videa.

4. **Testování a ladění**  
   - Pro testování můžete ručně aktivovat pohyb před PIR senzorem a ověřit, že systém správně reaguje.
   - V případě potřeby můžete upravit nastavení detekce pohybu.

## Summary in English
The Wildlife Camera (Fotopast) is an automatic motion-detection camera for nature observation. It starts upon power connection and records images or videos when movement is detected. The project utilizes Raspberry Pi 5 (8GB RAM), OpenCV, and PIR sensors. Filebrowser is used for remote management through a web interface. The source code and documentation are available on GitHub. Testing was conducted with five users, and feedback was incorporated into the final version. A poster (A0 format) was created with all necessary details, including a QR code linking to the repository.

---

**Autor:** [Denis Kratochvíl]
