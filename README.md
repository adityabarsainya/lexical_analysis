# Abstract
Sentimental Analysis of a Text Document using a lexical Analyzer, the goal is to
use a lexical analyzer to break the text document down into small chunks and
use a corpus to tag each token with its P.O.S (part of speech) tag. Once the
tokens are generated , the grammar of the language in which the book is written
is used to generate the parse tree for each sentence.Leaf nodes are then tagged
as a word from the sentence and a P.O.S tag.


# Output
The Characters from the novel are identified and an adjective list for each
character is generated using regular expressions.Each Character is given a
sentimental score on a continuous scale of -1 to 1.


# Setup
To satisfy the requirements to run the program follow the following steps:

STEP-1: Open command prompt on your system.
STEP-2: On the command prompt write : "python -m pip install -U pip setuptools".
STEP-3: Close the command prompt after it finishes installing pip and open a new
        command prompt.
STEP-4: In the new command prompt, write: "pip install nltk".
STEP-5: After nltk finishes, write: "pip install matplotlib".
STEP-6: After matplotlib finishes, write: "pip install textblob".
STEP-7: Go to the directory where the application files are stored and run the 
        GUI.py file by using command: "python GUI.py".
