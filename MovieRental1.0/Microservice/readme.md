# Random Number Generator Microservice
Here is a small microservice which generates a random number. Please follow the instructions below to run, and how to make calls.

## Background
This microservice implements a RESTful API that allows clients to send requests and receive responses in JSON format. The client can request and recieve randomly generated integers on a given range

## Prerequisites

- Node.js

## Installation

Instructions for setting up the project. Windows commands below:

1. Clone the repository:
    ```cmd
    git clone https://github.com/mv805/random_number_microservice_361.git
    ```
2. Install dependencies:
    ```cmd
    npm install
    ```
4. Start the server:
    ```cmd
    npm start
    ```

## Running the Sample Application
Run this sample application to make sure you are setup correctly and to observe an example of how to make calls. 

>**Note:** Make sure the server is running in parallel before running the program.

Run this command from the command line from the root of the folder.
```bash
ts-node sampleApp.ts
```    
You should see output to the command line like the following:
```bash
Hello, here is your random integer between 1 and 1000: 671
Hello, here is your random integer between 100 and 10000: 3554
```
## API Reference
In a real scenario, the API would be running from a webserver, but for the purposes of the learning requirements, this service will just run of the users local machine. 

### Request
There are two ways to make a call to the microservice

1. **Random Integer between 1 and a given Max value:** Supply a single max integer limiter to recieve an integer between 1 and the given max. 
```
http://localhost:<Your backend port here>/api/max/<Max integer desired here>
```

**Example:** The given call below will generate an integer between 1 and 1000, assuming the port is 3050.
```
http://localhost:3050/api/random/max=1000
```

2. **Random Integer between a given Max and Min:** You can supply two queries to the address to define a maximum and minum value. The API will return a random integer in a range **inclusive** of the minimum and maximum.
```
http://localhost:<Your backend port here>/api/random/range?min=<Minimum Int>&max=<Maximum Int>
```
**Example:** The given call below will generate an integer between 100 and 10,000, assuming the port is 3050.
```
http://localhost:3050/api/random/range?min=100&max=10000
```
### Response
All calls shall return the data in JSON format as shown:

```json
{
    "randomNumber": <Integer>
}
```
## UML Sequence Diagram
Below is an example of a sequence of a call for the max integer random generation route
![Random Number Generator UML](./UML.PNG)