'use strict';

const request = require('request');
let cheerio = require('cheerio');
const R = require('ramda');

// Todos
// - Store the data into a Firebase database
// - Make requests to multiple different urls and cycle through the `?start=` query to get everything
// - Cycle through a list of guy feiri restaurants (businessURL)s

let success = true;

// this is the number of pagination steps we'd like to take
// TODO: make logic that auto-cycles through all the pages until
//       the pages are finished (it already boots out tho, so you could)
//       just make this number really big to achieve the same thing
const numberOfPages = 2;

// the important identifying aspect of a yelp URL
const businessURL = 'byways-cafe-portland';


function callback(error, response, body) {
  if (!error && response.statusCode == 200) {
    // load the body thru cheerio
    let $ = cheerio.load(body);

    if ($('.review-content .i-stars').length !== 0) {
      let storeArr = []

      // for each of the reviews on the page get stuff
      for (let i = 0; i < $('.review-content .i-stars').length; i++) {
        let ReviewContentArr = []

        // this goes into the review and gets each part of the
        // review, line by line, and adds it into an array
        // seperated by line breaks
        R.prop(i, $('.review-content p')).children.map((x) => {
          if (x.data !== undefined) {
            ReviewContentArr.push(x.data)
          }});

        // Now take all data per review and store them in an array that looks like
        // [ReviewDate, ReviewRating, ReviewContent]
        storeArr.push([

          R.prop(i, $('.review-content .rating-qualifier')).children[0].data.trim(), //date
          R.prop(i, $('.review-content .i-stars')).attribs.title[0], //rating
          ReviewContentArr //review
        ])
      }

      // console.log(storeArr.length);
      console.log(storeArr);
    }
    else {
      success = false;
    }
  }
}

let startNum = 0

// this is to cycle through given the number of pages set above
for (let i = 0; i < numberOfPages; i++) {
  if (success !== false) {
    // this will add the pagination `?start=` param
    startNum =  i * 20
    // this makes the request with the given params
    request({
      url: `https://www.yelp.com/biz/` + businessURL + `?start=` + startNum + `&sort_by=date_desc`
    }, callback)
  }
}
