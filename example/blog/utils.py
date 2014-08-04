# coding: utf-8
import random

saved = lambda seq: [s for s in seq if s.save() is None]

text = """
    Return a k length list of unique elements chosen from the
    population sequence. Used for random sampling without replacement.
    New in version 2.3.
    Returns a new list containing elements from the population
    while leaving the original population unchanged. The resulting
    list is in selection order so that all sub-slices will also be
    valid random samples. This allows raffle winners (the sample)
    to be partitioned into grand prize and second place winners
    (the subslices).
    Members of the population need not be hashable or unique.
    If the population contains repeats, then each occurrence is a
    possible selection in the sample.
    To choose a sample from a range of integers, use an
    xrange() object as an argument. This is especially fast
    and space efficient for sampling from a large population:
    sample(xrange(10000000), 60).
    """


get_text = lambda num: ' '.join(random.sample(text.split(), num))
