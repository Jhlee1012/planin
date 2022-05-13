let calendar = null;
window.onload = onLoadActions;

function onLoadActions (){
    drawCalendar();
}

//캘린더 옵션
function drawCalendar() {
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
                title : "디폴트 일정1",
                start : "2022-05-14 12:00:00",
                end : "2022-05-14 13:00:00"
            },
            {
                title : "디폴트 일정2",
                start : "2022-05-15 11:00:00",
                end : "2022-05-14 15:00:00"
            },
        ],
        // 신규 이벤트 생성 
        selectable: true,
        selectMirror: true,
        select: function(arg) {
            let title = prompt('일정 내용:');
            if (title) {
            calendar.addEvent({
                title: title,
                start: arg.start,
                end: arg.end,
                allDay: arg.allDay
            })
            }
            calendar.unselect()
        },
        eventClick: function(arg) {
            if (confirm('이벤트를 삭제하시겠습니까?')) {
            arg.event.remove()
            }
        },
        editable: true,
        
    });

    calendar.render();
}

//일정 제출하기
async function sendAllEvents(){
    let allEvents = calendar.getEvents();
    
    let payload = {
        events: [],
    };
    allEvents.forEach(eventData => {
        console.log(eventData.title);
        console.log(eventData.start);
        console.log(eventData.end);
        payload.events.push({
            "title" : eventData.title,
            "start": eventData.start,
            "end" : eventData.end,
        })
    });

    //받은 데이터 묶음 장고 모델로 보내기
    let result = await eventsToModel(payload);
    
    if (!result){
        alert("일정 제출에 실패했습니다.");
        return;
    }
    alert('일정 제출이 완료되었습니다.');
    
    //제출하기 버튼이 수정하기로 변하기 
    // const element = document.getElementById("data-upload");
    // element.innerHTML = "수정하기";

}

async function eventsToModel(payload){
    let response = await fetch('/calendar/save-events/',{
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
        }
    });
    if (response.status != 200){
        return false;
    }
    return true;
}

function getCsrfToken() {
    return document.cookie.split("&")
        .find(item => item.includes("csrftoken"))
        .split("=")[1];
}

// 일정 보여주기 
 // 버튼이 선택이 되면
function showCalendarof(){
    // 모델에서 이진현의 일정 가져오기 -딕셔너리 리스트 
    getEventList().then(eventList => {
    // getEventList().then(function logEvent(eventList) {
        for (const e of eventList.events) {
            console.log(e);
            calendar.addEvent(e);
        }
    });
    // 캘린더 위에 이진현의 일정 보여주기 - 각 딕셔너리를 이벤트에 요소로 하나씩 추가 
}
// 일정을 가져오고
// 일정을 title , start, end 형태로 변환 
async function getEventList(){
    let response = await fetch("/calendar/load-events/");
    if (response.status == 200){
        let responseBody = await response.json();
        console.log(responseBody);
        return responseBody;
    }
}
// 
    // for eventEl of eventlist 
    //     start: eventEl.start_date,
    //     end: eventEl.end_date,
    //     calendar.addEvent({
    
   
