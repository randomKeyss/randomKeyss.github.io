var extra_head_html = typeof extra_head_html === 'undefined' ? "" : extra_head_html;
var extra_body_html = typeof extra_body_html === 'undefined' ? "" : extra_body_html;
var room_number = typeof room_number === 'undefined' ? -100 : room_number;
var dirs = ["left", "right", "up", "down"];
var arrow_existance = typeof arrow_existance === 'undefined' ? {} : arrow_existance; 

var default_arrow_directions = {left: room_number-1, right:room_number+1, up:room_number+10, down:room_number-10}
var arrow_links = typeof arrow_links === 'undefined' ? {} : arrow_links;
for(var i = 0; i < dirs.length;i++) {
    arrow_existance[dirs[i]] = typeof arrow_existance[dirs[i]] === 'undefined' ? true : arrow_existance[dirs[i]];
    arrow_links[dirs[i]] = typeof arrow_links[dirs[i]] === 'undefined' ? default_arrow_directions[dirs[i]] : arrow_links[dirs[i]];
}
var title_text = typeof title_text === 'undefined' ? `Internet Hotel - Room ${room_number}` : title_text;
var center_text = typeof center_text === 'undefined' ? "" : center_text;
var is_center_text = center_text !== "";
var base_html = `<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>${title_text}</title>
    <link rel='icon' href='room_resources/favicon/favicon.ico' type='image/x-icon/'>
    <link rel='icon' href='room_resources/favicon/faviconTransparent.ico' type='image/x-icon/'>
    <link rel="stylesheet" href="../base_styles.css">
    ${extra_head_html}
</head>

<body style="font-family: Verdana, sans-serif;padding-bottom: 5px;">
    ${is_center_text ? `<h1>${center_text}</h1>` : ""}
    ${arrow_existance.left ? `<svg id = "left_arrow" class = "arrow" width="75" height="150" viewBox="0 0 75 150" fill="none" xmlns="http://www.w3.org/2000/svg">
        <a href="../${arrow_links.left}/index.html">
            <path d="M75 150L0 75L75 0V150Z" fill="black"/>
        </a>
    </svg>` : ""}
        
    ${arrow_existance.right ? `<svg id = "right_arrow" class = "arrow" width="75" height="150" viewBox="0 0 75 150" fill="none" xmlns="http://www.w3.org/2000/svg">
        <a href="../${arrow_links.right}/index.html">
            <path d="M0 0L75 75L0 150V0Z" fill="black"/>
        </a>
    </svg>` : ""}
    
    ${arrow_existance.up ? `<svg id = "up_arrow" class = "arrow" width="150" height="75" viewBox="0 0 150 75" fill="none" xmlns="http://www.w3.org/2000/svg">
        <a href="../${arrow_links.up}/index.html">
            <path d="M150 75L75 0L0 75H150Z" fill="black"/>
        </a>
    </svg>` : ""}
    
    ${arrow_existance.down ? `<svg id = "down_arrow" class = "arrow" width="150" height="75" viewBox="0 0 150 75" fill="none" xmlns="http://www.w3.org/2000/svg">
        <a href="../${arrow_links.down}/index.html">
            <path d="M0 0L75 75L150 0H0Z" fill="black"/>
        </a>
    </svg>` : ""}
    
    ${extra_head_html}

    <script>

    </script>


</body>
<html></html>`

document.open("text/html", "replace");
document.write(base_html);  // htmlCode is the variable you called newDocument
document.close();


    document.addEventListener("keyup", (e) => {
        console.log(e.keyCode);
            switch (e.keyCode) {
                case 37:
                    if(document.getElementById("left_arrow")){
                        var new_href = document.getElementById("left_arrow").firstElementChild.getAttribute('href');
                        window.location.href = new_href;
                    }
                    break;

                case 39:
                    if(document.getElementById("right_arrow")){
                        var new_href = document.getElementById("right_arrow").firstElementChild.getAttribute('href');
                        window.location.href = new_href;
                    }
                    break;
                case 38:
                    if(document.getElementById("up_arrow")){
                        var new_href = document.getElementById("up_arrow").firstElementChild.getAttribute('href');
                        window.location.href = new_href;
                    }
                    break;
                case 40:
                    if(document.getElementById("down_arrow")){
                        var new_href = document.getElementById("down_arrow").firstElementChild.getAttribute('href');
                        window.location.href = new_href;
                    }
                    break;
            }
            e.preventDefault();
        });