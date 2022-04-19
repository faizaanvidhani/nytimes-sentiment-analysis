# :chart_with_upwards_trend: Analysis Deliverable 



## Hypothesis Testing

#### *H1: Is there a significant difference between the sentiment scores of a headline and its corresponding article?*

- H1<sub>0</sub>: The mean difference in sentiment scores between headlines and their corresponding articles is zero. Mathematically, u<sub>D</sub> = u<sub>H</sub> - u<sub>A</sub>= 0.
- H1<sub>a</sub>: The mean difference in sentiment scores between headlines and their corresponding articles is not zero . Mathematically, u<sub>D</sub> = u<sub>H</sub> - u<sub>A</sub> != 0.

**Statistical Testing Method:**
- Two-tailed paired t-test

**Why did you use this statistical test or ML algorithm?**
- Since we are interested in the difference between the headline rating and article rating for the same article, it seemed appropriate to conduct a paired t-test. 

**Which other tests did you consider or evaluate?** 
- We considered running a two-sample t-test, but since we are working with related samples as opposed to independent samples, it seemed more appropriate to conduct a paired t-test.

**How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model?** 

- We measured success/failure by assessing whether our p-value seemed reasonable. Since our p-value took on a value between 0 and 1, it seemed reasonable to conclude that our paired t-test was successful.

**Did you have to clean or restructure your data?**
- Since our model outputted the sentiment score for each article and its corresponding headline, there was not much cleaning/restructuring that was needed to perform the paired t-test.

**What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**
* Our t-statistic was -15.84. Our p-value was approximately 0 (p=1.52e-52). Our level of significance was 𝝰=0.05. Since p < 0.05, we reject the null hypothesis. There is enough evidence to suggest that the mean difference in sentiment scores between headlines and their corresponding articles is not zero. 
* That is, the sentiment scores of headlines differ significantly from the sentiment scores of their corresponding articles. 
* The set up of our hypothesis test and our negative standardized test statistic t=-15.84 suggests that headlines seem to be more negative than their corresponding articles.
* Previous research has shown that the stories that are most read or most shared on social media sites tended to be the ones that were more negative. Our hypothesis test seems to support previous research. Thus, we are mostly confident in our results. We are not that surprised by the results of our hypothesis test.

___

#### ***H2:** Are the sentiment scores of arts headlines significantly greater than the sentiment scores of technology headlines?*

- H2<sub>0</sub>: The mean sentiment score of arts headlines is equal to the mean sentiment score of technology headlines. Mathematically, u<sub>A</sub> = u<sub>T</sub> . 
- H2<sub>a</sub>: The mean sentiment score of arts headlines is significantly greater than the mean sentiment score of technology headlines. Mathematically, u<sub>A</sub> > u<sub>T</sub>.

**Statistical Testing Method**
- One-tailed two-sample t-test

**Why did you use this statistical test or ML algorithm?**

- Since we are interested in exploring whether the mean value of one group is significantly greater than the mean value of another group, we chose to run a two-sample t-test.

**Which other tests did you consider or evaluate?**
- We considered running a paired t-test, but the paired t-test is appropriate for related samples, whereas the two-sample t-test is appropriate for independent samples. Since arts headlines and technology headlines are not related, we chose to proceed with the two-sample t-test.
- We also considered running a one-way ANOVA. Both tests would provide the same results, but since we are interested in only comparing the means of two groups as opposed to multiple groups, we proceeded with the two-sample t-test.

**How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model?** 
- We measured success/failure by assessing whether our p-value seemed reasonable. Since our p-value took on a value between 0 and 1, it seemed reasonable to conclude that our two-sample t-test  was successful.

**Did you have to clean or restructure your data?**
- Since our model outputted the sentiment score for each article and its corresponding headline, there was not much cleaning/restructuring that was needed to perform the two-sample t-test. The cleaning/restructuring for this hypothesis test entailed filtering the data frame such that we had the sentiment scores for the Arts and Technology categories. 

