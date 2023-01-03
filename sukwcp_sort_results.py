import csv
filename='22_03_Multi_'
with open(filename+'.csv') as csvdatei:
    ergebnisse = csv.DictReader(csvdatei, delimiter=';')
    #print(ergebnisse)
    results = []
    tabelle = []
    calls = []
    #Kopiere alle relevanten Daten aus der Ergebnisliste
    for row in ergebnisse:
        #print(row["Rufzeichen (Basis)"],row["DOK"],row["Band"],row["Punkte"])
        result_zeile = {"Rufzeichen": row["Rufzeichen (Basis)"],"DOK": row["DOK"],"Band": row["Band"],"Punkte": row["Punkte"]}
        results.append(result_zeile)
        #Erzeuge eine Liste aller Rufzeichen aus der Liste
        if row["Rufzeichen (Basis)"] not in calls:
            calls.append(row["Rufzeichen (Basis)"])
    calls.sort()
    for x in calls:
        #print(x)
        zeile = {"Rufzeichen": 0, "DOK": 0, "145 MHz": 0, "435 MHz": 0, "1.2 GHz": 0, "2.3 GHz": 0, "3.4 GHz": 0, "5.7 GHz": 0, "10 GHz": 0, "24 GHz": 0, "47 GHz": 0, "76 GHz": 0, "122 GHz": 0, "135 GHz": 0, "245 GHz": 0, "300 GHz": 0} 
        zeile.update({"Rufzeichen": x})
        for row in results:
            if row["Rufzeichen"]==x:
                #print(row["DOK"],row["Band"],row["Punkte"])
                zeile.update({"DOK": row["DOK"], row["Band"]: row["Punkte"]})
        print(zeile)
        tabelle.append(zeile)
    #for row in tabelle:
        #print(row)
        #write to csv file
        try:
            with open(filename+'formatted.csv', 'w') as csvfile:
                csv_columns = ["Rufzeichen", "DOK", "145 MHz", "435 MHz", "1.2 GHz", "2.3 GHz", "3.4 GHz", "5.7 GHz", "10 GHz", "24 GHz", "47 GHz", "76 GHz", "122 GHz", "135 GHz", "245 GHz", "300 GHz"]
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for row in tabelle:
                    writer.writerow(row)
        except IOError:
            print("IO error")
