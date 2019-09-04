# Final Project
Last Update: 2019/07/01  <br />
First Proposed: 2019/06/28 <br />
Author(s): Aisha, Nara, Nic, Qianti <br />
Reviewer(s): <br />
Status: [Draft] <br />

## Objective
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We want to use Machine Learning techniques, specifically Classification, to raise awareness in regards to what can and what should not be recycled. The final product will be in the form of an app that a consumer can use to identify individual items according to their county’s regulations. <br />
  
##  Background
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recycling as we know it in the United States truly became a part of our culture following World War II. More specifically, during the environmentalist movements in the 1960s and 70s. Since then it is estimated that recycling has created at least 1 million jobs with total sales being estimated at around $300 billion in 2012.<sup>1</sup> In more relevant terms, it is also estimated that by 2030, a recycling rate of 75% in the U.S. will create 1.1 million new jobs.<sup>2</sup> Globally, the UN predicts that recycling will create 60 million new jobs.<sup>3</sup> <br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Although this is quite an optimistic outlook, there have been recent international decisions that threaten to risk all of the progress that is just now starting to be fully integrated in many American lifestyles. In 2017, China announced a new import policy permanently banning the import of nonindustrial waste. Given that, since 1972 China has imported more than 45% of all plastics, the cost of dealing with our recycling has increased exponentially.<sup>4</sup> Many communities in America can’t afford the new costs of recycling and are defaulting to incineration.<sup>5</sup> <br />
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Much of the new cost is dealing with plastic contamination and sorting onsite rather than shipping everything to China. This is where machine learning comes into play – we want to provide a service that can help households sort their trash and increase general recycling knowledge so that recycling plants do not have to suffer the consequences of false ‘rules of thumb’. Furthermore, we hope that this app can be extrapolated to work with any recycling regulation based off of an individual’s zip code.

#### Footnotes 
1. https://ilsr.org/history-post-ww-ii-recycling-movement/
2. https://www.ecocycle.org/zerowaste/jobs
3. http://www.ilo.org/global/publications/books/WCMS_181836/lang--en/index.htm
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6010324/
5. https://www.theatlantic.com/technology/archive/2019/03/china-has-stopped-accepting-our-trash/584131/

## Overview
One page of high-level overview that will describe what needs to be done in this project.

#### 1. Get Data
After knowing the recycling rule of the target region(s), LA county, we will search for relevant datasets containing pictures of recyclable/non-recycle objects and e-waste according to the rules. **Note that we will need to collect some of our own data that we will manually label into their respective categories.**
1. Research similar existing projects (github) 
2. Use datasets from those projects and improve them by adding our variations of trash, recyclable items
3. Take photos if needed

**Some datasets:**
1. Image website(beer bottle): http://www.image-net.org/synset?wnid=n02823428
2. Type of Plastic: https://www.kaggle.com/piaoya/plastic-recycling-codes
3. Stanford project github page:: https://github.com/garythung/trashnet 

#### 2. Cumulate and Clean Data (Preprocessing steps)
We are going to use ImageDataGenerator as our preprocessing tool for the training datasets. With this we can flip, rescale, rotate, zoom the images and normalise the image features. Also we can do color fixing of the images with this tool. By doing all these preprocessing step we could be able to randomize our training datasets effectively and be able to deduct future complications regarding object identifications when we train our model.

#### 3. Create Model
Our model will ideally consist of two major parts: image classifier (gate) that can distinguish a general category for the item and image classifier that can distinguish sub types of recyclable items. However, due to time constraints, we decided to focus our model only as a general classifier. The model could include: Classification with TensorFlow, Keras and, Scikit-learn, Convolutional Neural Network, and DNN. We are also planning to create our model based off a model that already exists and improve it by modifying the hyperparameters and add our own layers since it will be much more efficient and less time consuming than creating our own model from scratch. In addition we will try to modify our training datasets based on user’s feedback in order to improve the accuracy and precision of the model.

#### 4. Train Model
Using transfer learning, we will train and improve upon our model.

