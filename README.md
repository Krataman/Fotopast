# Projekt: Fotopast

## 1. Úvod
Fotopast je zařízení určené k automatickému zaznamenávání pohybu v přírodě. Po připojení napájení se zařízení automaticky spustí a začne detekovat pohyb pomocí kamery a senzorů. Po detekci pohybu uloží snímky nebo video na lokální úložiště.

## 2. Použité technologie
- **Hardware:** Raspberry Pi 5 (8GB RAM), kamera, PIR senzor, microSD karta, napájecí modul
- **Software:** Python, OpenCV, v4l2-ctl, systémové služby pro automatické spuštění
- **Úložiště:** Lokální SD karta
- **Správa:** SSH přístup pro konfiguraci, **Filebrowser** pro webové rozhraní pro správu pořízených medií (mazání, stahování atd.)

## 3. Funkčnost
Fotopast je navržena tak, aby vykonávala následující funkce:

- **Automatické spuštění po připojení napájení:** Zařízení se automaticky spustí po připojení napájení a začne okamžitě detekovat pohyb.
- **Detekce pohybu pomocí PIR senzoru:** PIR senzor je aktivován, když je detekován pohyb v jeho okolí, což následně spustí kameru pro pořízení snímků.
- **Ukládání snímků:** Snímky pořízené kamerou jsou uloženy na SD kartu v zařízení. Snímky jsou také rotovány o 180 stupňů pro zajištění správného zobrazení.
- **Možnost vzdálené správy prostřednictvím webového rozhraní Filebrowser:** Uživatelé mohou vzdáleně přistupovat k pořízeným snímkům a videím, prohlížet je, mazat nebo stahovat pomocí webového rozhraní **Filebrowser**.

## 4. Správa pomocí Filebrowseru
Po nastavení a spuštění zařízení můžete spravovat pořízené snímky a videa pomocí webového rozhraní **Filebrowser**. Tento nástroj umožňuje:

- **Prohlížení souborů:** Uživatelé mohou prohlížet pořízené snímky a videa, které byly uloženy na SD kartě Raspberry Pi.
- **Mazání souborů:** Pokud chcete uvolnit místo na SD kartě, můžete pomocí Filebrowseru mazat staré soubory.
- **Stahování souborů:** Snímky a videa lze stáhnout na váš počítač nebo jiná zařízení pro zálohu nebo další použití.

### Krok za krokem:
1. **Přístup k Filebrowseru**
   - Otevřete webový prohlížeč a zadejte IP adresu Raspberry Pi.
   - V přihlašovacím okně použijte přihlašovací údaje:
     - **Uživatelské jméno:** admin
     - **Heslo:** admin
2. **Správa souborů**
   - Jakmile se přihlásíte, budete mít přístup k souborům uloženým na SD kartě.
   - Klikněte na složky pro prohlížení snímků a videí.
   - Použijte tlačítka pro mazání nebo stahování souborů podle potřeby.

## 5. GitHub repo
Repozitář obsahuje zdrojový kód, instalační postup a uživatelskou dokumentaci.
**Odkaz:** [GitHub Repository](https://github.com/Krataman/Fotopast)

## 6. Testování
Projekt byl otestován pěti uživateli. Uživatelé poskytli zpětnou vazbu prostřednictvím GitHub Issues, která byla následně zapracována do finální verze projektu. Testování zahrnovalo:
- Ověření správnosti detekce pohybu.
- Testování kvality pořízených snímků a jejich rotace.
- Zajištění správné funkčnosti webového rozhraní pro správu souborů.

## 7. Dokumentace

### 7.1 Technická dokumentace
Fotopast je postavena na Raspberry Pi 5 (8GB RAM), což poskytuje dostatečný výkon pro zpracování obrazových dat v reálném čase. Pro detekci pohybu je použit **PIR senzor**, pro správu kamery **picamera2** a pro manipulaci s obrazovými soubory je použit **PIL** (Python Imaging Library).

- **PIR senzor:** Detekuje pohyb a spouští pořízení snímku pomocí kamery.
- **Kamera (Picamera2):** Používá se pro pořízení snímků a videí.
- **Snímky:** Jsou ukládány na SD kartu, přičemž RAW snímky jsou po pořízení rotovány o 180 stupňů pro správné zobrazení.

Pro vzdálenou správu je použito webové rozhraní **Filebrowser**, které poskytuje uživatelům přístup k pořízeným snímkům a videím. Toto rozhraní umožňuje prohlížení, stahování a mazání souborů.

### 7.2 Uživatelská příručka
#### Instalace a konfigurace
1. **Připojení zařízení**
   - Připojte Raspberry Pi k napájení.
   - Připojte kameru a PIR senzor k Raspberry Pi.
   - Připojte Raspberry Pi k místní síti pomocí Ethernetu.

2. **Spuštění skriptu pro fotopast Po nainstalování potřebných knihoven můžete spustit skript,
   který zajistí detekci pohybu a pořízení snímků:**

```bash
sudo python3 sens.py
```

3. **Správa pomocí Filebrowser**
   - Po připojení k zařízení můžete spravovat snímky a videa prostřednictvím webového rozhran Filebrowseru.

   - Pro přístup k Filebrowseru otevřete webový prohlížeč a zadejte IP adresu Raspberry Pi.
   - Přihlašovací údaje jsou **admin/admin**.

4. **Testování a ladění**

   - Pro testování aktivujte pohyb před PIR senzorem a ověřte, zda fotopast správně reaguje.
   - Pokud je to nutné, můžete upravit nastavení detekce pohybu nebo upravit intervaly mezi snímky.
  
**Autor: [Denis Kratochvíl]**








