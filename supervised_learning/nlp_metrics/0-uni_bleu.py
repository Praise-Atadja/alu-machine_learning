#!/usr/bin/env python3
"""
calculates the unigram BLEU score for a sentence
"""
import numpy as np


def uni_bleu(references, sentence):
    """
    function that calculates the unigram BLEU score
    in a machine translation paradigm
    """

    # Convert sentence to a np.ndarray, handle string vs. list
    if not isinstance(sentence, list):
        # Convert all characters to lowercase
        sentence = sentence.lower()
        # Convert the sentence to an array of words
        sentence = np.array(sentence.split())
    else:
        # Convert all characters to lowercase
        sentence = np.array([word.lower() for word in sentence])
    sentence_len = sentence.shape[0]

    # Convert references to a list of np.ndarray, handle string vs. list
    if not np.all([isinstance(reference, list) for reference in references]):
        # Convert all characters to lowercase
        references = [reference.split() for reference in references]
        # Convert the references to array of words
        references = [np.array(reference.split()) for reference in references]
    else:
        # Convert all characters to lowercase
        references = [np.array([word.lower() for word in reference])
                      for reference in references]
    references_len = [reference.shape[0] for reference in references]

    # Initialize the precision score
    clipped_precision_score = 0

    # Compute the sentence unigrams
    # sentence_n_grams = n_gram_generator(sentence, 1)
    sentence_n_grams = sentence
    # print(sentence_n_grams)
    unique, counts = np.unique(sentence_n_grams, return_counts=True)
    sentence_n_grams_dict = dict(zip(unique, counts))
    # Alternative option, import Counter:
    # sentence_n_grams_dict = Counter(n_gram_generator(sentence, n))
    # print("sentence_n_grams_dict:", sentence_n_grams_dict)

    # Compute the references unigrams
    references_n_grams_dicts = []
    for reference in references:
        # reference_n_grams = n_gram_generator(reference, 1)
        reference_n_grams = reference
        # print(reference_n_grams)
        unique, counts = np.unique(reference_n_grams, return_counts=True)
        reference_n_grams_dict = dict(zip(unique, counts))
        references_n_grams_dicts.append(reference_n_grams_dict)

    # Compute the (modified/clipped) precision on unigrams
    count = sum(sentence_n_grams_dict.values())
    for n_gram in sentence_n_grams_dict.keys():
        references_n_gram_count = [reference_n_grams_dict[n_gram]
                                   for reference_n_grams_dict
                                   in references_n_grams_dicts
                                   if n_gram in reference_n_grams_dict]
        if not len(references_n_gram_count):
            keep_max = 0
            # print("keep_max:", keep_max)
        else:
            keep_max = max(references_n_gram_count)
            # print("keep_max:", keep_max)
        if (sentence_n_grams_dict[n_gram] > keep_max):
            sentence_n_grams_dict[n_gram] = keep_max
    clipped_count = sum(sentence_n_grams_dict.values())
    clipped_precision_score += (clipped_count / count)
    # print("clipped_precision_score:", clipped_precision_score)

    # Compute the Brevity Penalty (BP)
    if sentence_len > np.min(references_len):
        BP = 1
    else:
        bp = 1 - (np.min(references_len) / sentence_len)
        # bp = 1 - (sentence_len / np.min(references_len))
        BP = np.exp(bp)

    # Compute the unigram BLEU score
    BLEU = BP * clipped_precision_score

    return BLEU