**What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**
- Our t-statistic was 2.68. Our corresponding p-value was 0.0038. Our level of significance was 0.05. Since p < 0.05, we reject the null hypothesis. There is enough evidence to suggest that the mean sentiment score of arts headlines is significantly greater than the mean sentiment score of technology headlines.
- Our motivation for conducting this test was that we predicted technology headlines to be more negative and arts headlines to be more positive. With the rise of technology, we have been seeing more negative article headlines conveying the dangers of technology. On the contrary, articles about the arts tend to be less negative.
- Surprisingly, the results of our hypothesis test appear to align with our intuitions. We are mostly confident in our findings as we had sufficient data when conducting our hypothesis test. 

___

#### ***H3:** Is the mean difference in sentiment scores for headlines and their corresponding articles for a given author the same across all authors?*

* H3<sub>0</sub>: The mean difference in sentiment scores for headlines and their corresponding articles for a given author is the same across all authors. Mathematically, u<sub>1</sub> = u<sub>2</sub> =...= u<sub>j</sub>  where j is the number of authors.
* H3<sub>a</sub>: The mean difference in sentiment scores for headlines and their corresponding articles for a given author is not the same for all authors. Mathematically, u<sub>i</sub> != u<sub>k</sub> for at least one pair of i, k {1,2,...,j}, i != k.

**Statistical Testing Method**
* One-way ANOVA Test

**Why did you use this statistical test or ML algorithm?** 
- Since we are looking to compare the mean differences for more than two groups, it was more appropriate to use the ANOVA test. 

**Which other tests did you consider or evaluate?** 
- We originally considered the t-test; however, the t-test is more appropriate when comparing the means of two groups.

**How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model?** 
- We measured success/failure by assessing whether our p-value seemed reasonable. Since our p-value took on a value between 0 and 1, it seemed reasonable to conclude that our one-way ANOVA test was successful.

**Did you have to clean or restructure your data?**
- Yes, we had to remove rows where there were multiple authors corresponding to a particular article or if the author was unknown.

**What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**
- Our F-value was 1.04. Our corresponding p-value was 0.30. Our level of significance was 𝝰=0.05. Since p > 0.05, we fail to reject the null hypothesis. There is not enough evidence in support of the alternative hypothesis.
- The evidence suggests that the mean difference in sentiment scores for headlines and their corresponding articles for a given author appears to be the same across all authors.
- We were slightly surprised by the results of our hypothesis test. We were expecting certain authors to have more variation in the sentiment scores for headlines and corresponding articles than other authors.
- We are mostly confident in our results since we had sufficient data when conducting our hypothesis test. In the future, if we were to re-investigate our claim, we could rerun our hypothesis test with more data from other publications.
___

## :computer: Machine Learning

