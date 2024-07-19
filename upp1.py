# Uppgift 1:
# a) Skriv en egendefinierad funktion read_file(filnamn) som tar ett filnamn som parameter/argument och returnerar en lista med innehållet i filen.
# #Funktionen skall öppna filen och därefter läsa in filens innehåll till en lista och returnera resultatet.
# Observera att csv-filerna kpi.csv och varutjanstegrupp.csv använder semikolon (;) som avgränsningstecken. Teckenkodningen ska vara ’UTF-8’.
# b) Anropa funktionen read_file för att skapa listan kpiData från csv-filen kpi.csv och listan livsData från csv-filen varutjanstegrupp.csv.
# Kontrollera därefter att funktionen har returnerat förväntad information genom att skriva ut de två första raderna i kpiData och livsData.
# c) Lägg till anrop till read_file() i menyn (uppgift 0) och kontrollera att uppgift 1 utförs korrekt när du väljer alternativ 1 i menyn.

import csv

# för att kunna läsa in en csv fil så skapas denna funktion


def read_file(filnamn):
    data_list = []  # skapa en tom lista där den inlästa datan från vald fil kommer att hamna

    # för att se till att kodningen blir utf-8
    with open(filnamn, "r", encoding="utf-8", newline="") as file:
        # för att läsa in filens innehåll skapas en läsare
        csv_reader = csv.reader(file, delimiter=";", )

        for rad in csv_reader:  # loopa igenom datan i filen och lägg till den i listan
            data_list.append(rad)

        return data_list    # för att avsluta funktionen, returnera listan med inlaggd data


kpiData = read_file("kpi2023.csv")
livsData = read_file("varutjanstegrupp.csv")
# [0:2] skriver ut de två först raderna
# print(kpiData[0:2])
print(livsData)
