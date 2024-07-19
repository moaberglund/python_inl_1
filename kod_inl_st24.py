# Skriv en inledande kommentar som talar om vad programmet gör.


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Placera ev. funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:

# Konverterare för sträng till lista med integers


def converter(string):
    # Delar upp varje värde för listan vid ett komma + mellanslag
    li = list(string.split(", "))
    # ser till att om siffror är i str-format, omvandla till int-format
    # Användning av map() för att konvertera varje element i listan till heltal
    li = list(map(int, li))
    return li


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:


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


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:


def plottaKPI(kpiData):

    # Spara angivna månader i en lista,
    # användning av converter funktion från ovan
    month_input = converter(
        input("Ange vilka månader som ska analyseras (ex. 5, 10): "))

    # Funktionen från upp.1 används för att läsa in listan med kpidata-filen
    data_list = read_file(kpiData)

    # Plocka ut åren och lägg dem i stigande ordning (x-axeln)
    years = []
    for row in data_list[1:]:
        years.append(row[0])
    years.reverse()

    # Loopa genom varje vald månad
    for month_index in month_input:
        # Extraherar värdena för den aktuella månaden från data_list, exklusive rubrikraden
        values = [row[month_index] for row in data_list[1:]]
        # Vänder på ordningen av listan, stigande ordning
        values.reverse()

        # Ersätter komma med punkt i varje värde för att kunna konvertera till float
        for i in range(len(values)):
            values[i] = values[i].replace(',', '.')
            # Konverterar värdena till float
            values[i] = float(values[i])

        # Skapar en lista med månadsetiketter (används för att sätta rätt etikett i diagrammet)
        month_labels = []
        month_labels.extend(data_list[0][1:])

        plt.plot(years, values, label=month_labels[month_index - 1])

    # Anpassa diagrammet
    plt.xlabel("År")
    plt.ylabel("Konsumentprisindex")
    plt.title("Konsumentprisindex År 1980-2023")
    plt.legend()
    plt.grid()
    # Anpassa x-axeln för att visa endast vart tionde år
    xticks = [years[0], years[10], years[20], years[30], years[40]]
    plt.xticks(xticks)

    # Redo för att visa diagramet
    plt.show()


# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:

def varortjanster(livsData):

    # Funktionen från upp.1 används för att läsa in listan med tillhörande fil
    data_list = read_file(livsData)

    print('''
          
Välj vilka varu-/tjänstegrupper du vill analysera (ex. 1, 3, 4):
          
1. livsmedel och alkoholfria drycker
2. kläder och skor
3. boende
4. hälso- och sjukvård
5. post och telekommunikationer
6. rekreation och kultur
7. restauranger och logi   
''')
    # Spara användarens val till en konverterad lista
    groups_input = converter(input("> "))

    print("Ange mellan vilka år du vill göra analysen (ex. 2000, 2010)")

    # spara valda år i en lista som konverteras till int med hjälp av
    # convert funktionen
    year_input = converter(input("> "))
    # ta ut index i 2d listan för inputen av start året
    start_year = year_input[0] - 1980
    # ta ut slut året
    end_year = year_input[1] - 1980

    # Plocka ut åren för utskrift till x-axeln
    years = []
    years.extend(data_list[0][1:])

    # Loopa genom varje vald grupp
    for index in groups_input:
        # Ta ut värdena för de valda grupperna exklusive rubrikraden
        values = data_list[index][1:]
        # Ta ut de värden som faller inom den angivna tidsperioden
        selected_values = values[start_year:end_year + 1]
        selected_years = years[start_year:end_year + 1]

        # Konvertera värdena till float
        selected_values = list(map(float, selected_values))

        # Skapar en lista med gruppetiketter (används för att sätta rätt etikett i diagrammet)
        group_labels = data_list[index][0]

        plt.plot(selected_years, selected_values, label=group_labels)

    # Anpassa diagrammet
    plt.xlabel("År")
    plt.ylabel("Prisutveckling")
    plt.title(f"""Prisutveckling för olika kategorier av varor och tjänster för år
              {year_input[0]} - {year_input[1]}""")
    plt.legend()
    plt.grid()
    # Redo för att visa diagrammet
    plt.show()


# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:

