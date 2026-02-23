BMI Calculator Microservice

This project is a simple BMI (Body Mass Index) Calculator Microservice developed using Python and Flask. A microservice is a small application that performs a specific task. In this project, the service calculates BMI using weight and height provided by the user through URL parameters and returns the result in JSON format.

The main objective of this project is to develop a working microservice, store the complete source code in a public GitHub repository, and deploy the application on a cloud platform. This project demonstrates understanding of REST API development, version control using GitHub, and cloud deployment.

The application was developed using Python 3 and the Flask framework. Git and GitHub were used to manage and store the source code. The application was deployed on the Render cloud platform.

The microservice provides two main endpoints. The home endpoint ( / ) returns a welcome message. The BMI endpoint ( /bmi?weight=70&height=1.75 ) calculates BMI using the formula:

BMI = weight / (height × height)

The service returns the BMI value and the health category such as Underweight, Normal, Overweight, or Obese in JSON format.

The complete source code is available in the public GitHub repository:
https://github.com/KowsiAss/bmi-flask-microservice

The live deployed application is available at:
https://bmi-flask-microservice.onrender.com/

To run the application locally, first install Flask using pip install flask. Then run the application using python app.py. Open the browser and access http://127.0.0.1:5000/
.

The application was successfully developed, tested locally, pushed to GitHub, and deployed on Render. This project fulfills all assignment requirements including development, documentation, public repository storage, and cloud deployment.
