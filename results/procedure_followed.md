## Procedure that I followed

# A. Data data everywhere!
## (Info on where the results are stored and what I'm calling things)

I'm calling all of the original "_tt.json" data that was in the /data folder the "original" data.

The output from our preprocessing is "our test set" or "our data". Thus the results are "our results" and so on.

#### input

I've made folders for original_input and our_input. Note that our_input is a the original data with our test sets **appended** to the end of the files. This makes the first X records in the file the training set (aka the original data) and the last Y records our test set. 

#### output
You'll find all of the individual results csv files in the /original_results and /our_results folders and four csvs in the outer datafiles folder that contain either the combined meanscore results for original data / our data or all the results (not just the meanscores) for original data / our data. It should be a simple thing to make excel pivot tables out of these.

# B. What did I edit in the code?

Two things basically.

1. I added some extra lines at the bottom of review_classifier_evaluate.py to make it run through for each of the labels instead of just for Bugs/Not_Bugs (NOTE that I did this for running the original data as well)
 
2. I modified several of the lines between 433 and 454 in review_classifier.py (mostly commented stuff out). It is actually embarassing how few changes were needed when it came down to it. **You guys will have to check my work**

```
        num_folds=1 #Only run once through. ie don't do cross validation.
        for i in range(num_folds):

            for label in labels:
                test_counter[label] = 0
                train_counter[label] = 0

            # Doesn't randomize anymore -Alex
            #random.shuffle(self.data_with_label)

            # select test and training sets
            # Since we have appended the test set to the training set file we need
            #   to select based on record number (i.e. first X are training, the rest are test)
            # Number of training entries in training sets varies:
            # Bug_tt.json : 740
            # Feature_tt.json : 616
            # Rating_tt.json : 740
            # UserExperience_tt.json : 740
            tr_cnt_len={"Bug":740,"Feature":616,"Rating":740,"UserExperience":740}
            tr_te_split = tr_cnt_len[labels[0]]
            self.train=self.data_with_label[:tr_te_split] #Training data = everything before the split point
            self.test = self.test = self.data_with_label[tr_te_split:] #Test data = everything after the split point
```

So it is still looking for files named SOMELABEL_tt.json in the /data file and it has the training/test split points hard coded in based on the names of the files so it is really fragile and requires that you use the original names for the files (i.e. Bugs_tt.json, Feature_tt.json, etc)


# C. Ok so you copy/pasted all the csv files together...?

No I made a jupyter notebook (PYTHON 3) to do it for me! I had thought we wanted to combine ALL the csvs that get outputted into one handy list that can be turned into a pivot table so I wrote `CombineResultCSVs.ipynb`. I guess it is overkill since we really just needed the data from meanscores (who cares about the details of each K-fold result? We just want the means of those results!). This change in my thinking is why there are two code cells in the notebook. Top one just snags the meanscore csvs and combines them. Bottom one is if you would rather get all the csvs and combine them (probably don't need that). 

**NOTE:** I was running the notebook on a different folder naming scheme so the code is looking for an 'output_all' folder and saving with a specific filename. If you are going to run it you'll probably want to change those values (to 'our_output" or 'original_output" and whatever filename you want to save the combined results as).

Hopefully I didn't miss anything! :)



