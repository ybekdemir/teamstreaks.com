var Streak = require('../models/streak');


exports.get_streak = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaks').find().sort({ 'count': -1 }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

exports.get_all_streak = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaks').find({ 'streak_type_id': parseInt(req.params.streaktype) })
            .sort({ 'count': -1 }).toArray(function(err, result) {
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
        }).sort({ 'count': -1 }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};