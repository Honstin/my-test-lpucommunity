var startdelay 		= 2; 		// START SCROLLING DELAY IN SECONDS
var scrollspeed		= 1.1;		// ADJUST SCROLL SPEED
var scrollwind		= 1;		// FRAME START ADJUST
var speedjump		= 30;		// ADJUST SCROLL JUMPING = RANGE 20 TO 40
var nextdelay		= 0; 		// SECOND SCROLL DELAY IN SECONDS 0 = QUICKEST
var topspace		= "2px";	// TOP SPACING FIRST TIME SCROLLING
var frameheight		= 176;		// IF YOU RESIZE THE CSS HEIGHT, EDIT THIS HEIGHT TO MATCH


current = (scrollspeed);

function HeightData() {
    // height of member scroller frame
    AreaHeight = dataobj.offsetHeight;
    // height of HoF scroller frame
    AreaHeight1 = dataobj1.offsetHeight;
    if (AreaHeight===0) {
        setTimeout("HeightData()",( startdelay * 1000 ));
    }
    else {
        ScrollNewMemberDiv();
    }
    if (AreaHeight1===0) {
        setTimeout("HeightData()",( startdelay * 1000));
    }
    else {
        ScrollHoFDiv();
    }
}

// Triggers by <body onLoad="ScrollStart"> in base.html
function ScrollStart() {
    // Controls latest member scroller
    dataobj=document.all? document.all.NewMemberDiv : document.getElementById("NewMemberDiv");
    dataobj.style.top=topspace;
    // Controls latest HoF entry scroller
    dataobj1=document.all? document.all.NewHoFDiv : document.getElementById("NewHoFDiv");
    dataobj1=style.top=topspace;
    setTimeout("HeightData()",( startdelay * 1000 ));
}

function ScrollNewMemberDiv() {
    dataobj.style.top=scrollwind+'px';
    scrollwind-=scrollspeed;
    if (parseInt(dataobj.style.top)<AreaHeight*(-1)) {
        dataobj.style.top=frameheight+'px';
        scrollwind=frameheight;
        setTimeout("ScrollNewMemberDiv()",( nextdelay * 1000 ));
    } else {
        setTimeout("ScrollNewMemberDiv()",speedjump)
    }
}

function ScrollHoFDiv() {
    dataobj1.style.top=scrollwind+'px';
    scrollwind-=scrollspeed;
    if (parseInt(dataobj1.style.top)<AreaHeight1*(-1)) {
        dataobj1.style.top=frameheight+'px';
        scrollwind=frameheight;
        setTimeout("ScrollHoFDiv()", ( nextdelay * 1000));
    } else {
        setTimeout("ScrollHoFDiv()",speedjump)
    }
}