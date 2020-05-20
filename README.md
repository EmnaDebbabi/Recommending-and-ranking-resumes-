# Recommending-and-ranking-resumes-
## Project overview
Implementation of an application for recommending and ranking profiles from Resumes database for HR recruitment needs.
Scraping, Data preparation, Analysis and Prediction.

The project consists in implementing IBM master plan steps in the standard data mining process
which aim to understanding the business and data, collecting and preparing data, extracting models which are then assessed to make sure that they fall in line with the business initiatives to extract useful information from it to do predictions. Our challenge
is to implement the application, which is a recommendation and
classification application for profiles of resumes database already created from WEB (from
LinkedIn) to speed up the HR recruitment process and propose relevant CVs according to the profile research.

According to IBM master plan methodology, a data science project begins with the most important chapter which is business understanding; doing the plan and strategy to respond to our main goals and meet the expectation of having significant results. Then, we have data collection, data understanding and data preparation in order to be ready for the modeling step. After modeling we have to evaluate our model before deployment of our application.</br>
<p align="center">
<img src="/images/1.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>

#### BUSINESS UNDERSTANDING AND DATA ANALYTICS

The first stage of the IBM master plan process is to understand what we want to accom-
plish from a business prespective. Our organization may have competing objectives and

constraints that must be properly balanced. The goal of this stage of the process is to
uncover important factors that could influence the project outcome because neglecting
this step can mean that a great deal of effort is put into producing the right answers to
the wrong questions.

### BUSINESS OBJECTIVES

In our project the business objectives that we will define are implementation of a recommendation and classification application for profiles of a Resumes database in order to speed up the HR recruitment process and to propose relevant resumes according to the profile sought by
the recruitment manager. In other words, the creation of a recommendation system for the purpose of optimizing recruitment, that is to say providing the profile that matches the profile sought. The tool allows the filtering and classification of profiles according to the position requested (diplomas, skills, seniority, place of residence, etc.). This application allows increasing overall revenue by ensuring a gain in terms of search time and gain
in terms of number of HR agents responsible for recruitment. Also we need a strategic dashboard that helps the HR manager to make strategic decisions.

### DATA SCIENCE OBJECTIVES

The principal purpose of data science is to find patterns within data. It uses various
statistical techniques to analyze and draw insights from the data. From data extraction,
wrangling and pre-processing, a data scientist must scrutinize the data thoroughly. Then,

we have the responsibility of making predictions from the data. The goal of a Data Sci-
entist is to derive conclusions from the data. Through these conclusions, we are able to

assist companies in making smarter business decisions.
In this project our data science objectives are defined below:
<ul type="circle" >
<li> Distributed Big Data architecture to support data </li>
<li> Creation of new variables </li>
<li> Data reliability check </li>
<li> Data source understanding </li>
<li> External data collection </li>
<li> Data cleaning </li>
<li> Creation of models using AI / ML / DL </li>  
</ul>
Every project, regardless of its size, starts with business understanding, which lays the foundation for successful resolution of the business problem for that mastering well the first phase of our plan is essential to succeed our project, so first of all we defined our business and data science objectives. In the next chapter we will start the second phase which is data preparation.</br>

### DATA COLLECTION AND DATA PREPARATION

#### INTERNAL DATA
##### Data source description:

We have a document-oriented database: MongoDB </br>
Collection Name: databasebrute </br>
Documents: 10,000 </br>
Avg. Document size: 5.0 KB </br>
Total Document size: 50.1 </br>
We have at least 10,000 profiles from linkedIn. </br>

##### Data understanding and data preparation:

The list of treatments performed:
<ul type="circle" >
<li> Transform the collection(10,000 json files) to a dataframe (shape : 10000,9)
We have 9 columns :’id’, ’search’, ’url’, ’personalinfo’, ’skills’, ’scrapedtime’, ’experiences’, ’interests’ and ’accomplishments’.
(Each column is composed of several attributes ==> Normalization) </li> 
<p align="center">
<img src="/images/2.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p> 
<li> Normalization : using the json_normalize library we try to decompose the columns
Example: the personal_info column will be broken down into: [’name’, ’headline’,’company’, ’school’, ’location’, ’summary’, ’image’,’followers’, ’email’, ’phone’, ’connected’, ’websites’] Experiences column into [’jobs’, ’education’, ’volunteering’] . . . </li>
<p align="center">
<img src="/images/3.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>  
  <li> Removal of compound columns and concatenation of new columns </li>
  <li> Removal of columns without any information: ’_id’ and ’scraped_time’, and columns
    which are completely empty: ‘test_scores’, ’certifications’ </li>
  <li> To update our data, we scrapped from LinkedIn. We scrapped the same LinkedIn
profiles that we have in the internal data (We used the 10,000 URLs that we have).
    Libraries used: BeautifulSoup, webdriver </li>
