import nltk
import tkinter as tk
from textblob import TextBlob
from newspaper import Article

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')

def get_summary():
    try:
        url = URL.get('1.0', tk.END).strip()  # Strip newline or spaces

        if not url:
            raise ValueError("URL cannot be empty")

        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        text = article.text

        title.config(state='normal')
        title.delete('1.0', tk.END)
        title.insert('1.0', article.title if article.title else "No Title Available")
        title.config(state='disabled')

        author.config(state='normal')
        author.delete('1.0', tk.END)
        author.insert('1.0', ', '.join(article.authors) if article.authors else "No Authors Available")
        author.config(state='disabled')

        publication.config(state='normal')
        publication.delete('1.0', tk.END)
        publication.insert('1.0', article.publish_date if article.publish_date else "No Date Available")
        publication.config(state='disabled')

        summary.config(state='normal')
        summary.delete('1.0', tk.END)
        summary.insert('1.0', article.summary if article.summary else "No Summary Available")
        summary.config(state='disabled')

        sentiment.config(state='normal')
        sentiment.delete('1.0', tk.END)
        sentiment_analysis = TextBlob(text).sentiment.polarity
        sentiment_text = "Positive" if sentiment_analysis > 0 else "Negative" if sentiment_analysis < 0 else "Neutral"
        sentiment.insert('1.0', f"Sentiment: {sentiment_text}")
        sentiment.config(state='disabled')

    except Exception as e:
        print(f"Error: {e}")

# GUI setup
root = tk.Tk()
root.title('News Summariser')
root.geometry('1200x600')

# Labels and text fields
tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

salabel = tk.Label(root, text='Sentiment Analysis')
salabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

URL = tk.Text(root, height=1, width=140)
URL.config(state='normal', bg='#dddddd')
URL.pack()

# Summarize button
btn = tk.Button(root, text='Summarize', command=get_summary)
btn.pack()

# Run the application
root.mainloop()
