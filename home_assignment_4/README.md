Adatok előkészítése

Nézd át az adathalmazt, és válogasd ki a változók közül azokat, melyek nem szám formátumúak (a hiányzó értékek megengedettek), illetve dobd el a "price_created_at" változót.
Tölts ki a hiányzó értékeket úgy, hogy azok értéke a minimális számérték -1 legyen.
A target az m2_price oszlop, a train_test_split-el bontsd fel az adatot tanító és teszt adatokra. (test_size legyen 0.2, a random_state pedig 42.)
Feature extraction módszerek

Készíts függvényeket, ami egy-egy feature extraction módszert használ úgy, hogy a függvény bemenetén megadjuk a módszer nevét és átadjuk az X_train és X_test adatokat. A függvény bent tanítsa be az átalakítást tanító adathalmazon, majd számolja ki az értéket a és új oszlopként adja hozzá az X_train és X_test-hez. A dataframe-ben az új változók neve az alábbi alakot vegye fel: <módszerneve>_<változósorszáma0tólszámozva>
Az alábbi módszerekhez készítsd el a függvényt:
"PCA": PCA módszer első 10 komponensét adja vissza a függvény
"KMEANS": Normalizáció (Z-normalizáció) után építs egy KMeans-t 10 klaszterrel úgy, hogy a random_state=42
"SVD": Az CsonkoltSVD módszerével hozz létre 10 változót (random_state=42)
Teljes adatgeneráló függvény egyben
Az eddig elkészült függvényekkel készíts egy nagy függvényt, ami képes elkészíteni a fenti három függvény segítségével az összes új (30 darab) oszlopot. 

Feature selection módszerek:

Az eredeti és a 30 új változóból véletlenszerűen válasszunk ki 16 darabot, majd ezekre vonatkozóan végezzünk változó szelektálást a tanító adathalmazon és mind a 4 esetben értékeljük ki, hogy a kiválasztott változókra való szűrés esetén milyen MSE érhető el a teszt adathalmazon, ha a modell egy GBM - (FRISSITVE:) 160 helyett 16 fával, 4 mélységgel és 42-es random_state-el.

1.        A választást alapozzuk a train adaton a target (m2_price) értékeivel való korrelációk erősségére. Annak eldöntéséhez, hogy mennyi változót válasszunk ki a legjobb korrelációval bírók közül használjunk optimalizálást. Az optimalizálás során az MSE metrikára támaszkodjunk és használjunk cross-validation technikát. Erre lehetőséget ad a cross_val_predict függvény. Állítsunk be 2-es cv paramétert és használjuk a fenti paraméterekkel meghatározott GBM-et.

2.        A változók kiválasztásához alkalmazzon forward selection módszert. Használja az sklearn SequentialFeatureSelector objektumát. A választott változók számának eldöntése legyen automatikus ami a „n_features_to_select” paraméter „auto”-ra történő állításával érhető el. Az „auto” beállítás esetén elengedhetetlen a „tol” paraméter beállítása is, ami legyen 0.00001. Ha ezt nem állítjuk be akkor a változók felét választja ki. (Az auto módhoz sklearn 1.1 verzió szükséges). Mindezek mellett szükség lesz egy scorer függvényre amit az MSE metrikából készítsen az sklearn.metrics. make_scorer  segítségével. Az optimalizáláshoz használjon ugyanolyan paraméterekkel beállított modellt mint amivel a teszten is visszaméri a performanciát.

3.        Lasso regresszió használatával végezzünk változók kiválasztást. A regularizációra vonatkozó paramétert (alpha) optimalizáljuk ki a következő lehetőségek közül: [0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1, 2, 5, 10, 25, 50, 100]. Az optimalizálás során a korábbiakhoz hasonlóan végezzünk cross-validation-t a cross_val_predict használatával. A cv paramétert állítsuk 4-re és a random_state legyen 42. A max_iter paraméterét pedig állítsuk 10000-re. A legjobb MSE értékhez tartozó regularizációnál megtartott változók használatával nézze meg milyen MSE érhető el a teszten a szokásos GBM modellnél
