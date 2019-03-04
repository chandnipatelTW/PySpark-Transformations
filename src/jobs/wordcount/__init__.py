import os
import time

from main import ROOT_DIR
from shared.context import JobContext

__author__ = 'thoughtworks'


class WordCountJobContext(JobContext):
    def _init_accumulators(self, sc):
        self.initalize_counter(sc, 'words')


def load_file_from_resources(file_name):
    return os.path.join(ROOT_DIR, 'resources', file_name)


def split_words(rdd):
    return rdd.split(' ')


def wordcount(rdd):
    return (rdd.flatMap(split_words)
            .map(lambda word: (word.lower(), 1))
            .reduceByKey(lambda a, b: a + b)
            .sortBy(lambda pair: pair[1], ascending=False))


def create_wordcount_csv(rdd, file_path_output):
    rdd.map(lambda t: t[0] + "," + str(t[1])).saveAsTextFile(file_path_output)


def run(sc):
    print("Running wordcount")
    context = WordCountJobContext(sc)

    file_path = load_file_from_resources('words.txt')
    file_path_output = load_file_from_resources('wordcount' + str(time.time()) + '.csv')

    rdd = sc.textFile(file_path)

    wordcount_rdd = wordcount(rdd)
    create_wordcount_csv(wordcount_rdd, file_path_output)

    # print(wordcount_rdd.collect())
    context.print_accumulators()
    return wordcount_rdd.collect()
