# Model Evaluation CyNER vs SecureBERT

The goal is to evaluate NER models- Cyner and SecureBERT on given dataset and determine which one is better.
I focused on precision, recall and latency.

first, I evaluated how the model handles a large context window by passing the entire dataset. 
As excepted, there was a significant imbalance between recall VS precision.
Recall was extremely low and the number of FN was high.
The model was unable to detect most of entities in the dataset

To improve it, I parsed the dataset sentence by sentence.
Assuming an empty line represent end of sentence.
This change, Using a small contexts improved the evaluation process.

## Results:

### Cyner Model

- True Positives (TP): 2826
- False Positives (FP): 5975
- False Negatives (FN): 14529
- Precision: 0.32109987501420295
- Recall: 0.16283491789109766
- Avg latency: 0.03384428568236875 s/sentence
### Analysis:

- high number of false negatives
- Low recall indicates that the model misses most entities.
- Low precision shows many incorrect predictions.
We can see the model is weak


### SecureBERT

During the debugging, I identified that the same labels outputs sometimes split into multiple entities. This caused to inaccurate evaluation.
To fix it, I changed the aggregation_strategy to max.

I also removed unsupported entity ( Purp, Features, DOM, ENCR, IP, URL, MD5, PROT, EMAIL, SHA1, SHA2) to ensure fair comparison.

- True Positives (TP): 14041
- False Positives (FP): 4081
- False Negatives (FN): 3314
- Precision: 0.7748041055071184
- Recall: 0.8090463843272832
- Avg latency: 0.025403662559714144 s/sentence

- There is a balance between precision VS  recall
- The FNs are significantly lower compared to Cyner 
- better classification, there is more label predictions instead of generic lables like "Organization"
- Better latency 


## Conclusion:

SecureBERT was selected as the better model for this need

## If I had more time :

- Filter only high predictions score and test the measurements- may reduce the FP
- Calc the Precision and recall per sentence and then sum to average 
- Separate evaluation base labels( "APT" ,"malware"). 
	- This way I could explore where the model weak and where its strong 
- Test and improve( if needed) the aggregation strategy
- Test what is the best context window size
	- Find what the optimal max size for sentence 
- Test it on more datasets ( noisy, mixed ...)
- Explore the extra predictions( IP, URL...)
- Analyzes boundary match(start and end)
- Parser it better:
	- Make it more generic for any input, without assuming that a single space separates words.
	- make it more running time efficient 
	- Support large files (GBs) - using 'yield' concept and load to memory one\ few lines at the same time. Not like ```f.readlines()```
	- Improve error handling
- Over all -Make the project more solid, clean code 
	- Efficient running and memory. 
	- Move hard coded parameters into configuration\const files.
	- Add logging
	-


## Part 2: Web UI Development using Streamlit:

A web user interface developed using Streamlit.
This platform allows any user to upload TXT files, process each file through model and show the result in a visual fomat.

#### Dependencies:
```python
pip install transformers pandas streamlit

```

#### Running the web interface:
```c
streamlit run basic_ui.py

```

### The architecture in short:
1. UI using streamlit for basic UI:
	1.  Live filtering by label and key word
	2. Display all the predicted results in convenient table with option to download a reault file
2. File Processing:
	1. Split TXT file into sentences 
	2. Send each sentence to the model 
	3. Combine the results
	4. Convert results into DataFrame
3. Performance:
	1. Model caching-  Its cached per path to avoid reloading every time
	2. If available using GPU to reduce the latency 

### If I had more time: 
1. Add model selection dropdwon
2. Add general analytics at the UI
3.  Improve the UI and make it more user friendly

### Docker:

```powershell
docker build -f dockerFile.txt -t web .
docker run -p 80:80 web
Local URL: http://localhost:80
```
