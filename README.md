## What is this

This package is for reading and visualizing the comments section of a tt video. 

## Installation

```
pip3 install openai
pip3 install bs4
pip3 install scikit-learn
pip3 install bokeh
pip3 install numpy
```

## Running

Go to a comments section, right click, press inspect. Then hover over the code in the right-hand side and copy the relevant text code. Save that code into a file in this directory.

NOTE: You need an OPENAI API KEY. Go get one from openai website.

```
OPEN_AI_KEY=YOURAPIKEY python3 visualize_comments.py --fpath YOUR_TT_COMMENTS_SECTION.html
```

If you want to start over, delete the folder **comment_data**