<li> Replace the content in the connectionsCount column with 1 if number of followers
  >=500 or 0 otherwise.</li>
  <li> Convert each row of the ‘Languages’ column to a list to facilitate their manipulation later.</li>
  <li> Correction of the content of the ’Language’ column (we found a lot of errors in writ-
ing the language and still writing with different languages, so we made a dictionary

that contains all the possible scripts for each language and we get: Arabe, Anglais,
Français, Allemand) </li>
 <li> Replace the content of the ‘Location’ column with 1 (if the candidate is in Tunisia)
or 0 (if not)
   (1 if there is a sub-chain "tunis" in the address chain) </li>
 <li> Add a column ‘Gender’ which contains either 0 (male) or 1 (female) In fact, we
created two dictionaries, one containing the female names and the other containing
the company names (the other names will be automatically assigned to masculine)
   and we browse the 10,000 profiles to assign either 0 or 1. </li>
 <li> Delete company profiles from our database. (Because our objective is to recommend
profiles of candidates). </li>  
  <li> Fill in the empty fields or NaN with the string "vide". </li> 
  <li> Add 55 columns (skills). We only worked on the skills requested in the 9 proposed
profiles (Java, SQL, NOSQL, NodeJS, Linux . . . ).
Using nltk for each skill, if it exists in the candidate’s skills list, we add the experience
duration for that skill in months. </li> 
 <p align="center">
<img src="/images/4.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>  
  <li> Transform the content of the column exp_duree into the number of months of this
experience.
example: 5 ans 7 mois -> 67 mois </li>
  <p align="center">
<img src="/images/5.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p> 
  <p align="center">
<img src="/images/6.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>   
  <li> Add a column "turnover" which contains 1 if the candidate has the habit of chang-
ing positions quickly (exp_duree <= 12 for most of the positions occupied) or 0

otherwise.</li> 
  <li> Replace the content of the degree_name column with a classification of Diplomas
(License, Engineer, Master, Doctor, BTS, BTP, Other). </li> 
  <li> Encode categorical variables such as degree_name with OneHotEncoder. </li> 
    <p align="center">
<img src="/images/7.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p> 
  <li> From degree_year we extract a new column ‘Young_Graduate_Student’ (1 if sys-
date –degree_year <=2 years and 0 otherwise)</li> 
  <li> Replace “vide” in ‘Full_name’ column with the name that can be found in the ‘URL’
column. </li>

#### EXTERNAL DATA

For external data we extracted information from Git Hub, Tweeter and Facebook. From GitHub:
We have from the websites column links to GitHub, so we extract from it all skills which
are used in projects and the percentage of appearance of every skill.</br>
From Tweeter: </br>
From our database we browse enterprises and we extract tweets for ev-
ery entreprise. Then, apply NLP on these tweets in order to classify enterprises according
to their reputation.</br>
<p align="center">
<img src="/images/8.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/9.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/10.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
From Facebook: </br>
Using ‘facebook_scraper’ library and ‘get_posts’ module to be exact, we extract data
from publications of enterprises in order to find the most frequent words to find out the
main activity sector of the company. This information will help us to know whether the
candidate has worked in the same sector of activity requested or not. </br>

#### DATA EXPLORATION

Once we have prepared our dataset which contains all the numerical variables, we try to
explore it better to extract more information.
<p align="center">
<img src="/images/11.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/12.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
We see that we have enough PhD students among our candidates, however we have a
limited number of engineering / license / Master titles.
<p align="center">
<img src="/images/13.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/14.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/15.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
According to these tables we have more men having a Master’s Degree and engineering
degree than women.
<p align="center">
<img src="/images/16.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
Most PhD profiles are males.
<p align="center">
<img src="/images/17.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
27% of PhD students are in Tunisia vs 40% abroad
<p align="center">
<img src="/images/18.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
68% of PhD students tend to change their job.
<p align="center">
<img src="/images/19.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
The percentage of engineers that tend that change their position is low.
<p align="center">
<img src="/images/20.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/21.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
There is almost a balance between the candidates who have less than 500 Followers
and those beyond the 500.

#### MODELING

