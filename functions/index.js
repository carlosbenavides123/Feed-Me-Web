/*eslint-disable */
const functions = require("firebase-functions");
const request = require("request-promise");
const cors = require('cors')({
  origin: true
});

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
  // example from docs
  //https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY
  cors(req, res, () => {});

  // take out the paramters
  const radius = req.query.radius;
  const query = req.query.query;
  const lat = req.query.lat;
  const long = req.query.long;

  if (lat == "" || long == "") {
    res.send("please allow your location!");
  }

  // api key
  const ApiKey = "AIzaSyAEAXEZ8Z-3ReCoSukBYutcDpzCvP9R-Jw";

  // base url (w/o inputs)
  const baseUrl =
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json?";

  // The API url to call
  // lat and long is required! (at least for now)
  let api = baseUrl + "location=" + lat + "," + long;

  if (radius) {
    api = api + "&radius=" + radius;
  }

  api = api + "&type=restaurant";

  if (query) {
    api = api + "&keyword=" + query;
  }

  api = api + "&key=" + ApiKey;

  makeApiRequest(api)
    .then(response => {
      // var result = retrieveRandom(response)
      var temp = response.results.length;
      let randIndex = Math.floor(Math.random() * temp);
      while (
        response["results"][randIndex]["opening_hours"]["open_now"] === false
      ) {
        randIndex = Math.floor(Math.random() * temp);
      }
      res.send(response["results"][randIndex]);
      return;
    })
    .catch(err => {
      res.status(500).send(err);
    });
});

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.helloWorld = functions.https.onRequest((request, response) => {
  response.send("Hello from Firebase!");
});