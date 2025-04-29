# Postup návrhu – Fotopast

## 1. Cíl projektu
Cílem projektu bylo navrhnout a vytvořit fotopast – zařízení schopné automaticky pořizovat snímky v přírodě při detekci pohybu. Zařízení musí fungovat autonomně, přenášet pořízené snímky na vzdálený server a umožnit jejich správu přes webové rozhraní.

## 2. Funkční požadavky
- Detekce pohybu pomocí PIR senzoru.
- Automatické pořízení snímku při detekci pohybu.
- Přenos snímků na vzdálený server pomocí protokolu SFTP.
- Správa snímků přes webové rozhraní (stahování, mazání, prohlížení).
- Bezpečný přenos dat pomocí SSH autentizace (public key).
- Autonomní provoz – zařízení po spuštění funguje bez potřeby dalšího zásahu.

## 3. Nefunkční požadavky
- Raspberry Pi musí být trvale napájeno (projekt nepočítá s bateriovým provozem).
- Nutnost připojení k internetu – bez připojení není možný přenos snímků na server.
- Okamžité zpracování snímků není garantováno kvůli hardwarovým omezením. Z tohoto důvodu fotopast pořizuje více snímků (2–3) pro kompenzaci zpoždění mezi detekcí a pořízením prvního snímku.

## 4. Návrh hardwarové části
- **Raspberry Pi 5 (8 GB RAM):** Vybráno pro dostatečný výkon a možnost budoucího rozšíření.
- **PIR senzor:** Spolehlivý pohybový senzor s dosahem cca 8 metrů a úhlem detekce 120°, efektivnější než laserové řešení.
- **RPi kamera:** Nízkonákladová kamera kompatibilní s Raspberry Pi.
- **Napájení:** 5V / 3A napájecí adaptér zajišťující stabilní provoz.

## 5. Návrh softwarové části
- **Programovací jazyk:** Python – jednoduchý pro vývoj a dostupný na RPi s bohatou nabídkou knihoven.
- **Detekce pohybu:** Realizována přes PIR senzor pro minimální zatížení CPU.
- **Zpracování obrazu:** Knihovny OpenCV a PIL (rotace snímků o 180° pro správné zobrazení).
- **Přenos dat:** Automatický SFTP upload snímků na vlastní server pomocí SSH klíčů.
- **Správa dat:** Filebrowser jako jednoduché webové rozhraní pro správu mediálních souborů.

## 6. Architektura systému
1. PIR senzor detekuje pohyb.
2. Kamera pořídí snímek (nebo sérii snímků).
3. Snímek je uložen do lokální složky na RPi.
4. Python skript provede rotaci a nahrání přes SFTP na server.
5. Na serveru jsou soubory dostupné a spravovatelné prostřednictvím webového rozhraní Filebrowser (https://fotopast.2007.cz).

## 7. Výběr technologií a jejich odůvodnění
- **SFTP místo lokální SD karty:** Snížení rizika ztráty dat při výpadku napájení a možnost rozšíření úložiště na serveru.
- **Filebrowser:** Rychlé nasazení a přívětivé uživatelské prostředí.
- **Open source nástroje:** Snadná integrace, dostupná dokumentace a flexibilita.

## 8. Rizika a omezení
- **Výpadek připojení k internetu:** Znemožní odeslání snímků na server.
- **Zpoždění při pořízení snímků:** Kvůli inicializační době kamery není možné garantovat okamžité zachycení prvního pohybu.
- **Napájení:** Projekt v aktuální podobě nepočítá s mobilním (bateriovým) napájením.

## Závěr
Projekt **Fotopast** úspěšně splnil stanovené cíle. Zařízení je schopno po zapnutí automaticky detekovat pohyb a pořizovat snímky, které následně bezpečně nahrává přes SFTP na vlastní server. Uživatel má k těmto snímkům přístup přes webové rozhraní Filebrowser, dostupné na adrese [https://fotopast.2007.cz](https://fotopast.2007.cz).

Při vývoji byla kladena důraz na spolehlivost, jednoduchost ovládání a snadnou dostupnost dat. Byly implementovány základní bezpečnostní mechanismy pro ochranu přístupu a přenosu dat.

Díky zpětné vazbě od testerů bylo možné odstranit drobné chyby a doladit uživatelské prostředí. Projekt tak splňuje nejen technické požadavky, ale je i prakticky použitelný v reálném nasazení.

Celkově hodnotím práci na projektu jako přínosnou – rozšířil jsem své znalosti v oblasti Linuxu, práce s kamerou na Raspberry Pi, webových technologií a síťové bezpečnosti.


