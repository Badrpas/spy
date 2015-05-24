var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/schedule/:id', function(req, res, next) {
    res.send(req.params);
});

module.exports = router;
