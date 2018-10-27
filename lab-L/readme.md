# Web and API's

## Goals

- Use Squidex to create an API
- Create a schema
- Demonstrate the different apu methods

## Setup you environment

The environment will use an open source project [Squidex](https://squidex.io/) to create an api. Squidex is a headless content management system. It allows you to create custom content definitions (schema) and it will create an api that allows you to create, retrieve, update and delete (CRUD) your custom content.

To start the environment

```
PS C:\ist346-labs> docker-compose up -d
```

Give it a minute and you should be able to go to (http://localhost/)[http://localhost] and see the Squidex login screen.

Login to Squidex using **admin@example.com** and **mySecret123!**. You will then come to the tutorial. Walk through the tutorial to understand the different features of Squidex. Once the tutorial is complete you should end up the screen shown below.

![Dashboard](assets/dashboard.png)

To explain what an api is lets create a new app in Squidex. Click on the **New App** button. And create a new app called **my-beer-app**

![Beer App Create](assets/beer-app.png)

Squidex allows you to define content based on schemas. To create a new schema for our beer app, click the New Schema button on the my-beer-app dashboard.

![New Schema Button](assets/new-shema.png)

When the dialog pops up enter the name **beers**

Create the fields required for our beers. 

- name (String Field)
- brewery (String Field)
- location (Geolocation field)
- type (String Field)
- calories (Number Field)

Once all of the fields are created, click on Published (so it turns green) in the upper right corner.

See the image below

![Beer Fields](assets/fields.png)

Now we can add beers to our content. You can do this by using the Content button on the left. Choose the beers schema, then click the green **new** button in the upper right corner.

Fill out the form with your favorite beer. Like the one below, then click **Save and Publish** in the upper right.

![Dogfish Head 60 Min IPA](assets/beer-example.png)

But we don't want everyone to use the admin interface to access our data! We need to expose and API (Application Programming Interface). To do this most applications use the [Oauth2](https://oauth.net/2/) industry-standard protocol. This requires a client id and a client secret for authentication to and API. We can generate one of those with the admin interface.

Click on the settings gear in the left menu. Then enter test-client for the name and click **Add Client** you should end up with something similar to the image below.

![Test Client](assets/client-example.png)

To access the api you will need to generate an access token, this can also be done with curl. For our case we are just going to generate it with the user interface. To generate a new token, click the **Create Token** button. It will show a modal containing your access token, copy and past this token into a blank Notepad or TextEdit document for later use.

And example looks like this:

```
Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkxRkRENEVCRDYwNjMxNURFREI4MENEMDkzMERFRkZBMjFEREE2NkIiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJrZjNVNjlZR01WM3R1QXpRa3czdi1pSGRwbXMifQ.eyJuYmYiOjE1NDA2NTI0MzQsImV4cCI6MTU0MzI0NDQzNCwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdC9pZGVudGl0eS1zZXJ2ZXIiLCJhdWQiOlsiaHR0cDovL2xvY2FsaG9zdC9pZGVudGl0eS1zZXJ2ZXIvcmVzb3VyY2VzIiwic3F1aWRleC1hcGkiXSwiY2xpZW50X2lkIjoibXktYmVlci1hcHA6dGVzdC1jbGllbnQiLCJzY29wZSI6WyJzcXVpZGV4LWFwaSJdfQ.wkPN_hl4ftxUPdHdXDh0Yqe7Vl5UIiDYwCuoogG6pzg5WYesWB7DoRxjG22xk3RJl5Wk7ihOyO2GA3QG9dClrk_8Ko_dDVaYOB0AZtikNw5AVXg7vAm0FmApMm9O02gSZqMQ8VQVUIETl64CB_X-5pIlU0_eGnRlWatkWcdLfW9P_Ex9-msMGCfOw0npHGUoLRbZicBVPb37l_n_Zmh2hJBeoJJUKAFLGzkzAQOR1y0xRMwz4W1pGFxPU9-dGSB7nSMNALg55AAoqvJOtrQq1il6qu1Qu681Dvg75BkyRFCkCIn3oSeolksl1SxZwa0OXQlD6mZDTNWTjJXZfAWV_g
```

Now lets take a look at the API Squidex has created for us click the API button on the left, then choose Swagger.

Swagger show us the different endpoints to interact with our content. To use our API we need your access token to interact with your api through the HTTP protocol.

REST API's can be interacted with by using HTTP verbs. Each verb is meant to perform a different action. The 4 verbs we will be using are GET, POST, PUT, and DELETE.

- GET: Retrieves or gets data
- POST: Creates data
- PUT: Updates data
- DELETE: Deletes data

Using the simple **curl** command you can interact the API to manage the data about beers. **Make sure you enter the access token you retrieved where indicated.**

You can view the different api urls and what they return by looking at the documentation. [http://localhost/api/content/my-beer-app/docs](http://localhost/api/content/my-beer-app/docs)

First we need to know what beers are available.

```
PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -X GET 'http://squidex_squidex/api/content/my-beer-app/beers' -H 'Authorization: [YOUR_ACCESS_TOKEN]'
```
 Using the example access token:

 ```
 PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -v -X GET http://squidex_squidex/api/content/my-beer-app/beers -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkxRkRENEVCRDYwNjMxNURFREI4MENEMDkzMERFRkZBMjFEREE2NkIiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJrZjNVNjlZR01WM3R1QXpRa3czdi1pSGRwbXMifQ.eyJuYmYiOjE1NDA2NTI0MzQsImV4cCI6MTU0MzI0NDQzNCwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdC9pZGVudGl0eS1zZXJ2ZXIiLCJhdWQiOlsiaHR0cDovL2xvY2FsaG9zdC9pZGVudGl0eS1zZXJ2ZXIvcmVzb3VyY2VzIiwic3F1aWRleC1hcGkiXSwiY2xpZW50X2lkIjoibXktYmVlci1hcHA6dGVzdC1jbGllbnQiLCJzY29wZSI6WyJzcXVpZGV4LWFwaSJdfQ.wkPN_hl4ftxUPdHdXDh0Yqe7Vl5UIiDYwCuoogG6pzg5WYesWB7DoRxjG22xk3RJl5Wk7ihOyO2GA3QG9dClrk_8Ko_dDVaYOB0AZtikNw5AVXg7vAm0FmApMm9O02gSZqMQ8VQVUIETl64CB_X-5pIlU0_eGnRlWatkWcdLfW9P_Ex9-msMGCfOw0npHGUoLRbZicBVPb37l_n_Zmh2hJBeoJJUKAFLGzkzAQOR1y0xRMwz4W1pGFxPU9-dGSB7nSMNALg55AAoqvJOtrQq1il6qu1Qu681Dvg75BkyRFCkCIn3oSeolksl1SxZwa0OXQlD6mZDTNWTjJXZfAWV_g"
 ```

 If everything works you should see similar output

 ```
>
< HTTP/1.1 200 OK
< Date: Sat, 27 Oct 2018 15:02:37 GMT
< Content-Type: application/json; charset=utf-8
< Transfer-Encoding: chunked
< ETag: 6TzYcxQgk4TPmwDeG90mjnjq7h+R38Nf5JDnQ8eLgh4=
< Surrogate-Key: 1acf007c-290b-4f82-832b-5804d1749a88
<
{ [474 bytes data]
100   467    0   467    0     0  33565      0 --:--:-- --:--:-- --:--:-- 35923
* Connection #0 to host squidex_squidex left intact
{"total":1,"items":[{"id":"1acf007c-290b-4f82-832b-5804d1749a88","createdBy":"subject:5bd366507c06f60001f0b309","lastModifiedBy":"subject:5bd366507c06f60001f0b309","data":{"name":{"iv":"60 Minute IPA"},"brewery":{"iv":"Dogfish Head"},"location":{"iv":{"latitude":38.7433406,"longitude":-75.3390347}},"type":{"iv":"IPA"},"calories":{"iv":150}},"isPending":false,"created":"2018-10-26T22:39:56Z","lastModified":"2018-10-26T22:39:56Z","status":"Published","version":1}]}
 ```

 At the bottom is the json formatted text that show the results of our query. We can also query for individual items by using the id provided in our results: In the example the id is **1acf007c-290b-4f82-832b-5804d1749a88**, yours will be different.

 To get a single item (the -v is removed and the -s is added for less verbose output):

 ```
 PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X GET http://squidex_squidex/api/content/my-beer-app/beers/1acf007c-290b-4f82-832b-5804d1749a88 -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]"
 ```

 We can also create a new beer by using the post command.

 ```
 PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X POST http://squidex_squidex/api/content/my-beer-app/beers?publish=true -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]" --data '{\"name\": {\"iv\": \"Summer Ale\"},\"brewery\": {\"iv\": \"Samuel Adams\"},\"location\": {\"iv\": {\"latitude\": -90,\"longitude\": -180}},\"type\": {\"iv\": \"American Pale Wheat Ale\"},\"calories\": {\"iv\": 150}}'
 ```
 
 If it works you will see the json output of the newly created beer. Copy the id for this beer for later. To see how many we have now just use the list command again.

 ```
 PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X GET http://squidex_squidex/api/content/my-beer-app/beers -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]"
 ```

You should see in the output that there are now 2 items!

You can also update and item by using the PUT verb, Update the one you just entered with the proper latitude and longitude for Boston, you will need the id copied from the create command

```
PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X PUT http://squidex_squidex/api/content/my-beer-app/beers/[ID_FROM_CREATE_COMMAND] -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]" --data '{\"name\": {\"iv\": \"Summer Ale\"},\"brewery\": {\"iv\": \"Samuel Adams\"},\"location\": {\"iv\": {\"latitude\": 42.3146488,\"longitude\": -71.1051005}},\"type\": {\"iv\": \"American Pale Wheat Ale\"},\"calories\": {\"iv\": 150}}'
```

In the results you should see that the latitude and longitude are updated.

To remove and item you will use the DELETE verb.

```
PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X DELETE http://squidex_squidex/api/content/my-beer-app/beers/[ID_FROM_CREATE_COMMAND] -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]"
```

If all goes well nothing actually, but you can verify by using the list command again

```
PS C:\ist346-labs> docker exec lab-l_curl-client_1 curl -s -X GET http://squidex_squidex/api/content/my-beer-app/beers -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: [YOUR_ACCESS_TOKEN]"
```

You should see that there is only 1 item now, the new one was removed.

Even though you are using **curl** this is exactly how other application and clients interact with web apis.


