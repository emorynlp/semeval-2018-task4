# SemEval 2018 Task 4

## Character Identification on Multiparty Dialogues

Character Identification is an entity linking task that identifies each mention as a certain character in multiparty dialogue. 
Let a mention be a nominal referring to a person (e.g., *she*, *mom*, *Judy*), and an entity be a character in a dialogue. 
The goal is to assign each mention to its entity, who may or may not participate in the dialogue. 
For the following example, the mention "mom" is not one of the speakers; nonetheless, it clearly refers to the specific person, Judy, that could appear in some other dialogue. Identifying such mentions as real characters requires cross-document entity resolution, which makes this task challenging.

![Character Identification Example](http://nlp.mathcs.emory.edu/character-mining/img/character-identification-example.png)

## Citation

* [SemEval 2018 Task 4: Character Identification on Multiparty Dialogues](http://aclweb.org/anthology/S18-1007), Jinho D. Choi and Henry Y. Chen, Proceedings of the International Workshop on Semantic Evaluation, SemEval'18, 57-64, New Orleans, LA, 2018.  


## References

* [Robust Coreference Resolution and Entity Linking on Dialogues: Character Identification on TV Show Transcripts](http://www.aclweb.org/anthology/K/K17/K17-1023.pdf), Henry Y. Chen, Ethan Zhou, and Jinho D. Choi, Proceedings of the 21st Conference on Computational Natural Language Learning, CoNLL'17, 216-225 Vancouver, Canada, 2017.
* [Character Identification on Multiparty Conversation: Identifying Mentions of Characters in TV Shows](http://www.aclweb.org/anthology/W16-3612), Henry Y. Chen and Jinho D. Choi, Proceedings of the 17th Annual SIGdial Meeting on Discourse and Dialogue, SIGDIAL'16, 90-100, Los Angeles, CA, 2016.

## Organizers

* [Jinho D. Choi](http://www.mathcs.emory.edu/~choi) (Emory University).
* [Henry Y. Chen](http://henryyhc.info) (Snap Inc.).

## Datasets

The first two seasons of the TV show Friends are annotated for this task. 
Each season consists of episodes, each episode comprises scenes, and each scene is segmented into sentences. 
The followings describe the distributed datasets:

* [friends.train.episode_delim.conll](dat/friends.train.episode_delim.conll): the training data where each episode is considered a document.
* [friends.train.scene_delim.conll](dat/friends.train.scene_delim.conll): the training data where each scene is considered a document.
* [friends.test.episode_delim.conll](dat/friends.test.episode_delim.conll): the test data where each episode is considered a document.
* [friends.test.scene_delim.conll](dat/friends.test.scene_delim.conll): the test data where each scene is considered a document.
* [friends.test.episode_delim.conll.nokey](dat/friends.test.episode_delim.conll.nokey): same as [friends.test.episode_delim.conll](dat/friends.test.episode_delim.conll); the gold keys are replaced by `-1`.
* [friends.test.scene_delim.conll.nokey](dat/friends.test.scene_delim.conll.nokey): same as [friends.test.scene_delim.conll](dat/friends.test.scene_delim.conll); the gold keys are replaced by `-1`.

Note that the evaluation sets did not include the gold keys during the competition; we made them available after the competition.
No dedicated development set was distributed for this task; feel free to make your own development set for training or perform cross-validation on the training sets.

## Format

All datasets follow the CoNLL 2012 Shared Task data format.
Documents are delimited by the comments in the following format:

```
#begin document (<Document ID>)[; part ###]
...
#end document
```

Each sentence is delimited by a new line ("\n") and each column indicates the following:

1. Document ID: `/<name of the show>-<season ID><episode ID>` (e.g., `/friends-s01e01`).
1. Scene ID: the ID of the scene within the episode.
1. Token ID: the ID of the token within the sentence.
1. Word form: the tokenized word.
1. Part-of-speech tag: the part-of-speech tag of the word (auto generated).
1. Constituency tag: the Penn Treebank style constituency tag (auto generated).
1. Lemma: the lemma of the word (auto generated).
1. Frameset ID: not provided (always `_`).
1. Word sense: not provided (always `_`).
1. Speaker: the speaker of this sentence.
1. Named entity tag: the named entity tag of the word (auto generated).
1. Entity ID: the entity ID of the mention, that is consistent across all documents.

Here is a sample from the training dataset:

```
/friends-s01e01  0  0  He     PRP   (TOP(S(NP*)    he     -  -  Monica_Geller   *  (284)
/friends-s01e01  0  1  's     VBZ          (VP*    be     -  -  Monica_Geller   *  -
/friends-s01e01  0  2  just   RB        (ADVP*)    just   -  -  Monica_Geller   *  -
/friends-s01e01  0  3  some   DT        (NP(NP*    some   -  -  Monica_Geller   *  -
/friends-s01e01  0  4  guy    NN             *)    guy    -  -  Monica_Geller   *  (284)
/friends-s01e01  0  5  I      PRP  (SBAR(S(NP*)    I      -  -  Monica_Geller   *  (248)
/friends-s01e01  0  6  work   VBP          (VP*    work   -  -  Monica_Geller   *  -
/friends-s01e01  0  7  with   IN     (PP*))))))    with   -  -  Monica_Geller   *  -
/friends-s01e01  0  8  !      .             *))    !      -  -  Monica_Geller   *  -
```
```
/friends-s01e01  0  0  C'mon  VB   (TOP(S(S(VP*))  c'mon  -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  1  ,      ,                 *  ,      -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  2  you    PRP           (NP*)  you    -  -  Joey_Tribbiani  *  (248)
/friends-s01e01  0  3  're    VBP            (VP*  be     -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  4  going  VBG            (VP*  go     -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  5  out    RP           (PRT*)  out    -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  6  with   IN             (PP*  with   -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  7  the    DT             (NP*  the    -  -  Joey_Tribbiani  *  -
/friends-s01e01  0  8  guy    NN            *))))  guy    -  -  Joey_Tribbiani  *  (284)
/friends-s01e01  0  9  !      .               *))  !      -  -  Joey_Tribbiani  *  -
```

A mention may include more than one word:

```
/friends-s01e02  0  0  Ugly         JJ   (TOP(S(NP(ADJP*  ugly         -  -  Chandler_Bing  *  (380
/friends-s01e02  0  1  Naked        JJ                *)  naked        -  -  Chandler_Bing  *  -
/friends-s01e02  0  2  Guy          NNP               *)  Guy          -  -  Chandler_Bing  *  380)
/friends-s01e02  0  3  got          VBD             (VP*  get          -  -  Chandler_Bing  *  -
/friends-s01e02  0  4  a            DT              (NP*  a            -  -  Chandler_Bing  *  -
/friends-s01e02  0  5  Thighmaster  NN               *))  thighmaster  -  -  Chandler_Bing  *  -
/friends-s01e02  0  6  !            .                *))  !            -  -  Chandler_Bing  *  -
```

The mapping between the entity ID and the actual character can be found in [`friends_entity_map.txt`](dat/friends_entity_map.txt).

## Evaluation

Your output must consist of the entity ID of each mention, one per line, in the sequential order.  There are 6 mentions in the above example, which will generate the following output:

```
284
284
248
248
284
380
```

Given this output, the evaluation script will measure,

1. The label accuracy considering only 7 entities, that are the 6 main characters (Chandler, Joey, Monica, Phoebe, Rachel, and Ross) and all the others as one entity.
1. The macro average between the F1 scores of the 7 entities.
1. The label accuracy considering all entities, where characters not appearing in the tranining data are grouped as one entity, others.
1. The macro average between the F1 scores of all entities.
1. The F1 scores for 7 entities.
1. The F1 scores for all entities.

The following shows the command to run the [evaluate.py](src/evaluate.py):

```
python evaluate.py ref_out sys_out
```

* `ref_out`: the reference output including the gold keys (download [ref.out](dat/ref.out)).
* `sys_out`: the path to a file containing your system output; this should include 2,429 lines of keys, where each line indicates the entity ID of the corresponding mention.

## Results

This task was hosted at CodaLab from 08/21/2017 to 01/29/2018: [https://competitions.codalab.org/competitions/17310](https://competitions.codalab.org/competitions/17310).

### All Entities + Others

This evaluation considers all characters appearing in training, development, and evaluation sets as individual classes.
Characters that appear only one or two of these sets are grouped as one class called `OTHERS`.

|User ID | Label Accuracy | Average F1 |
|:------:|:--------------:|:----------:|
| AMORE UPF    | **74.72** | **41.05** |
| Cheoneum     | 69.49 | 16.98 |
| Kampfpudding | 59.45 | 37.37 |
| Zuma         | 25.81 | 14.42 |
 
### Main Entities + Others

This evaluation considers 6 main characters as individual classes and all the other characters as one class called `OTHERS`.

|User ID | Label Accuracy | Average F1 |
|:------:|:--------------:|:----------:|
| Cheoneum     | **85.10** | **86.00** |
| AMORE UPF    | 77.23 | 79.36 |
| Kampfpudding | 73.36 | 73.51 |
| Zuma AR      | 46.07 | 43.15 |

### System Outputs + Detailed Evaluation

The system output from all participants as well as their detailed evaluation results.

|User ID | Output | Evaluation |
|:------:|:------:|:----------:|
| AMORE UPF    | [AMORE_UPF.out](sys/AMORE_UPF.out)       | [AMORE_UPF.eval](sys/AMORE_UPF.eval) |
| Cheoneum     | [Cheoneum.out](sys/Cheoneum.out)         | [Cheoneum.eval](sys/Cheoneum.eval) |
| Kampfpudding | [Kampfpudding.out](sys/Kampfpudding.out) | [Kampfpudding.eval](sys/Kampfpudding.eval) |
| Zuma AR      | [Zuma.out](sys/Zuma.out)                 | [Zuma.eval](sys/Zuma.eval) |
