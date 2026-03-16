# Predizione della sopravvivenza nei disastri marittimi storici
## Gruppo
- Anno: 2025/2026
- Gruppo: 10
- Membri: (Nome, cognome, matricola)
    - Emanuele, Di Benedetto, 1000031016 
    - Davide, Greco, 1000099238
    - Samuele, Moscuzza, 1000016511

## Abstract
L'obiettivo del progetto è sviluppare e valutare modelli predittivi per stimare la sopravvivenza dei passeggeri coinvolti in disastri navali storici, tra cui il Titanic, l'Estonia e il Lusitania. I dati sono stati preprocessati creando un set di feature uniformi

`['survived', 'sex', 'age', 'age_missing', 'class', 'crew']`,

normalizzando tutte le variabili e combinando i tre dataset originali in un unico dataset integrato.

Sono stati addestrati quattro tipi di modelli principali:
- Softmax
- Multilayer Perceptron (MLP)
- Regressore Logistico
- Support Vector Machine (SVM)

Per l'MLP sono state testate due architetture con uno e con più layer nascosti, mentre il regressore logistico è stato addestrato con due funzioni di loss: `BCELoss` e `BCEWithLogitsLoss`, applicando `pos_weight` per bilanciare le classi.

I risultati mostrando prestazioni simili tra i modelli, con accuratezza di test intorno al **71-72%** per MLP, Softmax e SVM. Il regressore logistico con `BCELoss` ha raggiunto un'accuratezza di **71.5%** ma con bassa recall, circa **0.15**, mentre la versione con `BCEWithLogitsLoss` ha ottenuto un'accuratezza inferiore con **59.7%** presentando però un bilanciamento leggermente migliore tra precision e recall. Questi risultati indicano che modelli più complessi non garantiscono necessariamente miglioramenti significativi rispetto a modelli lineari semplici per questo dataset. **DA MODIFICARE SE DOVESSERO CAMBIARE I RISULTATI**

## Introduzione
Il presente progetto nasce con l’obiettivo di applicare tecniche di Machine Learning all'analisi di dati storici relativi a incidenti navali, con lo scopo di stimare la probabilità di sopravvivenza dei passeggeri e dei membri dell'equipaggio coinvolti. Il problema affrontato rientra nell’ambito della classificazione binaria, poiché la variabile di interesse assume due soli valori possibili: sopravvissuto o non sopravvissuto. Attraverso l’analisi dei dati disponibili, il progetto mira a evidenziare come alcune caratteristiche individuali e di contesto possano influenzare in modo significativo l’esito finale di un evento catastrofico.

L'interesse principale di questo lavoro è duplice. Da un lato si vuole comprendere il ruolo giocato da fattori socio-demografici e funzionali, come la classe di viaggio, il sesso e la mansione svolta a bordo, nella determinazione delle probabilità di sopravvivenza. Dall’altro lato, il progetto si propone di progettare, addestrare e confrontare diversi modelli predittivi, valutandone prestazioni, limiti e affidabilità in un contesto reale e complesso.

L'analisi di eventi storici di questo tipo consente inoltre di riflettere su aspetti sociali ed etici rilevanti. In situazioni di emergenza, fattori come l'accesso ai mezzi di salvataggio, le decisioni prese in condizioni di forte stress e le differenze sociali possono influenzare in modo significativo le probabilità di sopravvivenza. L’utilizzo di modelli predittivi permette di formalizzare queste osservazioni e di trasformarle in conoscenza quantitativa, rendendo possibile un’analisi sistematica delle dinamiche che caratterizzano tali eventi.

Il progetto prende come riferimento alcuni tra i più noti incidenti navali della storia moderna, scelti per la loro rilevanza storica e per la disponibilità di dati utili all’analisi.

Il naufragio del RMS Titanic, avvenuto nella notte tra il 14 e il 15 aprile 1912 durante il viaggio inaugurale da Southampton a New York, rappresenta uno dei casi di studio più emblematici. Il Titanic era considerato un simbolo del progresso tecnologico dell'epoca e ritenuto virtualmente inaffondabile. Tuttavia, la collisione con un iceberg portò a un disastro che mise in luce profonde differenze nelle probabilità di sopravvivenza tra i passeggeri. La classe di viaggio ebbe un ruolo determinante, così come il sesso, influenzato dalla prassi non ufficiale di dare priorità a donne e bambini.

