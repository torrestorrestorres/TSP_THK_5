# TSP - KI/ TH Koeln 

![Robot](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExazZ3eXFtNDFycjhzenhybGF3NW1pcXVueGMwZ2VkNTk0aml2bHNtayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/0lGd2OXXHe4tFhb7Wh/giphy.gif)

## Teammitglieder
- [x] Niclas Schößow
- [x] Maximilian Goomer
- [x] Tristan Wingert

## TSP - Traveling Salesman Problem
Das Problem des Handlungsreisenden (engl. Travelling Salesman Problem, TSP) ist ein kombinatorisches Optimierungsproblem.

* **Gegeben**: n Städte
* **Gesucht**: kürzeste Rundreise, die jede Stadt genau einmal besucht und zum Ausgangspunkt zurückkehrt
* **Voraussetzungen**: Kantengewichten (Distanzen)
* **Binäre Variable**: x_ij = 1, wenn die Reise von Stadt i nach Stadt j führt, sonst 0
* **Nebenbedingungen**: 
    * Jede Stadt wird genau einmal besucht
    * Jeder Knoten hat genau eine eingehende und eine ausgehende Kante
    * Die Rundreise endet am Startpunkt
  
### Permuation
Eine Permutation ist eine Anordnung von Objekten in einer bestimmten Reihenfolge.
**Zwei Zeilen Notation**


### Charakteristika
* Starten mit einer (oder mehreren) zufälligen Lösungen
* Führen iterative Schritte durch, durch die eine (oder mehrere) neue Lösung(en) generiert werden
* Neue Lösung durch Modifikation (Variation) bereits existierender
* Anzahl von Schritten begrenzt (häufig vorher festgelegt)
* Führen Exploration und Exploitation durch

  #### Bausteine
* **Repräsentation**: Permutation
* **Variationsoperatoren**: Mutation, Rekombination
* **Relation zwischen Lösungen**: → Zielfunktion
* **Startlösung**
* **Strategie** 
* **Fitnessfunktion**: Zielfunktion einer Optimierungsaufgabe
* **Rekombination**: (Crossover) Neuanordnung von Teilen zweier Lösungen (theoretisch auch mehrerer)
* **Mutation**: Zufällige Veränderung einer Lösung
* **Selektion**: Auswahl von Lösungen für die nächste Generation
* **Variation**: Mutation und Rekombination 

**Mutation**: 
* Mit bestimmter Wahrscheinlichkeit wird eine zufällige Anzahl von Bits invertiert
* Invertierung: 0 → 1, 1 → 0
* Unsere Wahrscheinlichkeit: 1/ Anzahl der Städte
* Beispiel: 1001 → 1011
* Oder: 1001011 → 1001010 


## Aufgabenstellung
Implementierung eines evolutionären Algorithmus (EA) zur Lösung des Traveling Salesman Problems (TSP).
Dabei sollen verschiedene Parameter des Verfahrens frei wählbar
sein und die Auswirkungen verschiedener Einstellungen untersucht werden.




## Testinstanzen

Die Testinstanzen sind im Ordner [`data`](./data) zu finden. 
Die Instanzen sind im TSPLIB-Format gespeichert.
[TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)


## Implementierung

### Verwendete Testinstanzen
- [x] [blabla]()
- [x] [blabla]()


### Verwendete Repräsentation


### Verwendete Variationsoperatoren
