'''
'''
'''
#########
# Tools #
#########
* Postman -                 https://www.getpostman.com/ 

* PyCharm Professional -    Free for students w/ Jet Brains Account 
                            https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows 


################
# Data Formats #
################
* Json
    . Can usually convert directly to a Python Dictionary
    . Most popular format for web-based API's and cross-application communication
    . Human readable (raw text)

* XML
    . Very structured
    . Can be validated with an XML Schema Definition File

* CSV
    . Very popular for data analytics due to human delivery
    . Older format so there are many tools built around csv processing
    
* Binary / Other
    . Can be much more efficient (e.g. compressed)
    . Must use application to read
    . e.g. Protobufs (https://developers.google.com/protocol-buffers/)
    





##################
# Python Clients #
##################
* Many data sites provide pre-built python "clients" that you can use to interact with their sites. 
* However, most sites are leaning towards just using RESTful APIs
* Sometimes these are provided as a convenience to developers, sometimes they may be required.  
* Includes many "client-side" object definitions out of the box (creates classes for you)

e.g. PyMongo:  https://api.mongodb.com/python/current/ (suggested)
     Google Maps: https://github.com/googlemaps/google-maps-services-python (convenience)
     Twitter: https://github.com/bear/python-twitter (optional / convenience)
     RethinkDB: https://www.rethinkdb.com/docs/install-drivers/python/ (required) (no real restful API available) (not http based)
     
     



EXAMPLE: python_client_example.py (Twitter API)













##############
RESTFul API's
##############
* Mainly for CRUD operations, but we all need a little RPC in our lives.
* Libraries available (e.g. Requests, urllib)
* Provides many advantages to the developer of the API (platform agnostic / loosely coupled)
* Documentation is provided via "Help" pages. (comes out of the box for some .NET API's)
e.g. http://ep4-uat.erecording.com/help


Usually rely on JSON In / JSON Out... but not required, and the "robust" ones will handle both JSON & XML.

HTTP Based


Uses following HTTP verbs: (SEE: http://www.restapitutorial.com/lessons/httpmethods.html)

GET (Read)
POST (Create)
PUT (Update / Replace) - Usually used for both replace / modify
PATCH (Update / Modify)
DELETE (Deletes)

Identifies "Resources" at a specific endpoint
e.g.

POST - Content to be created goes in the body of the request.
 e.g. http://www.example.com/customer will create a new customer resource
POST https://ep4-uat.erecording.com/api/v1/package
POST https://ep4-uat.erecording.com/api/v1/package/12354/document

PUT/PATCH http://www.example.com/customer/1234 will update customer with id 1234

POST / PUT / PATCH  will require json in the body of the request

GET / DELETE do not require anything in the body
GET http://www.example.com/customer/1234 will Read customer with ID 1234
GET https://ep4-uat.erecording.com/api/v1/package/48060



DELETE http://www.example.com/customer/1234 will Delete Customer with ID 1234

Can also access "nested" resources

GET http://www.example.com/customers/1234/order will get all of that customers orders

Eventually / Sometimes true rest may get broken and the uri becomes a "query string"
e.g. https://ep4-uat.erecording.com/api/v1/package/48055?returnFileType=pdf&embed=true&contentType=json&includeImage=true


There are GUIDELINES / Standard for exposing REST query structures:

OData is a very popular one: http://www.odata.org/
http://www.odata.org/getting-started/basic-tutorial/









################
HTTP Clients
################
* Sometimes consuming data via an http request is ALL done through a POST, with request details in the body
* This is more of an "HTTP Client", most would not refer to this as RESTful.

e.g. Solr / Elasticsearch
* POST https://webservices-uat.erecording.com/SearchService/api/v1/search... Body is :

{
    "SearchTerm":"676754",
    "SearchExactMatchOnly":false,
    "SearchType":"ep4.worklist",
    "StartDate":"1/1/2018",
    "EndDate":"7/29/2018",
    "CountyID":-1,
    "State2DigitAbbreviation":"ALL",
    "IncludeDownloaded":true,
    "IncludeFlagged":true,
    "SortBy":"LastModifiedDate",
    "SortByDirection":"desc",
    "Mode":"desc",
    "OrgID":66,
    "ServiceCode":"All",
    "HasMultipleOfficeRole":true,
    "OfficeIDs":[
        -1,
        ],
    "SearchFields":[
        "PackageName"
            ],
    "ResultFields":[
        "*"
    ],
    "Start":0,
    "Rows":100
}









######
SOAP
######
* Used by many older RPC style web services
* SEE: https://wiki.python.org/moin/WebServices
* Has the advantage of having pre-packaged methods (instead of just resources)
* Used more for "actions" than CRUD operations (e.g. Convert Speed Below)
* Very popular in B2B or G2B G2G


#########
# Tools #
#########
* SoapUI: https://www.soapui.org/downloads/soapui.html
*        * Pulling WSDL
         * Creating Mock Web Service
         * More and more rest resources.

'''