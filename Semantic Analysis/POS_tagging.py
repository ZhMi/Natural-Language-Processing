# -*- coding: utf-8 -*-

# author : zhmi
# mail : zhmi120@sina.com
# description : Tagging part of speech in articles.

import nltk
import constant_def
import csv


class POS_tagging_class(object):

    def __init__(self):
        pass

    def read_file(self, filePath):
        '''
            function : Read file and get raw data.
            return rawData : List of file data.
                             Every elem in rawData contains ['url', 'main_title', 'second_title', 'publish_time', 'summary'] record.
        '''
        rawData = []
        csvfile = file(filePath, 'rb')
        reader = csv.reader(csvfile)
        for line in reader:
            rawData.append(line)
        csvfile.close()
        return rawData

    def filter_article_category(self, categoryIndex, rawData):
        '''
            parameter : categoryIndex : 0 --- > 'url'
                                        1 --- > 'main_title'
                                        2 --- > 'second_title'
                                        3 --- > 'publish_time'
                                        4 --- > 'summary'
            function : Filter one content of raw data record.
                       For example : filter_article_category(summary, rawData), return summary field of all records.
        '''
        return [''.join(map(lambda x: x[categoryIndex].decode('utf-8').strip(), rawData))]

    def word_segmentation(self, text):
        sents = nltk.sent_tokenize(text, language='english')
        return map(lambda sent: nltk.word_tokenize(sent), sents)

    def word_tokenize(self, words):
        tag = []
        for segment in words:
            tag.append(nltk.pos_tag(segment))
        return tag



testObject = POS_tagging_class()
filePath = constant_def.filePath
rawData = testObject.read_file(filePath)

summary = testObject.filter_article_category(4, rawData[1:])
words = testObject.word_segmentation(summary[0])

tags = testObject.word_tokenize(words)
print tags



