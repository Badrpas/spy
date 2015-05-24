var express = require('express');
var router = express.Router();

var repository = require('../repositories/online_history')

/* GET users listing. */
router.get('/history/:id', function(req, res, next) {
    var rows = repository.getHistory(req.params.id, function(rows){
        res.send(rows);
    });
});
router.get('/schedule/:id', function(req, res, next) {
    var rows = repository.getSchedule(req.params.id, function(onlines){
        res.send(onlines);
    });
});

module.exports = router;
