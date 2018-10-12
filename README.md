### Progress Report

Currently on the capstone I have no problems with the data.  I have gotten the data in and transformed how I wanted it.  I also have done good deal of EDA on the data.  I will have a little more to do as I am currently reworking my model.

I tried both regression modeling predicting the Home Win Margin which I then used to make a pick versus the line.  I also tried categorical modeling using both home cover and away cover as dependent variables. (I need to do this because about 2% of the cases are pushes which are now categorized as loses)  I am creating a new variable called payout that will take that into consideration and provide a metric to determine how the model is doing and also be something to maximize on.  Might be willing to have lower precision if the payout is higher.  

The modeling did not go well so far.  I look at my ROC plots and they are basically a straight line with scores just over .5.  There were a few bubbles with a predicted prob of about .6 that had decent prediction for the away cover on the test data, but I did not even try them out on my true test data the last two years, because they looked suspect.  I feel that my problem is that much of the data I have been using on the aggregate level has been used to generate the lines.  

Today and tomorrow I am going to test out a new method by segregating the data into pieces that I think are logically interesting using ideas of either streaks or regression to the mean and see if I can use these new features to find wholes in the analysis, or pockets that are predictive.  I hope to do most of this today and tomorrow so that I can determine if this will work out.  

I will probably test these new features both with and without the aggregate features that I have created to determine if I can get meaningful results.  If I have to I can probably go back to my first categorical analysis that produced some results and see if that works versus new data, but I would be suspect of using the methods.  It might be OK for a presentation, but not in practice.  I hope that this avenue will prove productive.  Hopefully, I will get some results by tonight or tomorrow that will give me an indication about whether or not I can go forward with this new method or if I will need to come up with a new approach or return to the first one and write up the results as best as I can.

