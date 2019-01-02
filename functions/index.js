/*eslint-disable */
const functions = require("firebase-functions");
const request = require("request-promise");
const cors = require("cors")({
  origin: true
});

var randomFood = [
  "burger",
  "chicken",
  "pizza",
  "bbq",
  "vietnamese",
  "chinese",
  "korean",
  "pho",
  "mexican",
  "burrito"
];

/**
 * Makes a GET request to given URL with the access token
 */
function makeApiRequest(url) {
  return request.get({
    url: url,
    transform: body => JSON.parse(body)
  });
}

// Our test function
exports.testApi = functions.https.onRequest((req, res) => {
  var query;
  var radius;

  // example from docs
  //https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY
  if (req.query.radius.length < 3) {
    query = randomFood[Math.floor(Math.random() * randomFood.length)];
  } else {
    query = req.query.radius;
  }

  if (req.query.radius.length < 3) {
    radius = 300;
  } else {
    radius = req.query.radius;
  }
  // take out the paramters
  // var radius = 300;
  // var query = randomFood[Math.floor(Math.random() * randomFood.length)];
  let lat = req.query.lat;
  let long = req.query.long;

  cors(req, res, () => {});

  if (lat == "" || long == "") {
    res.send("please allow your location!");
  }

  // api key
  let ApiKey = "AIzaSyAEAXEZ8Z-3ReCoSukBYutcDpzCvP9R-Jw";

  // base url (w/o inputs)
  let baseUrl = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?";

  // The API url to call
  // lat and long is required! (at least for now)
  var api = baseUrl + "location=" + lat + "," + long;

  api = api + "&radius=" + radius;

  api = api + "&type=restaurant";

  api = api + "&keyword=" + query;

  api = api + "&key=" + ApiKey;

  makeApiRequest(api)
    .then(response => {
      var temp = response.results.length;
      var randIndex = Math.floor(Math.random() * temp);
      while (
        response["results"][randIndex]["opening_hours"]["open_now"] === false
      ) {
        randIndex = Math.floor(Math.random() * temp);
      }
      res.send(response["results"][randIndex]);
      return;
    })
    .catch(err => {
      errormsg = {
        message: "oops"
      };
      res.status(500).send(errormsg);
    });
});

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.helloWorld = functions.https.onRequest((request, response) => {
  response.send("Hello from Firebase!");
});
