# Predizione della sopravvivenza nei disastri marittimi storici
## Gruppo
- Anno: 2025/2026
- Gruppo: 10
- Membri: (Nome, cognome, matricola)
    - Emanuele, Di Benedetto, 1000031016 
    - Davide, Greco, matr
    - Samuele, Moscuzza, 1000016511

## Abstract
L'obiettivo del progetto è sviluppare e valutare modelli predittivi per stimare la sopravvivenza dei passeggeri coinvolti in disastri navali storici, tra cui il Titanic, l'Estonia e il Lusitania. I dati sono stati preprocessati creando un set di feature uniformi

`['survived', 'sex', 'age', 'age2', 'class', 'sex_class', 'crew']`,

normalizzando tutte le variabili e combinando i tre dataset originali in un unico dataset integrato.

Sono stati addestrati quattro tipi di modelli principali:
- Softmax
- Multilayer Perceptron (MLP)
- Regressore Logistico
- Support Vector Machine (SVM)

Per l'MLP sono state testate due architetture con uno e con più layer nascosti, mentre il regressore logistico è stato addestrato con due funzioni di loss: `BCELoss` e `BCEWithLogitsLoss`, applicando `pos_weight` per bilanciare le classi.

I risultati mostrando prestazioni simili tra i modelli, con accuratezza di test intorno al **71-72%** per MLP, Softmax e SVM. Il regressore logistico con `BCELoss` ha raggiunto un'accuratezza di **71.5%** ma con bassa recall, circa **0.15**, mentre la versione con `BCEWithLogitsLoss` ha ottenuto un'accuratezza inferiore con **59.7%** presentando però un bilanciamento leggermente migliore tra precision e recall. Questi risultati indicano che modelli più complessi non garantiscono necessariamente miglioramenti significativi rispetto a modelli lineari semplici per questo dataset.

## Introduzione
Il presente progetto nasce con l’obiettivo di applicare tecniche di Machine Learning all'analisi di dati storici relativi a incidenti navali, con lo scopo di stimare la probabilità di sopravvivenza dei passeggeri e dei membri dell'equipaggio coinvolti. Il problema affrontato rientra nell’ambito della classificazione binaria, poiché la variabile di interesse assume due soli valori possibili: sopravvisuto o non sopravvisuto. Attraverso l’analisi dei dati disponibili, il progetto mira a evidenziare come alcune caratteristiche individuali e di contesto possano influenzare in modo significativo l’esito finale di un evento catastrofico.

L'interesse principale di questo lavoro è duplice. Da un lato si vuole comprendere il ruolo giocato da fattori socio-demografici e funzionali, come la classe di viaggio, il sesso e la mansione svolta a bordo, nella determinazione delle probabilità di sopravvivenza. Dall’altro lato, il progetto si propone di progettare, addestrare e confrontare diversi modelli predittivi, valutandone prestazioni, limiti e affidabilità in un contesto reale e complesso.

L'analisi di eventi storici di questo tipo consente inoltre di riflettere su aspetti sociali ed etici rilevanti. In situazioni di emergenza, fattori come l'accesso ai mezzi di salvataggio, le decisioni prese in condizioni di forte stress e le differenze sociali possono influenzare in modo significativo le probabilità di sopravvivenza. L’utilizzo di modelli predittivi permette di formalizzare queste osservazioni e di trasformarle in conoscenza quantitativa, rendendo possibile un’analisi sistematica delle dinamiche che caratterizzano tali eventi.

Il progetto prende come riferimento alcuni tra i più noti incidenti navali della storia moderna, scelti per la loro rilevanza storica e per la disponibilità di dati utili all’analisi.

Il naufragio del RMS Titanic, avvenuto nella notte tra il 14 e il 15 aprile 1912 durante il viaggio inaugurale da Southampton a New York, rappresenta uno dei casi di studio più emblematici. Il Titanic era considerato un simbolo del progresso tecnologico dell'epoca e ritenuto virtualmente inaffondabile. Tuttavia, la collisione con un iceberg portò a un disastro che mise in luce profonde differenze nelle probabilità di sopravvivenza tra i passeggeri. La classe di viaggio ebbe un ruolo determinante, così come il sesso, influenzato dalla prassi non ufficiale di dare priorità a donne e bambini.

Un secondo evento di grande importanza è il naufragio del MS Estonia, avvenuto nel Mar Baltico il 28 settembre 1994. A differenza del Titanic, l'Estonia operava in un'epoca caratterizzata da sistemi di sicurezza più moderni e regolamentazioni più stringenti. Nonostante ciò, il cedimento del portellone di prua in condizioni meteorologiche avverse portò a un affondamento rapido e a un numero molto elevato di vittime. In questo caso, la velocità con cui si sviluppò l'incidente ridusse drasticamente le possibilità di evacuazione.

Infine, l'affondamento del RMS Lusitania, avvenuto il 7 maggio 1915 durante la Prima Guerra Mondiale, costituisce un esempio di disastro navale in un contesto bellico. La nave fu colpita da un siluro lanciato da un sottomarino tedesco e affondò in tempi estremamente rapidi. In una situazione di questo tipo, la gestione dell'emergenza risultò fortemente compromessa dall'assenza di preavviso e dalle condizioni di guerra.

Dal punto di vista metodologico, il lavoro si articola in diverse fasi. In primo luogo viene effettuato il preprocessing dei dataset, uniformando e combinando i dati provenienti da diversi incidenti navali in un unico dataset coerente. Successivamente vengono addestrati e confrontati diversi modelli di classificazione, tra cui regressione logistica, Support Vector Machine (SVM), classificatore Softmax e Multilayer Perceptron (MLP). Infine, le prestazioni dei modelli vengono valutate attraverso metriche standard come accuracy, precision, recall e F1-score.