Un secondo evento di grande importanza è il naufragio del MS Estonia, avvenuto nel Mar Baltico il 28 settembre 1994. A differenza del Titanic, l'Estonia operava in un'epoca caratterizzata da sistemi di sicurezza più moderni e regolamentazioni più stringenti. Nonostante ciò, il cedimento del portellone di prua in condizioni meteorologiche avverse portò a un affondamento rapido e a un numero molto elevato di vittime. In questo caso, la velocità con cui si sviluppò l'incidente ridusse drasticamente le possibilità di evacuazione.

Infine, l'affondamento del RMS Lusitania, avvenuto il 7 maggio 1915 durante la Prima Guerra Mondiale, costituisce un esempio di disastro navale in un contesto bellico. La nave fu colpita da un siluro lanciato da un sottomarino tedesco e affondò in tempi estremamente rapidi. In una situazione di questo tipo, la gestione dell'emergenza risultò fortemente compromessa dall'assenza di preavviso e dalle condizioni di guerra.

Dal punto di vista metodologico, il lavoro si articola in diverse fasi. In primo luogo viene effettuato il preprocessing dei dataset, uniformando e combinando i dati provenienti da diversi incidenti navali in un unico dataset coerente. Successivamente vengono addestrati e confrontati diversi modelli di classificazione, tra cui regressione logistica, Support Vector Machine (SVM), classificatore Softmax e Multilayer Perceptron (MLP). Infine, le prestazioni dei modelli vengono valutate attraverso metriche standard come accuracy, precision, recall e F1-score.

## Dataset
Il dataset utilizzato in questo progetto raccoglie informazioni relative ai passeggeri coinvolti in alcuni tra i più noti incidenti navali della storia moderna: il naufragio del RMS Titanic (1912), quello del MS Estonia (1994) e l'affondamento del RMS Lusitania (1915).

L'obiettivo del dataset è fornire un insieme di caratteristiche dei passeggeri che possano essere utilizzate per addestrare un modello di classificazione binaria, in grado di prevedere la probabilità di sopravvivenza in base alle informazioni disponibili.

Il dataset finale è stato ottenuto tramite la formattazione e la concatenazione di tre dataset distinti, uno per ciascun incidente navale.
Complessivamente sono presenti **3841 record** e **6 features** di natura eterogenea, comprendenti sia dati numerici sia dati categorici descritti nella **Tabella 1**

<p align="center">
    <table align="center">
        <thead>
            <tr>
                <th>Feature</th>
                <th>Tipo</th>
                <th>Descrizione</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>survived</td>
                <td>binaria</td>
                <td>variabile target che indica la sopravvivenza</td>
            </tr>
            <tr>
                <td>sex</td>
                <td>binaria</td>
                <td>sesso del passeggero</td>
            </tr>
            <tr>
                <td>age</td>
                <td>numerica</td>
                <td>età del passeggero</td>
            </tr>
            <tr>
                <td>age_missing</td>
                <td>binaria</td>
                <td>flag che indica se l'età è mancante</td>
            </tr>
            <tr>
                <td>class</td>
                <td>classe del biglietto</td>
                <td>categorica</td>
            </tr>
            <tr>
                <td>crew</td>
                <td>categorica</td>
                <td>ruolo a bordo</td>
            </tr>
        </tbody>
    </table>
    <i>Tabella 1: Tipo e descrizione delle variabili presenti nel dataset finale</i>
</p>

