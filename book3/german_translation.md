# Übersetzung ins Deutsche

## Übersetzungsfortschritt

Vorwort:

- [ ] A0-preface.mkd

Inhaltskapitel:

- [ ] 01-intro.mkd
- [x] 02-variables.mkd
- [x] 03-conditional.mkd
- [x] 04-functions.mkd
- [x] 05-iterations.mkd
- [x] 06-strings.mkd
- [ ] 07-files.mkd
- [ ] 08-lists.mkd
- [ ] 09-dictionaries.mkd
- [ ] 10-tuples.mkd
- [ ] 11-regex.mkd
- [ ] 12-network.mkd
- [ ] 13-web.mkd
- [ ] 14-objects.mkd
- [ ] 15-database.mkd
- [ ] 16-viz.mkd

Appendix:

- [ ] AA-contrib.mkd
- [ ] AB-copyright.mkd

## Allgemeines

- Deutsche Anführungszeichen im Fließtext verwenden: nicht "...", sondern „...“
- Darauf achten, dass in der Übersetzung Backticks (`` ` ``) erhalten bleiben (zur Auszeichnung von Code mit Markdown).
- Eine `.mkd`-Datei muss zwingend mit **zwei** Leerzeilen schließen, damit beim Kompilieren die nächste Kapitelüberschrift als solche erkannt wird.
- Die Zeilen eines Absatzes vorzugsweise zusammenführen.
- Englische Begriffe, für die eine etablierte deutsche Übersetzungen existiert, sollten bei der ersten Einführung des Begriffs in Klammern genannt werden (sofern der englische Begriff auch im Deutschen geläufig ist). Zum Beispiel: `Eine Zeichenkette (englisch *String*) ist eine Folge einzelner Zeichen (englisch *Character*).`

## Übersetzungstabellen

Übersetzungstabellen zum Zwecke einer einheitlichen Übersetzung. Übersetzungen gelten kapitelübergreifend und werden hier nicht doppelt aufgeführt. Bitte die Suchfunktion verwenden. In erster Linie geht es hier um das Festlegen sinnvoller Indexeinträge.

### Kapitel 2

```
\index{value} : \index{Wert}
\index{type} : \index{Datentyp}
\index{string} : \index{Zeichenkette}
\index{class!str} : \index{Klasse!str}
String : Zeichenkette
\index{quotation mark} : \index{Anführungszeichen}
\index{int type} : \index{Ganzzahl}
\index{class!int} : \index{Klasse!int}
\index{float type} : \index{Gleitkommazahl}
\index{class!float} : \index{Klasse!float}
\index{semantic error} : \index{semantischer Fehler}
\index{error!semantic} : \index{Fehler!semantischer}
\index{error message} : \index{Fehlermeldung}
\index{variable} : \index{Variable}
name : Bezeichner
\index{assignment statement} : \index{Zuweisung}
\index{statement!assignment} : \index{Anweisung!Zuweisung}
\index{keyword} : \index{Schlüsselwort}
\index{underscore character} : \index{Unterstrich}
\index{statement} : \index{Anweisung}
\index{interactive mode} : \index{interaktiver Modus}
\index{script mode} : \index{Skript-Modus}
\index{operator, arithmetic} : \index{Operator, arithmetisch}
\index{arithmetic operator} : \index{arithmetischer Operator}
\index{operand} : \index{Operand}
\index{operator} : \index{Operator}
\index{expression} : \index{Ausdruck}
\index{floating-point division} : \index{Fließkommadivision}
\index{division!floating-point} : \index{Division!Fließkomma}
\index{evaluate} : \index{Auswertung}
**Exercise : **Übung
\index{order of operations} : \index{Auswertungsreihenfolge}
\index{rules of precedence} : \index{Vorrangregeln}
\index{precedence} : \index{Vorrang}
\index{parentheses!overriding precedence} : \index{Klammern!Vorrangregeln überschreiben}
\index{modulus operator} : \index{Modulo-Operator}
\index{operator!modulus} : \index{Operator!Modulo}
\index{string!operation} : \index{Zeichenkette!Operation}
\index{operator!string} : \index{Operator!Zeichenkette}
\index{divisibility} : \index{Teilbarkeit}
\index{concatenation} : \index{Konkatenation}
\index{keyboard input} : \index{Benutzereingaben}
\index{prompt} : \index{Prompt}
\index{newline} : \index{Newline}
\index{comment} : \index{Kommentar}
\index{syntax error} : \index{Syntaxfehler}
\index{error!syntax} : \index{Fehler!syntax}
\index{exception} : \index{Ausnahme}
\index{exception!ValueError} : \index{Ausnahme!ValueError}
\index{runtime error} : \index{Laufzeitfehler}
\index{error!runtime} : \index{Fehler!Laufzeit}
\index{case-sensitivity, variable names} : \index{case-sensitivity, Variablennamen}
Glossary : Glossar
assignment : Zuweisung
\index{assignment} : \index{Zuweisung}
\index{floating-point} : \index{Gleitkommazahl}
\index{integer} : \index{Ganzzahl}
Exercises : Übungen
```

### Kapitel 3

```
Conditional execution : Bedingte Ausführung
\index{boolean expression} : \index{boolescher Ausdruck}
\index{expression!boolean} : \index{Ausdruck!boolescher}
\index{logical operator} : \index{logischer Operator}
\index{operator!logical} : \index{Operator!logischer}
\index{True special value} : \index{True Wahrheitswert}
\index{special value!True} : \index{Wert!True}
\index{special value!False} : \index{Wert!False}
\index{False special value} : \index{False Wahrheitswert}
\index{bool type} : \index{bool Datentyp}
\index{type!bool} : \index{Datentyp!bool}
\index{comparison operator} : \index{Vergleichsoperator}
\index{operator!comparison} : \index{Operator!Vergleich}
\index{and operator} : \index{and Operator}
\index{or operator} : \index{or Operator}
\index{not operator} : \index{not Operator}
\index{Operator!and} : \index{Operator!and}
\index{Operator!or} : \index{Operator!or}
\index{Operator!not} : \index{Operator!not}
\index{conditional statement} : \index{bedingte Anweisung}
\index{statement!conditional} : \index{Anweisung!bedingte}
\index{if statement} : \index{if-Anweisung}
\index{statement!if} : \index{Anweisung!if}
\index{conditional executions} : \index{bedingte Ausführung}
\index{condition} : \index{Bedingung}
\index{compound statement} : \index{zusammengesetzte Anweisung}
\index{statement!compound} : \index{Anweisung!zusammengesetzte}
\index{pass statement} : \index{pass Statement}
\index{statement!pass} : \index{Anweisung!pass}
Chevrons : Größer-Zeichen
Alternative execution : Alternative Ausführung
\index{alternative execution} : \index{alternative Ausführung}
\index{else keyword} : \index{else Schlüsselwort}
\index{keyword!else} : \index{Schlüsselwort!else}
\index{branch} : \index{Verzweigung}
\index{chained conditional} : \index{verkettete Bedingung}
\index{conditional!chained} : \index{Bedingung!verkettete}
\index{elif keyword} : \index{elif Schlüsselwort}
\index{keyword!elif} : \index{Schlüsselwort!elif}
\index{nested conditional} : \index{verschachtelte Bedingung}
\index{conditional!nested} : \index{Bedingung!verschachtelte}
\index{traceback} : \index{Traceback}
\index{short circuit} : \index{abgekürzte Auswertung}
guardian pattern : Wächter-Muster
\index{guardian pattern} : \index{Wächter-Muster}
\index{pattern!guardian} : \index{Muster!Wächter}
\index{debugging} : \index{Debugging}
\index{whitespace} : \index{Whitespace}
body : Block
\index{body} : \index{Block}
```

### Kapitel 4

```
\index{function call} : \index{Funktionsaufruf}
\index{argument} : \index{Argument}
\index{return value} : \index{Rückgabewert}
\index{type conversion} : \index{Typumwandlung}
\index{conversion!type} : \index{Umwandlung!Datentyp}
\index{int function} : \index{int Funktion}
\index{function!int} : \index{Funktion!int}
\index{parentheses!argument in} : \index{Klammern!Argument in}
\index{float function} : \index{float Funktion}
\index{function!float} : \index{Funktion!float}
\index{str function} : \index{str Funktion}
\index{function!str} : \index{Funktion!str}
\index{math function} : \index{math Modul}
\index{module} : \index{Modul}
\index{module object} : \index{Modul-Objekt}
\index{dot notation} : \index{Punkt-Notation}
\index{log function} : \index{log Funktion}
\index{function!log} : \index{Funktion!log}
\index{sine function} : \index{sine Funktion}
\index{trigonometric function} : \index{trigonometrische Funktion}
\index{sqrt function} : \index{sqrt Funktion}
\index{function!sqrt} : \index{Funktion!sqrt}
\index{random number} : \index{Zufallszahl}
\index{deterministic} : \index{deterministisch}
\index{pseudorandom} : \index{pseudozufällig}
\index{random module} : \index{random Modul}
\index{module!random} : \index{Modul!random}
\index{random function} : \index{random Funktion}
\index{function!random} : \index{Funktion!random}
\index{randint function} : \index{randint Funktion}
\index{function!randint} : \index{Funktion!randint}
\index{choice function} : \index{choice Funktion}
\index{function!choice} : \index{Funktion!choice}
\index{function} : \index{Funktion}
\index{function definition} : \index{Funktionsdefinition}
\index{definition!function} : \index{Definition!Funktion}
\index{def keyword} : \index{def Schlüsselwort}
\index{keyword!def} : \index{Schlüsselwort!def}
\index{parentheses!empty} : \index{Klammern!leer}
\index{parentheses!parameters in} : \index{Klammern!Parameter in}
\index{header} : \index{Funktionskopf}
\index{body} : \index{Funktionsrumpf}
\index{indentation} : \index{Einrückung}
\index{colon} : \index{Doppelpunkt}
\index{ellipses} : \index{Ellipse (Auslassungspunkte)}\index{Auslassungspunkte (Ellipse)}
\index{function object} : \index{Funktionsobjekt}
\index{object!function} : \index{Objekt!Funktion}
\index{parameter} : \index{Parameter}
\index{function parameter} : \index{Funktionsparameter}
\index{function argument} : \index{Funktionsargument}
\index{fruitful function} : \index{Rückgabewert einer Funktion}
\index{void function} : \index{void, Funktion ohne Rückgabewert}
\index{function, fruitful} : \index{Funktion mit Rückgabewert}
\index{function, void} : \index{Funktion ohne Rückgabewert, void}
\index{None special value} : \index{None, Wert}
\index{special value!None} : \index{Wert!None}
\index{function, reasons for} : \index{Funktionen}
\index{flow of execution} : \index{Programmablauf}
import statement : Importanweisung
\index{import statement} : \index{Importanweisung}
\index{statement!import} : \index{Anweisung!Import}
```

### Kapitel 5

```
\index{iteration} : \index{Iteration}
\index{update} : \index{Aktualisierung}
\index{variable!updating} : \index{Variable!aktualisieren}
\index{initialization (before update)} : \index{Initialisierung}
\index{increment} : \index{Inkrementieren}
\index{decrement} : \index{Dekrementieren}
\index{statement!while} : \index{Anweisung!while}
\index{while loop} : \index{while-Schleife}
\index{loop!while} : \index{Schleife!while}
\index{loop} : \index{Schleife}
\index{infinite loop} : \index{Endlosschleife}
\index{loop!infinite} : \index{Schleife!endlos}
\index{break statement} : \index{break-Anweisung}
\index{statement!break} : \index{Anweisung!break}
\index{continue statement} : \index{continue-Anweisung}
\index{statement!continue} : \index{Anweisung!continue}
\index{for statement} : \index{for-Schleife}
\index{statement!for} : \index{Schleife!for}
\index{accumulator!sum} : \index{Akkumulator!Summe}
\index{loop!maximum} : \index{Schleife!Maximum}
\index{loop!minimum} : \index{Schleife!Minimum}
\index{debugging!by bisection} : \index{Debugging!mittels Bisektion}
\index{bisection, debugging by} : \index{Bisektion, Debugging mittels}
\index{accumulator} : \index{Akkumulator}
\index{counter} : \index{Schleifenzähler}
```

### Kapitel 6

```
\index{sequence} : \index{Folge}
\index{character} : \index{Einzelzeichen (Character)}
\index{bracket operator} : \index{indexbasierter Zugriffsoperator}\index{Zugriffsoperator, indexbasiert}
\index{operator!bracket} : \index{Operator!indexbasierter Zugriff}
\index{index} : \index{Index}
\index{} : \index{} 
\index{index!starting at zero} : \index{Index!beginnt mit Null}
\index{zero, index starting at} : \index{Null, Index beginnt mit}
\index{exception!TypeError} : \index{Ausnahme!TypeError}
\index{TypeError} : \index{TypeError}
\index{len function} : \index{len, Funktion}
\index{function!len} : \index{Funktion!len}
\index{exception!IndexError} : \index{Ausnahme!IndexError}
\index{IndexError} : \index{IndexError}
\index{index!negative} : \index{Index!negativ}
\index{negative index} : \index{negativer Index}
\index{traversal} : \index{Traversieren}
\index{loop!traversal} : \index{Schleife!Traversieren}
\index{for loop} : \index{for-Schleife}
\index{loop!for} : \index{Schleife!for}
\index{slice operator} : \index{slice-Operator}
\index{operator!slice} : \index{Operator!slice}
\index{index!slice} : \index{Index!slice}
\index{string!slice} : \index{Zeichenkette!slice}
\index{slice!string} : \index{slice!Zeichenkette}
\index{copy!slice} : \index{Kopieren!slice}
\index{slice!copy} : \index{slice!Kopieren}
\index{mutability} : \index{Veränderbarkeit}
\index{immutability} : \index{Unveränderlichkeit}
\index{string!immutable} : \index{Zeichenkette!unveränderlich}
\index{object} : \index{Objekt}
\index{item assignment} : \index{Element-Zuweisung}
\index{assignment!item} : \index{Zuweisung!Element}
\index{counting and looping} : \index{Zählen mit Schleifen}
\index{looping and counting} : \index{Schleifen und Zählen}
\index{looping!with strings} : \index{Schleife!mit Zeichenketten}\index{Iteration!durch Zeichenketten}
\index{encapsulation} : \index{Auslagern von Code in Funktionen}
\index{in operator} : \index{in-Operator}
\index{operator!in} : \index{Operator!in}
\index{boolean operator} : \index{boolescher Operator}
\index{operator!boolean} : \index{Operator!boolescher}
\index{string!comparison} : \index{Zeichenkette!Vergleich}
\index{comparison!string} : \index{Vergleich!Zeichenkette}
\index{method} : \index{Methode}
\index{string!method} : \index{Zeichenkette!Methode}
\index{invocation} : \index{Aufruf einer Methode}
\index{optional argument} : \index{optionales Argument}
\index{argument!optional} : \index{Argument!optional}
\index{count method} : \index{count-Methode}
\index{method!count} : \index{Methode!count}
\index{format operator} : \index{Formatierungsoperator}
\index{operator!format} : \index{Operator!Formatierung}
\index{format string} : \index{Format-String}
\index{format sequence} : \index{Formatierungszeichen}
format string : Format-String
format sequence : Formatierungszeichen
\index{empty string} : \index{leere Zeichenkette}
format operator : Formatierungsoperator
flag : Flag
\index{flag} : \index{Flag}
item : Element
\index{item} : \index{Element}
\index{search pattern} : \index{Suchmuster}
\index{pattern!search} : \index{Muster!Suche}
\index{slice} : \index{Teilzeichenkette}
\index{string method} : \index{Zeichenkette!Methode}
\index{method!string} : \index{Methode!Zeichenkette}
```
