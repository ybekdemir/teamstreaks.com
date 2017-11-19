var Team = require('../models/team');
var ObjectID = require('mongodb').ObjectID;


// Display team details
exports.get_all_team = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('teams').find().toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

// Display team details
exports.get_team_by_id = function(req, res) {
    var MongoClient = require('mongodb').MongoClient


    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('teams').find({ '_id': ObjectID(req.params.id) }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};