I tre datasets relativi ai disastri navali sono stati raccolti da fonti pubbliche disponibili online sulla piattaforma [Kaggle](https://kaggle.com)
In particolare, i dataset utilizzati sono disponibili ai seguenti link:
- [RMS Titanic](https://www.kaggle.com/datasets/abdelrahmansaad10/titanic)
- [MS Estonia](https://www.kaggle.com/datasets/christianlillelund/passenger-list-for-the-estonia-ferry-disaster)
- [RMS Lusitania](https://www.kaggle.com/datasets/rkkaggle2/rms-lusitania-complete-passenger-manifest)

Questi datasets contengono informazioni sui passeggeri coinvolti nei rispettivi incidenti navali e sono stati utilizzati come base per la costruzione del dataset finale utilizzato nel progetto.

L'acquisizione del dataset finale utilizzato per l'addestramento dei modelli è stata effettuata tramite i notebooks `merge_ship_datasets.ipynb` e `datasets_stats.ipynb`.

Il primo notebook descrive il processo di acquisizione dei dati dai tre datasets originali, nonchè le operazioni di uniformazione e integrazione necessarie per ottenere un unico dataset utilizzabile per l'addestramento dei modelli di apprendimento automatico.
Il secondo notebook presenta invece un'analisi esplorativa dei datasets, finalizzata ad individuare le variabili più rilevanti per il problema affrontato e a produrre diversi grafici riassuntivi delle caratteristiche dei dati.

Lo strumento principale utilizzato per la manipolazione e l'analisi dei dati è stata la libreria Python `pandas`.

I dataset sono stati scaricati dalle rispettive fonti in formato CSV `.csv` e successivamente sono stati analizzati, poiché presentavano strutture e variabili differenti tra loro.

Tra le variabili disponibili si è deciso di selezionare
- sopravvissuto
- età 
- sesso
- classe di viaggio 
- ruolo a bordo

Sono state invece escluse alcune variabili considerate meno rilevanti ai fini della previsione della sopravvivenza, tra cui il nome, costo del biglietto, nazionalità, porto d'imbarco, cittadinanza e stato civile.

Durante questa fase sono emerse alcune difficoltà legate all'eterogeneità delle informazioni disponibili nei diversi dataset. In particolare, nel dataset relativo al RMS Titanic non è presente l'informazione relativa al ruolo a bordo, mentre nei dataset relativi ad MS Estonia e al RMS Lusitania non risulta disponibile la classe del biglietto.

Il preproccessing effettuato prevede le seguenti operazioni sulle variabili del dataset:
- Variabile `survived`: viene creata copiando il valore numero `0` (non sopravvissuto) e `1` (sopravvissuto) se disponibile. Nei casi in cui la variabile sia espressa in forma testuale, come nel dataset del RMS Lusitania dove i valori sono `lost` e `saved`, questi vengono mappati rispettivamente a `0` ed `1`.
- Variabile `sex`: le stringhe `male` e `female`, o le abbreviazioni `m` ed `f`, vengono mappate nei valori numerici `0` (maschio) ed `1` (femmina).
- Variabile `age`: viene mantenuto il valore numerico originale. In presenza di valori mancanti, questi vengono sostituiti con la mediana dell'età dei passeggeri e viene impostata la variabile `age_missing = 1` come **flag** per indicare al modello che il valore originale non è disponibile.
- Variabile `class` (classe del biglietto): se il valore non è disponibile viene assegnato `0`; altrimenti viene utilizzato il corrispettivo valore numerico della classe (1 = prima classe, 2 = seconda classe, 3 = terza classe).
- Variabile `crew` (ruolo a bordo): viene codificata come `1` se il soggetto è membro dell'equipaggio e `0` se passeggero. In assenza di informazioni, viene utilizzato il valore `-1`.

Successivamente, prima dell'addestramento dei modelli, i dati vengono suddivisi in training set e test set e normalizzati. La suddivisione è effettuata tramite la funzione `train_test_split` della libreria `scikit-learn` impostando il parametro `test_size = 0.2`, ottenendo uno split del **80%** per il training set e del **20%** nel test set. Per garantire che la distribuzione delle classi sia rappresentata in entrambi i set, viene impostato il parametro `stratify = Y`, dove `Y` corrisponde ai label di sopravvivenza. Ad esempio, se i label sono suddivisi in 70% per `0` e 30% per `1`, lo stesso rapporto verrà mantenuto sia nel training set sia nel test set.

La normalizzazione delle variabili numeriche del training set viene effettuata tramite standardizzazione (z-score), definita come:
$$
X_{norm} = \frac{X - \mu}{\sigma}
$$
dove $\mu$ e $\sigma$ rappresentano rispettivamente la media e la deviazione standard di $X$.

Tra i grafici riassuntivi dei dati calcolati nel notebook `datasets_stats.ipynb` è presente l'analisi della distribuzione della variabile target `survived`, che indica se un passeggero è sopravvissuto o meno all'incidente navale.

Il grafico in **Figura 1** mostra il numero di passeggeri sopravvisuti e non sopravvisuti presenti nel dataset complessivo.

<p align="center">
    <img src="../media/survival_distribution.png" width="33%">
    <br>
    <i>Figura 1: Distribuzione della sopravvivenza dei passeggeri</i>
</p>

Questo tipo di analisi è utile per verificare se il dataset presenta sbilanciamento tra classi, che potrebbe influenzare l'addestramento dei modelli di classificazione. L'analisi evidenzia effettivamente una maggiore presenza della classe `0` (passeggeri non sopravvisuti) con il **67.53%** dei record totali nel dataset.

Successivamente è stata analizzata la distribuzione del sesso dei passeggeri. Come mostrato in **Figura 2**, la popolazione del dataset è composta per circa il **66%** da passeggeri di sesso maschile e per circa il **33%** di passeggeri di sesso femminile.

<p align="center">
    <img src="../media/sex_distribution.png" width="33%">
    <br>
    <i>Figure 2: Distribuzione del sesso dei passeggeri</i>
</p>

Un'ulteriore analisi riguarda la distribuzione della sopravvivenza in funzione del sesso dei passeggeri, riportata in **Figura 3**.

<p align="center">
    <img src="../media/survival_by_sex.png" width="33%">
    <br>
    <i>Figura 3: Distribuzione della sopravvivenza in funzione del sesso dei passeggeri</i>
</p>

Nel caso del naufragio del RMS Titanic era presente il noto protocollo informale "prima le donne e bambini" (**Figura 3.1**), che portava a dare priorità alle donne nelle operazioni di evacuazione. Tuttavia, poiché il dataset include anche i disastri navali del RMS Lusitania e del MS Estonia (**Figura 3.2 e Figura 3.3**), questo effetto risulta meno marcato nel dataset complessivo. Infatti le percentuali di sopravvivenza risultano relativamente simili tra i due sessi, con circa il **31%** dei passeggeri maschi sopravvisuti e circa il **34%** delle passeggere femmine.

<table align="center">
    <tr>
        <td align="center">
            <img src="../media/survival_by_sex_titanic.png" width="80%"><br>
            <i>Figura 3.1: Distribuzione della sopravvivenza in funzione del sesso dei passeggeri del RMS Titanic</i>
        </td>
        <td align="center">
            <img src="../media/survival_by_sex_estonia.png" width="80%"><br>
            <i>Figura 3.2: Distribuzione della sopravvivenza in funzione del sesso dei passeggeri del MS Estonia</i>
        </td>
        <td align="center">
            <img src="../media/survival_by_sex_lusitania.png" width="80%"><br>
            <i>Figura 3.3: Distribuzione della sopravvivenza in funzione del sesso dei passeggeri del RMS Lusitania</i>
        </td>
    </tr>
</table>

Un'altra caratteristica rilevante per l'analisi dei passeggeri è rappresentata dall'età. La **Figura 4** mostra la distribuzione dell'età nel dataset, mentre la **Figura 4.1** riporta la distribuzione della sopravvivenza in funzione dell'età dei passeggeri.

<table align="center">
    <tr>
        <td align="center">
            <img src="../media/age_distribution.png" width="66%"><br>
            <i>Figura 4: Distribuzione dell'età dei passeggeri</i>
        </td>
        <td align="center">
            <img src="../media/age_distribution_by_survival.png" width="66%"><br>
            <i>Figura 4.1: Distribuzione della sopravvivenza per età dei passeggeri</i>
        </td>
    </tr>
</table>

Nei due grafici sono considerati solamente i valori di età effettivamente disponibili nel dataset, escludendo quelli inseriti durante la fase di preprocessing. Questa scelta è stata adottata per evitare che i valori inseriti artificialmente potessero alterare la distribuzione reale dei dati. L'analisi dell’età permette inoltre di osservare come la popolazione dei passeggeri sia distribuita principalmente nelle fasce di età adulte, con una presenza minore di bambini e anziani.

## Metodologia

