function viewbooks(obj) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var data = JSON.parse(this.response);
            var s = "";
            var output = data['x'];
            for (var i = 0; i < output.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + output[i]['title'] + "</td>";
                s += "<td>" + output[i]['description'] + "</td>";
                s += "<td>" + output[i]['price'] + "</td>";
                s += "<td>" + output[i]['edition'] + "</td>";
                s += "<td>" + output[i]['author'] + "</td>";
                s += "<td>" + output[i]['genre'] + "</td>";
                s += "<td>" + output[i]['category'] + "</td>";
                s += "<td><img src='static/media/" + output[i]['photo'] + "' alt='' width='100'></td>";
                s += "<td><button type='button' class='btn text-warning' onclick='editbook(" + JSON.stringify(output[i]) + ")'><i class='fa fa-edit'></i></button></td>";
                s += "<td><a href='samplebook?id=" + output[i]['id'] + "' class='btn text-primary'><i  class='fa fa-book-reader'> </i></a></td>";
                s += "<td><button type='button' class='btn text-danger' onclick='deletebooks(" + output[i]['id'] + ")'><i class='fa fa-trash'></i></button></td>";
                s += "</tr>";
            }
            document.getElementById("viewbookdata").innerHTML = s;
        }
    };
    xml.open('GET', 'viewbooks?catname=' + obj, true);
    xml.send();
}

function deletebooks(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            window.location.href = "booksview"
        }
    };
    xml.open('GET', 'deltebooks?id=' + id, true);
    xml.send();
}

function editbook(obj) {
    $("#id").val(obj.id);
    $("#title").val(obj.title);
    $("#description").val(obj.description);
    $("#price").val(obj.price);
    $("#edition").val(obj.edition);
    $("#author").val(obj.author);
    $("#genre").val(obj.genre);
    $("#img").attr('src', 'static/media/' + obj.photo);
    $("#editbooks").modal("show");
}

function updateData() {
    var id = document.getElementById("id").value;
    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;
    var price = document.getElementById("price").value;
    var edition = document.getElementById("edition").value;
    var author = document.getElementById("author").value;
    var genre = document.getElementById("genre").value;
    var file = document.getElementById("file").files[0];
    console.log(id, title, description, price, edition, author, genre, file);
    var data = new FormData();
    data.append('id', id);
    data.append('title', title);
    data.append('description', description);
    data.append('price', price);
    data.append('edition', edition);
    data.append('author', author);
    data.append('genre', genre);
    data.append('file', file);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // alert(this.response);
            // $("#formData").reset();
            $("#editbooks").modal("hide");

        }
    };
    xml.open('post', 'updateData', true);
    xml.send(data);
}

function deletesample(id, bid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            window.location.href = "samplebook?id=" + bid
        }
    };
    xml.open('get', 'deletesample?id=' + id, true);
    xml.send();
}



function viewusers() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var data = JSON.parse(this.response);
            var s = "";
            var output = data['x'];
            for (var i = 0; i < output.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + output[i]['id'] + "</td>";
                s += "<td>" + output[i]['password'] + "</td>";
                s += "<td>" + output[i]['confirmpassword'] + "</td>";
                s += "<td>" + output[i]['name'] + "</td>";
                s += "<td>" + output[i]['address'] + "</td>";
                s += "<td>" + output[i]['state'] + "</td>";
                s += "<td>" + output[i]['mobile'] + "</td>";
                s += "<td>" + output[i]['name'] + "</td>";
                s += "<td><img src='static/media/" + output[i]['photo'] + "' alt='' width='100'></td>";
                s += "<td><button type='button' class='btn text-danger' onclick='deleteusers(" + output[i]['id'] + ")'><i class='fa fa-trash fa-2x'></i></button></td>";
                s += "<td><button type='button' class='btn text-warning' onclick='editusers(" + output[i]['id'] + ")'><i class='fa fa-edit fa-2x'></i></button></td>";

                s += "</tr>";
            }
            document.getElementById("viewuser").innerHTML = s;
        }
    };
    xml.open('POST', 'viewuser', true);
    xml.send();
}

function deleteusers(id) {
    var email = id;
    alert(email);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            window.location.href = "viewuser"
        }
    };
    xml.open('GET', 'deleteuser?email=' + email, true);
    xml.send();
}