Recommender systems are among the most popular applications of data science today.
The recommendation is to guide the user in his exploration of the data so that he finds
relevant information.
In recommendation systems, the usefulness of an item is usually represented by a score.
So, recommendation systems are classified according to the approach used to estimate
this score: </br>
1) Content-based method: the user will be recommended similar elements (in the sense
of a measure of similarity between elements) </br>
2) Collaborative method or based on collaborative filtering: the user will be recommended
elements that other users with similar tastes and preferences (in the sense of a similarity
between users and elements)</br>
3) Hybrid method: combination of the two previous methods.
Methods 2 and 3 are to be eliminated, we cannot use them for our application because in
our case we do not have several users of our recommendation system, it is well used by
the HR agent in charge of recruitment. So we used a content-based method.
For content-based recommendations, the task is to determine which elements of the catalog
best match user preferences. Such an approach does not require a large community of
users or a large history of system usage. 
<p align="center">
<img src="/images/22.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
The simplest way to describe an element catalog is to have an explicit list of the
characteristics of each element (we also speak of attributes, element profile, etc.). Then
store these characteristics (in a database).
For us we have our database of 10,000 profiles ready and we have 111 attributes.</br>
Dimentionnality reduction: In order to reduce the dimentionality of our database, we
studied the correlation between the different variables.
There is no strong correlation between the attributes.
Then, we use PCA (Principal Component Analysis) and we found 40 components which
have eigen-value >=1.</br>
So, according to kaiser’s criteria we can maintain only these 40 components. These 40
dimensions summarize more than 99% of the total information in our dataset. So, for score
calculation we will use only those 40 attributes which are mainly skills. Score calculation:
We followed the principle of content-based algorithms and we developed our own algorithm
which is customized for our application and our objectives. First of all, we formulated
the score for the 9 profiles proposed according to the skills and coefficients requested by
Client.
<p align="center">
<img src="/images/23.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/24.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
Then for each profile among the 10,000 profiles, we calculated the corresponding scores.
Clustering:</br>
Clustering aims to divide the population or data points into a number of groups such that
data points in the same groups are more similar to other data points in the same group
and dissimilar to the data points in other groups.</br>
For this we used “Kmeans”:</br>
<p align="center">
<img src="/images/25.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
And also we used “DBscan” :</br>
<p align="center">
<img src="/images/26.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
k-nearest neighbor distances to determine eps in DBSCAN
and this is the DBscan clustering
<p align="center">
<img src="/images/27.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
Classification We aim to assign each candidate to the closest profiles of the 9 profiles
proposed.</br>
So, we attribute the profile and the score for each candidate in our data base.</br>
<p align="center">
<img src="/images/28.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
Filtration:</br>
We Removed profiles which their score is null and extracting only those affected to profiles
proposed by client.</br>
<p align="center">
<img src="/images/29.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
We have at least 3934 profiles from 10000 which are affected to our 9 profiles.
Similarity measure:</br>
Cosine is widely used to measure the similarity between two vectors. Its calculation is
very efficient, especially for sparse vectors, as only the non-zero dimensions need to be
considered.
We used cosine similarity to obtain top 10 profiles closest to each of the 9 profiles proposed.

#### EVALUATION

To measure the capacity of our recommendation algorithm to predict correctly, we used
the evaluation metrics specific to recommendation systems.
A great recommender system makes both relevant and useful recommendations. Using a
combination of multiple evaluation metrics, we can start to assess the performance of a
model by more than just relevancy.
To evaluate our model, we use Intra_List_Similarity and Personalization.</br>
Personalization:</br>
Personalization is a great way to assess if a model recommends many of the same items
to different users. It is the dissimilarity (1- cosine similarity) between user’s lists of
recommendations.</br>
A high personalization score indicates user’s recommendations are different, meaning
the model is offering a personalized experience to each user.</br>
Intra-list Similarity:</br>

Intra-list similarity is the average cosine similarity of all items in a list of recommenda-
tions. This calculation uses features of the recommended items to calculate the similarity.

If a recommender system is recommending lists of very similar items to single users, then
the intra-list similarity will be high.</br>
We did get a high score. So, our model is able to predict correctly and our application
is ready to be deployed.

#### DEPLOYMENT

Once our data and our model are ready we can start the deployment phase. It is the last
phase before feedback and the most important because it highlights the whole project.
In this step, we enable users to use and to benefit from our application.
First of all we have users interface registration.</br>
Then, we have login interface.</br>
Moreover, we have description and visualization of the content of our database. We
think that it is very important and very helpful that the RH agent explore what kind of
candidates he has in the data base.</br>
Furthermore, the recruitment agent can choose whatever profile he wants from our
data base and our application will give him a list of top 10 profiles closest to the chosen
profile, with graphs illustrating the degree of similarity of each proposed candidate with
the chosen profile.

Now it’s time for the recruitment agent to enter whatever profile he wants with new at-
tributes according to his choice and his requirements and our application will give him a

list of top 10 profiles closest to this profile and also with graphs illustrating the degree of
similarity of each proposed candidate with the desired profile.</br>
<p align="center">
<img src="/images/30.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
<p align="center">
<img src="/images/31.png" alt="Alt text" title="Optional title" style="display: block; margin: 0 auto; max-width: 50%">
</p>
Recommender systems have great value in recommending relevant resources to users. It
can be quite useful in finding novel and serendipitous recommendations.
Our application of CV recommendation system is ready, we achieved all steps of IBM
master plan and we reached successfully our objectives fixed at the beginning.
We extracted Data using Web Scraper. Then, we cleaned Extracted Data. Furthermore,
we used Cosine Similarity. And finally, we offered Recommendations based on similarity
score.
