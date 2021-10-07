# Flight-Optimal-Time-Prediction
Introduction:
Nowadays, airline ticket prices can vary dynamically and significantly for the
same flight, even for nearby seats within the same cabin. Customers are seeking to
get the lowest price while airlines are trying to keep their overall revenue as high as
possible and maximize their profit. Airlines use various kinds of computational
techniques to increase their revenue such as demand prediction and price
discrimination. From the customer side, two kinds of models are proposed by
different researchers to save money for customers: models that predict the optimal
time to buy a ticket and models that predict the minimum ticket price.

Aim of the Assignment:
Airlines employ complex, secretly kept algorithms to vary flight ticket prices
over time based on several factors, including seat availability, airline capacity, the
price of oil, seasonality, etc. Our aim is to predict the optimal time to buy a ticket
with the minimum ticket price. So can we can predict the time when a customer
can book a ticket before the travel to get the best price according to the airline.

### Data is scarped from www.kayak.co.in 
### Link - https://flight-time.herokuapp.com/   (Use Chrome for better experience)
### EDA 
### MOdel used-
    Model Name	            Train R2	Train MAE	Test R2	Test MAE
    0	CatBoost Regressor	1.000	    524.586	    0.998	1756.857
    1	SVC Regressor	    0.998	    2941.927    0.998	2974.582
    2	Knn	                1.000	    0.921	    0.991	1133.553
    3	Xgboost Regressor	1.000	    103.999	    0.993	2017.389
    4	Random Forest 
            Regressor	    0.996	    2032.324	0.988	3703.585
    5	MLP Regressor	    0.995	    4187.926	0.995	4159.600
    6	SGD Regressor	    0.999	    2193.268	0.999	2229.082
    7	Lasso Regression	0.999	    2196.623	0.999	2246.860
    8	Ridge Regression	0.999	    2197.549	0.999	2243.425
    
### Deployment using flask
![Screenshot (361)](https://user-images.githubusercontent.com/58500044/119014612-c3cad080-b9b5-11eb-966e-482508b8b610.png)
![Screenshot (362)](https://user-images.githubusercontent.com/58500044/119014622-c5949400-b9b5-11eb-8398-a6c794215576.png)
