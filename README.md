# Ask The Holy Quran
This Project Submitted in Partial Fulfillment of the Requirements for the Degree of Bachelor of Science in Systems and Computers Engineering(Al-azhar University).

Submitted By:
* Omar Shamkh Mohamed @OmarShamkh
* Ahmad Abdulrhman Radwan @ahr9n
* Abdelkhalek Ahmed Alashker @abdelkhalekalashker
* Elaraby Mahmoud Elaidy @elarabyelaidy19

## Project Overview:
There are two popular types of Quran searching techniques: lexical or keyword-based and semantic or concept-based that is a challenging task, especially in a complex corpus such as the Holy Quran. This thesis is developed to help all people, especially Muslims to deal with the Holy Quran easier and faster, allowing them to search in the Holy Quran for specific Verses, by a key-word or a conceptual topic. It consists of multiple phases: First, we collected the pre-trained models from authenticated sources with high accuracy, that are generating features’ vectors for words by training a Continuous Bag of Words (CBOW) architecture on large Classic, Modern Standard and Colloquial Arabic and Quranic corpus. Also, we collected a suitable database to display Verses on a website with the correct Tashkeel, and their explanation (Tafseer). Second, we calculate the features’ vectors of both input query and Quran verses, using different techniques like computing max and average similarity, max frequencies for a high similarity, and Pooling for each word in a sentence. We assigned a sentence with a vector using the different word vectors techniques and computed the cosine similarity between both query and verses’ vectors, to finally get the most likely sentence representation in vectors, to retrieve the most relevant verses and answer your questions more efficiently in the Holy Quran.

Example: 

![maxpo](https://user-images.githubusercontent.com/44472968/206178766-8deb2eaf-5a56-4531-bd0c-b285edafc8a0.png)



## Results:


![Screenshot from 2022-07-22 15-25-29](https://user-images.githubusercontent.com/44472968/206178662-eec8859d-234d-4f14-a0aa-ce03933582f6.png)

----------------------------------------------------------------------------------------------------------------------------

### Resourses:

Full Documentation : https://docs.google.com/document/d/1Ikh38lms8rNb7g67VLCNhIOCQg4EsF41nRGQbSuiHA0/edit?usp=sharing

### Versions:
Here is the newest Version modified by @ahr9n:
https://github.com/ahr9n/quranic-search-v2 

