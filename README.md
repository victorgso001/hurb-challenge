# hurb-challenge

This project was designed as a techincal challenge for Hurb data science team appreciation. It is based on the Hotel Booking Prediction Kaggle notebook, which uses data available [in this link](https://storage.googleapis.com/dsc-public-info/general/jobs_challenges/machine_learning/entry_level/datasets/hotel_bookings.csv), as part of the [Hotel Booking Demand Datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191).
The model used was the CatBoost, trained based on [this notebook](https://www.kaggle.com/code/niteshyadav3103/hotel-booking-prediction-99-5-acc). The model was choosen by accuracy score evaluation available in the end of the notebook.

# Important Note
By the limitations in the dataset, classification will only work in the dates between 2015 to 2017.

# Installation
## Prerequisites
* Docker and docker-compose;

## Installation steps
* Clone the repository;
* Create a folder named model on project's root folder;
* Download the .csv dataset [here](https://storage.googleapis.com/dsc-public-info/general/jobs_challenges/machine_learning/entry_level/datasets/hotel_bookings.csv) and paste it inside model folder;
* Run `docker-compose up -d` to run the containers.

# Usage
This project was based on Flask API, with tree main routes to use. The api is available locally by the link `http://localhost:8000`.

## Routes

### ´/´
* Method: GET;
* Inputs: None;
* Outputs: Text "Hurb Technical Challenge API"

### ´/model/fit´
* Method: GET;
* Inputs: None;
* Outputs: Text "Model trained successfully!";
* Description: Model training route. When succeeded, it will make metrics available in the MLFlow application.

### ´/model/predict´
* Method: GET;
* Inputs: JSON with dataset columns as keys and values as described in the article;
* Outputs: JSON with prediction class;
* Description: Model prediction route.

Input example:
```
{
	"reservation_status_date": "10/27/2017",
	"hotel": "Resort Hotel",
	"meal": "SC",
	"market_segment": "Direct",
	"distribution_channel": "Direct",
	"reserved_room_type": "E",
	"deposit_type": "Refundable",
	"customer_type": "Transient",
	"lead_time": 457,
	"arrival_date_week_number": 43,
	"arrival_date_day_of_month": 10,
	"stays_in_weekend_nights": 2,
	"stays_in_week_nights": 2,
	"adults": 2,
	"children": 0,
	"babies": 0,
	"is_repeated_guest": 0,
	"previous_cancellations": 0,
	"previous_bookings_not_canceled": 1,
	"required_car_parking_spaces": 0,
	"total_of_special_requests": 0,
	"agent": 8,
	"company": 110,
	"adr": 120,
	"days_in_waiting_list": 0,
	"arrival_date_year": 2015,
	"assigned_room_type": "C",
	"booking_changes": 3,
	"reservation_status": "Check-Out",
	"country": "PRT",
	"arrival_date_month": "October",
	"is_canceled": 0
}
```

Output example:
```
{
	"pred_class": 1
}
```
