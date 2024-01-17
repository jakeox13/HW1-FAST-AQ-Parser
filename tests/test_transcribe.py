# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Correct Example
    in_seq = "ATGTGC"
    out_seq = "UACACG"
    assert transcribe(in_seq)== out_seq
    assert transcribe(in_seq, reverse=True)== "GCACAU"

    # Negative example
    with pytest.raises(ValueError):
        transcribe("XGTCG")
    pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    in_seq = "ATGTGC"
    out_seq = "GCACAU"
    assert reverse_transcribe(in_seq)== out_seq
    pass