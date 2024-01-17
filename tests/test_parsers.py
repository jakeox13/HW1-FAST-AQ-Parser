# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Read in fasta file and compare inital sequences
    fasta_obj = FastaParser('data/test.fa')
    seqs = [record for record in fasta_obj]
    assert seqs[0][0]=="seq0" , "Incorrect Seq labels"
    assert seqs[0][1]=="TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA" , "Incorrect sequence"

    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # test fastq read in
    fasta_obj = FastaParser('data/test.fq')
    seqs = [record for record in fasta_obj]
    assert seqs[0][0] == None

            
    
    #test blank read in 
    fasta_obj = FastaParser('tests/blank.fa')
    with pytest.raises(ValueError, match= r"File (.*) had 0 lines."):
        [record for record in fasta_obj]

    
    
    # test bad read in
    fasta_obj = FastaParser('tests/bad.fa')
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        [record for record in fasta_obj]


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Read in fastq file and compare inital sequences and quality
    fastq_obj = FastqParser('data/test.fq')
    seqs = [record for record in fastq_obj]
    assert seqs[0][0]=="seq0" , "Incorrect Seq labels"
    assert seqs[0][1]=="TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG" , "Incorrect sequence"
    assert seqs[0][2]=='''*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32=''' , "Incorrect quality reads"
    

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # test fastq read in
    fasta_obj = FastaParser('data/test.fa')
    seqs = [record for record in fasta_obj]
    assert seqs[0][0] != None, "Check if file is in fastq format"

    

    