#### 5. Test Model
Making sure our model works fine with our training data, we will then test our model based on the testing data which will include random images of trash, recyclables and E-waste. Based on how accurate our test score is, we will keep on training our model until we get somewhat of a high accuracy score. For example, the images that get the wrong classification can be used to retrain our model.

#### 6. App Creation w/ integration
We will then create an app based on our model. The app involves the user to take/upload a picture of a trash/recyclable object and then receive a classification label if  the object is a plastic/glass/metal etc. If the classification label is correct, the object will be sub classified into the type of glass, plastic, paper etc. If the first classification label is wrong, the user has an option to select the right label for the object. We will use the user’s ‘corrected selection’ to retrain our data. 
After the sub classification, if the label is correct, the object will be categorized as trash, recyclable or E-waste depending on recycling rules of that particular county.


## Schedule/Sequence Diagram/Interface Design

## Fairness Considerations

#### Write a one-paragraph story describing a fictional person who was positively affected by a model trained with this data
Abel is a recent college graduate who works a 9-5 job at the local Blockbuster. He goes to Starbucks every morning and orders takeout a couple times a month. He understands and is aware of the importance of recycling, however, he relies on his availability heuristic when deciding which bin to throw away his trash in. The availability heuristic is a mental shortcut that relies on immediate examples that come to a given person's mind when evaluating a specific topic, concept, method or decision. With our new Recycling app, Abel is able to quickly snap a photo of his starbucks cup and know to recycle the cup and throw away the lid. He snaps a photo of his pizza box and knows to not recycle it if there is too much grease. Abel goes on with his life and spreads his newfound ‘rules of thumb’ and community awareness increases as a whole.

#### Describe at least two sources of bias the particular model in your story could have
1. The model could perform well for common consumer items, however, have difficulty classifying foreign packaging. We can attempt to include as diverse of a dataset as we can by searching for as many types of recyclables that we may expect our users to use.
2. Following these lines, our model may be susceptible to reporting bias. Given that we will be using image-net.org for a lot of our images, we may be creating a dataset that isn’t proportionate to what it should expect. In addition, we want our model to train on individual items, and will need to make sure it does not include pictures with more than one main item. 
3. Finally, given that we are dealing with images, our model is susceptible to different lightings/camera qualities and will need to adjust appropriately to minimize differences between each user’s environment/resources.

#### Describe at least one way we could modify the model to mitigate this bias
1. If the model incorrectly classifies an item, we can make our model’s output also include what it classified the item as (more specific than trash/recyclable/e-waste). That way the user can clearly understand where the issue occurred and report it. The user will be able to include an accurate label and then their image/label will be included in the next day’s training.
2. In reference to the variability in image quality, we can make sure our model edits the image to normalize brightness and other factors that could negatively affect our model’s accuracy.

#### Describe at least one way we could modify the dataset to mitigate this bias
In order to handle the seemingly infinite potential input, we can look at a variety of items and include the data they used in an effort to pool as many examples as possible.In addition, some projects have had issues with classifying between plastic and glass water bottles. Therefore, we can make sure our model has enough of each to be able to properly discern between the two.

#### Describe at least one way we could modify the context surrounding the model to mitigate this bias
One option is to make it clear that the classification may not be 100% correct so that users do not blindly trust the model. We could also state a percent confidence for each classification.

#### Write a one-paragraph story describing a fictional person who was negatively affected by a model trained with this data
Greg has finally found a career that he is passionate about. As a trash sorter at the local recycling plant, Greg spends his days sorting bales of trash into three piles: trash, recycling, and e-waste. However, our new app has made his job less important as more people are correctly sorting out their own trash. Due to the decrease in demand for trash sorters, Greg is laid off. Left with no job, Greg blames his misfortune to the increasing use of A.I. in every industry. With all the time on his hands, he begins to rally others who have lost their jobs in a similar fashion and single-handedly begins a movement that destabilizes the A.I. movement, driving the world into a dark age as technology becomes taboo.
