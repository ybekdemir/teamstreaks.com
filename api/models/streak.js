var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var StreakSchema = new Schema({
    team_id: { type: Schema.ObjectId, ref: 'Team', required: false },
    competition_id: { type: String, required: true },
    count: { type: String, required: true }
});


//Export model
module.exports = mongoose.model('Streak', StreakSchema);