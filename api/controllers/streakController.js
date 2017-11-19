var Streak = require('../models/streak');


exports.get_streak = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaks').find().toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

exports.get_all_streak = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaks').find({ 'streak_type_id': parseInt(req.params.streaktype) }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

exports.get_streak_by_tournament = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaks').find({
            'streak_type_id': parseInt(req.params.streaktype),
            'competition_id': parseInt(req.params.tournament)
        }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};