var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var TeamSchema = new Schema({
    name: { type: String, required: false },
    short_name: { type: String, required: false },
    competition_id: { type: String, required: false }
});


//Export model
module.exports = mongoose.model('Team', TeamSchema);