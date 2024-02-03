Feladat

Beolvassa és feldolgozza a nyers adathalmazt
Minden egyes sorra adatelőkészítő műveleteket végez el. Ezekről részletesen írunk a következőkben
Létrehoz egy célváltozót, ami a lakás négyzetméterárából képződik úgy, hogy a hirdetés feladásának dátuma alapján eliminálásra kerül a lakásárakban észlelhető trend.
A módszer használatánál kerek magyar mondatokban magyarázzuk meg, hogy miért fontos ezt a műveletet elvégezni, és a használt módszer miért teljesíti ezt a kitételt.

Tanítsunk be modelleket az adatokon:
    Lineáris regressziót
    GradientBoostingMachine-t
    Neuralis hálózatot (Az sklearn implementáció mellett akár deep learning is).
    Mindnél: Legalább egy paraméterét hangoljuk be úgy, hogy az előrejelzés MAPE értéke minél kisebb legyen.
Néhol az egyik, néhol a másik algoritmus fog jobb eredményt adni, ennek ellenére tanulságos figyelni, hogy a később ismertetett adatelőkészítési lépések melyik modellnek mennyit segítettek.

    A betanításnál használjunk hármas keresztvalidációt. 
    Véletlenszerűen daraboljuk háromfele az adathalmazt. 
    Tanuljunk az adatok kétharmadán, adjunk becslést az adatok egyharmadára. 
    Ezt minden kombinációra tegyük meg, így lényegében a teljes adathalmazra lesz egy-egy becslésünk. 
    Ha modelleket hasonlítanánk össze, akkor a kisebb MAPE érték fele térjünk el, 
    itt érdemes a teljes adathalmazon vett MAPE értékkel számolni.
    Számítsuk ki emellett, hogy hány olyan ingatlant kellene az eredményt feldolgozó szakértői csapatnak feldolgoznia: 
        ha a becsült árat vesszük reális árnak, akkor azon lakások számát nézzük, amik a reális árnál 5%-25%-kal olcsóbbak. 
        Kérdés, hány ilyen ingatlan van.
Adatelőkészítési lépések:

    Az adathalmaz oszlopainak sorrendjét véletlenszerű sorrendbe rakjuk. A véletlen legyen determinisztikus, de legyen hallgatónként egyedi (a random seed lehetne egy véletlen, de fix tíz jegyű szám)
Vegyük sorra az egyes változókat (amilyen sorrendben a megtekert adathalmazban láthatók), és készítsük elő az adatot úgy, hogy a modellek fel tudják azt dolgozni (hiányzó értékek eliminálása, kiugró értékek kezelése, stb). Az ad_view_cnt és az active_days változók kihagyandók. Minden egyes változó előkészítése során nézzük meg, hogy mennyit segít az eddigi eredményekhez képest. Ha ront is, akkor is hagyjuk bent őket a bemenő változók között.

Az alábbi változóknál többfajta adatelőkészítési lépést is vizsgáljunk meg. 
Ezeknél sokfajta módszer használata lehetséges.

A vizsgálat után a kapott futási eredmények ismeretében döntsünk, 
hogy melyik fajta átalakítást hagyjuk benne a megoldásunkban, 
és lépjünk a bemenő adathalmazban sorra következő változóra.

    Kerületek – Nézzünk meg legalább három módszert a kerületek figyelembevételére

    Irányítószámok – Nézzük meg legalább két módszert a kerületek figyelembevételére

    Ingatlan tájolása – Legalább két módszert vizsgáljunk meg

    Fűtés típusa – Legalább két módszert vizsgáljunk meg

    Emelet – Hanyadik emeleten van a lakás – Vizsgáljunk meg legalább két módszert

    Állapot – Lakás állapotának vizsgálata – Vizsgáljunk meg legalább két módszert

    Milyen napon tették ki a hirdetést (a hét melyik napján) – Vizsgáljunk meg legalább két módszert

A többfajta módszer összehasonlításánál nem kell mindig külön optimalizálni a modelleket (de szabad).
Az egyes részeredményeket is mentsük ki egy adathalmazba, táblázatba.
Végezetül adjunk egy áttekinthető vizualizációt arra vonatkozóan, hogy mennyire segítettek az egyes változók az egyes modelleken.
Szövegesen kerek magyar értelmes mondatokban írjunk néhány sort arról, hogy milyen tanulságok vonhatók le a látottakból. 
Mivel a három modell más-más módon reagáltak a különböző adatelőkészítési lépésekre ezeket érdemes akár külön is megjeleníteni.
Végül hozzunk létre egy végső adatelemzési folyamatot, amit az adott kontextusban a leghatékonyabbnak tekintünk, majd futtassuk le azt. A végén az említett 5-25%-os alulértékeltséggel jellemzett lakások adatait mentsük ki egy „results_<NEPTUN>.csv” file-ba indexek nélkül. Ezt a file-t is mellékeljük a megoldásunkhoz.


Az eredményeket az edu.tmit.bme.hu oldal megfelelő helyére töltsük fel. Az alábbi file-okra van szükség:
Elemzést tartalmazó notebook / kód pdf-ben és .jpynb /.py kiterjesztésű file-ként is
Py kiterjesztés esetén a szöveges megfogalmazásokat kommentben kérjük szépen megformázva
Results_<NEPTUN>.csv file
ChatGPT / Bard / etc promptok és válaszok pdf formátumban. Itt ne zavartassuk magunkat különösebben a promptok szépsége kapcsán, akár több file is csatolható be ide. A lényeg, hogy ha innen jön külső kód, akkor az itt megjelenjen.
Form kitöltése
