from unittest.mock import patch

from parameterized import parameterized
from pysparkling import Context

from jobs.wordcount import run, wordcount, split_words


@patch('jobs.wordcount.WordCountJobContext.initalize_counter')
@patch('jobs.wordcount.WordCountJobContext.inc_counter')
@patch('jobs.wordcount.create_wordcount_csv')
def test_wordcount_analyze(_, __, ___):
    result = run(Context())
    print("the result:", len(result))
    assert len(result) == 4352
    assert result[:6] == [('the', 1327), ('to', 822), ('and', 694), ('', 579), ('he', 572), ('of', 550)]


@patch('jobs.wordcount.WordCountJobContext.initalize_counter')
@patch('jobs.wordcount.WordCountJobContext.inc_counter')
@patch('jobs.wordcount.create_wordcount_csv')
def test_save_results_in_csv(create_wordcount_csv, _, __):
    sc = Context()
    run(sc)
    assert create_wordcount_csv.called


def test_ordering_words():
    text = "a b b c c c d d d d"
    sc = Context()
    ds = sc.parallelize([text])
    result = wordcount(ds).collect()
    assert result == [('d', 4), ('c', 3), ('b', 2), ('a', 1)]


def test_case_insensitivity():
    text = "a a A A"
    sc = Context()
    ds = sc.parallelize([text])
    result = wordcount(ds).collect()
    assert result == [('a', 4)]


@parameterized.expand([
    ("space", "ciao mamma mia", ["ciao", "mamma", "mia"]),
    ("comma", "ciao mamma mia", ["ciao", "mamma", "mia"]),
    ("hypen", "ciao mamma mia", ["ciao", "mamma", "mia"]),
    ("period", "ciao mamma mia", ["ciao", "mamma", "mia"]),
])
def test_splitting(test_case, text, expected):
    sc = Context()
    print("Test case:", test_case)
    ds = sc.parallelize([text])
    result = ds.flatMap(split_words).collect()
    assert result == expected
