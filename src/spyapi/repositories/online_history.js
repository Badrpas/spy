var mysql = require('mysql');

var connectionConfig = require('./connection_config.json');

var connection = mysql.createConnection(connectionConfig);
var repository = function (){

    this.getHistory = function (id, callback) {
        connection.query('select * from online_history where user_id = ?;', [id], function (err, rows, fields) {
            if (err) throw err;
            callback(rows);
        });
    },

    this.getSchedule = function (id, callback) {
        this.getHistory(id, function(rows) {
            var onlineTimes = [];
            var start, end;
            var idCounter = 0;

            for ( var i = 0; i < rows.length; i++) {
                if( rows[i].online_status_change == 1) {
                    start = rows[i];
                    end = null;
                } else {
                    end = rows[i];
                }
                if (start && end) {
                    onlineTimes.push( {
                        id: idCounter++,
                        start: start.ondate,
                        end: end.ondate
                    });
                    start = end = null;
                }
            }
            callback(onlineTimes);
        });
    }

};



module.exports = new repository();