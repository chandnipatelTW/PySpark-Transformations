import os

from main import ROOT_DIR
from shared.context import JobContext

__author__ = 'thoughtworks'


class WordCountJobContext(JobContext):
    def _init_accumulators(self, sc):
        self.initalize_counter(sc, 'words')


def load_file_from_resources(file_name):
    return os.path.join(ROOT_DIR, 'resources', file_name)


def split_words(ds):
    return ds.split(' ')


def wordcount(ds):
    result = (ds.flatMap(split_words)
              .map(lambda word: (word.lower(), 1))
              .reduceByKey(lambda a, b: a + b)
              .sortBy(lambda pair: pair[1], ascending=False)
              .collect())
    return result


def run(sc):
    print("Running wordcount")
    context = WordCountJobContext(sc)

    file_path = load_file_from_resources('words.txt')
    ds = sc.textFile(file_path)
    result = wordcount(ds)

    print(result)
    context.print_accumulators()
    return result
