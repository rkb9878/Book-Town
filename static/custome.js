"use strict";

function _instanceof(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _classCallCheck(instance, Constructor) { if (!_instanceof(instance, Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var canvas = document.getElementById("canvas"),
    context = canvas.getContext("2d"),
    width = canvas.width = window.innerWidth,
    height = canvas.height = window.innerHeight,
    densityX = 60,
    densityY = 50,
    devideX = Math.floor(width / densityX),
    devideY = Math.floor(height / densityY),
    largeSize = [12, 9, 8],
    middleSize = [7, 6.5],
    smallSize = [6, 4],
    colorPallet_1 = ["#ba9217", "#a11e5d", "#fcc335", "#23a5b8"],
    colorPallet_2 = ["#755812", "#66133B", "#004959"],
    colorPallet_3 = ["#3b2c09", "#003a47"],
    originSpeed = .1,
    speed2 = 1.4;
var largeParticles = [],
    middleParticles = [],
    smallParticles = [],
    collision = false;

var Particle =
/*#__PURE__*/
function () {
  function Particle(x, y, size, color) {
    _classCallCheck(this, Particle);

    this.x = x;
    this.y = y;
    this.r = size;
    this.angle = Math.random() * Math.PI * 2;
    this.vx = originSpeed * Math.cos(this.angle);
    this.vy = originSpeed * Math.sin(this.angle);
    this.color = color;
  }

  _createClass(Particle, [{
    key: "update",
    value: function update() {
      if (this.x - this.r < 0 || this.x + this.r > width) {
        this.vx *= -1;
      } else if (this.y - this.r < 0 || this.y + this.r > height) {
        this.vy *= -1;
      }

      if (!collision) {
        //current velocity
        var cv = {
          s: this.currentSpeed(),
          a: this.currentAngle()
        }; //easing

        if (originSpeed < cv.s) {
          this.vx -= Math.cos(cv.a) * (cv.s - originSpeed) * .1;
          this.vy -= Math.sin(cv.a) * (cv.s - originSpeed) * .1;
        }
      }

      this.x += this.vx;
      this.y += this.vy;
    }
  }, {
    key: "currentSpeed",
    value: function currentSpeed() {
      return Math.sqrt(this.vx * this.vx + this.vy * this.vy);
    }
  }, {
    key: "currentAngle",
    value: function currentAngle() {
      return Math.atan2(this.vy, this.vx);
    }
  }]);

  return Particle;
}(); //set particles


for (var h = 0; h < devideY; h += 1) {
  for (var w = 0; w < devideX; w += 1) {
    //avoid collision
    var x = densityX * w + 40 + (densityX - 80) * Math.random(),
        y = densityY * h + 40 + (densityY - 80) * Math.random(),
        randomNum = Math.floor(Math.random() * 3.5);

    if (randomNum === 0 || randomNum === 2) {
      largeParticles.push(new Particle(x, y, largeSize[Math.floor(Math.random() * largeSize.length)], colorPallet_1[Math.floor(Math.random() * colorPallet_1.length)]));
    }

    if (randomNum === 0 || randomNum === 1) {
      middleParticles.push(new Particle(x, y, middleSize[Math.floor(Math.random() * middleSize.length)], colorPallet_2[Math.floor(Math.random() * colorPallet_2.length)]));
    }

    if (randomNum === 1 || randomNum === 2) {
      smallParticles.push(new Particle(x, y, smallSize[Math.floor(Math.random() * smallSize.length)], colorPallet_3[Math.floor(Math.random() * colorPallet_3.length)]));
    }
  }
}

function checkDistance(array) {
  for (var i = 0, len = array.length; i < len - 1; i++) {
    for (var j = i + 1; j < len; j++) {
      var p0 = array[i],
          p1 = array[j],
          pDistance = (p1.x - p0.x) * (p1.x - p0.x) + (p1.y - p0.y) * (p1.y - p0.y),
          pAngle = Math.atan2(p1.y - p0.y, p1.x - p0.x);

      if (pDistance < 7500 && array === largeParticles || pDistance < 5000 && array === middleParticles || pDistance < 3000 && array === smallParticles) {
        context.globalAlpha = .4;

        if (array === largeParticles) {
          context.strokeStyle = "#fff";
        } else if (array === middleParticles) {
          context.strokeStyle = "#666";
        } else if (array === smallParticles) {
          context.strokeStyle = "#333";
        }

        context.beginPath();
        context.moveTo(p0.x, p0.y);
        context.lineTo(p1.x, p1.y);
        context.stroke();
      }

      if (pDistance < (p0.r + p1.r) * (p0.r + p1.r)) {
        collision = true;
        p1.vx = Math.cos(pAngle) * speed2;
        p1.vy = Math.sin(pAngle) * speed2;
        p0.vx = -Math.cos(pAngle) * speed2;
        p0.vy = -Math.sin(pAngle) * speed2;
      } else {
        collision = false;
      }
    }
  }
}

function draw(array) {
  checkDistance(array);

  for (var i = 0, len = array.length; i < len; i++) {
    var p = array[i];
    p.update();
    context.globalAlpha = 1;
    context.fillStyle = p.color;
    context.beginPath();
    context.arc(p.x, p.y, p.r, 0, Math.PI * 2, false);
    context.fill();
  }
}

render();

function render() {
  context.clearRect(0, 0, width, height);
  draw(smallParticles);
  draw(middleParticles);
  draw(largeParticles);
  requestAnimationFrame(render);
}