# Visualizing The Quran Verse Count

One day, I found a video online showing that the verse count in the Quran could actually draw Allah's name.

By arranging the surah's index number as the x axis and its verse count as the y axis like so,

<img src="https://github.com/oxraphc/Visualizing-The-Quran-Verse-Count/blob/main/images/how_its_arranged.jpg?raw=true" width="200"/>

We could connects the dots together to draw Allah's name,

<img src="https://github.com/oxraphc/Visualizing-The-Quran-Verse-Count/blob/main/images/result_example.jpg?raw=true" width="200"/>

This interest me. So after scraping wikipedia's lists of all the surah in the Quran and saving it to a CSV, I feed the data to a simple python script that utilize matplotlib to visualize the data.

And my result came,
<img src="https://github.com/oxraphc/Visualizing-The-Quran-Verse-Count/blob/main/visualization_result.png?raw=true"/>

It's arguably beautiful, and all I need to do is to connect the dots togehter.

<img src="https://github.com/oxraphc/Visualizing-The-Quran-Verse-Count/blob/main/visualization_result_connected.png?raw=true"/>

So there you go, I personally think that it's a pretty cool modern-day miracle of the Quran.
<br>
<br>
<small>p.s I definitely had done a number of grammatical mistake, lmao
I'll take this as my first attempt of documenting my projects</small>

## Usage

```bash
# For Debian, Ubuntu, and derivatives
apt install python3-pip python3-tk python3-pil.imagegtk
pip install matplotlib

# Scrap data
python3 scrap_wiki.py

# Visualize!
python3 visualize.py
```