* **Why did you use this ML algorithm? Which other tests did you consider or evaluate?** 

    We decided to use an LSTM based ML algorithm since they are used in lots of NLP tasks including sentiment analysis due to their architecture being well suited for handling long sequential data such as text based documents. Other ML algorithms that we considered using included lexicon based methods such as AFINN, Textblob, and VADER but decided to opt for an LSTM model we could individually train and test. Similarly, we found that accuracies for Textblob and VADER on the SST-5 have been reported to be 28.4% and 31.5% which is lower than what our LSTM model was able to achieve . We also tried to evaluate our article dataset using AFINN but realized that the range of sentiment values varied significantly with the lowest article headline sentiment score being -9 and the highest being 7 and for article texts the lowest score was -138 and the highest was 196.  This was most likely due to the fact that AFINN sentiment scores can vary dramatically with longer texts, which is why we opted not to use this model.

    - [Results of AFIN Sentiment Analysis]( https://colab.research.google.com/drive/15ASCWWrke6gouJCYbcpw4WLzMVQpDaol?usp=sharing)


* **What is your interpretation of the results? Are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**

    At first glance the  LSTM model accuracy wasn’t as high as we had hoped when classifying the SST-5 data set. However, after some research into other model performances we realized that most models trained to perform  the same task have accuracy values ranging from 40-59%. Even with this in consideration, we are still hesitant to say we are fully confident in the results produced by running our model on our New York Times dataset due to the low accuracy. Nonetheless, lots of the classifications scores produced by our model on the New York Times data do seem to make sense. For example, the model classified the following headline “China’s ‘Zero Covid’ Mess Proves Autocracy Hurts Everyone” as highly negative (sentiment score = 0). Similarly, the following headline was classified as having a sentiment score of 4 (highly positive): “There’s a Light at the End of This Dark Year”. 

    We argue that we were able to get a model accuracy score of around ~39% due to our LSTM being better suited for interpreting longer sequential data. The use of an LSTM architecture compared to something like an RNN allows us to propagate information and contextual clues through our model by using a remember module which is helpful for gauging the context of longer input sequences. Similarly, an LSTM incorporates a forget model to “forget” or discard information that is no longer relevant to the current context. We contribute these architecture enhancements to our model accuracy being higher than other lexicon models. Similarly, accuracy scores achieved by other models on SST-5 higher than our accuracy are due to the use of much more complicated and advanced architectures that are outside our ability to implement within this class. Overall, we are happy with our model and semi-confident in the classification values of the New York Times articles. 
 
* **Do you believe the tools for analysis that you chose were appropriate? If Yes/No why or what method could have been used?**

    We do believe that using our ML model was the appropriate tool chosen for performing sentiment analysis on New York Time articles and headlines. Other tools available for sentiment analysis such as lexicon based models including AFFIN and Textblob are not meant to perform sentiment analysis on long form inputs (such as news articles) accurately. Similarly, these models tend to only classify sentiments of inputs  as positive, neutral, or negative giving less information about the degree of negative or positive sentiment an input has.


* **Was the data adequate for your analysis? If not what aspects of the data was problematic and how could you have remedied that?**

    The data we used was sufficiently adequate for our analysis in this project given we were able to successfully classify the sentiments of the SST-5 Fine-grained dataset with about ~39% accuracy and around ~77% accuracy if we classify a  correct categorization as being within 1 unit of the true value in our 0-4 sentiment scale. Similarly, when looking at the performance of different ML models on the same dataset we found that most models have an accuracy somewhere between 40-59%.
    
    One consideration to note about our analysis is that we trained our model on a dataset consisting of movie reviews whereas our model was trying to predict sentiments of news articles from the New York Times (NYT). The difference in the context of the data the model was trained on and the data we performed our analysis on could have an effect on the accuracy of our model on NYT articles but given the results of our hypothesis we believe that our model still performed well on the NYT data.

___

## :bar_chart: Data Visualizaitons

- For your visualization, why did you pick this graph? What alternative ways might you communicate the result? Were there any challenges visualizing the results, if so, what where they? Will your visualization require text to provide context or is it standalone (either is fine, but it’s recognized which type your visualization is)?

    Bar-Chart Visualization: 
    
    ![](https://i.imgur.com/WwCrq7j.png)

    In H2, we were examining the headline sentiment scores between two news categories (namely arts and technology). A two key bar chart (using seaborn library) is an excellent representation because it allows readers to clearly see the distinction between the categories across all possible sentiment scores. The alternative way to visualize this data would possibly be through a density plot (although we decided against it since we were dealing with discrete values), or a stacked column chart by having a vertical bar for both two categories. This could also have been represented using a pie chart for each category. But the limitation with that implementation is that it essentially meant we couldn't capture the differences between them since there would be two separate graphs.  The challenges in visualizing the results were generally adding the data to the csv and writing out the function. The visualization merely requires a title. The function was written to allow comparisons across various different categories as specified by the input. 

    ![](https://i.imgur.com/7sxgX1X.png)

    Similarly H1 follows the same set up as our second hypothesis since we are examining differences between two datasets, only now we would be looking at the articles and headlines themselves rather than the categories. The biggest challenge in this case would be dealing with the large article dataset since we would need a representation for each.
     

    Box-Plot:
    
    ![](https://i.imgur.com/gWBP1OY.png)


    Box Plot would be an excellent way to visualize the difference between two categories in our H2 since there are only two. It would answer the hypothesis question and supplement the first data visualization we had set above for H2. We can also use the box plot to answer our H1 and H3 since we are also examining the differences between sentiment scores in headlines and articles in comparison to just categories.


