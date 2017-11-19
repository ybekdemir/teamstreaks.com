exports.get_bet_types = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('bettypes').find().sort({ 'uid': 1 }).toArray(function(err, bettypes) {
            if (err) throw err
            db.collection('streaktypes').find().sort({ 'bet_type_id': 1 }).toArray(function(err, streaktypes) {
                if (err) throw err

                res.json({ 'bettypes': bettypes, 'streaktypes': streaktypes })
            })
        })



    })
};

exports.get_streak_types = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('streaktypes').find({ 'bet_type_id': parseInt(req.params.bettypes) })
            .sort({ 'bet_type_id': 1 }).toArray(function(err, result) {
                if (err) throw err

                res.json(result)
            })
    })
};

exports.get_tournaments = function(req, res) {
    var MongoClient = require('mongodb').MongoClient

    MongoClient.connect(mongo_url, function(err, db) {
        if (err) throw err

        db.collection('competitions').find({}).sort({ 'league': 1 }).toArray(function(err, result) {
            if (err) throw err

            res.json(result)
        })
    })
};