/*eslint-disable */
const functions = require('firebase-functions');
const request = require('request-promise');

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
    // TODO: process the request, extract parameters, authenticate the user etc

    // The API url to call - edit this
    const url = `https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAEAXEZ8Z-3ReCoSukBYutcDpzCvP9R-Jw`;

    makeApiRequest(url)
        .then(response => {
            res.send(response);
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