def ff(livsData):

    # Funktionen från upp.1 används för att läsa in listan med tillhörande fil
    data_list = read_file(livsData)

    print('''
          
Ange en kategori (1-7) som du vill analysera (ex. 1):
          
1. livsmedel och alkoholfria drycker
2. kläder och skor
3. boende
4. hälso- och sjukvård
5. post och telekommunikationer
6. rekreation och kultur
7. restauranger och logi   
''')
    # Spara användarens val, konverterad till int
    group_input = int(input("> "))

    # Ta ut data för vald grupp, exkludera första elementet som är kategorinamnet
    group_data = data_list[group_input][1:]

    # Plocka ut åren för utskrift till x-axeln
    years = data_list[0][1:]

    # Tom lista för förändringsfaktorerns
    ff_values = []

    # Beräkning av förändringsfaktor för varje år från 1981 till 2023
    # 1980 har inget föregående år, starta på index 1
    # Loopa från andra året (index 1) till det sista året
    for i in range(1, len(group_data)):
        # Hämta KPI för "aktuellt" år och gör om till float
        KPI_current = float(group_data[i])
        # Hämta KPI för dess föregående år([i-1]) och gör om till float
        KPI_previous = float(group_data[i-1])
        # Beräkna förändringsfaktorn som procentuell förändring(* 100) från föregående år
        FF = ((KPI_current - KPI_previous) / KPI_previous) * 100
        # Lägg till förändringsfaktorn i listan
        ff_values.append(FF)

    # Skapa ett stapeldiagram
    plt.bar(years[1:], ff_values)
    plt.xlabel("År")
    plt.ylabel("Förändringsfaktor (%)")
    plt.title(f"Förändringsfaktor för {data_list[group_input][0]}")
    # Anpassa x-axeln för att visa endast vart tionde år
    # Start på 1981 för 1980 finns icke
    xticks = [years[1], years[10], years[20], years[30], years[40]]
    plt.xticks(xticks)
    plt.grid()
    plt.show()


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:

def statistik(livsData):

    # Funktionen från upp.1 används för att läsa in listan
    data_list = read_file(livsData)

    # Plocka bort rubrikraden från 2d listan
    groups = data_list[1:]

    # Skriv ut rubrikerna innan man börjar loopa
    print(f'{"Varu-/tjänstegrupp":<40} {"Max":<10} {"Median":<10} {"Medelvärde":<10}')
    print("-"*80)

    # Listor för diagrammet
    max_values = []
    average_values = []
    median_values = []
    group_names = []

    for group in groups:
        # Index 0 är namnet på kategorin, spara dess etikett
        name = group[0]

        # Konvertera alla strängar till flyttal, hoppa över col 0
        values = list(map(float, group[1:]))
        values.sort()   # sortera listan för att kunna göra uträkningarna

        # Hösta värdet ligger sist i den sorterade listan
        max = values[-1]

        # Medelvärde - summan delat på längden av listan
        average = sum(values) / len(values)

        # Medianberäkning
        nr = len(values)

        if nr % 2 == 0:  # Om antalet i listan är jämnt hämtas de två mittersta talen
            # // används för absolut delning, avrundar neråt
            median = (values[nr // 2 - 1] + values[nr // 2]) / 2
        else:    # Om udda hämtas det mittersta elementet
            median = values[nr // 2]

        # Spara statistik för diagrammet
        max_values.append(max)
        average_values.append(average)
        median_values.append(median)
        group_names.append(name)

        # utskrift :<placering och .antal decimaler
        print(f'''{name:<40} {max:<10.2f} {
              median:<10.2f} {average:<10.2f}''')
        print("-"*80)

    # Skapa stapeldiagram
    plt.bar(group_names, max_values, width=0.6, color="blue", label="Maxvärde")
    plt.bar(group_names, median_values, width=0.4,
            color="red", label="Medianvärde")
    plt.bar(group_names, average_values, width=0.2,
            color="green", label="Medelvärde")
    # Rotera namnen på x-axeln 10 grader för bättre läsbarhet
    plt.xticks(rotation=(-10))
    plt.ylabel("Maxvärde, medianvärde och medelvärde")
    plt.title(
        "Maxvärde, medianvärde och medelvärde för varu-/tjänstegrupp år 1980-2023")

    plt.legend()

    plt.show()


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:


def main_menu():
    while True:
        print('''
Meny
        
1. Hämta data från fil - uppgift 1
2. Analysera data - uppgift 2
3. Analysera data - uppgift 3
4. Analysera data - uppgift 4
5. Analysera data - uppgift 5
6. Avsluta
              
Välj menyalternativ (1-6):
              
        ''')

        choice = input("> ")

        if choice == '1':
            kpiData = read_file("kpi2023.csv")
            livsData = read_file("varutjanstegrupp.csv")

            print(kpiData[0:2])
            print(livsData[0:2])

        elif choice == '2':
            plottaKPI("kpi2023.csv")

        elif choice == '3':
            varortjanster("Varutjanstegrupp.csv")

        elif choice == '4':
            ff("Varutjanstegrupp.csv")

        elif choice == "5":
            statistik("Varutjanstegrupp.csv")

        elif choice == "6":
            print("Programmet avslutas")
            break
        else:
            print("Ogiltigt val, försök igen.")


main_menu()
