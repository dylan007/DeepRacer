# DeepRacer
This is the set of all the reward functions that were created as a part of an AWS Deepracer contest. 

Highest performing model was model9 and model6. 

The following is the barely descriptive notes that I had to track each model. 


Model1 -> Use directional tangent = 21 seconds

Model2 -> On top of model1 prefer more speed= 16.726

Model3 -> Use slower car ~ reduce action space from 4 m/s to 3 m/s = 20.291

Model4 -> On top of model3 prefer more speed and steering = 17.594

Model5 -> Self explorator = 22.976 

Model6 -> On top of model2 = 14.601

Model7 -> On top of model6 = 15.079

Model8 -> On top of model2 but using model7 weights = 17.1

Model9 -> On top of model6 but also trying to keep it on track = 14.174

Model12 -> Low effort attempt at training to follow a precomputed racing line using path optimizations algorithm that can be found at [Remi Coulon's Thesis](https://www.remi-coulom.fr/Publications/Thesis.pdf) and [Race Lines](https://github.com/cdthompson/deepracer-k1999-race-lines) ~ 18 seconds