exports.get_bet_types = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('bettypes').find().toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

exports.get_streak_types = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaktypes').find({ 'bet_type_id': parseInt(req.params.bettypes) }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};

exports.get_tournaments = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('competitions').find({}).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};