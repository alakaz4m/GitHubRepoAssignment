var canvas = document.querySelector('canvas')
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Create Canvas
var c = canvas.getContext('2d');
c.fillRect(10,100,450,350)
// createLinearGradient(x,y,x1,y1)
var grd = c.createLinearGradient(105,0,200,5);
grd.addColorStop(0, "red");
grd.addColorStop(1, "white");
c.fillStyle = grd;

// c.fillRect(x, y, width, height)
c.fillRect(110,100,30, 200)

grd = c.createLinearGradient(0,0,500,0)
grd.addColorStop(0, "red");
grd.addColorStop(1, "white")
c.fillStyle = grd

c.fillRect(160,200,30, 200)
grd = c.createLinearGradient(0,0,800,0)
grd.addColorStop(0, "red");
grd.addColorStop(1, "white")
c.fillStyle = grd

c.fillRect(210,300,30, 200)

c.beginPath();
c.moveTo(90,150);
c.lineTo(150,70);
c.strokeStyle = "black";
c.lineWidth = 30;
c.stroke();


c.beginPath();
c.moveTo(160,400);
c.lineTo(160,400);
c.strokeStyle = "black";
c.lineWidth = 30;
c.stroke();


// Line
// c.moveTo(x, y)
