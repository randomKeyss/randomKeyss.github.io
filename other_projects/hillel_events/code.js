/*function successFunc(data) {
    data = data.sheet1;
    for(var i = 0; i<data.length;i++){
        if(data[i]){
          var b = document.createElement("button");
            b.innerText = data[i].subject.split().join("&nbsp");
            b.setAttribute("onclick", `location.href='${data[i].zoomLink}'`);
            b.setAttribute("type", "button");
          document.getElementsByClassName("grid-container")[0].appendChild(b);
        }
    }
}

var request = new XMLHttpRequest();
request.open('GET', 'https://v2-api.sheety.co/b0b9b67f97e5f0def33bc752f16ead7d/ptVirtualTutoring/sheet1', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var data = JSON.parse(request.responseText);
    successFunc(data);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};

request.send();*/
