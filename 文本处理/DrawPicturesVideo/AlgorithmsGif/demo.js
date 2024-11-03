var S;
var Coordinate_y = 40;
var Rect = new Array();
var track_insert = new Array();
var cons = 0;
var cnt;

function func() {
//获取字符串，存入数组
    S = document.getElementsByName("string")[0].value.split("");
//依据数组元素，完成对象数组
    for (var i = 0; i < S.length; i++) {
        var rect = {
            x: 30 * i,
            y: Coordinate_y,
            target_x: 30 * i,
            target_y: Coordinate_y,
            text: S[i]
        }
        Rect.push(rect);
    }
    insertSort(S);
}

function insertSort(arr) {
    var i = 1,
    j, key, temp;
    for (; i < arr.length; i++) {
        j = i;
        key = arr[i];
        while (--j >= 0) {
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                arr[j] = key;
//当数据有交换时，记录下标
                track_insert.push(j);
            } else {
                break;
            }
        }
    }
}
//坐标更新
function update() {
    if (cons > track_insert.length) {
        return;
    }
    if (cons == 0) {
        cnt = track_insert[cons];
        Rect[cnt].target_x = Rect[cnt + 1].x;
        Rect[cnt + 1].target_x = Rect[cnt].x;
        cons += 1;
        console.log(cnt);
    }
    if (Rect[cnt].x == Rect[cnt].target_x) {
        if (cons == track_insert.length) {
            cons += 1;
            return;
        }
        var tem = Rect[cnt];
        Rect[cnt] = Rect[cnt + 1];
        Rect[cnt + 1] = tem;
        cnt = track_insert[cons];
        Rect[cnt].target_x = Rect[cnt + 1].x;
        Rect[cnt + 1].target_x = Rect[cnt].x;
        cons += 1;
        console.log(cnt);
    } else {
        Rect[cnt].x += 1;
        Rect[cnt + 1].x -= 1;
    }
}
//绘制图像
function draw(context) {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
    for (var i = 0; i < Rect.length; i++) {
        if ((Rect[i].x - Rect[i].target_x) >= 2 || (Rect[i].x - Rect[i].target_x) < -2) {
            context.fillStyle = "yellow";
            context.fillRect(Rect[i].x, Rect[i].y, 25, 25);
            context.fillStyle = "blue";
            context.fillText(Rect[i].text, Rect[i].x + 10, Rect[i].y + 15);
        } else {
            context.strokeStyle = "blue";
            context.strokeRect(Rect[i].x, Rect[i].y, 25, 25);
            context.fillStyle = "blue";
            context.fillText(Rect[i].text, Rect[i].x + 10, Rect[i].y + 15);
        }
    }
    context.fillText("插入排序", 40, 80);
}
function showDemo() {
    func();
    var c = document.getElementById("mycanvas");
    c.width = 600;
    c.height = 300;
    var context = c.getContext("2d");
//40ms调用一次函数
    setInterval(function() {
        draw(context);
        update();
    }, 40);
}