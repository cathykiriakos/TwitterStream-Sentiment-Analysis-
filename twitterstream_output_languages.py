import jsonlines    
import pandas as pd
import matplotlib.pyplot as plt
import pylab


def readTwitterData(twitterDataFile):
    tweets_data = readTwitterData('output.json')


    tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
    tweets['lang'] = list(map(lambda tweet: tweet['user']['lang'] if 'user' in tweet else None, tweets_data))
    tweets_by_lang = tweets['lang'].value_counts()
    print (tweets_by_lang[:10]) #outputs top 10 languages

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of Tweets' , fontsize=15)
    ax.set_title('Top 10 Languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:10].plot(ax=ax, kind='bar', color='green')

    pylab.show()
