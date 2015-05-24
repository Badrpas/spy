

YUI().use(
    'aui-io-request',
    'aui-scheduler',
    function(Y) {


        var events = [
            {
                content: 'AllDay',
                endDate: new Date(2013, 1, 5, 23, 59),
                startDate: new Date(2013, 1, 5, 0)
            }
        ];




        //var agendaView = new Y.SchedulerAgendaView();
        var dayView = new Y.SchedulerDayView();
        //var eventRecorder = new Y.SchedulerEventRecorder();
        var monthView = new Y.SchedulerMonthView();
        var weekView = new Y.SchedulerWeekView();

        var id = parseInt(window.location.pathname.substr(3));
        if (!id)
            id = 179576497;
        console.log(window.location.href);
        Y.io.request(
            '/api/schedule/'+id,
            {
                dataType: 'json',
                on: {
                    success: function() {
                        // gets the result of this asynchronous request
                        var data = this.get('responseData');

                        // iterates on all states to create a new <option> on that <select>
                        for (i = 0; i < data.length; i++) {
                            events.push({
                                //content: data[i].id,
                                startDate: new Date(data[i].start),
                                endDate: new Date(data[i].end)
                            });
                        }
                        console.log(events);

                        new Y.Scheduler(
                            {
                                activeView: weekView,
                                boundingBox: '#myScheduler',
                                //date: new Date(2013, 1, 4),
                                //eventRecorder: eventRecorder,
                                items: events,
                                render: true,
                                views: [dayView, weekView, monthView]
                            }
                        );


                    }
                }
            }
        );




    }
);