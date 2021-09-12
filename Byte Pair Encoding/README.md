## Byte Pair Encoding Algorithm

Byte Pair Encoding (BPE) (Gage, 1994) is a simple data compression technique that iteratively replaces the most frequent pair of bytes in a sequence with a single, unused byte. We adapt this
algorithm for word segmentation. Instead of merging frequent pairs of bytes, we merge characters or
character sequences.
<br />
<br />
The translation of rare words is an open problem and this algorithm is especially useful in dealing with unknown words.\
<br />
NLP algorithms often learn some facts about language from one corpus and then use these trained reality to make decisions about words it has never seen before.
Thus if our training corpus contains, say the words *low*, *new*, *newer* but not *lower*, then if the word *lower* appears in our unknown corpus,
our system will not know what to do.\
<br />

## So basicly how it works?

The BPE token learner begins with a vocabulary that is just the set of all individual characters. It then examines the training corpus, chooses the two symbols that
are most frequently adjacent ('A', 'B'), adds a new merged symbol 'AB' to the vocabulary, and replaces every adjacent 'A' 'B' in the corpus with new 'AB'. It continues
to count and merge, creating new longer and longer character strings, until k merges have been done creating k novel tokens; k is thus is a parameter of the algorithm.
The resulting vocabulary consists of the original set of characters plus k new symbols.
<br />
<br />
<br />
## Python implementation is shown here:
![image](https://user-images.githubusercontent.com/44132720/132998438-652e3257-d11b-48a2-bfd0-57aaa5446373.png)
###### Algorithm of BPE (Sennrich et al., 2015)
<br />
r · → r·
<br />
l o → lo    <br />
lo w → low    <br />
e r· → er·       <br />
BPE merge operations learned from dictionary {‘low’, ‘lowest’, ‘newer’, ‘wider’}.
