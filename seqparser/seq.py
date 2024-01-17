# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    A function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    Args:
        seq (str): The input DNA Sequence
        reverse (bool, optional): Should the sequence be reversed after transcription. Defaults to False.

    Returns:
        str: The transcribed RNA
    """ 
    # Preprocess string inputs
    # Convert string to all uppercase to match keys
    seq =seq.upper()

    # Check if all chracters are vaild
    for bp in seq :
        if bp in ALLOWED_NUC:
            pass
        else:
            raise ValueError("{} is invalid input".format(bp))

    # Transcribe sequence
    outseq = "".join([TRANSCRIPTION_MAPPING[bp] for bp in seq])
    if reverse == True:
        return (outseq[::-1])
    else:
        return outseq
    
    pass

def reverse_transcribe(seq: str) -> str:
    """
     Write a function that will transcribe an input sequence and reverse
    the sequence

    Args:
        seq (str): The input DNA Sequence

    Returns:
        str: The transcribed and reversed sequence
    """    
    # Run transcribe with Reverse == True
    return transcribe(seq, reverse=True)
    pass

