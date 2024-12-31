import csv
import matplotlib
matplotlib.use('TkAgg')  # Switch to TkAgg backend bcuz my environment sucks
import matplotlib.pyplot as plt


quran_data_file = "Quran Data.csv"

x_axis_surah_index = []
y_axis_verse_count = []
surah_name_label = []

with open(quran_data_file, "r") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
        x_axis_surah_index.append(int(row[0]))
        surah_name_label.append(row[1])
        y_axis_verse_count.append(int(row[2]))

plt.scatter(x_axis_surah_index, y_axis_verse_count)
plt.gca().invert_xaxis()
plt.xticks(ticks=x_axis_surah_index, labels=surah_name_label, rotation=90, fontsize=6)
plt.xlabel("Surah Name & Index")
plt.ylabel("Verse Count")
plt.title("Visualizing The Quran Verse Count")
plt.show()
