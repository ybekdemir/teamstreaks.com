var express = require('express');

var router = express.Router();

// Require controller modules
var team_controller = require('../controllers/teamController');
var data_controller = require('../controllers/dataController');
var streak_controller = require('../controllers/streakController');


router.get('/team/', team_controller.get_all_team);

router.get('/team/all', team_controller.get_all_team);

router.get('/team/:id', team_controller.get_team_by_id);

router.get('/streak', streak_controller.get_streak);

router.get('/streak/:streaktype', streak_controller.get_all_streak);

router.get('/streak/:streaktype/:tournament', streak_controller.get_streak_by_tournament);

router.get('/data/bettypes', data_controller.get_bet_types);

router.get('/data/:bettypes/streaktypes', data_controller.get_streak_types);

router.get('/data/tournaments', data_controller.get_tournaments);





module.exports = router;