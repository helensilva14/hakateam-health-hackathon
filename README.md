# AI Application for Best Customer Experience: InstaDoc

**Problem:** Usually, Customer Experience has a lot of “friction”, causing High Stress Due to Inefficiencies of Booking System. Even with Specialized Apps, is always difficult to find “instantly” the availability of a physician to schedule a medical appointment. Besides not offering a fast booking experience, it is also difficult to get an agenda close to home or workplace. Sometimes, he/she does not have some Specialist physician in the expected range. It is a total waste of time and a constant dissatisfaction. The main difference is that our product, besides proposing to solve these common problems, provides a personalized experience: doctor suggestion system based on customer/patient profile.

**Solution:** We designed a machine learning algorithm (KNN: K-Nearest Neighbors), that helps to create a totally different experience among Customer and his Managed Healthcare Supplier. InstaDoc integrates its provider network seamlessly, providing full and immediate access to its customers to book medical, examination or treatment appointments,at fingertips (thru mobile and web page). It shares updated network associates, with full and direct access to agenda slots. Also, the InstaDoc balances customer profile to provide best fitting considering medical needs, location, time, historical demand and social behaviour. Customer also can give scores to each professional, and get access to average ranking. In its RoadMap, InstaDoc will also combine AI and Doctor team to organize a Personal Health Planning to each customer, avoiding waste of time and resources.

From the MH Supplier side, that suffers of low profitability due to bad Customer Experience, it provides managerial Dashboard (by Tableau), helping to manage its associated network in real time, getting high level view in several cuts, including Heat Map (or Graphs) of geographical availability (or gaps) and satisfaction KPI´s, evaluating each collaborator constantly. Hence, MH Supplier can attack gaps, make Quality assurance corrections and replace providers before getting to any local crisis. Associated with other HR solution, MH Supplier will be able to recruit or replace any missing or bad component, streamlining customer service, avoiding losses and building a better profitability standard.

## Features

We propose an API-based solution (Flask Web Service using the Free Firebase Realtime Database) which provides data for:

### The patient
- Mobile application for doctor suggestion based on patient profile: [demo on YouTube](https://youtu.be/vrLiuwJX4iM)

### Healthcare supplier:
- Data for business reporting and Dashboard in Tableau, providing effective decision making tool and cost reduction.

![Panel 1](/tableau/tableau-panel1-nofilter.jpeg)

![Panel 2](/tableau/tableau-panel2-filteredbydoctor.jpeg)

## Construction of Databases

The generated dataset contains the information about the clinical appointments of each patient. The base data was extracted from a real diagnostic health company with adjustments to fit our proposal. Respecting the ethics needed to protect the patients data, the generated values are fictitious (with the exception of the names of some doctors, since CRM is public data available for research). Three different datasets were generated to be used by the AI model, the Tableau charts and the mobile app: **consultations dataset**, **patients dataset** and the **doctors dataset**.

## Development of the AI model

We opted for the KNN (K-Nearest Neighbors) algorithm for the classification model. The algorithm suggests a doctor based on patient profile by calculating the distances to the nearest neighbors which present a similar patient profile.
Then it recommends the most relevant doctor: the one with the most consultations within the cluster. 

## Tableau Dashboard

The Dashboard made in Tableau serves as a BI tool for analysts working at the Managed Healthcare Supplier to assist in the strategic decision making. Aiming for diminish waste, the allocation of accredited doctors in areas where the demand for a particular specialty by patients is high will be optimized, aiming at the management in the distribution of their resources. It is a medical report, where it is possible to filter each doctor or even a specific specialty, in addition to presenting the filter of the notes given by the patient (ranging from 1 to 5). It presents the number of consultations segmented by the note that the patients gave to the doctor, vision by age and gender of the patient, performance of plans within the operator, number of consultations performed during the quarter and the ranking of doctors with more consultations performed with the average scores attributed to them by the patients.

## High fidelity prototyping using Adobe XD

Collection and creation of Interface Design artifacts such as typography, color palette, iconography, screen flows and motion. There was also the creation of artifacts for the user experience, such as 5W2H, wireframe and high fidelity prototype. The initial idea was to understand the problem and translate it into the design deliverables so that it meets the main needs of personalized service. We seek to create a flow of what would be the ideal interface of the MVP, so that with the fewest number of features delivered, the most value in terms of the journey. Thus, we simulate the Homepage, the interaction with the patient in the form of Chatbot to facilitate the collection of data and make the experience more humanized and later the visualization of the doctors match with the need for intelligent scheduling for the patient.
