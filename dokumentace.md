# Uživatelská dokumentace – Fotopast

## 1. Úvod

Fotopast je zařízení určené k automatickému zaznamenávání pohybu v přírodě. Po připojení napájení se zařízení automaticky spustí a začne detekovat pohyb pomocí kamery a senzorů. Po detekci pohybu pořídí snímek, který se automaticky odešle na vzdálený server a je dostupný přes webové rozhraní.

## 2. Použité technologie

- **Hardware:** Raspberry Pi 5 (8GB RAM), kamera, PIR senzor, microSD karta, napájecí modul  
- **Software:** Python, OpenCV, v4l2-ctl, systémové služby pro automatické spuštění  
- **Úložiště:** Vzdálený server (SFTP)  
- **Správa:** SSH přístup pro konfiguraci, webové rozhraní na doméně [fotopast.2007.cz](https://fotopast.2007.cz) pro správu pořízených snímků

## 3. Funkčnost

- **Automatické spuštění:** Po připojení napájení se zařízení automaticky spustí a začne detekovat pohyb.
- **Detekce pohybu:** PIR senzor detekuje pohyb v okolí a aktivuje pořízení snímku.
- **Pořízení a úprava snímků:** Kamera pořídí snímek, který je rotován o 180° pro správné zobrazení.
- **Nahrávání snímků:** Snímky jsou pomocí SFTP automaticky nahrávány na vzdálený server a pomocí autentizace public key je přenos a přístup na server zabecpečen.
- **Webová správa:** Nahrané soubory jsou přístupné přes webové rozhraní na [fotopast.2007.cz](https://fotopast.2007.cz), kde lze soubory prohlížet, stahovat a mazat.

## 4. Webové rozhraní

Po nahrání snímků na server jsou tyto dostupné přes webové rozhraní na adrese:

👉 [https://fotopast.2007.cz](https://fotopast.2007.cz)

### Funkce rozhraní:

- **Prohlížení:** Náhled a prohlížení jednotlivých snímků.
- **Mazání:** Možnost odstraňování nepotřebných snímků.
- **Stahování:** Stahování jednotlivých nebo více snímků.

### Přístup:

1. Otevřete webový prohlížeč a přejděte na [https://fotopast.2007.cz](https://fotopast.2007.cz)  
2. Přihlaste se pomocí přístupových údajů  
3. Spravujte soubory dle potřeby

## 5. GitHub repozitář

Repozitář obsahuje zdrojový kód, instalační postup a dokumentaci k projektu:

🔗 [https://github.com/Krataman/Fotopast](https://github.com/Krataman/Fotopast)

## 6. Testování

Projekt byl testován pěti uživateli. Testování zahrnovalo:

- Detekci pohybu a spouštění kamery
- Kvalitu a správnou orientaci snímků
- Ověření správného fungování nahrávání na server
- Test použitelnosti webového rozhraní
- Zpětná vazba byla shromážděna přes GitHub Issues a byla zapracována

## 7. Dokumentace

### 7.1 Technická dokumentace

- **PIR senzor:** Detekuje pohyb a spouští kameru.
- **Kamera (Picamera2):** Pořizuje snímky, které jsou následně upraveny pomocí knihovny PIL (rotace).
- **SFTP přenos:** Automatizovaný skript přenáší snímky na server.
- **Webová správa:** Snímky jsou ihned dostupné k prohlížení a správě na webu.

### 7.2 Uživatelská příručka

#### Instalace a konfigurace

1. **Připojení zařízení**
   - Připojte napájení, kameru a PIR senzor k Raspberry Pi
   - Připojte zařízení do sítě pomocí Ethernetu nebo Wi-Fi

2. **Automatický start**
   - Při spuštění zařízení se automaticky spustí služba pro detekci pohybu
   - Pořízené snímky se automaticky odesílají na server přes SFTP

3. **Správa snímků**
   - Otevřete [https://fotopast.2007.cz](https://fotopast.2007.cz)
   - Přihlaste se a spravujte soubory (prohlížení, mazání, stahování)

---

> 🛠️ Projekt vytvořen v rámci školní technické praxe.  
> 📷 Pro více informací nebo úpravy navštivte repozitář na GitHubu.
