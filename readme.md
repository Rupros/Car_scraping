# Automašīnu sarakstu Tīmekļa skrāpis

## PROJEKTA INFORMĀCIJA

Pie projekta strādāju individuāli. Tā kā bieži pārbaudu jaunu automašīnu piedāvājumus, nolēmu izveidot autonomu botu, kas apkopotu piedāvājumus, par kuriem es būtu ieinteresēts.

## Pārskats

Šis ir vienkāršs tīmekļa skrāpis, kas paredzēts automašīnu sarakstu apkopošanai, pamatojoties uz lietotāja norādītiem kritērijiem. Skrāpis ir rakstīts Python un izmanto selēna bibliotēku tīmekļa skrāpēšanai. Tas ir paredzēts kā sākumpunkts lietotājiem, kuri vēlas apkopot automašīnu sarakstus no dažādām vietnēm savām īpašajām interesēm.

Lai padarītu to cilvēciskāku, tiek izmantoti nejauši laika intervāli

## Iespējas

- **Pielāgojami meklēšanas kritēriji:** Cena | Nobraukums, pamatojoties uz manām vajadzībām | meklēju tikai Audi | Pie dīlera, ļauju cenai būt augstākai, jo tur ir savs uzcenojums
  
- **Vairāku vietņu atbalsts:** Vietņu pārbaude ss.lv un mollerauto.lv

- **Datu izvade:** failā saglabā saites uz automašīnām, kas atbilst maniem kritērijiem

## Priekšnoteikumi

Pirms skrāpja palaišanas pārliecinieties, vai ir instalēta šāda informācija:

- Python 3.x
- Selenium

## ATRUNA

Šis tīmekļa skrāpis ir paredzēts tikai izglītojošiem nolūkiem. Izmantojot to bieži, vietne var to noteikt kā robotu. Tika īstenoti pretpasākumi, piemēram, nejaušināts laiks starp mijiedarbībām. Selēna JS paraksts nav slēpts, jo tas ir atkarīgs no mašīnas, kurā tas tiks darbināts.

Projekts iespējams var nedarboties, ja mājaslapas tiek atjauninātas un neatbilst vairs iepriekšējai funkcionalitātei. SEKOT LĪDZI!

### IZMANTOTAS BIBLIOTĒKAS

## Selenium integrācija

Šis tīmekļa skrāpis izmanto Selēna bibliotēku, lai uzlabotu tīmekļa skrāpēšanas iespējas. Selēns tiek izmantots gadījumos, kad vietne lielā mērā ir atkarīga no JavaScript vai kad datu izguvei ir jāmaina tīmekļa lapas interaktīvie elementi.

### Selenium sastāvdaļas

- **WebDriver:** Webdriver klase ir galvenā saskarne mijiedarbībai ar tīmekļa pārlūkprogrammām. Tas ļauj skrāpim atvērt pārlūkprogrammas logu, pārvietoties uz tīmekļa lapām un mijiedarboties ar lapas elementiem.

- **Options:** klase Opcijas kopā ar Firefox ļauj konfigurēt pārlūkprogrammas darbību. To bieži izmanto, lai iestatītu tādas opcijas kā pārlūkprogrammas palaišana bezgalvu režīmā (bez redzama lietotāja saskarnes).

- **By:** Klase "Pēc" tiek izmantota, lai tīmekļa lapā atrastu HTML elementus. Tas nodrošina dažādus mehānismus elementu atrašanai, piemēram, pēc ID, nosaukuma, klases nosaukuma utt.

- **WebDriverWait:** klase "WebDriverWait" tiek izmantota, lai gaidītu, līdz iestājas noteikts nosacījums, pirms turpināt skripta izpildi. Šī sinhronizācija nodrošina, ka skripts turpinās tikai tad, ja ir izpildīti īpaši nosacījumi.

- **expected_conditions:** Šis modulis nodrošina iepriekš definētus nosacījumus, kurus var izmantot ar WebDriverWait. Tas ļauj gaidīt konkrētus notikumus vai stāvokļus tīmekļa lapā.

- **TimeoutException:** TimeoutException tiek palielināts, kad darbībai iestājas noildze. Bieži tiek izmantots kopā ar WebDriverWait, lai apstrādātu situācijas, kad noteiktā laikā netiek izpildīts paredzētais nosacījums.

### Laiks un nejaušība

Papildus Selenium skriptā ir iekļauti šādi moduļi:

- **time:** modulis "laiks" ievieš skripta aizkavi. Elementu ielādes gaidīšana pirms mijiedarbības ir izplatīta tīmekļa skrāpēšanā, un “time.sleep()” nodrošina vienkāršu veidu, kā pievienot aizkaves.

- **random:** Nejaušības modulis tiek izmantots, lai ieviestu nejaušību gaidīšanas laikos. Tas palīdz izvairīties no vietņu atklāšanas, kas var bloķēt vai ierobežot piekļuvi automatizētiem skriptiem. Nejauši gaidīšanas laiki liek skrāpēšanai vairāk līdzināties cilvēka uzvedībai.
