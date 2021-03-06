let calendar;
let dragPalette;

window.onload = () => {
    let calendarEl = document.getElementById('calendar');
    
    calendar = new FullCalendar.Calendar(calendarEl, {
        scrollTime: '08:00:00',
        businessHours : false,
        eventConstraint: null, 
        expandRows: true,
        longPressDelay: 1000,
        slotMinTime: '00:00',
        slotMaxTime: '24:00',
        selectable: true,
        dragScroll: true,
        editable: true,
        droppable: true,
        themeSystem: 'bootstrap5',
        //timeZone: 'GMT+9',
        initialView: 'timeGridWeek',
        firstDay: (new Date().getDay()), // duratin one week ?
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'today',
        },
        events : [
            {
                title: 'testEvent',
                start: '2022-05-8T10:00:00',
                end: '2022-05-8T12:00:00'
              },

        ],
        
        //일정 삭제 버튼 
        // eventDidMount: function(info) {
        //     let eventElement = document.querySelector('fc-timegrid-event');
        //     let mydiv = document.createElement('div');
        //     mydiv.className = 'removebtn';
        //     eventElement.appendChild(mydiv);
        //     console.log(eventElement)
        //   },
    });

    calendar.render();

    // 신규 이벤트 세팅 - 외부에서 드래그 앤 드롭
    let eventEl = document.getElementById('external-events-list');
    dragPalette = new FullCalendar.Draggable(eventEl, {
        itemSelector: '.fc-event',
        eventData: function(eventEl) {
            return {
                title: eventEl.innerText.trim(),
                duration: '01:00',
            }
        }
    });
    
    // dragPalette.render();

    function setDuration (eventPalette){
        // let EventPalette = eventEl
        // if eventEl.eventData.duration = 
    }


    // AllDay 이벤트 세팅 - 외부에서 드래그 앤 드롭
   
    let eventElAllDay = document.getElementById('external-events-list-all-day');
    dragPaletteAllDay = new FullCalendar.Draggable(eventElAllDay, {
        itemSelector: '.fc-event',
        eventData: function(eventElAllDay) {
            return {
                title: eventElAllDay.innerText.trim(),
                allDay: true,
            }
        }
    });
    
}


function showCalendarof(){
    let showcalendar_my = document.getElementById('showcalendar_my');
   // let showcalendar_co = document.getElementById('showcalendar_co');
   // let showcalendar_B = document.getElementById('showcalendar_B');
        if (showcalendar_my.value== 'on') {
        console.log(showcalendar_my.value)
        calendar.addEvent({
            title : '공통 일정 입니다',
            start : '2022-05-8T16:00:00', 
            end : '2022-05-8T18:00:00',
        })
    };
}


function promptBasedEvent(){
    let start = prompt("start: YYYY-MM-DD");
    let end = prompt("end: YYYY-MM-DD");
    let display = prompt("event data");
    addEventAllDay(start, end, display);
}


// addEventAllDay("2022-05-02", "2022-05-04", "qwer");
// addEventAllDay("2022-05-02", "2022-05-04", "asdf");
// addEventAllDay("2022-05-02", "2022-05-04", "zxcv");

let id = 0;
function addEventAllDay(start, end, display){
    calendar.addEvent({
        title: display,
        start: start,
        end: end,
        allDay: true,
        id: id.toString()
    });

    id += 1;
}

// 업무시간 설정 

function buisnessHoursOnOff(){
    let buisnessHoursConfig = {
        startTime: '09:00',
        endTime: '21:00',
        daysOfWeek: [ 1, 2, 3, 4, 5 ]
      }
    let buisnessHoursSwitch = document.getElementById('businessHours');
    if (buisnessHoursSwitch.checked) {
        calendar.setOption('businessHours', buisnessHoursConfig);
        calendar.setOption('eventConstraint',"businessHours");
        removeEventsInBuisness();
    } else {
        calendar.setOption('businessHours', false);
        calendar.setOption('eventConstraint',null);
        
    }
}
// 업무시간 설정했을때, 업무시간 전에 이미 설정된 이벤트 제거

function removeEventsInBuisness() {

    let allEvents = calendar.getEvents();
    allEvents.forEach(e => {
        let startday = e.start.getDay()
        let endday = e.end.getDay()
        let starthour = e.start.toString().substr(16,5)
        let endhour = e.end.toString().substr(16,5)
        let businessHours = calendar.getOption('businessHours')

        //업무시간의 요일 리스트에 이벤트의 시작 시간의 요일이 존재하지 않으면
        if (!businessHours.daysOfWeek.includes(startday) ||
        //업무시간의 요일 리스트에 이벤트의 끝 시간의 요일이 존재하지 않으면 
         !businessHours.daysOfWeek.includes(endday) ||
        //요일에는 포함, 업무시간의 시작시간과 끝 시간 내에 이벤트가 존재하지 않으면
        businessHours.startTime > starthour ||
        businessHours.endTime < endhour 
         ){
        //제거
            e.remove();
        }

     });
 }

//일정조정기간

let new_startDate = document.getElementById('adjustable-date-start');
let new_endDate = document.getElementById('adjustable-date-end');

function setBackgroundTime(){
        calendar.setOption('firstDay',Date(new_startDate).getDay());
}

