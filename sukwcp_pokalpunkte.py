##################
# Berechnung der Pokalpunkte fuer den saechsischen UKW Contest Pokal
# Formel: Pokalpunkte = Ergebnis/(Ergebnis des 1.) * Bandmulti * (Teilnehmer des Bandes)
##################
import csv
import os

filename='22_11_Multi_formatted'
#Liste der gueltigen Baender
bands = ["145 MHz", "435 MHz", "1.2 GHz", "2.3 GHz", "3.4 GHz", "5.7 GHz", "10 GHz", "24 GHz", "47 GHz", "76 GHz", "122 GHz", "135 GHz", "245 GHz", "300 GHz"]
#Verzeichnis der Multiplikatoren pro Band
bandmult={"145 MHz": 20, "435 MHz": 25, "1.2 GHz": 30, "2.3 GHz": 35, "3.4 GHz": 35, "5.7 GHz": 35, "10 GHz": 35, "24 GHz": 35, "47 GHz": 35, "76 GHz": 35, "122 GHz": 35, "135 GHz": 35, "245 GHz": 35, "300 GHz": 35}
#in diesem Verzeichnis wird die Anzahl der Teilnehmer pro Band gespeichert
teilnehmer={"145 MHz": 0, "435 MHz": 0, "1.2 GHz": 0, "2.3 GHz": 0, "3.4 GHz": 0, "5.7 GHz": 0, "10 GHz": 0, "24 GHz": 0, "47 GHz": 0, "76 GHz": 0, "122 GHz": 0, "135 GHz": 0, "245 GHz": 0, "300 GHz": 0}
maxerg={"145 MHz": 0, "435 MHz": 0, "1.2 GHz": 0, "2.3 GHz": 0, "3.4 GHz": 0, "5.7 GHz": 0, "10 GHz": 0, "24 GHz": 0, "47 GHz": 0, "76 GHz": 0, "122 GHz": 0, "135 GHz": 0, "245 GHz": 0, "300 GHz": 0}
resulttable = []

with open(filename+'.csv') as csvdatei:
    ergebnisse = csv.DictReader(csvdatei, delimiter=',')
    #Teilnehmerzahl pro Band bestimmen und max. Ergebnis
    for row in ergebnisse:
        #print(row)
        for band in bands:
            if row[band]!='0':
                #print(band+':'+row[band])
                teilnehmer[band]+=1
                if int(row[band])>int(maxerg[band]):
                    maxerg[band]=row[band]
    print('Teilnehmer: ')
    print(teilnehmer)
    print('Bestes Ergebnis:')
    print(maxerg)
    csvdatei.seek(0) #an Anfang der Datei zurueckspringen
    #Punkte pro Band berechnen
    ergebnisse = csv.DictReader(csvdatei, delimiter=',')
    for row in ergebnisse:
        pp = {"Rufzeichen": 0, "DOK": 0, "Gesamt": 0, "145 MHz": 0, "435 MHz": 0, "1.2 GHz": 0, "2.3 GHz": 0, "3.4 GHz": 0, "5.7 GHz": 0, "10 GHz": 0, "24 GHz": 0, "47 GHz": 0, "76 GHz": 0, "122 GHz": 0, "135 GHz": 0, "245 GHz": 0, "300 GHz": 0}
        pp.update({"Rufzeichen": row["Rufzeichen"], "DOK": row["DOK"]})
        for band in bands:
            punkte=int(row[band])
            #print(band+':'+str(punkte))
            if int(maxerg[band])!=0:
                pokalpunkte=float(punkte)/float(maxerg[band])*float(bandmult[band]*float(teilnehmer[band]))
                pokalpunkte_str = str(pokalpunkte)
                pokalpunkte_str = pokalpunkte_str.replace('.',',')
                #print(maxerg[band]+':'+str(bandmult[band])+':'+str(teilnehmer[band]))
                #print("Pokalpunkte: "+str(pokalpunkte))
                pp.update({band: pokalpunkte_str})
        print("Pokalpunkte:")
        print(pp)
        resulttable.append(pp)

    try:
        with open(filename+'pokalpunkte.csv', 'w') as csvfile:
            csv_columns = ["Rufzeichen", "DOK", "Gesamt", "145 MHz", "435 MHz", "1.2 GHz", "2.3 GHz", "3.4 GHz", "5.7 GHz", "10 GHz", "24 GHz", "47 GHz", "76 GHz", "122 GHz", "135 GHz", "245 GHz", "300 GHz"]
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';', lineterminator="\n")
            writer.writeheader()
            for row in resulttable: 
                writer.writerow(row)
    except IOError:
        print("IO error")
