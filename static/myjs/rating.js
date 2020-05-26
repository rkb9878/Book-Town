
function rate() {
    if ($('#ratep').valid()) {
        alert("hello");
        var author = $('#author').val();
        var price = $('#price').val();
        var genre = $('#genre').val();
        var descp = $('#descp').val();
        // alert(mobile);
        var formdata = new FormData();
        formdata.append('author', author);
        formdata.append('price', price);
        formdata.append('genre', genre);
        formdata.append('descp', descp);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.status == 200 && this.readyState == 4) {
                var output = this.response;
                if (output == "fail") {
                    window.location.href="userlogin"
                } else {
                    alert(output);
                    window.location.href="/"
                }
            }
        };
        xml.open('POST', 'rating', true);
        xml.send(formdata);
    }
}